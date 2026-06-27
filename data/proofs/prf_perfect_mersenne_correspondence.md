---
id: prf_perfect_mersenne_correspondence
claim_id: thm_perfect_mersenne_correspondence
method: informal
status: reviewed
dependencies:
- def_perfect_number
- def_mersenne_prime
- def_sigma_function
- def_multiplicative_function
- thm_fundamental_theorem_arithmetic
is_canonical: true
date_added: '2026-06-27T18:47:27.564532Z'
schema_version: 1
---

**$\Leftarrow$ (אוקלידס):** נניח $q = 2^p - 1$ ראשוני, נגדיר $n = 2^{p-1} q$. 

$\sigma$ מולטיפליקטיבית עבור $\gcd = 1$: $\sigma(n) = \sigma(2^{p-1}) \cdot \sigma(q) = (2^p - 1) \cdot (1 + q) = q \cdot 2^p = 2 \cdot 2^{p-1} q = 2n$. אז $n$ מושלם.

**$\Rightarrow$ (אוילר):** נניח $n$ מושלם זוגי. נכתב $n = 2^k \cdot m$ עם $m$ אי-זוגי ו-$k \geq 1$.

$\sigma(n) = (2^{k+1} - 1) \sigma(m) = 2n = 2^{k+1} m$. כי $2^{k+1} - 1$ אי-זוגי, חייב $2^{k+1} \mid \sigma(m)$. נכתב $\sigma(m) = 2^{k+1} \cdot s$, ואז $m = (2^{k+1} - 1) s$.

$s$ ו-$m$ מחלקים את $m$. $\sigma(m) \geq m + s$. השוואה ל-$\sigma(m) = m + s$ (לא יותר) אילצת $s = 1$ ו-$m$ ראשוני, כלומר $m = 2^{k+1} - 1$ ראשוני מרסן.

אז $n = 2^k (2^{k+1} - 1)$, בצורת אוקלידס עם $p = k+1$. $\blacksquare$
