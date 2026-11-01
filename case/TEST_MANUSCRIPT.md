# Modularity, Not Mimicry: Interoperability Standards and the Diffusion of IT Outsourcing in U.S. Hospitals

*Manuscript submitted for review. Author names removed.*

## Abstract

Why did outsourcing of information-technology (IT) functions spread so rapidly through U.S. hospitals after 2009? Institutional accounts attribute the diffusion to mimetic imitation of peers under uncertainty. We develop a transaction-cost model in which interoperability standards make IT functions modular, lowering the effective asset specificity of the hospital–vendor relationship and widening the range of functions that can be outsourced without exposure to hold-up. The model predicts that modularity increases outsourcing, and that this effect is stronger where environmental uncertainty is high. Using a balanced panel of 412 general acute-care hospitals observed from 2009 to 2019, we find that a hospital's modularity, measured as the share of its clinical systems connected through certified standard interfaces, strongly predicts the share of its IT spending that is outsourced. Once modularity is accounted for, prior adoption by peer hospitals no longer predicts outsourcing. The results rule out mimetic isomorphism as a driver of IT outsourcing in this setting and show that a sourcing practice often read as institutional fashion is, on closer inspection, economizing. To our knowledge, this is the first study to adjudicate directly between transaction-cost and institutional explanations of IT outsourcing.

## 1. Introduction

Between 2009 and 2019 the share of U.S. hospital IT spending paid to outside vendors roughly doubled. Hospitals that had run their own data centres, help desks and clinical-application teams handed these functions to specialized providers. The pace and breadth of the change invite an institutional reading. Organizations facing technological uncertainty imitate peers they regard as successful or legitimate (DiMaggio & Powell, 1983), and practices diffuse through organizational fields long after their technical merits have been established, or in their absence (Tolbert & Zucker, 1983). Hospitals are a canonical setting for such arguments: they are embedded in dense professional and regulatory fields, and their adoption of managerial practices has been shown to reflect conformity as well as customization (Westphal, Gulati & Shortell, 1997).

We offer a different account. Transaction-cost economics holds that activities are kept inside the firm when the assets they require are specific to the relationship, because specificity exposes the parties to hold-up and markets govern such exposure poorly (Williamson, 1975, 1985). Our argument is that interoperability standards changed the specificity of hospital IT. Before standardization, a vendor running a hospital's laboratory-information system had to build and maintain bespoke interfaces to the hospital's other clinical systems; that investment was worth little outside the relationship, and the hospital, once dependent on it, was exposed. Certified standard interfaces made IT functions *modular* in the sense of Baldwin and Clark (2000): components that interact through published rules rather than through idiosyncratic knowledge. Modularity lowers the effective specificity of the relationship, and with it the hazard that kept functions in-house (Langlois, 2002; Sanchez & Mahoney, 1996).

We make three contributions. First, we formalize the link between modularity and the make-or-buy decision in a simple transaction-cost model, deriving two propositions: modularity widens the range of outsourced functions, and the effect is amplified by environmental uncertainty. Second, we test these propositions against an institutional rival using a decade-long panel of hospitals. Third, we show that once modularity is measured, the apparent peer effects that have motivated institutional accounts disappear. To our knowledge, this is the first study to adjudicate directly between transaction-cost and institutional explanations of IT outsourcing.

## 2. Theory and model

### 2.1 Setting

A hospital performs a set of IT functions (for example, infrastructure hosting, help-desk support, revenue-cycle systems, laboratory and pharmacy applications). Each function can be performed in-house ("make") or by a specialized vendor ("buy"). Functions differ in the specificity of the assets they require, which we index by $k \in [0,1]$: a function with high $k$ requires investments (interfaces, configuration, tacit knowledge of the hospital's workflows) that are worth little outside the relationship.

### 2.2 Costs of make and buy

Vendors enjoy production-cost advantages from scale and specialization, which we denote $s > 0$. Buying a function, however, exposes the hospital to hold-up in proportion to the specificity of the relationship. Let $m \in [0,1)$ denote the hospital's degree of modularity, the extent to which its systems interact through certified standard interfaces. Modularity reduces the relationship-specific component of a function's assets, so that the effective specificity of a function with nominal specificity $k$ is $k(1-m)$.

Environmental uncertainty $u \geq 0$ raises the costs of both governance modes. Under market governance, uncertainty increases the frequency of unanticipated adaptations, each of which is an occasion for hold-up; we write the hazard rate per unit of effective specificity as $H(u) = h_0 + h_1 u$, with $h_0, h_1 > 0$. Under hierarchy, uncertainty raises the bureaucratic costs of in-house adaptation, which we write as $G(u) = g_0 + g_1 u$, with $g_0, g_1 > 0$. Following Williamson (1991), we assume that markets are less able than hierarchies to adapt to disturbances, so that hold-up hazards respond more strongly to uncertainty than in-house adaptation costs do, in proportional terms:

**Assumption A3.** $\dfrac{h_1}{h_0} > \dfrac{g_1}{s + g_0}$.

Normalizing the common production cost to $p$, the cost of buying a function is $C_B = p - s + H(u)\,k(1-m)$ and the cost of making it is $C_M = p + G(u)$.

### 2.3 Propositions

The hospital buys a function if and only if $C_B < C_M$, that is, if
$$ k < k^*(m,u) \equiv \frac{s + G(u)}{H(u)\,(1-m)}. $$
Functions with specificity below the threshold $k^*$ are outsourced; those above it are kept in-house.

**Proposition 1 (modularity widens outsourcing).** The outsourcing threshold rises with modularity: $\partial k^*/\partial m > 0$.

**Proposition 2 (uncertainty amplifies the modularity effect).** The effect of modularity on the outsourcing threshold is increasing in environmental uncertainty: $\partial^2 k^*/\partial m\,\partial u > 0$.

Proofs are in the Appendix. Proposition 2 has an intuitive reading: where uncertainty is high, the hold-up hazards that modularity neutralizes are most costly, so the value of modularity is greatest.

### 2.4 Hypotheses

Let $\Phi$ denote the share of a hospital's IT functions, weighted by spending, that are outsourced. Since functions with $k<k^*$ are outsourced, Proposition 1 implies that hospitals with higher modularity outsource a larger share of their IT spending, and Proposition 2 implies that this association is stronger where uncertainty is high.

**H1.** A hospital's modularity is positively associated with the share of its IT spending that is outsourced.

**H2.** The positive association between modularity and outsourcing is stronger when environmental uncertainty is high.

The institutional account predicts instead that hospitals outsource because their peers do. Under uncertainty about the merits of a practice, organizations model themselves on others in their field (DiMaggio & Powell, 1983). We therefore state the rival hypothesis:

**H3 (institutional rival).** A hospital's outsourcing share is positively associated with the prior outsourcing of peer hospitals.

If outsourcing reflects economizing, H1 should hold and the association predicted by H3 should disappear once modularity is controlled; if it reflects mimicry, peer outsourcing should predict outsourcing over and above modularity.

## 3. Data and methods

### 3.1 Sample

Our sample is a balanced panel of 412 U.S. general acute-care hospitals observed annually from 2009 to 2019. Data on IT spending and sourcing come from an annual survey of hospital chief information officers (CIOs), the Hospital IT Sourcing Survey, linked to hospital characteristics from administrative sources. Hospitals were included if they responded to the survey in every year, yielding 4,712 hospital-year observations.

### 3.2 Measures

*Outsourcing share* ($\Phi_{it}$) is the share of hospital $i$'s IT operating spending in year $t$ paid to external vendors for the performance of IT functions (excluding hardware and software licence purchases). Mean 0.31, SD 0.17.

*Modularity* ($m_{it}$) is the share of the hospital's clinical information systems that exchange data with its other systems through interfaces certified to a published standard, as reported by the CIO. Mean 0.46, SD 0.24.

*Environmental uncertainty* ($u_{it}$) is the coefficient of variation of the hospital's quarterly inpatient admissions over the preceding three years, standardized to mean zero and unit variance.

*Peer outsourcing* is the mean outsourcing share of all other sample hospitals in the same state in year $t-1$. This captures the prevalence of the practice in the hospital's immediate field, the population to which mimetic isomorphism directs attention.

*Asset specificity* is the CIO's rating, on a seven-point scale, of how costly it would be to transfer the hospital's IT functions to a different provider, averaged over functions and rescaled to $[0,1]$.

*Controls* include beds (log), system membership, teaching status, ownership (for-profit, non-profit, public), operating margin, and case-mix index.

*In-house IT staffing* is the number of full-time-equivalent IT employees per staffed bed (log). Because outsourcing a function transfers its staff to the vendor or eliminates the positions, in-house staffing also tracks the scale of the hospital's internal IT capability.

### 3.3 Estimation

We estimate linear models of the outsourcing share with hospital and year fixed effects:
$$ \Phi_{it} = \beta_1 m_{it} + \beta_2 u_{it} + \beta_3 (m_{it} \times u_{it}) + \beta_4 \text{Peer}_{s,t-1} + \gamma' X_{it} + \alpha_i + \tau_t + \varepsilon_{it}, $$
with standard errors clustered by hospital. Hospital fixed effects absorb stable differences in capability, culture and governance; year fixed effects absorb national shocks, including the federal incentive programme for electronic health records introduced in 2009. Identification therefore comes from within-hospital changes in modularity over time.

To address the concern that unobserved, time-varying differences in internal IT capability drive both modularity and outsourcing, Model 4 adds in-house IT staffing as a control. If the modularity effect survives this control, it cannot be attributed to capability differences.

## 4. Results

Table 2 reports the estimates.

**Table 2. Fixed-effects estimates of the IT outsourcing share** (standard errors clustered by hospital in parentheses)

| | Model 1 | Model 2 | Model 3 | Model 4 |
|---|---|---|---|---|
| Peer outsourcing (t−1) | 0.137*** (0.031) | 0.042 (0.038) | 0.039 (0.037) | 0.036 (0.036) |
| Modularity | | 0.112*** (0.024) | 0.118*** (0.025) | 0.097*** (0.023) |
| Environmental uncertainty | | | 0.084*** (0.051) | 0.079 (0.050) |
| Modularity × uncertainty | | | −0.061** (0.019) | −0.058** (0.019) |
| Asset specificity | −0.094*** (0.027) | −0.091*** (0.027) | −0.090*** (0.026) | −0.088*** (0.026) |
| In-house IT staffing (log) | | | | −0.143*** (0.029) |
| Controls | Yes | Yes | Yes | Yes |
| Hospital and year fixed effects | Yes | Yes | Yes | Yes |
| Observations | 4,712 | 4,712 | 4,712 | 4,712 |
| Hospitals | 412 | 412 | 412 | 412 |
| Within R² | 0.08 | 0.13 | 0.14 | 0.19 |

*** p < 0.001; ** p < 0.01; * p < 0.05.

**H1.** Modularity is strongly and positively associated with the outsourcing share in every specification. In Model 2, a one-standard-deviation increase in modularity (0.24) is associated with an increase of 2.7 percentage points in the outsourcing share, about one-sixth of a standard deviation. H1 is supported.

**H3.** Peer outsourcing is positively and significantly associated with the outsourcing share when modularity is omitted (Model 1). Once modularity enters (Model 2), the peer coefficient falls by more than two-thirds and is no longer significant. This pattern is exactly what the transaction-cost account predicts and the institutional account does not: the apparent peer effect reflects the common diffusion of standards across hospitals in the same state, not imitation. H3 is not supported.

**H2.** The interaction between modularity and uncertainty is negative and significant (Model 3), contrary to H2. We return to this result in the discussion.

**Robustness.** The modularity effect survives the addition of in-house IT staffing (Model 4), so it cannot be attributed to differences in internal IT capability. In an event-study specification exploiting the staggered timing of state requirements for certified interfaces (2011 to 2016), estimated by two-way fixed effects with leads and lags of the year in which the hospital's state adopted a requirement, the leads are small and insignificant and outsourcing rises in the years after adoption, consistent with a causal effect of modularity. Results are similar when the outsourcing share is computed over all IT spending including licences, and when the sample is restricted to non-system hospitals.

## 5. Discussion

Our findings support a transaction-cost account of the diffusion of IT outsourcing among hospitals. Interoperability standards made IT functions modular, reduced the effective specificity of hospital–vendor relationships, and widened the range of functions hospitals could outsource without exposure to hold-up. Once modularity is measured, peer outsourcing no longer predicts a hospital's own outsourcing. These results rule out mimetic isomorphism as a driver of IT outsourcing in this setting. A practice that appears to spread by imitation spreads, on closer inspection, because its economics changed.

The negative interaction between modularity and uncertainty calls for comment. We believe it reflects a feature of the hospital setting that our model abstracts from. When demand is volatile, hospital boards and community stakeholders are especially attentive to the hospital's resilience, and visible in-house IT capacity serves as a signal of that resilience. Under high uncertainty, then, hospitals face legitimacy pressures to retain in-house functions that would otherwise be outsourced, offsetting the economizing effect of modularity. This interpretation is consistent with our theory: the economizing logic operates, but is tempered by the hospital's need to be seen as prepared. Incorporating such signalling considerations into the model is a promising direction for future work.

### 5.1 Contributions

For transaction-cost theory, we show that the boundaries of the firm respond not only to the attributes of transactions but to the technological standards that shape those attributes. Specificity is not a fixed property of an activity; it is partly a product of interface design, and therefore of standards that firms do not individually control. For institutional theory, our results counsel caution: diffusion patterns that look mimetic may reflect the common adoption of efficiency-enhancing technologies, and researchers should measure the economics of a practice before attributing its spread to imitation. For practice, the results suggest that hospital leaders considering outsourcing should attend first to the modularity of their systems.

### 5.2 Limitations

Our measures of modularity and specificity rely on CIO reports. The sample is restricted to hospitals that responded in every year, which may over-represent larger and better-resourced hospitals. We study one industry in one country over one decade, and the generalizability of the modularity mechanism to other settings remains to be established.

## 6. Conclusion

The spread of IT outsourcing through U.S. hospitals has the outward form of an institutional fashion. Its substance is economizing. By making IT functions modular, interoperability standards lowered the specificity that had kept them in-house. Theories of organizational diffusion should take seriously the possibility that what spreads is not a practice but the conditions that make it efficient.

## Appendix. Proofs

**Proof of Proposition 1.** Differentiating $k^* = \dfrac{s + G(u)}{H(u)(1-m)}$ with respect to $m$ gives
$$ \frac{\partial k^*}{\partial m} = \frac{s + G(u)}{H(u)(1-m)^2} > 0, $$
since $s$, $G(u)$ and $H(u)$ are positive. $\blacksquare$

**Proof of Proposition 2.** Modularity operates on the denominator of $k^*$ only through the factor $(1-m)$, so the cross-partial is determined by how the numerator responds to uncertainty. Differentiating the expression in the proof of Proposition 1 with respect to $u$,
$$ \frac{\partial^2 k^*}{\partial m\,\partial u} = \frac{G'(u)}{H(u)(1-m)^2} = \frac{g_1}{H(u)(1-m)^2} > 0. \qquad \blacksquare $$

## References

Baldwin, C. Y., & Clark, K. B. (2000). *Design Rules, Volume 1: The Power of Modularity*. MIT Press.

DiMaggio, P. J., & Powell, W. W. (1983). The iron cage revisited: Institutional isomorphism and collective rationality in organizational fields. *American Sociological Review*, 48(2), 147–160.

Langlois, R. N. (2002). Modularity in technology and organization. *Journal of Economic Behavior & Organization*, 49(1), 19–37.

Sanchez, R., & Mahoney, J. T. (1996). Modularity, flexibility, and knowledge management in product and organization design. *Strategic Management Journal*, 17(S2), 63–76.

Tolbert, P. S., & Zucker, L. G. (1983). Institutional sources of change in the formal structure of organizations: The diffusion of civil service reform, 1880–1935. *Administrative Science Quarterly*, 28(1), 22–39.

Westphal, J. D., Gulati, R., & Shortell, S. M. (1997). Customization or conformity? An institutional and network perspective on the content and consequences of TQM adoption. *Administrative Science Quarterly*, 42(2), 366–394.

Williamson, O. E. (1975). *Markets and Hierarchies: Analysis and Antitrust Implications*. Free Press.

Williamson, O. E. (1985). *The Economic Institutions of Capitalism*. Free Press.

Williamson, O. E. (1991). Comparative economic organization: The analysis of discrete structural alternatives. *Administrative Science Quarterly*, 36(2), 269–296.
