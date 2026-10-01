# Technical LaTeX, Tabular, and Rounding Standards (Direct IZA Compliance)

## 1. The Standard Error Rounding Benchmark Algorithm
To eliminate false precision, do not report excessive decimal points from raw software outputs. Calibrate the precision of all reported coefficients using their accompanying Standard Error (SE) as the benchmark :
1. Locate the very first non-zero digit appearing in the Standard Error.
2. If that first non-zero digit is **greater than 1**, that specific digit's decimal place determines the rounding threshold for both the coefficient and the standard error. Round both parameters to this common decimal place and report.
   * *Direct Example:* `0.00456789` with an SE of `0.0089` must be rounded and reported as **$0.005 \pm 0.009$**.
3. If the first non-zero digit in the Standard Error is **exactly 1**, the rounding threshold must be extended to the *next* decimal place immediately following it.
   * *Direct Example:* `12345.6789` with an SE of `12.3456789` must be rounded and reported as **$12345.7 \pm 12.3$** (adding one extra digit ensures accurate t-statistic calculations).
4. As a global baseline across finance and economic research, **two to three significant digits** are typically sufficient for all tables and prose.

## 2. LaTeX Tabular Environment Rules
- **The Autonomous Captions Rule:** Every table and figure must feature a caption and legend that is completely self-contained and self-explanatory . A member of the dissertation committee must be able to comprehend the entire narrative of the empirical output without referencing the primary body text.
- **Eradication of Software Code Terms:** Never allow raw variable labels or shorthand codes from statistical software programs (e.g., `YEDUCT2011`, `ABIL8225A`, `LN_E_T`) to surface inside a table environment or caption. Translate them into clean, descriptive analytical terms (e.g., `Education`, `Ability Proxy`, `Logged Rate of Exploitation`).
- **Parentheses for Errors:** Every single regression coefficient must be accompanied by its corresponding standard error wrapped cleanly in parentheses directly underneath it.