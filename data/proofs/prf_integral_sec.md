---
id: prf_integral_sec
claim_id: thm_integral_sec
method: informal
status: reviewed
dependencies:
- def_secant_cosecant_cotangent
- def_tan
- thm_derivative_tan
- thm_integral_substitution
- thm_integral_one_over_x
- def_antiderivative
is_canonical: true
date_added: '2026-06-28T20:34:16.565206Z'
schema_version: 1
---

נכפול ונחלק את האינטגרנד ב-$\sec x + \tan x$:

$$\sec x = \sec x \cdot \frac{\sec x + \tan x}{\sec x + \tan x} = \frac{\sec^2 x + \sec x \tan x}{\sec x + \tan x}.$$

נגדיר $u = \sec x + \tan x$. לפי `def_secant_cosecant_cotangent` ו-`def_tan`, ולפי כללי גזירה ידועים (`thm_derivative_tan` נותן $(\tan x)' = \sec^2 x$, וגזירת $\sec x = (\cos x)^{-1}$ נותנת $(\sec x)' = \sec x \tan x$): 

$$\frac{du}{dx} = \sec x \tan x + \sec^2 x,$$

כלומר $du = (\sec x \tan x + \sec^2 x) \, dx$ — בדיוק המונה.

על פי `thm_integral_substitution`:

$$\int \sec x \, dx = \int \frac{du}{u}.$$

לפי `thm_integral_one_over_x` נקבל $\ln|u| + C = \ln|\sec x + \tan x| + C$.

בדיקה לפי `def_antiderivative`: $\left(\ln|\sec x + \tan x|\right)' = \frac{\sec x \tan x + \sec^2 x}{\sec x + \tan x} = \frac{\sec x (\tan x + \sec x)}{\sec x + \tan x} = \sec x$. $\blacksquare$
