"""Pure DAG-logic tests — no I/O."""
from core.dag import dependents, has_cycle, leaves, traceability, transitive_closure


def test_transitive_closure_empty():
    assert transitive_closure("a", {}) == set()


def test_transitive_closure_simple():
    dep_map = {"a": ["b"], "b": ["c"], "c": []}
    assert transitive_closure("a", dep_map) == {"b", "c"}
    assert transitive_closure("c", dep_map) == set()


def test_has_cycle_self_loop():
    assert has_cycle("a", ["a"], {})


def test_has_cycle_two_step():
    assert has_cycle("a", ["b"], {"b": ["a"]})


def test_has_no_cycle_diamond():
    # a -> b, c; b -> d; c -> d  (diamond, no cycle)
    dep_map = {"b": ["d"], "c": ["d"], "d": []}
    assert not has_cycle("a", ["b", "c"], dep_map)


def test_traceability_tree():
    dep_map = {"thm": ["lem"], "lem": ["ax1", "ax2"]}
    tree = traceability("thm", dep_map)
    assert tree["id"] == "thm"
    assert len(tree["children"]) == 1
    assert tree["children"][0]["id"] == "lem"
    assert {c["id"] for c in tree["children"][0]["children"]} == {"ax1", "ax2"}


def test_dependents():
    dep_map = {"thm1": ["lem"], "thm2": ["lem", "ax"], "lem": ["ax"]}
    # Who transitively depends on ax? thm1 (via lem), thm2, lem
    assert dependents("ax", dep_map) == {"thm1", "thm2", "lem"}


def test_leaves():
    dep_map = {"thm": ["lem"], "lem": ["ax1", "ax2"], "ax1": [], "ax2": []}
    # Leaves reachable from thm = its axioms
    result = leaves("thm", dep_map)
    assert result == {"ax1", "ax2"}
