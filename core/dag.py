"""Pure DAG operations on claim-dependency maps.

A dependency map is dict[claim_id, list[claim_id]] — for each claim, the list of
claims its canonical proof leans on. These functions are I/O-free and side-effect-free
so they're trivial to test and to reuse from any layer.
"""
from __future__ import annotations

from typing import Iterable


DepMap = dict[str, list[str]]


def transitive_closure(claim_id: str, dep_map: DepMap) -> set[str]:
    """All claims that ``claim_id`` (transitively) depends on."""
    visited: set[str] = set()
    stack: list[str] = list(dep_map.get(claim_id, []))
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        stack.extend(dep_map.get(node, []))
    return visited


def has_cycle(claim_id: str, new_deps: Iterable[str], current_dep_map: DepMap) -> bool:
    """Would setting current_dep_map[claim_id] = new_deps create a cycle?

    Since the existing graph is acyclic by invariant, a new edge can only create
    a cycle involving its source. So checking whether claim_id appears in its own
    proposed transitive closure is sufficient.
    """
    proposed: DepMap = {**current_dep_map, claim_id: list(new_deps)}
    return claim_id in transitive_closure(claim_id, proposed)


def traceability(claim_id: str, dep_map: DepMap, max_depth: int = 100) -> dict:
    """Return a nested tree of dependencies rooted at claim_id.

    Each node: {"id": str, "children": [...], "cycle": bool?}.
    A claim that recurses into itself along a single path is marked cycle=True
    and not expanded further (defensive; the graph should be acyclic).
    """
    def build(cid: str, path: set[str], depth: int) -> dict:
        if depth > max_depth:
            return {"id": cid, "children": [], "truncated": True}
        if cid in path:
            return {"id": cid, "children": [], "cycle": True}
        new_path = path | {cid}
        children = [build(d, new_path, depth + 1) for d in dep_map.get(cid, [])]
        return {"id": cid, "children": children}

    return build(claim_id, set(), 0)


def reverse_map(dep_map: DepMap) -> DepMap:
    """Build the reverse adjacency: for each claim, who cites it."""
    reverse: DepMap = {}
    for cid, deps in dep_map.items():
        for d in deps:
            reverse.setdefault(d, []).append(cid)
    return reverse


def dependents(claim_id: str, dep_map: DepMap) -> set[str]:
    """All claims that (transitively) depend on ``claim_id``."""
    return transitive_closure(claim_id, reverse_map(dep_map))


def leaves(claim_id: str, dep_map: DepMap) -> set[str]:
    """The leaf claims (no dependencies) reachable from claim_id —
    typically the axioms a theorem ultimately rests on."""
    closure = transitive_closure(claim_id, dep_map)
    closure.add(claim_id)
    return {cid for cid in closure if not dep_map.get(cid)}


def traceability_dependents(
    claim_id: str,
    dep_map: DepMap,
    max_depth: int = 100,
) -> dict:
    """Tree of claims that (transitively) depend on ``claim_id``.

    Mirror of ``traceability`` but going UP the DAG — for each node, children
    are the claims whose canonical proofs cite this node.
    """
    return traceability(claim_id, reverse_map(dep_map), max_depth)


def neighborhood(
    claim_id: str,
    dep_map: DepMap,
    depth_down: int = 2,
    depth_up: int = 2,
) -> tuple[set[str], list[tuple[str, str]]]:
    """Return (node_ids, edges) within ``depth_down`` hops downward (dependencies)
    and ``depth_up`` hops upward (dependents) from ``claim_id``.

    Used to render a focused subgraph around a single claim — small enough to
    visualize cleanly, large enough to show context.
    """
    down: set[str] = set()
    frontier = {claim_id}
    for _ in range(depth_down):
        next_frontier: set[str] = set()
        for cid in frontier:
            for dep in dep_map.get(cid, []):
                if dep not in down and dep != claim_id:
                    down.add(dep)
                    next_frontier.add(dep)
        frontier = next_frontier
        if not frontier:
            break

    reverse = reverse_map(dep_map)
    up: set[str] = set()
    frontier = {claim_id}
    for _ in range(depth_up):
        next_frontier = set()
        for cid in frontier:
            for parent in reverse.get(cid, []):
                if parent not in up and parent != claim_id:
                    up.add(parent)
                    next_frontier.add(parent)
        frontier = next_frontier
        if not frontier:
            break

    all_ids = down | up | {claim_id}
    edges: list[tuple[str, str]] = []
    for src in all_ids:
        for tgt in dep_map.get(src, []):
            if tgt in all_ids:
                edges.append((src, tgt))
    return all_ids, edges
