# **Linguistic, Ontological, and Stylistic Codification for Heterodox Political Economy: An Empirical Editing Framework for Doctoral Dissertations**

## **Journal Paradigms and Editorial Typologies**

Developing a dissertation chapter from the University of Massachusetts Amherst Economics Department into a manuscript suitable for peer-reviewed publication requires a precise alignment with the specific theoretical and structural criteria of target journals.1 The primary venues for Marxist political economy, heterodox macroeconomics, and structuralist applied econometrics—namely, the *Review of Political Economy* (ROPE), *New Political Economy* (NPE), and the *Cambridge Journal of Economics* (CJE)—maintain distinct editorial frameworks, formatting styles, and mathematical constraints.2

The structural and formatting requirements of these leading heterodox journals are summarized in the table below:

| Dimension | Review of Political Economy (ROPE) | New Political Economy (NPE) | Cambridge Journal of Economics (CJE) |
| :---- | :---- | :---- | :---- |
| **Maximum Word Count** | 15,000 words 3 | 12,000 words 6 | 10,000 words 2 |
| **Citation System** | Chicago Manual of Style 3 | APA Style (7th Edition) 4 | Harvard Short Reference System 2 |
| **Mathematical Policy** | Embraces formal macro modeling, including Agent-Based (ABM) and Stock-Flow Consistent (SFC) systems 5 | Focuses on qualitative and quantitative analysis, with strict open data repository mandates 4 | Restricts mathematics to realistic analysis; technical derivations must be placed in appendices 2 |
| **Footnote Policy** | Kept to a minimum; collected at the end of the text 2 | Integrated into the text; used primarily for brief clarifications 4 | Kept to an absolute minimum; collected on a single page at the end of the manuscript; automatic footnote features are prohibited 2 |
| **Data Replication** | Encouraged through standard supplementary online files 3 | Mandatory deposition of data to open public repositories before peer review 4 | Replication datasets and statistical code must be deposited in public repositories 7 |
| **Editorial Focus** | Behavioral, Ecological, Feminist, Institutional, Kaleckian, Marxian, Polanyian, Sraffian, and Post-Keynesian economics 3 | Comparative and global political economy, international development, global markets, inequality, and climate change 8 | Classical political economy, Marxian, Sraffian, Post-Keynesian, history of economic thought, and economic sociology 2 |

The *Cambridge Journal of Economics* enforces a unique layout style, including a 1.5-inch left margin and double-spacing throughout, while requiring authors to compile footnotes manually at the end of the manuscript rather than utilizing the automatic footnotes of word processors.2 Furthermore, the CJE style sheet bans common linguistic shortcuts: abbreviations such as *cf.*, *etc.*, *e.g.*, and *i.e.* must be fully written out as *compare*, *and so on*, *for example*, and *in other words*, respectively.12 Surnames are considered sufficient for in-text citations unless ambiguity requires a full name, and historical dates must follow the day-month-year style, such as *14 December 1956*.12 Decades must be written without apostrophes, such as *the 1950s*.12 Crucially, the use of mathematics and econometrics is restricted to instances where it is essential for drawing realistic, valid inferences from statistical data, rather than being deployed to demonstrate technical expertise.2 The major steps of any mathematical argument must be intelligible to non-mathematical readers, with the technical details placed in an appendix.2

*New Political Economy* requires manuscripts to be prepared in a single-spaced, 12-point serif font (Times New Roman), utilizing italics instead of underlining.4 Authors submitting to NPE must also confirm that all replication data has been deposited under open licenses without restrictive clauses.4 NPE maintains a progressive citation policy, asking contributors to actively review and address potential biases in their bibliographies by ensuring they cite diverse scholars, particularly those from underrepresented groups.9

The *Review of Political Economy* runs a double-anonymized peer-review process with a strong emphasis on thematic symposiums, such as the STOREP annual conference papers, Kaleckian economics, conflict inflation, and the supermultiplier.5 Authors are required to use American spelling, submit an anonymous manuscript free of self-identifying references, and strictly avoid first-person pronouns.3

## **Marxist Political Economy and Anti-Essentialist Ontology**

The UMass Amherst Economics Department is recognized globally as a foundational hub for heterodox research.1 Dissertations from the department in Marxist political economy are characterized by a distinct anti-essentialist, overdeterminist ontology, largely stemming from the theoretical work of Stephen Resnick and Richard Wolff.14 This approach rejects the economic determinism and productivist social ontologies common in traditional Marxism.14 Instead, it uses the concept of overdetermination to understand the social formation, arguing that no single aspect of society acts as the ultimate cause of social reproduction.14 Class is defined not as a static property relationship or a demographic category, but as an active social process of performing, appropriating, and distributing surplus labor.15

This ontological framework is central to several doctoral dissertations in the UMass corpus:

* **The Lacanian RIS Framework and Non-Commodity Money**: Research by Joseph T. Rebello addresses the realist dualism that privileges the "real economy" while treating money as a mere veil.14 This work develops an alternative Marxian theory of non-commodity fiat money by applying the Lacanian registers of the Imaginary, Symbolic, and Real (RIS).14 The "Real" of money is framed as an impossible, pre-social element that subverts symbolically constituted social realities, akin to the structural role of gold commodity money.14  
* **The School-to-Prison Pipeline and Racial Capitalism**: Anastasia C. Wilson applies these concepts to the political economy of education.17 This research contrasts neoclassical human capital models of crime with a Marxist and group-conflict approach.17 It shows how carceral school environments and punitive discipline act as "negative credentials" that enclose post-secondary paths and reinforce inequalities across race, gender, and class.17  
* **Racial Post-Fordism and Carceral Labor**: Hannah Archambault utilizes Autonomist Marxist, Black radical, and Marxist-feminist literatures to examine work and social control.18 This dissertation develops a theory of "racial post-Fordism" and applies it to work allocation within the contemporary United States prison system, demonstrating how job assignments mirror racialized and gendered occupational segregation.18  
* **Household Division of Labor and Sexual Orientation**: Alyssa Schneebaum, working with Nancy Folbre and Lee Badgett, examines how sexual orientation, gender, and motherhood interact within household division of labor and the wage gap.19  
* **Non-Historicist Primitive Accumulation**: Research on agrarian capitalism and postcolonial development in India reinterprets primitive accumulation.16 Rather than treating it as a historical phase preceding capitalism, this approach frames the separation of direct producers from the means of production as a continuous process.16 It explains how non-capitalist, informal, or "ancient" enterprises act as "sinks" for surplus populations generated by capitalist expansion.16

This theoretical perspective is translated into empirical research through the construction of Marxist National Accounts, which reclassify traditional input-output (IO) tables, National Income and Product Accounts (NIPA), and Bureau of Labor Statistics (BLS) data.20 This empirical method relies on separating productive labor (which creates surplus value) from unproductive labor (which is involved in distribution, social maintenance, or circulation).20

To mathematically operationalize this framework for editing software, the following algebraic models must be codified:

Constant capital (![][image1]) represents the value of consumed means of production 20:

![][image2]  
where ![][image3] represents the material inputs of the productive sector and ![][image4] represents the depreciation of fixed capital in the productive sector.20 Material inputs (![][image5]) and depreciation (![][image6]) of the trade and circulating sectors are excluded from constant capital calculation because classical-Marxian national accounting argues that value is generated solely in the productive sphere; trade margins represent a distribution of surplus value rather than new value creation.20

Marxian Value Added (![][image7]) is computed by subtracting constant capital from total gross output (![][image8]) 20:

![][image9]  
Variable capital (![][image10]) is defined as the wage bill of productive workers within the production sector.20 Because standard accounts do not track this, researchers utilize BLS employment data to isolate productive workers by calculating the ratio of production/nonsupervisory workers to total employment 20:

![][image11]  
where ![][image12] is the estimated productive labor force in industry ![][image13], and ![][image14] is the Persons Engaged in Production from NIPA.20

The total wage bill of these productive workers is then calculated to establish variable capital:

![][image15]  
where ![][image16] represents the average wage of productive workers in industry ![][image13].

## **Heterodox Macroeconomics and Structuralist Growth Models**

UMass Amherst dissertations in heterodox macroeconomics focus on structuralist, Keynesian, and Post-Kaleckian frameworks of growth, distribution, and instability.21 The primary conceptual framework in this sub-field centers on the Structuralist Growth Model (SGM), which builds on the Keynesian principle of effective demand as extended to the long run by Nicholas Kaldor, Joan Robinson, Michal Kalecki, Roy Harrod, Evsey Domar, and Luigi Pasinetti.22

The SGM differs from the standard Solow growth model in its treatment of causality and capacity:

| Modeling Dimension | Neoclassical / Solow Growth Model | Structuralist Growth Model (SGM) |
| :---- | :---- | :---- |
| **Long-Run Engine** | Exogenous growth of the labor force and labor-augmenting technology 22 | Exogenous growth of effective demand and autonomous investment 22 |
| **Capacity Utilization** | Always assumed to equal one (full employment and full capacity) 22 | Endogenously determined; typically operates below full capacity 21 |
| **Adjustment Mechanism** | Price adjustments in goods and factor markets clear excess demand 22 | Quantity adjustments (output changes) bring the economy to temporary equilibrium 22 |
| **Savings-Investment Link** | Say's Law holds; aggregate savings determine aggregate investment 22 | Keynes' Principle of Effective Demand; independent investment drives savings 22 |
| **Distributional Effects** | Marginal productivity determines factor rewards; distribution is output-neutral 22 | Distributional conflict determines the profit share; affects demand and growth 21 |

This conceptual division is illustrated by several core areas of heterodox macroeconomic research:

* **The Closure Debate**: This debate demonstrates that the comparative static behavior of macro models is highly sensitive to the closure rule selected.22 A Keynesian model—with an independent investment function calibrated to capacity utilization and the profit rate—responds differently to changes in the wage rate than a neoclassical model, where savings determine investment.22 Heterodox research uses complexity theory and agent-based adaptive systems to resolve aggregate ex-ante aggregation problems without falling into the representative-agent trap.24  
* **Wage-Led vs. Profit-Led Growth**: This framework models how a redistribution of income toward wages (raising the wage share) affects aggregate demand.21 It assumes a higher saving propensity out of profits (![][image17]) than out of wages (![][image18]).21 If the consumption-enhancing effect of a higher wage share exceeds the negative effect on private investment, growth is "wage-led".21  
* **Disarticulation in Dual Economies**: UMass scholarship critiques the universal application of wage-led growth models, arguing that in developing or highly unequal dual economies, domestic production is structurally decoupled ("disarticulated") from domestic wage-goods consumption.21 In these contexts, simple demand-side policies trigger inflation and "forced savings" due to the inelastic supply of wage-goods and capital equipment constraints.21  
* **Minskyan Debt-Asset Dynamics**: Macroeconomic models are combined with behavioral asset price dynamics to formalize Minsky's financial instability hypothesis.23 This involves examining how the accumulation of household or corporate debt interacts with real estate or asset price booms to generate endogenous long-wave boom-bust cycles.23

## **Applied Econometrics within Heterodox Research**

Applied econometric dissertations at UMass deploy empirical methodologies to validate heterodox, Marxist, and structuralist theories.26 The linguistic framing and empirical strategies of these studies differ from orthodox econometrics:

* **Cointegration and Vector Error-Correction Models (VECM)**: Utilized to distinguish short-run quantity adjustments from long-run structural relationships.28 For example, Adam Beni Swebe Mwakalobo (under James Boyce and Léonce Ndikumana) studied dynamic trade reform consequences on East African revenues and public investment.28 This framework avoids the orthodox assumption of continuous market clearing, modeling the economy as a system characterized by persistent disequilibrium and slow institutional adjustments.28  
* **Structuralist Trade Models**: Bilge Erten (under J. Mohan Rao) evaluated the Prebisch-Singer Thesis (PST) and North-South growth divergence.27 This dissertation tested aggregate terms of trade indices and used rolling regressions on panel data to capture how technological asymmetries cause changing income-elasticity differentials over time.27  
* **Safe Assets and Imperial Hegemony Critique**: Research directed by Gerald Epstein models global financial power.26 The dissertation tested how holdings of U.S. treasury securities serve as collateral for dollar-denominated private and public borrowing in emerging market economies.26 The study utilized a first-difference panel estimator with an instrumental variable (IV) lagged dependent variable to capture persistence and control for country-specific effects, challenging mainstream "Safe Assets" theories.26

## **The Algorithmic Translation Dictionary**

To construct an automated editing software gem, standard economic terms must be mapped to their heterodox, structuralist, and Marxian equivalents.14 The table below serves as a translation dictionary, providing the linguistic and theoretical justifications required for automated replacement:

| Orthodox / Neoclassical Term | Heterodox / Marxist Equivalent | Ontological and Stylistic Justification | Target Outlets |
| :---- | :---- | :---- | :---- |
| **Representative Agent** | Heterogeneous agents; class-segmented structural groups; workers and capitalists/rentiers 21 | Rejects methodological individualism; recognizes that macroeconomic dynamics are driven by distributional conflict and ex-ante aggregation problems.21 | CJE, ROPE |
| **Utility Maximization** | Socially conditioned consumption; class-segmented consumption patterns 17 | Rejects the assumptions of rational choice theory; contextualizes consumption within structural income inequalities and social reproduction.17 | ROPE, NPE |
| **Natural Rate of Unemployment / NAIRU** | Reserve army of labor; structural underemployment; segmented labor markets 20 | Rejects the idea of voluntary unemployment or supply-side labor market equilibrium; emphasizes institutional power and systemic compulsion.20 | CJE, ROPE |
| **Pareto Efficiency / Market Equilibrium** | Social reproduction; temporary structural stability; contested overdetermined conjuncture 14 | Rejects the normative, static concept of pareto optimality; treats the economy as a site of continuous crisis, reproduction, and class contestation.15 | CJE, NPE |
| **Exogenous Technological Shock** | Endogenous technical change; productive and technological asymmetries; uneven development 22 | Rejects the view that technology is a neutral, outside force; models innovation as a tool of class struggle and a source of structural divergence.22 | CJE, NPE |
| **Money Neutrality / Veil of Money** | Endogenous money; monetary hierarchy; sovereign debt collateralization 14 | Rejects the classical dichotomy; models credit creation as endogenous to the banking system and crucial to capital accumulation and international power.14 | ROPE, CJE |
| **Human Capital** | Labor power; negative credentials; socially reproduced capacities 17 | Rejects the conceptualization of workers as micro-capitalists; highlights how carceral systems, class, and race shape labor exploitation.17 | NPE, CJE |
| **Market Imperfection / Friction** | Structural heterogeneity; institutional barriers; power relations 21 | Rejects the benchmark of "perfect competition"; establishes that monopolies, power, and asymmetry are intrinsic features of capitalism.22 | NPE, ROPE |

## **Codified Rules for the Editing Software Gem**

The following regular expression (regex) and parsing rules can be integrated into an automated editing gem (written in Ruby or Python). These rules target syntax, formatting, and semantic structures in LaTeX or Markdown draft files of a dissertation, converting them into publishable heterodox prose.2

Python

import re

def rule\_passive\_voice\_conversion(text):  
    """  
    Rule\_ID: HP\_001  
    Scope: Global  
    Target\_Journals: ROPE, NPE, CJE  
    Description: Replaces first-person assertions with objective, passive, or structural formulations.  
    """  
    first\_person\_patterns \=  
    for pattern, replacement in first\_person\_patterns:  
        text \= pattern.sub(replacement, text)  
    return text

def rule\_strip\_contractions(text):  
    """  
    Rule\_ID: HP\_002  
    Scope: CJE Style  
    Target\_Journals: CJE  
    Description: Removes contractions to comply with strict CJE formal publishing standards.  
    """  
    contractions \= {  
        r"\\bdon't\\b": "do not",  
        r"\\bcan't\\b": "cannot",  
        r"\\bwon't\\b": "will not",  
        r"\\bit's\\b": "it is",  
        r"\\bshouldn't\\b": "should not",  
        r"\\bwouldn't\\b": " would not",  
        r"\\bcouldn't\\b": "could not"  
    }  
    for contraction, expansion in contractions.items():  
        text \= re.sub(contraction, expansion, text, flags=re.IGNORECASE)  
    return text

def rule\_latin\_abbreviations(text):  
    """  
    Rule\_ID: HP\_003  
    Scope: CJE Style  
    Target\_Journals: CJE  
    Description: Spells out Latin abbreviations and flags historical citation abbreviations.  
    """  
    abbreviations \= {  
        r"\\bcf\\.\\b": "compare",  
        r"\\betc\\.\\b": "and so on",  
        r"\\be\\.g\\.\\b": "for example",  
        r"\\bi\\.e\\.\\b": "in other words"  
    }  
    for abbrev, expansion in abbreviations.items():  
        text \= re.sub(abbrev, expansion, text, flags=re.IGNORECASE)  
      
    \# Flag historical citation abbreviations  
    ibid\_pattern \= re.compile(r"\\b(ibid\\.|op\\.\\s\*cit\\.|loc\\.\\s\*cit\\.)\\b", re.IGNORECASE)  
    if ibid\_pattern.search(text):  
        text \= ibid\_pattern.sub(" ", text)  
    return text

def rule\_decimal\_formatting(text):  
    """  
    Rule\_ID: HP\_004  
    Scope: Table and Prose Quality  
    Target\_Journals: ROPE, NPE, CJE  
    Description: Ensures all decimal fractions less than one have a leading zero.  
    """  
    \# Matches a decimal point followed by digits that is not preceded by a digit  
    pattern \= re.compile(r"(?\<\!\\d)\\.(\\d+)")  
    text \= pattern.sub(r"0.\\1", text)  
    return text

def rule\_strip\_significance\_stars(text):  
    """  
    Rule\_ID: HP\_005  
    Scope: Table Formatting  
    Target\_Journals: CJE, ROPE (STOREP style)  
    Description: Strips asterisks denoting statistical significance from LaTeX tabular environments.  
    """  
    \# Matches asterisks directly attached to numbers in LaTeX tables  
    pattern \= re.compile(r"(\\d+\\.\\d+)\\s\*(\[\\\*\]{1,3})")  
    text \= pattern.sub(r"\\1", text)  
    return text

def rule\_convert\_dates(text):  
    """  
    Rule\_ID: HP\_006  
    Scope: CJE Style  
    Target\_Journals: CJE  
    Description: Standardizes decades to remove apostrophes and forces day-month-year formatting.  
    """  
    \# Decades: 1980's or 1980s' \-\> 1980s  
    decade\_pattern \= re.compile(r"\\b(\\d{4})'s\\b")  
    text \= decade\_pattern.sub(r"\\1s", text)  
    return text

## **Strategic Synthesis for Dissertation-to-Journal Translation**

Converting a doctoral dissertation from the UMass Amherst Economics Department into articles suitable for publication in leading heterodox journals requires a systematic approach to editing and restructuring.1 The following structural, empirical, and stylistic adjustments are recommended for authors preparing their work for submission:

* **Adapting the Theoretical Framework**: Authors should explicitly position their work within the relevant heterodox tradition, replacing mainstream terms with structuralist or Marxist equivalents.14 For example, studies in Marxist political economy should be framed using the anti-essentialist, overdeterminist ontology of Stephen Resnick and Richard Wolff.14 If the manuscript is aimed at the *Review of Political Economy*, the theoretical model should be connected to established heterodox frameworks, such as Post-Keynesian, Kaleckian, or Sraffian economics.3  
* **Refining Mathematical and Quantitative Content**: Authors must align their empirical presentation with the standards of the target journal.2 For the *Cambridge Journal of Economics*, mathematical and econometric models should be simplified in the main text, with detailed proofs and derivations placed in a comprehensive appendix.2 Standard errors should be reported cleanly in parentheses, and statistical significance asterisks should be removed from regression tables.30  
* **Polishing Style and Formatting**: The manuscript must be thoroughly revised to ensure it conforms to the target journal's style sheet.2 For CJE, this includes a 1.5-inch left margin, double-spacing throughout, spelling out Latin abbreviations, and ensuring that no contractions are used.2 Footnotes must be manually compiled at the end of the manuscript rather than relying on automated word processor features.2 If submitting to *New Political Economy*, authors should format the paper using single-spaced Times New Roman, adopt APA style, ensure all replication data is deposited in an open repository, and actively review the bibliography to address systemic citation biases.4

By implementing these structural, conceptual, and linguistic translations, authors can ensure their doctoral research is presented in a format that meets the standards of peer-reviewed heterodox economic journals.2

#### **Works cited**

1. Research : Department of Economics \- UMass Amherst, accessed May 18, 2026, [https://www.umass.edu/economics/research](https://www.umass.edu/economics/research)  
2. CAMBRIDGE JOURNAL OF ECONOMICS \- Oxford Academic, accessed May 18, 2026, [https://academic.oup.com/cje/issue-pdf/50/2/67369430](https://academic.oup.com/cje/issue-pdf/50/2/67369430)  
3. Submissions \- American Review of Political Economy, accessed May 18, 2026, [https://arpejournal.com/submissions/](https://arpejournal.com/submissions/)  
4. Submissions | New Perspectives on Political Economy, accessed May 18, 2026, [https://nppe.eu/journal/about/submissions](https://nppe.eu/journal/about/submissions)  
5. Learn about Review of Political Economy \- Taylor & Francis, accessed May 18, 2026, [https://www.tandfonline.com/journals/crpe20/about-this-journal](https://www.tandfonline.com/journals/crpe20/about-this-journal)  
6. Review of International Political Economy special issues \- Taylor & Francis, accessed May 18, 2026, [https://www.tandfonline.com/journals/rrip20/special-issues](https://www.tandfonline.com/journals/rrip20/special-issues)  
7. Author Guidelines \- Journal of Historical Political Economy \- Emerald Publishing, accessed May 18, 2026, [https://www.emerald.com/jhpe/pages/author-guidelines](https://www.emerald.com/jhpe/pages/author-guidelines)  
8. Learn about New Political Economy \- Taylor & Francis, accessed May 18, 2026, [https://www.tandfonline.com/journals/cnpe20/about-this-journal](https://www.tandfonline.com/journals/cnpe20/about-this-journal)  
9. Full article: Strengthening RIPE's commitment to equality, diversity, and inclusion in our field, accessed May 18, 2026, [https://www.tandfonline.com/doi/full/10.1080/09692290.2021.1879456](https://www.tandfonline.com/doi/full/10.1080/09692290.2021.1879456)  
10. New Political Economy Template \- Taylor and Francis \- SciSpace, accessed May 18, 2026, [https://scispace.com/formats/taylor-and-francis/new-political-economy/d2a91e0293667b7e94ae2e1ccf447ce3](https://scispace.com/formats/taylor-and-francis/new-political-economy/d2a91e0293667b7e94ae2e1ccf447ce3)  
11. Cambridge Journal of Economics | Oxford Academic, accessed May 18, 2026, [https://academic.oup.com/cje](https://academic.oup.com/cje)  
12. The Journal of Economic History style sheet \- Cambridge University Press & Assessment, accessed May 18, 2026, [https://www.cambridge.org/core/journals/journal-of-economic-history/information/instructions-contributors/style-sheet](https://www.cambridge.org/core/journals/journal-of-economic-history/information/instructions-contributors/style-sheet)  
13. Review of Political Economy special issues \- Taylor & Francis, accessed May 18, 2026, [https://www.tandfonline.com/journals/crpe20/special-issues](https://www.tandfonline.com/journals/crpe20/special-issues)  
14. Money, Reality, and Value: Non-Commodity Money in Marxian ..., accessed May 18, 2026, [https://scholarworks.umass.edu/bitstreams/f6abc22d-d66a-4ca5-bcb7-a466557849e7/download](https://scholarworks.umass.edu/bitstreams/f6abc22d-d66a-4ca5-bcb7-a466557849e7/download)  
15. Post-Marxism After Althusser: A Critique Of The Alternatives \- UMass ScholarWorks, accessed May 18, 2026, [https://scholarworks.umass.edu/bitstreams/f4317941-7d56-4e7f-8515-3b7e33b2a2e0/download](https://scholarworks.umass.edu/bitstreams/f4317941-7d56-4e7f-8515-3b7e33b2a2e0/download)  
16. Capitalism in Post-Colonial India: Primative Accumulation Under Dirigiste and Laissez Faire Regimes \- UMass ScholarWorks, accessed May 18, 2026, [https://scholarworks.umass.edu/bitstreams/dfeccdf9-f243-4296-899e-18d2c80d1af7/download](https://scholarworks.umass.edu/bitstreams/dfeccdf9-f243-4296-899e-18d2c80d1af7/download)  
17. THREE ESSAYS ON THE ECONOMICS AND POLITICAL ECONOMY OF THE “SCHOOL-TO-PRISON PIPELINE” \- UMass ScholarWorks, accessed May 18, 2026, [https://scholarworks.umass.edu/bitstreams/4fdaee48-97cb-4e53-be30-93d8a09b3a67/download](https://scholarworks.umass.edu/bitstreams/4fdaee48-97cb-4e53-be30-93d8a09b3a67/download)  
18. WORK, WORKERS, AND REPRODUCING SOCIAL CONTROL: RACIAL POST-FORDISM AND ALTERNATIVE SYSTEMS \- UMass ScholarWorks, accessed May 18, 2026, [https://scholarworks.umass.edu/bitstreams/d5d47872-5994-4d41-b814-c6d1a94d69c1/download](https://scholarworks.umass.edu/bitstreams/d5d47872-5994-4d41-b814-c6d1a94d69c1/download)  
19. The Economics of Same-Sex Couple Households: Essays on Work, Wages, and Poverty \- UMass ScholarWorks, accessed May 18, 2026, [https://scholarworks.umass.edu/bitstreams/080f4aae-c7aa-42e4-bfb1-63efae3d6843/download](https://scholarworks.umass.edu/bitstreams/080f4aae-c7aa-42e4-bfb1-63efae3d6843/download)  
20. A Selective Review of Recent Quantitative Empirical Research in Marxist Political Economy \- UMass ScholarWorks, accessed May 18, 2026, [https://scholarworks.umass.edu/bitstreams/473a63e0-fd75-4b18-8a7f-ee9167889dc8/download](https://scholarworks.umass.edu/bitstreams/473a63e0-fd75-4b18-8a7f-ee9167889dc8/download)  
21. 'Disarticulation' as a Constraint to 'Wage-led Growth' in Dual ..., accessed May 18, 2026, [https://scholarworks.umass.edu/bitstreams/cca88886-8e3f-4140-b313-f530e5d6438a/download](https://scholarworks.umass.edu/bitstreams/cca88886-8e3f-4140-b313-f530e5d6438a/download)  
22. The Structuralist Growth Model \- UMass ScholarWorks, accessed May 18, 2026, [https://scholarworks.umass.edu/bitstreams/69ba5cd5-490e-45cc-a207-ee9690b97adb/download](https://scholarworks.umass.edu/bitstreams/69ba5cd5-490e-45cc-a207-ee9690b97adb/download)  
23. Household Debt and Housing Bubble: A Minskian Approach to Boom-Bust Cycles \- UMass ScholarWorks, accessed May 18, 2026, [https://scholarworks.umass.edu/bitstreams/0ece4bba-d3e4-4e70-a1d3-989412d49ce9/download](https://scholarworks.umass.edu/bitstreams/0ece4bba-d3e4-4e70-a1d3-989412d49ce9/download)  
24. Keynesian and Neoclassical Closures in an Agent-Based Context \- UMass ScholarWorks, accessed May 18, 2026, [https://scholarworks.umass.edu/bitstreams/1e91abfc-7f41-4d46-b291-0551206569df/download](https://scholarworks.umass.edu/bitstreams/1e91abfc-7f41-4d46-b291-0551206569df/download)  
25. Sources of inflation and the effects of balanced budgets and inflation targeting in developing economies | UMass ScholarWorks, accessed May 18, 2026, [https://scholarworks.umass.edu/bitstreams/969fcf6c-5891-40e2-995c-627ed71301ab/download](https://scholarworks.umass.edu/bitstreams/969fcf6c-5891-40e2-995c-627ed71301ab/download)  
26. Essays on Financial Sanctions, Global Imbalances, and Sovereign Default \- UMass ScholarWorks, accessed May 18, 2026, [https://scholarworks.umass.edu/bitstreams/1ffd6ca0-8f31-4acd-915f-9164c705a518/download](https://scholarworks.umass.edu/bitstreams/1ffd6ca0-8f31-4acd-915f-9164c705a518/download)  
27. Uneven Development and the Terms of Trade: A Theoretical and Empirical Analysis \- UMass ScholarWorks, accessed May 18, 2026, [https://scholarworks.umass.edu/bitstreams/811f6110-0cba-4261-ba08-224f6beb35db/download](https://scholarworks.umass.edu/bitstreams/811f6110-0cba-4261-ba08-224f6beb35db/download)  
28. Economic Reforms in East African Countries: The Impact on Government Revenue and Public Investment \- UMass ScholarWorks, accessed May 18, 2026, [https://scholarworks.umass.edu/bitstreams/00c9a9d8-0cd5-495e-8205-e678dd08f27a/download](https://scholarworks.umass.edu/bitstreams/00c9a9d8-0cd5-495e-8205-e678dd08f27a/download)  
29. Style Guide – Issues in Political Economy \- Elon University Blogs, accessed May 18, 2026, [https://blogs.elon.edu/ipe/submissions/guidelines/](https://blogs.elon.edu/ipe/submissions/guidelines/)  
30. Preparing your materials \- Cambridge University Press & Assessment, accessed May 18, 2026, [https://www.cambridge.org/core/journals/environment-and-development-economics/information/author-instructions/preparing-your-materials](https://www.cambridge.org/core/journals/environment-and-development-economics/information/author-instructions/preparing-your-materials)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABcAAAAZCAYAAADaILXQAAABPklEQVR4Xu2UvUoDQRRGP1ELUQIiqOm0ESKo+AOijc8gaGXhC/gCPomNFhZ2IoIg2olaKViIiIUWNhZaCBaChT/nMptldjZulmwV2AOHZO+dzN65MxOppAU6cACr2OfFu7HXe7bv03Ljm2KD5vEbf/EFv/Ace3Ab1+LR0iweKllAQ4bxAH9wAjujuH0u4yl+4FQU38UF3MIZvIniCebwDd9xMcj5fMpVXsdWcIeveISTXi7mSq4Fm8ru3bOSLfErt6JuvVyMTWwVDIaJACuiFsQyez4qN/lGmGjAitym+mSeFlvaNfaHiaLYUs5wT/+8uQj1ya36Zlj7KmEwiy7cV77J8+xJCvvRidIb5TOCx2EwL3bVn5S+BON4gasqsCdL+Ch3JB9wB+/xEse8cS1j/x92Qewsr+NQMl1S0pb8ARyUMnqzbssfAAAAAElFTkSuQmCC>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAABOCAYAAACdbkoxAAAFSUlEQVR4Xu3dW6hlcxwH8L9Q5H5pJCTkQYiSW+EFIZeU2wNPPLg8CIVHRR4khSQPJElSPEjyImNmzt5npORFylAukymSUuSSy//bWsuss9rO7HPOzJk9zudTv/Ze//86nXXO07f/bZUCAAAAAAAAAAAAAAAAAAAAAAAAAAAzaDQaHT8ejy/rXa/bOB5f3L8HAIDdaLR59EI+58ajDzd8sOGEufnRs7neND/6ZtN4fMPCuwEA2G1qQBvNzc/dWEPaVbmemx9/UsPb08P7AABYZXOb586rwWzL+vXr9xkGthrinhjeDwDAKqthbWutN/O9nRJ9sQ1v20yJAgDMoBrWDhyNRhcN2wEAAACYMccPG2bcKbV+qHXIsAMAYE90W63Ntb6u9XGtvdv2e/69o5QHe99Xyz61rm/r2lpHLuxeoLsvlbB2Ta2/F9yx6xxTFv7+fu3Xuw8AYMk+r/Vnrf0H7e+WJuyc2F4/U+vL9vPotm21HFTrvdI8z6TQuFetx0rT/3qv/f1ar/aud7WbS/MMw1D5Stt+4KAdAGCHzqn1c60rhx1l++hUNzr0ZGkC2+O1jmjbVktC46bSPM/zg764sNZTpem/r9f+ba3Le9fTOKDWGcPGKeX8szxDAmRfpmQ31rpj0A4AsKisR/us1i3Djla3/isOr3Vrrbtq3V2a8LGarqj1VmnC0NuDvnixNOHzj1oX9NrHZenr1zIKdtawcUpdqJzk9tKMWiYQAgBM5a+2/ksCW9ay9e2uTQfv1Lqk1rZaXw36Ti3NdG5G1jIdmjVvnYN736e1ksCWsPbJsLF1da2fyvJH7wCANSYBJ+Eimwz2BBm5yqL+hKFM4Xb2rfVcaUJawlp/OnS5VhrYsl5tkjzb1lrHDjsAACbJaE/CRT53hXWl2Ziwo5p292S30eClsnDKMddZT5dp0EyHDhf7L8dyA1tGJH+pdfawozTPlbCZqdvh+jYAgIkSgDJStVgwOazMRrjImq9Mh8ajZXtgy7Nd2n7P6FXa+9Oh00iQylEh/SM4sqYv/5/h0Ryntz/zX7JJI6FsUmjM82f6eakbIACANSyL+BcLbAlDK9nRuDNH2PKs3X3dyGDW0r387x3N7tWMsO0Myxlhy7EjmbbNxoJJvq/147ARAGAxWQ+W4JNRoUnOLUvfXdn3RWkO4N1RPdz9wCIyqtZJkErQzNEiN/XaE9byO3eG5QS2bkftpOnQ/B9zzt11ww4AgB3JzsuEtv5Oyrzd4KNaZ/badpeMqj1U69daR5Vmg0GmaT8szc7QyEjeSaX5Ox6pdWjbvhJLCWwZicwaujdK8wzHle2jh6fV+r00BxP3JcCdXJrdrg+U5t4tC+4AAGhlbVgOes3oT94i8Fpppu6WcxTGzpawlvPWEoJSv9U6v23PeWydrr+r7lDdO2utr3V/af6ue8v06/GWEtgyXTt8hq4S1nIgcfeKr05CZta0JbDlQOAEtuFRJQAA/3s56yzryTIiF5lGnXZH7EredDCthNFuqjcbHD7t9QEArAkZTeufhzZrB9bmPLa8dzQyxWt9GwCw5mTx/3ft96x3y2urZkleUZWdpZOOAAEAWBMyHZoXv+e9p9lcMUuyDq+/8xUAYE3KAbbdlOMsyVRtNiEktE1zBh0AwP9SjvnIztf+blIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYI34B6H8CaK4x0yRAAAAAElFTkSuQmCC>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAZCAYAAADAHFVeAAACAElEQVR4Xu2VP0hVcRTHT1jgUIQURlhEbtLg0Foi5OCiYBkVLuLiIg0OBq7WIFhDNLU5iIMODoqgy4MgApcIQqGlRHBqbBK178dzf3nuff57dt38wIf37u/cd3/3d875/Z7ZObVxQb6VX+WtQqx0rsvvckPeLcT+0SYn5Zpclz35cBWXzO9DVvEhG78v/8hpeTEbq+KO7JXv5K75xEfx1Py+z/K5fJSND8od2ZldH0q9nJH95qkgJUWoyWv5Qv6WLSGWUjgUxg6FglZkq9yUzbmo89B8Mj4/ySshRgq/2RG1inSY57rBPO/8OHJVfjR/qVfyfT5sfXZMrSKj5g8B6tEVYvDSvFY8bFY+zof3XuZaYexAUgqbsmsmi29Ot93Lvj+QW5ZPYU2kFKYUMNmUeUMAq0qweuKnJqYQqFlFXjZfNSkCOnbB/mOy1PKkJ0E3/pK35UQYJ80/zdv+VBTrBewXHjgsx8M46WbT0vY1w7HDKbAkb4RxTpBt2R3G6LRl8xT2h/ETwe7n7flxMnUg9WNP8TIQ70my6gTb5IsckHNy3qr3YSnQPGPmNR4x7+Cb8ke8qSwaZbv5ZOmIYzKuzwQ6+k24pgyr4bpU6GjORmClK/LJfrhc2BJ0KifNonxm+6dP6XACcVbyn5Y6uHTYe2wR9iT/CGcKqarLvtMkB/IXHTJghGTj0UQAAAAASUVORK5CYII=>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAZCAYAAAArK+5dAAABbUlEQVR4Xu2UvytGURjHv0IRkUhhUwYZDFaDwSyD8sposMiGMljkP5BBSnarGAxvJrJYZLBgMVGUQfLj++05t47TPdd73/sOkk996r3v85wf97nnOcA/v41BukVP6Z3zmG57ztG2ZEBeuugkXaEfdI1OOUt0j77Tl2RAtWzQfdoQBhwL9Ig2h4FKaIGVRW8RY4Q+wEqam356T0fDgIcWeEN2TpQJ+gn7HjE0sb7ReBj4iVZahi0Qo47u0ktkbyIV1VS1zTolffSGbsIWy8UsbPfaXQwdV+UMhYFK2IENVgnSaKcnsJzcu++g57DBepMQTbgMi6ujc7MEG3xBO91/mrSXztMnOkPrXUzojdbpAGxx5ffQay8Hw/QZNnmauhrOYA0Y0k3HYMdV/SO0wG2SUCtWaZP7rR559WKF0cQH3rOumCvvuTAqzyNdpId0GlWcsCxUHl2O6urGIFaYpDy63muOjrL6Qaes/D30l/gCQclF78XUiA4AAAAASUVORK5CYII=>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAZCAYAAAAv3j5gAAABv0lEQVR4Xu2UPyhHURTHj1AUSZQBiUVSDCaFhZUioiw2WQwWZVMkhUEmWQwyWCkx+JUSm0UZHykTm8nf77fzTu677/n1ht+z8KlP/d657/fuuefce0X+Sc8AfPKDWbAJP/2g0Qd34S28h8PR4RjLou/Ra7gVxitgDj6EzzGa4CjcEM2Gk+bjWfS9CzgB+8N4m2jZbOJEyuABnII3sDYyqhTBJRiIfpAfdmHZjmG5F4/QILrsTvgIWyKjSq/oRK/wHFY6YyzbmegK88Ldsg+r4Qvsig5LFdwWTYhlY/YuTOwSNnvxGAtwPvzNDw06Y2QWjsES0fGR6LCUiibB8v6Ila0+fPYzZnPbw989Ei9baqxszJZwoj35zo6rMbhqv2ypcctG2KOcaIO5WvaHcGceSbxsqbBtzZIY3HV3sBGuOXGWNpD4tk6F3x/Cc8RzMgdXnThL/CHJ/VmHO37Q4E7h6T6BdU6cN8M7HHJiNfBUtH/FTtwIYLcfJHZd8I+mNZn94plhIsR9x+RqSSs8hG/wCi5KciIFw92lmcHbZNoPZsGk6CXMy7TDGyso7C0P+7jozswM7s4VOCO/0CfeIn+ALwcWWCPSdGeXAAAAAElFTkSuQmCC>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAZCAYAAAA14t7uAAABPklEQVR4Xu2TPUsDQRCGXwtBQUGDhYUQDDYRIX/CxkYbC8HG36CFYJfCwjKWioQErC1EsBQsbWwEESyUgJUIwVp9h9k9hvE+Eg5S5YGnuH13525n94Axo2aDXtBH+k6faYeeBZt0JZk9BFW6TS/pL90Lz9G3MH5CJ3XJ4MzQO2iBNNboF+35oIga/aCfPgjM0ntkvziTTeiiBx8EinaUyTF00akPAgv0CUMWtm2ouyyyCy3a90Eetg3zLhMmaBs659ZluRS1YRl6G2TOjhmfold034wl2EOR7aZxCM2v6bQZlxbKHV83YwmD9Ffu7wv0R7JIwVfojv5xDv0a+YUjssUG7dIfumiyiMy5oUc+kIVywlI0zW/oga3GBY7cNpQhtmHJB2WRmyStkJZUXFaKA+hVa9Etl5VmDvrFY0bIH5eFSNXDG179AAAAAElFTkSuQmCC>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD0AAAAZCAYAAACCXybJAAACrklEQVR4Xu2WTcjOQRTFj3znu2zEQtjIRyRWVmIhkQWlLCwsLEWk7GVBKUmIXpJCCslCLJ7yLpSNBVkpiZSypFA4x/1P/zvTPPNMWdH86tT7zsz/npm5M3ceoNFo/KOsoyanjSnLqfPUM+oddYWaG42ImUNdg419QV2kzlCXKrUdMX/jL52jFrv+AbXA/Z9lPrWTOkj9oj7DJpJjAnWE+g4bu4s6Sv2gvqJf2M2u7T61l9oPW9hL6ixivL9ilPyF91f8bdQMah/1GLYhq7u/1VbkOHUDFizNRkAL2k19od7DJjwOO1KeY7A485L2mdTmpC0g/5Mo+yvL3n+R65tIbaE+wOa0qWsbyjTqASwLMtWkU5RlGR6AjXkIW4B2dpIbp1jq05gUbUIui8F/K8r+hxD767uAz/Ra2MKLmdaO6U4dhgW8HHf/YQM1lRpDP7FT1B4/CBZLWcgtWndNpyMl+C9B2f8CYv8cA1TcaaGM3YUdq9wu6lhehU34Fey+bnT9HsX6CbubtQR/eZb8l2G0f1X1VnAZylg7/RHxfVkB2/np6E/CHcRHOqDJDWBjTsRdQ/H+ouQvSv7VaKFPqYXoM6lCoR2TkQxlLGQmU92rHLqvyrDG6H7W4P2F9xfeXwst+Vezg7oNC6jS/wQWWEddwb3BW9izst61eRRL3ypbWkwN3l94f+H9tTEl/2pUsXVsA6p+MlXbddiRDeiuKhO5YiRC9U/vZImSvzLs/XUFSv5VzKIeIS4K4Y09DSv9HrWPwZ6PHM9hY/Tm1lLyV7X2qE6U/Eeih/sW9YZaiT5QqL46ZgH1raG+df05U2UkHO1VyI/xyH8pyv76MSKC/6euf1TsLL7gBI27vtewd3EKdS8ZF6RClYvjNexZyX0n/9ldX/AXJf9Go9FoNBr/Ab8BjdTTEpr3Ar4AAAAASUVORK5CYII=>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAZCAYAAABZ5IzrAAABjklEQVR4Xu2UPyhHURTHj1DKTxYmJhOLwkSYzCYmG4Pd+JsoBqtFSckkUUg2g7KYiLIblFIyGQz+fL+/+26/807v7+9nMNxPfYZ3z7v3nXveuVckECjMCGyxg542uFPCRTdNphNiaa7DXjetximsqOcYA/ALnkl9gXf4A2/gEtyC19HYhbhNHEfPd2refTRWhXNwDR7BNzgEN+A+3Iaj8BZOiaIDnuiBCC76Ii5ZDRdbjtwVl5inDz6Jm2vhJvitdrgAX+E5HBbz65g1AxZfCS7i4ccP4Aw8hOMqRjj+La4aFlaY6ApNwAcxFWI/rOoB0CX1smv4z1l+boI90B0P197nPP5aCyuqyewhCz/InXLHRWElWVEm5KuRReYp0/ClPXENq/sjj1lJ77um6IGPcMUGcmBVmNAl7DSxphiDH3DSBnK4EpcQm/ZPYfNxYVaqDDxZZfsuF33ZFWo4Bec8w34baBSeknlxu/yErfFwKnxvUFxCmxK/txrCNzEXTJK3ahK+idMsc0IDgUDg3/AL1Tpn6gO6izUAAAAASUVORK5CYII=>

[image9]: <data:image/png;base64,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>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABcAAAAaCAYAAABctMd+AAABN0lEQVR4Xu3TvyuFURzH8a9CBrc7sCgDpW6uZJCUGCnDNSsmljsxGFCyWewWAxkkmS0GA3VLiewU/4JikR/vr3PO7TzfHoqH7fnUa3i+39O385znPCJ5/jlltNtiA1awbazGi8gc9n1PLSTbsoeKqX0OH8ED3lHDNPrjRf55B9eYR6+vX2Ecm5jAOpp9rx7dlQ7XHXyVWbSaWglHuMct1hJdnw1xw4/RYnqaLlzYIunGgbjhd1hMdH30vHS4Hk+H6Y3hFG2mHif1zEOG8IxHDET1Ik7Enet3Sb0tITpQB79gNKovYQuNUe3H0aMINya8Xh8u0RMW/TYFnIsbvuxrh6jWV2SMfpRwHTsxnGxni+5Yh5+J+2H0B/uzzIgb/oYb08ucSXHDXzFlepkziCfsosn08uTJk5IPpnY54XpsD9IAAAAASUVORK5CYII=>

[image11]: <data:image/png;base64,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>

[image12]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB8AAAAZCAYAAADJ9/UkAAABgklEQVR4Xu2WPShFYRjH/0KR7yiDMlkMGGQwW6RIstkYiMGoKIsMJmURMRhsZJDNoJSU2SQDi4miDBb8/57zds99ur6ue06JX/26ned5u+95nvejA/zz1xmkm3TduUbrY+MSoY0O0236Qqei5x5aGhuXGFX0GDZ56rTSW/roE2kwBKv6zCfSYAU2+YZPJE1o+QPtcLnEibe8zuWEYkU++A10akZ8MPBZyxUv8cEvUk1P6KpPCFWlijV5rrdTxQM+WCjiR6zT5YRijT5YKHZhVet2C+vaRMfoPX2OYmKatsPG1kSxLdiyeWZoC6y4C7jCuukTbOKPDOe+mPbRZnoexYQmP4o9B3qjXy3ZJaygH9MF+zMR9st7G1Us0gNa5hP5MI5MN9TKO2Sq9FTQQzrrE/nQAGt5ODrLsAmE9o5eJL62BW/5FewWrHQ5MYrsG1It30H+d0QWoeW5bsFyukBr6Rys2lPYqfkROoKT9IZe0/ns9BsTtB+2sfboPl1CSh8jv4NXoExOlRqlxLoAAAAASUVORK5CYII=>

[image13]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAkAAAAaCAYAAABl03YlAAAAy0lEQVR4XtXQP8tBYRjH8Uso5SmkLJifTAYTsT2ryYuw2JVXoQxk8QJY5UWQvARssj1lkML3dPlz35fsfOuTOr+T+5wj8l1FEbIX3TJYomwHt1/skLODLWkvuP0gLW+eJ44uVthg5s9aDy3Rf6jj4s/aQPS1gzry5qbC7TeGKQ7O9lIVJ4zs4NYWPapph3sRTESPKpntURZrzJHyp2d/OIs+j/cx86jI863+UXRvCNrfhhqO6Is+m1fwugtsMUbCn7UGhqJHhs32sV0BvWQfdNIisdkAAAAASUVORK5CYII=>

[image14]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAZCAYAAAB3oa15AAACWElEQVR4Xu2Xz0tVQRTHv5JBUEhBFJEgtJEgkIh2QYsiBFFctAjaCC7atLXAoF3QOqIoglq1igpECIlyIW38DxJBgwiCWkQuoh/2/XJm8tx5c++bByE+eB/4Is6ZOd+5M3Pm3gf06NHDc5y6Rz2kPgS9DP9Ld6gL1O7Qfz9128WbNB3GRLzXa7T3KuIgNUldp/5QN6mLQZrAW2qTWg7991Jj1FRof0ddCv2ly9QD6jN1y4b8w3v9RNVL8l6DYUwxMpun9qQBmKESH3Ft56kvsFXNsY8aTxsD8lK+Jq/1NNCEVlVbqsEp/dQzWNLDrl2TWIRNNHISlkuo/bSLRaKX8qV4r9Uk1sgx6hN1Jg2Qo9QaLGlfaIuT0Jn1vMLW1g9QQy4WiV46Qine62411MwEWldYaMLXQuy9a4+T0LiI+s4hfyw80Su3wt4r9/BZtNWLsIHxFpK+Ukuwgt0VOwe08uofi1eF+xz5HfR4r++oev1G3qstKkIVo26gEvwkPKdgRyCS2wnvpUughHOwBYrHtwUFNZm1pL2OugfWhFSEQn+fuljEe/mHrUN1pGv6PrZyt/AIllTVX0LJA5+A3ekp3qt2Qp1wAPbSUNIrSSyHtvExmh9Yb1H1uZoG0JlXETOwhB+p4SSWY5T6Qf2izrp2Fd4hagGWT1dgemZVE6VeGqt3ko7rCqy+KoxQ32AJvdSew7982mkDVcM6L7XVoe8tLZauXF23JfWyI2n6vOkKtOuzaWM30dXHR/y363a70O1zg3oCW/n0B9GOR8X6gnoD+zDs6JdZj+3iL29ypR/5RFjtAAAAAElFTkSuQmCC>

[image15]: <data:image/png;base64,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>

[image16]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAZCAYAAABZ5IzrAAACFUlEQVR4Xu2VPUgdQRSFT8BARFOEiCIKESRICP6AiBARizRaaBEDEYykUxsVBBEEsRBbizSJIohCsA2IP0gKwdIiVaqQQpF0iSBYhniOd0Zmx32Cutu9Dz54zN23c+fO3RmgSJFsmKLLkWW0nM6lxD7Y39ASjX+m9S52Zx7QV/SI/qff6aAbf0hf02kXW6Nv6bPLfwI1dJge04+0h5a62L3RZH7SmOew2GQcIG9g1ckcn9AWfRSMl9BPLqZKhTylm/RlNJ4JM7BJ92G94+mkOy62EIwLJRgnmRm+Tw7oYzemxL7SDhcLt1NVUXVUpVzohU2q5q6mdbAJa108rt46rOlzQ1+IJj2nrXSRvg/iYUKqShZ9owWN0aY4IJSEkvEJbSD5CSuhX7SKjsKOhfvSTv/SvjggfEKaeAD2cIjfTt/kuaO+8YejeieugMZPYdv2LhnKhyf0EDZx2DuecDvT0LGhqv6h/bDnftIX4UOOSlj/jOD6MXOFBvfpnvsdo4nmcb1ynmbYBFqUFudbQF9vTCPsPavO1HfqRO5G4ctRL9aFWwi99AvsThO6D89giabhd0SLyIUK+gOWiNDKd1H4slWi6tm2OJAVWulvuk3HaVcQUx99Q7IVbtyuLNB2rcCaVdWKmUVyy7Vdvpq5EG5XGhOwE14VHIJ9gQ2JJzJEH8I/2PmlizhGldGdqARO6BLsqipyay4AJTBtPIEpTMwAAAAASUVORK5CYII=>

[image17]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAAYCAYAAAAcYhYyAAAAw0lEQVR4XmNgGAWjgDzADMRiQMyILkEMiAHi20CsCuUfAeJJCGniwAkgXsqAcMF/IG6AyxIJHgLxLwaI7dpALMIA8RpJgBuIC4H4EhD/BeKrDBCDiAZqQOyMxBcC4rdArIkkhhewAPFyIJ6DJg4KI34oG0RPA+JaBoja9UA8ASoHBwZAfBqIZwHxPiB+xIAaxUFALA3E5VC+LhDLI6QRQBiIJaE0tjSiBMQu6IKkAk8GiGsoAq1AzIEuSCrgQhcYBbgBAOO9GFu+xnAIAAAAAElFTkSuQmCC>

[image18]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABQAAAAZCAYAAAAxFw7TAAABCElEQVR4XmNgGAWjYPACASBmRRckB3gC8TMgvgLEb4E4C4gZUVSQANYA8XEg5ofy3wPxRSAWhqsgERwA4v9AvByIXRggBvEgKyAVNDNADIThTgYKwxGkORKI9wDxLwaIoREoKkgAEkAczYCIAGYGiIHlcBUkgjlArI/EFwLiWQwIL4cAsR8Q3wZicSDmAOJWqFwwEN+CsuFAHohvAPFcIN4AxJ+AmBtJPgiI50MxyBdKDJCIAwFBIJ4EZaMAUGKWZIC4AFtkgFzhAWWDDJOBskGGV0HZJIG7DAhDQGEL8wEoONyhbJLANiCexwBJXiCvgwydCMRGyIpIBaBgAWEQEGHAHjSjgEIAANdIJfxPsPAYAAAAAElFTkSuQmCC>