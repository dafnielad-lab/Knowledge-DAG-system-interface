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
date_added: '2026-06-28T15:07:55.537550Z'
schema_version: 1
---

**$\Leftarrow$ (אוקלידס):** נניח $q = 2^p - 1$ ראשוני, נגדיר $n = 2^{p-1} q$.

$\sigma$ מולטיפליקטיבית עבור $\gcd = 1$: $\sigma(n) = \sigma(2^{p-1}) \cdot \sigma(q) = (2^p - 1) \cdot (1 + q) = q \cdot 2^p = 2 \cdot 2^{p-1} q = 2n$. אז $n$ מושלם.

**$\Rightarrow$ (אוילר):** נניח $n$ מושלם זוגי. נכתב $n = 2^k \cdot m$ עם $m$ אי-זוגי ו-$k \geq 1$.

$\sigma(n) = \sigma(2^k)\sigma(m) = (2^{k+1} - 1) \sigma(m) = 2n = 2^{k+1} m$. כי $2^{k+1} - 1$ אי-זוגי וזר ל-$2^{k+1}$, חייב $2^{k+1} \mid \sigma(m)$. נכתב $\sigma(m) = 2^{k+1} \cdot s$. מציבים: $(2^{k+1} - 1) \cdot 2^{k+1} s = 2^{k+1} m$, כלומר $m = (2^{k+1} - 1) s$.

נשים לב ש-$s \mid m$: מ-$m = (2^{k+1} - 1) s$ ברור ש-$s$ מחלק את $m$. בנוסף $m \mid m$. נטען ש-$s \neq m$: אם $s = m$ אז $m = (2^{k+1} - 1) m$, ולכן $2^{k+1} - 1 = 1$, כלומר $k = 0$, בסתירה ל-$k \geq 1$.

לכן $s$ ו-$m$ הם שני מחלקים שונים של $m$, ומכאן $\sigma(m) \geq m + s$ (סכום של לפחות שני מחלקים נפרדים). אבל $\sigma(m) = 2^{k+1} s = (2^{k+1} - 1) s + s = m + s$. שילוב: $\sigma(m) = m + s$ בדיוק.

מכאן ש-$m$ ו-$s$ הם המחלקים החיוביים היחידים של $m$. למספר חיובי יש בדיוק שני מחלקים אם ורק אם הוא ראשוני, ובמקרה זה המחלקים הם $1$ והמספר עצמו. לכן $s = 1$ ו-$m$ ראשוני, כלומר $m = 2^{k+1} - 1$ הוא ראשוני מרסן.

אז $n = 2^k (2^{k+1} - 1)$, בצורת אוקלידס עם $p = k+1$. $\blacksquare$
