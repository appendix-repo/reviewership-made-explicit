# Run 09: Adversarial Probe, identification and numerical consistency (Part 1)

## 0. Run metadata

- **Role:** Role 4, Adversarial Probe (capability 3). Instruction set: Reviewership v0.1 (23 October 2026).
- **Manuscript:** `ms:TEST`, "Modularity, Not Mimicry: Interoperability Standards and the Diffusion of IT Outsourcing in U.S. Hospitals".
- **Probe types:** P-ID, P-NUM.
- **Target:** the estimation strategy (`ms:§3.3`), Table 2 (`ms:T2`), the robustness claims in `ms:§4`, and every reported statistic in `ms:§3` and `ms:§4`.
- **Status:** Part 1 (steps 1 to 3). No check has been run. Every finding below is `asserted`. Step 4 (disposition) waits for the harness output.
- **Perspective:** no perspective specification came with this assignment. I use these working defaults and state them wherever they matter. The reviewer should confirm them (see Decisions).
  - INF.2: MI6 is endorsed only with its own proviso ("absent time-varying confounders"). MI7 is not endorsed.
  - EPI.5: intervals and equivalence tests count for more than significance.
  - TEC.4: always.
- **Basis convention:** "says" means the manuscript states it, with the locus cited. "Inferred" means this scorekeeper draws it from what the manuscript states.
- **Simulation assumptions not given in the manuscript** (each check flags them again where it uses them):
  - the number of states (50);
  - how many hospitals make up each state's field (40);
  - how many states adopted a requirement for certified interfaces (40 of 50, in 2011 to 2016 as `ms:§4` says);
  - all variance and effect parameters. These are illustrative, chosen to be of the same order as the moments reported in `ms:§3.2` and `ms:T2`.

## 1. Reconstruction (L14 ArgMap; Explain classifies each step)

| Step | Locus | From → to | Presented as | Reconstructed as |
|---|---|---|---|---|
| `p09:arg:1` | `ms:§3.3` | Two-way FE, SEs clustered by hospital → β1 is identified "from within-hospital changes in modularity over time" | deductive | inductive, under MI6. The proviso (no time-varying confounding, no feedback from Φ to m) is not argued |
| `p09:arg:2` | `ms:§3.3`, `ms:§4` | β1 survives the in-house staffing control (Model 4) → the effect "cannot be attributed to capability differences" | deductive | invalid: the control is a descendant of the outcome by `ms:§3.2` (see `p09:fnd:5`) |
| `p09:arg:3` | `ms:§2.4`, `ms:§4` | The peer coefficient is significant in Model 1 and not significant in Model 2 → the peer association "reflects the common diffusion of standards ... not imitation" | deductive ("exactly what the transaction-cost account predicts") | abductive, and it relies on MI7. A rival (mimicry operating through modularity, or through a noisily measured field) predicts the same pattern (`p09:fnd:6`, `p09:fnd:7`) |
| `p09:arg:4` | Abstract; `ms:§5` | `p09:arg:3` → results "rule out mimetic isomorphism as a driver" | deductive | Extend: the scope goes beyond the evidence. Non-significance is read as absence (`p09:fnd:3`) |
| `p09:arg:5` | `ms:§4` Robustness | The TWFE event study on state requirements shows small leads and a later rise in outsourcing → "consistent with a causal effect of modularity" | inductive | abductive. The estimand is the effect of state requirements on outsourcing. No first stage or exclusion argument is given. TWFE under staggered adoption is at risk of contamination (`p09:fnd:9`) |
| `p09:arg:6` | `ms:§4` Robustness | Results with licences included, and in the non-system subsample, are "similar" | inductive | deferred to unreported estimates, so they cannot be checked |
| `p09:arg:7` | `ms:§4` H1 | 0.112 × 0.24 → 2.7 pp ≈ one-sixth of an SD | deductive (arithmetic) | deductive; checked in `p09:chk:4` |
| `p09:arg:8` | `ms:§4` H2; `ms:§5` | The negative interaction is "contrary to H2" → a legitimacy-signalling rescue | abductive | outside these probe types; referred (`p09:ref:1`, `p09:ref:2`) |

## 2. Scoreboard

```json
{
  "Scoreboard": {
    "id": "p09:sb:1",
    "manuscript": "ms:TEST",
    "scorekeeper": "p09 (Adversarial Probe; P-ID, P-NUM)",
    "commitments": [
      {"id": "p09:cmt:1", "type": "avowed", "text": "Two-way FE estimates of beta1 identify the effect of modularity from within-hospital change.", "locus": "ms:§3.3 'Identification therefore comes from within-hospital changes in modularity over time.'", "entitlement": "challenged", "basis": "MI6 endorsed only with its proviso; proviso (no time-varying confounding, no feedback) not argued", "challenges": ["p09:chl:1"]},
      {"id": "p09:cmt:2", "type": "avowed", "text": "Hospital FE absorb stable capability, culture, governance; year FE absorb national shocks incl. the 2009 EHR incentive programme.", "locus": "ms:§3.3", "entitlement": "default"},
      {"id": "p09:cmt:3", "type": "avowed", "text": "If the modularity effect survives the in-house staffing control, it cannot be attributed to capability differences.", "locus": "ms:§3.3; ms:§4 Robustness", "entitlement": "unentitled", "challenges": ["p09:chl:2"]},
      {"id": "p09:cmt:4", "type": "avowed", "text": "In-house IT staffing falls when functions are outsourced, and also tracks internal IT capability.", "locus": "ms:§3.2 'outsourcing a function transfers its staff to the vendor or eliminates the positions'", "entitlement": "default"},
      {"id": "p09:cmt:5", "type": "consequential", "text": "In-house staffing is a descendant of the outcome Phi (and of capability); conditioning on it neither blocks the capability path nor leaves beta1 unbiased.", "inference": "from p09:cmt:4 by the back-door criterion (Pearl 2009, to verify)", "entitlement": "default"},
      {"id": "p09:cmt:6", "type": "avowed", "text": "The Model 1 to Model 2 change shows the peer association reflects common diffusion of standards within states, not imitation.", "locus": "ms:§4 H3 'the apparent peer effect reflects the common diffusion of standards across hospitals in the same state, not imitation'", "entitlement": "unentitled", "challenges": ["p09:chl:3"]},
      {"id": "p09:cmt:7", "type": "avowed", "text": "The results rule out mimetic isomorphism as a driver of IT outsourcing in this setting.", "locus": "Abstract; ms:§5 'These results rule out mimetic isomorphism as a driver'", "entitlement": "unentitled", "basis": "rests on MI7 (not endorsed) and on p09:cmt:6", "challenges": ["p09:chl:3", "p09:chl:4"]},
      {"id": "p09:cmt:8", "type": "avowed", "text": "Under economizing, the H3 association should disappear once modularity is controlled.", "locus": "ms:§2.4 last paragraph", "entitlement": "challenged", "challenges": ["p09:chl:3"]},
      {"id": "p09:cmt:9", "type": "consequential", "text": "beta4 in Model 2 is the association of Peer with Phi net of m (a direct effect), not the total association that H3 states.", "inference": "regression anatomy (Frisch-Waugh-Lovell) applied to the ms:§3.3 equation", "entitlement": "default"},
      {"id": "p09:cmt:10", "type": "avowed", "text": "Balanced panel of 412 hospitals observed annually 2009-2019; 4,712 hospital-year observations in every model.", "locus": "ms:§3.1; ms:T2 Observations", "entitlement": "challenged", "challenges": ["p09:chl:5"]},
      {"id": "p09:cmt:11", "type": "avowed", "text": "Peer = mean outsourcing share of all other sample hospitals in the same state in t-1; it captures the field mimetic isomorphism attends to.", "locus": "ms:§3.2 Peer outsourcing", "entitlement": "challenged", "challenges": ["p09:chl:6"]},
      {"id": "p09:cmt:12", "type": "avowed", "text": "H1: one SD of modularity (0.24) is associated with +2.7 pp outsourcing, about one-sixth of an SD; effect is 'strong' 'in every specification'.", "locus": "ms:§4 H1", "entitlement": "evidenced", "basis": "arithmetic pending p09:chk:4"},
      {"id": "p09:cmt:13", "type": "avowed", "text": "Modularity and the outsourcing share are both reported by the CIO for the same hospital-year.", "locus": "ms:§3.1 (CIO survey); ms:§3.2 Modularity 'as reported by the CIO'", "entitlement": "default"},
      {"id": "p09:cmt:14", "type": "avowed", "text": "Model 3 uncertainty main effect: 0.084, SE 0.051, p < 0.001.", "locus": "ms:T2.M3.uncertainty", "entitlement": "challenged", "challenges": ["p09:chl:5"]},
      {"id": "p09:cmt:15", "type": "avowed", "text": "Model 2 peer coefficient 0.042 (SE 0.038).", "locus": "ms:T2.M2.peer", "entitlement": "evidenced"},
      {"id": "p09:cmt:16", "type": "avowed", "text": "TWFE event study on staggered state requirements (2011-2016): small insignificant leads, outsourcing rises after adoption, 'consistent with a causal effect of modularity'.", "locus": "ms:§4 Robustness", "entitlement": "challenged", "challenges": ["p09:chl:7"]},
      {"id": "p09:cmt:17", "type": "avowed", "text": "Results similar with licences included in the outsourcing share, and in the non-system subsample.", "locus": "ms:§4 Robustness", "entitlement": "challenged", "basis": "no estimates reported", "challenges": ["p09:chl:8"]},
      {"id": "p09:cmt:18", "type": "avowed", "text": "Standard errors clustered by hospital.", "locus": "ms:§3.3; ms:T2 header", "entitlement": "challenged", "challenges": ["p09:chl:9"]},
      {"id": "p09:cmt:19", "type": "consequential", "text": "Year FE absorb national shocks only; state-year shocks to outsourcing (e.g., the state requirements of ms:§4) remain in the error and in lagged Peer.", "inference": "from p09:cmt:2 and ms:§4 (state requirements are state-year events)", "entitlement": "default"}
    ],
    "incompatibilities": [
      {"id": "p09:inc:1", "pair": ["p09:cmt:3", "p09:cmt:5"], "reason": "A control that the outcome itself moves (cmt:4) cannot certify that a coefficient is free of confounding; survival under it is uninformative."},
      {"id": "p09:inc:2", "pair": ["p09:cmt:10", "p09:cmt:10"], "reason": "Internal: 412 x 11 = 4,532, not 4,712; with Peer lagged one year at most 412 x 10 = 4,120 rows carry Peer from in-window data."},
      {"id": "p09:inc:3", "pair": ["p09:cmt:7", "p09:cmt:15"], "reason": "'Rule out' is incompatible with a reported estimate whose 95% interval reaches about 0.117, 85% of the Model 1 association."},
      {"id": "p09:inc:4", "pair": ["p09:cmt:14", "p09:cmt:14"], "reason": "Internal: 0.084/0.051 = 1.65, two-sided p about 0.10, not < 0.001."}
    ],
    "challenges": [
      {"id": "p09:chl:1", "on": "p09:cmt:1", "request": "Exclude time-varying confounding (capability; differential exposure to EHR incentives) and feedback from outsourcing to same-year reported modularity."},
      {"id": "p09:chl:2", "on": "p09:cmt:3", "request": "Give a control for capability that is not caused by outsourcing (pre-determined, or measured before the sourcing change)."},
      {"id": "p09:chl:3", "on": ["p09:cmt:6", "p09:cmt:7", "p09:cmt:8"], "request": "Show that within-state co-movement of peer outsourcing and own modularity is a common cause rather than peers -> own modularity -> outsourcing."},
      {"id": "p09:chl:4", "on": "p09:cmt:7", "request": "Report an interval and an equivalence test against a stated smallest effect of interest, and a test of the change in the peer coefficient."},
      {"id": "p09:chl:5", "on": ["p09:cmt:10", "p09:cmt:14"], "request": "Reconcile N with the panel design and the lag; correct the Model 3 uncertainty cell."},
      {"id": "p09:chl:6", "on": "p09:cmt:11", "request": "Report hospitals per state, how Peer is defined where a state has one sample hospital, and the reliability of the sample mean as a measure of field prevalence."},
      {"id": "p09:chl:7", "on": "p09:cmt:16", "request": "Report estimator, window, binning, reference period, coefficients, cohorts, never-treated states; first stage on modularity; exclusion argument."},
      {"id": "p09:chl:8", "on": "p09:cmt:17", "request": "Report the estimates."},
      {"id": "p09:chl:9", "on": ["p09:cmt:18", "p09:cmt:19"], "request": "Cluster at the state level (Peer and the standards component of m vary by state-year) and address persistent state shocks."}
    ]
  }
}
```

## 3. Findings (step 2)

Each finding below is `asserted`. Severities are provisional until step 4.

### 3.1 P-NUM findings

```json
[
  {
    "id": "p09:fnd:1", "probe_type": "P-NUM", "status": "asserted", "check": "p09:chk:1",
    "locus": "ms:§3.1 'balanced panel of 412 ... observed annually from 2009 to 2019' and '4,712 hospital-year observations'; ms:T2 Observations (all models)",
    "commitment": "p09:cmt:10",
    "incompatibility": "says: 412 hospitals, 2009-2019, balanced, 4,712 obs. inferred: 412 x 11 = 4,532; 4,712/412 = 11.44 is not an integer, so 4,712 cannot be a balanced 412-hospital panel. Peer is measured 'in year t-1' (ms:§3.2) and enters all four models, so unless 2008 survey data exist outside the stated window, at most 412 x 10 = 4,120 rows carry Peer. Any state with a single sample hospital has no 'other sample hospitals' and no Peer (inferred; number of states not reported).",
    "severity": "fixable",
    "severity_note": "Raise to damaging if the estimation sample turns out not to be the described panel (e.g., unbalanced or including non-respondent years).",
    "repair": "Report the estimation sample of each model; say how Peer is built for 2009 and for states with one sample hospital; report the number of states and hospitals per state."
  },
  {
    "id": "p09:fnd:2", "probe_type": "P-NUM", "status": "asserted", "check": "p09:chk:2",
    "locus": "ms:T2.M3.uncertainty '0.084*** (0.051)'",
    "commitment": "p09:cmt:14",
    "incompatibility": "inferred: t = 0.084/0.051 = 1.65; two-sided p about 0.10 (normal or t with 411 df); *** requires p < 0.001. The Model 4 cell 0.079 (0.050), unstarred, is consistent, which isolates Model 3 as the error. The check sweeps all 16 coefficient cells, allowing for rounding of the third decimal.",
    "severity": "minor",
    "severity_note": "The uncertainty main effect is not a hypothesis. But one of coefficient, SE or stars is mistranscribed, and the reviewer cannot tell which from the table; if the SE column is affected, the H2 interaction's precision may be too.",
    "repair": "Correct the cell from the estimation output; confirm the other Model 3 cells against the same output."
  },
  {
    "id": "p09:fnd:3", "probe_type": "P-NUM", "status": "asserted", "check": "p09:chk:3",
    "locus": "ms:T2.M2.peer '0.042 (0.038)'; ms:§4 H3; Abstract 'no longer predicts' and 'rule out'; ms:§5",
    "commitment": "p09:cmt:7 (with p09:cmt:15)",
    "missing_entitlement": "inferred: the reported statistics do not license absence. 95% CI for the Model 2 peer coefficient is about [-0.033, 0.117]; its upper end is 85% of the Model 1 association (0.137). A TOST equivalence test against a margin of half the Model 1 association fails, and the smallest margin at which equivalence could be declared at alpha = .05 is about 0.105. The fall from 0.137 to 0.042 is described but not tested; the test needs the covariance of the two estimates, which is not reported. The move from 'no longer significant' to 'no effect' is MI7, which this scorekeeper does not endorse (EPI.5 default).",
    "severity": "damaging",
    "repair": "Report the interval; pre-justify a smallest effect of interest and run an equivalence test; test the change in the peer coefficient (stacked or seemingly-unrelated estimation, or a cluster bootstrap); replace 'rule out' with a bounded statement."
  },
  {
    "id": "p09:fnd:4", "probe_type": "P-NUM", "status": "asserted", "check": "p09:chk:4",
    "locus": "ms:§4 H1 '2.7 percentage points ... about one-sixth of a standard deviation'; ms:§4 H3 'falls by more than two-thirds'; ms:§4 H1 'in every specification'",
    "commitment": "p09:cmt:12",
    "missing_entitlement": "Candidate finding that the check is expected to refute: 0.112 x 0.24 = 0.0269 (2.7 pp); 0.0269/0.17 = 0.158 (about one-sixth); (0.137 - 0.042)/0.137 = 0.69 (more than two-thirds). Residual points (inferred): (a) the SDs used are pooled SDs (ms:§3.2), while identification is within-hospital (ms:§3.3); the within SDs are not reported, so the effect of a typical within-hospital change is unknown and likely smaller; 'strongly' is then generous for one-sixth of a pooled SD. (b) In Models 3-4, 0.118 and 0.097 are effects at u = 0 (u is standardized, ms:§3.2). The modularity effect is zero at u = 0.118/0.061 = 1.93 SD (Model 3) and 0.097/0.058 = 1.67 SD (Model 4), so 'in every specification' holds only at mean uncertainty.",
    "severity": "minor",
    "repair": "Report within-hospital SDs of m and Phi; report the marginal effect of m across the range of u with intervals (needs the covariance of beta1 and beta3)."
  }
]
```

### 3.2 P-ID findings

```json
[
  {
    "id": "p09:fnd:5", "probe_type": "P-ID", "status": "asserted", "check": "p09:chk:5",
    "locus": "ms:§3.3 'If the modularity effect survives this control, it cannot be attributed to capability differences'; ms:§4 Robustness; ms:T2.M4; ms:§3.2 In-house IT staffing",
    "commitment": "p09:cmt:3",
    "incompatibility": "p09:inc:1. says (ms:§3.2): outsourcing a function moves or eliminates its staff, so staffing is caused by the outcome Phi; staffing 'also tracks' capability. inferred: staffing is a descendant of Phi and of the confounder. Conditioning on a descendant of the outcome does not block the capability path and itself biases beta1, in a direction that depends on unknown parameters. So survival of the coefficient (0.118 -> 0.097) is uninformative about confounding, and so is its fall. The within-R2 jump from 0.14 to 0.19 is expected mechanically, since the control partly re-measures the outcome. The same simulation also shows that within-hospital FE do not remove time-varying confounding (Model 3 analogue under a zero effect), which bears on p09:chl:1.",
    "severity": "damaging",
    "severity_note": "This is the only defence the manuscript offers against time-varying confounding of H1, and it fails. H1 as an association is not refuted; its causal reading (ms:§5, ms:§6) is left unprotected.",
    "repair": "Drop Model 4 as a robustness test. Use a capability measure fixed before the sourcing change (baseline staffing x year, or staffing lagged before the function was outsourced); or use the mandate-based design as an instrument with a reported first stage; or report a sensitivity analysis for omitted time-varying confounding (e.g., Oster 2019; Cinelli & Hazlett 2020, both to verify)."
  }
]
```

```json
[
  {
    "id": "p09:fnd:6", "probe_type": "P-ID", "status": "asserted", "check": "p09:chk:6",
    "locus": "ms:§2.4 last paragraph; ms:§4 H3; ms:T2.M1-M2 peer; Abstract; ms:§5; title",
    "commitment": "p09:cmt:6, p09:cmt:7, p09:cmt:8",
    "missing_entitlement": "says (ms:§4): peer outsourcing and own modularity co-move within states ('common diffusion of standards'). inferred: Model 2's beta4 is the peer association net of m (p09:cmt:9). If some of that co-movement runs peers -> own adoption of certified interfaces -> outsourcing (MI3 applied to the interface standard; or hospitals preparing to follow peers into outsourcing by modularizing first), then controlling for m removes the mimetic path, and the Table 2 pattern (peer significant in Model 1, falling by more than two-thirds and losing significance in Model 2, m significant) is predicted by mimicry as well as by economizing. The manuscript offers no evidence on the direction of the peer-modularity link. Its test therefore does not discriminate, and 'rule out' (and the title's 'Not Mimicry') lacks entitlement.",
    "severity": "fatal",
    "severity_note": "Fatal for the adjudication claim (title, Abstract, contribution 3, ms:§5, ms:§6). It does not touch H1 as an association. If the reviewer reads the central claim as H1 alone, downgrade to damaging (see Decisions).",
    "repair": "Estimate peers -> own modularity directly (does lagged peer prevalence predict own m, conditional on state requirements?). Report total and direct peer effects with the mediation assumptions stated. Use the timing of state requirements to separate coercive from voluntary (mimetic) adoption of interfaces. Find exogenous variation in peers (referent groups that cross state lines, e.g., system or vendor networks). Or restate the claim as one about direct effects net of modularity."
  },
  {
    "id": "p09:fnd:7", "probe_type": "P-ID", "status": "asserted", "check": "p09:chk:6",
    "locus": "ms:§3.2 Peer outsourcing; ms:§3.1 sample; ms:T2.M2 peer",
    "commitment": "p09:cmt:11",
    "missing_entitlement": "says: Peer is the mean of the other sample hospitals in the state (ms:§3.2), and the sample is the 412 hospitals that answered every year (ms:§3.1). inferred: with about 8 sample hospitals per state (412/50; the number of states is not reported), Peer measures field prevalence with sampling error. In a contest with a correlated regressor measured hospital by hospital (m), a noisy proxy's coefficient is pushed toward zero even when direct imitation exists. 'No longer significant' is then partly a measurement artefact.",
    "severity": "damaging",
    "repair": "Build field prevalence from all hospitals in the state (administrative or vendor-contract data), not only the 412 respondents. Use the referents that MI3 names (peers perceived as legitimate or successful: system, size band, network ties). Report reliability, and correct for errors in variables."
  },
  {
    "id": "p09:fnd:8", "probe_type": "P-ID", "status": "asserted", "check": "p09:chk:7",
    "locus": "ms:§3.3 'Identification therefore comes from within-hospital changes in modularity over time'; ms:§3.2 Modularity 'as reported by the CIO'; ms:§1 vendor 'had to build and maintain bespoke interfaces'",
    "commitment": "p09:cmt:1, p09:cmt:13",
    "missing_entitlement": "MI6 holds only with its proviso. says: m and Phi are same-year CIO reports (ms:§3.1-3.2), and a vendor that takes over a function builds its interfaces (ms:§1). inferred: once standards exist, outsourcing a function plausibly raises the share of certified interfaces, so Phi -> m in the same year. Within-hospital FE do not exclude this feedback. Lagging m does not cure it if errors are serially correlated. An instrument that moves m and not Phi directly (the state requirements of ms:§4) would.",
    "severity": "damaging",
    "severity_note": "Damaging for the causal reading of H1 ('economizing', ms:§5-6). H1 as an association stands.",
    "repair": "Use function-level timing (was a function's interface certified before it was outsourced?); use m at t-1 together with tests for serial correlation; use 2SLS with state requirements, reporting the first stage and an exclusion argument; verify modularity from certification records rather than the same informant."
  },
  {
    "id": "p09:fnd:9", "probe_type": "P-ID", "status": "asserted", "check": "p09:chk:8",
    "locus": "ms:§4 Robustness (event study, 'staggered timing of state requirements ... (2011 to 2016)', 'two-way fixed effects with leads and lags')",
    "commitment": "p09:cmt:16",
    "missing_entitlement": "(a) bound to the check: TWFE event studies under staggered adoption can be contaminated by effects from other periods and cohorts when effects are dynamic and differ by cohort (Sun & Abraham 2021; Goodman-Bacon 2021; Callaway & Sant'Anna 2021; de Chaisemartin & D'Haultfoeuille 2020; all to verify). So 'leads are small and insignificant' is not a clean pre-trend test, and such tests also have low power (Roth 2022, to verify). (b) argued, not bound: the treatment is the state requirement and the outcome is Phi, so the design identifies the effect of requirements on outsourcing. Attributing it to modularity needs a first stage (requirement -> m) and an exclusion restriction (requirements affect Phi only through m); neither is reported or argued. (c) No coefficients, window, binning, reference period, cohort sizes, never-treated count or clustering level are reported, so the claim cannot be checked.",
    "severity": "fixable",
    "severity_note": "Raise to damaging if the authors rely on the event study as their causal evidence (it is the design best placed to answer p09:fnd:5 and p09:fnd:8).",
    "repair": "Use a heterogeneity-robust estimator; report all event-time coefficients with intervals, cohorts and never-treated states, with SEs clustered by state; report the first stage on m and the implied Wald/IV estimate with an explicit exclusion argument."
  },
  {
    "id": "p09:fnd:10", "probe_type": "P-ID", "status": "asserted", "check": "p09:chk:9",
    "locus": "ms:§3.3 'standard errors clustered by hospital'; ms:T2 header; ms:§3.2 Peer (state-level)",
    "commitment": "p09:cmt:18",
    "missing_entitlement": "inferred: Peer is (nearly) constant within a state-year, and per ms:§4 m has a state-level component. With any state-year component in the error, hospital clustering understates SEs for state-level regressors (Moulton 1990; Cameron & Miller 2015; to verify). This inflates the Model 1 peer significance. It does not rescue the Model 2 null, which would be even less significant.",
    "severity": "fixable",
    "repair": "Cluster by state (or two-way, by state and hospital), with a small-cluster correction such as the wild cluster bootstrap given about 50 clusters."
  },
  {
    "id": "p09:fnd:11", "probe_type": "P-ID", "status": "asserted", "check": "p09:chk:9",
    "locus": "ms:§2.4 H3; ms:§3.3 year FE absorb 'national shocks'; ms:T2.M1 peer",
    "commitment": "p09:cmt:19 (with p09:cmt:11)",
    "missing_entitlement": "inferred: year FE remove national shocks only. Persistent state-level shocks to outsourcing make lagged state-mean outsourcing predict own outsourcing with no imitation at all (correlated effects; Manski 1993, to verify). So the Model 1 association is not evidence of mimicry, and its disappearance is not evidence against mimicry. Together with p09:fnd:6-7, the H3 design identifies neither the presence nor the absence of mimetic effects.",
    "severity": "damaging",
    "repair": "Exposure to peers needs variation within a state-year: referent groups that cross states, or the partial-overlap designs of the peer-effects literature (Bramoullé, Djebbari & Fortin 2009, to verify). State-by-year FE are not available, because Peer varies only at the state-year level."
  }
]
```

### 3.3 Severity summary

| Finding | Probe | Short title | Severity (provisional) | Check |
|---|---|---|---|---|
| `p09:fnd:1` | P-NUM | N = 4,712 is inconsistent with 412 × 2009–2019 and with lagged Peer | fixable | `p09:chk:1` |
| `p09:fnd:2` | P-NUM | Model 3 uncertainty: stars inconsistent with coefficient/SE | minor | `p09:chk:2` |
| `p09:fnd:3` | P-NUM | A peer null is read as absence; the interval admits large effects | damaging | `p09:chk:3` |
| `p09:fnd:4` | P-NUM | H1 magnitude arithmetic (expected sound), plus scope remarks | minor | `p09:chk:4` |
| `p09:fnd:5` | P-ID | In-house staffing is a bad control (descendant of the outcome) | damaging | `p09:chk:5` |
| `p09:fnd:6` | P-ID | Model 2 conditions on a possible mediator of mimicry | fatal (adjudication claim) | `p09:chk:6` |
| `p09:fnd:7` | P-ID | Noisy peer proxy in a contest with a better-measured regressor | damaging | `p09:chk:6` |
| `p09:fnd:8` | P-ID | Reverse timing: same-year outsourcing → reported modularity | damaging | `p09:chk:7` |
| `p09:fnd:9` | P-ID | Staggered TWFE event study; estimand is mandates, not modularity | fixable | `p09:chk:8` |
| `p09:fnd:10` | P-ID | Hospital clustering for a state-year regressor | fixable | `p09:chk:9` |
| `p09:fnd:11` | P-ID | Correlated state shocks: Peer coefficient does not identify mimicry | damaging | `p09:chk:9` |

## 4. Strengths found (step 5, provisional)

- **Stars and SEs.** The stars agree with coefficient/SE in 15 of the 16 coefficient cells of `ms:T2` by my reading (`p09:chk:2` will confirm). The Model 4 uncertainty cell is internally consistent.
- **Magnitudes.** The H1 magnitude and the "more than two-thirds" fall are arithmetically right by my reading (`p09:chk:4` is expected to refute `p09:fnd:4`'s arithmetic part).
- **Rival stated in advance.** The manuscript states its rival (H3) before testing it and tries to name a discriminating prediction (`ms:§2.4`). That is the right form, even though the prediction chosen does not discriminate (`p09:fnd:6`).
- **Unwelcome result reported.** The H2 result, contrary to the authors' hypothesis, is reported rather than hidden (`ms:§4`).
- **Right kind of design.** Exploiting the staggered state requirements is the right kind of design. Run as an instrumented design with a reported first stage, it could repair `p09:fnd:5` and `p09:fnd:8`.
- **No other inconsistency found.** Within R² rises monotonically (0.08, 0.13, 0.14, 0.19), and the reported means and SDs (`ms:§3.2`) are feasible for [0,1] shares. I find no inconsistency there.

## 5. Considered and not raised

- **Within R² against clustered t-ratios.** Taken at face value, the gain from 0.08 to 0.13 when m enters implies a conventional t of about 15.7 for modularity, against the clustered 4.67, a ratio of about 3.4. Serial correlation within hospitals can produce this. It cannot be settled without the data, so I raise nothing.
- **Selection on response.** The sample keeps only hospitals that answered every year (`ms:§3.1`). If outsourcing changes who answers the CIO survey, selection depends on the outcome. This is speculative; `ms:§5.2` acknowledges a related limitation.
- **Interaction under fixed effects.** The FE estimate of m × u can carry between-hospital variation unless the product is formed from within-demeaned terms (Giesselmann & Schmidt-Catran 2022, to verify). This is relevant to H2 but secondary given `p09:ref:1`.

## 6. Referrals outside P-ID and P-NUM (asserted; no check from this probe)

- **`p09:ref:1` (to P-DER): Proposition 2.** From `ms:§2.2` to `ms:§2.3`, ∂²k*/∂m∂u = [g1·H(u) − h1·(s + G(u))] / [H(u)²(1 − m)²]. The numerator reduces to g1·h0 − h1·(s + g0), which does not depend on u and is negative under Assumption A3. On this reading the model predicts a *negative* interaction on the k* scale. The Appendix proof drops the H′(u) term ("the cross-partial is determined by how the numerator responds to uncertainty"). If a P-DER check confirms this, then "contrary to H2" (`ms:§4`) and the legitimacy rescue (`ms:§5`) rest on a derivation error. This bears on how Table 2's interaction should be read.
- **`p09:ref:2` (to P-DER/P-INF): scale of the test.** H2 is tested on Φ, a spending-weighted share, while Proposition 2 concerns the threshold k*. Carrying the sign from k* to Φ needs the distribution of k and the spending weights.
- **`p09:ref:3` (to P-INF): coercive isomorphism.** The event study's source of variation is state requirements, which are coercive pressure in DiMaggio & Powell's (1983) sense. Diffusion driven by mandates is itself an institutional mechanism, so the "economizing versus institutional" framing needs care.
- **`p09:ref:4` (to P-MEAS): the peer construct.** Peer is a state mean of respondent hospitals. MI3's construct is referents perceived as legitimate or successful.
- **`p09:ref:5` (to P-LIT): priority.** "First study to adjudicate directly" (Abstract, `ms:§1`) is not checked here.

## 7. Checks (step 3; not run)

Every check is self-contained, uses only `numpy`, `scipy`, `statsmodels` and `pandas`, sets its own random seed, and prints one or more lines beginning `VERDICT:`. Its premises come from the manuscript's own statements, cited in comments. Where a simulation needs a quantity the manuscript does not give, the comment marks it `ASSUMPTION`.

### p09:chk:1

```json
{"CheckSpec": {"id": "p09:chk:1", "finding_ids": ["p09:fnd:1"], "probe_type": "P-NUM", "method": "arithmetic recomputation", "premises": ["ms:§3.1 balanced panel, 412 hospitals, 2009-2019", "ms:§3.1 and ms:T2: 4,712 observations", "ms:§3.2 Peer measured in t-1; Peer in all models (ms:T2)"], "verdict_rule": "DEMONSTRATED if 4,712 equals neither 412 x 11 nor 412 x 10 and is not a multiple of 412"}}
```

```python
# p09:chk:1 -- observation count against the stated panel design (P-NUM)
# ms:§3.1: "a balanced panel of 412 U.S. general acute-care hospitals observed annually from 2009 to 2019"
# ms:§3.1: "yielding 4,712 hospital-year observations"; ms:T2: Observations 4,712 in Models 1-4
# ms:§3.2: Peer outsourcing is measured "in year t-1"; it enters all four models (ms:T2)
hospitals = 412
first_year, last_year = 2009, 2019
years = last_year - first_year + 1
reported_n = 4712
balanced_n = hospitals * years
lagged_n = hospitals * (years - 1)   # Peer(t-1) cannot be formed for 2009 from in-window data
print(f"years in window (inclusive): {years}")
print(f"balanced panel N = {hospitals} x {years} = {balanced_n}")
print(f"N with Peer(t-1) from in-window data = {hospitals} x {years - 1} = {lagged_n}")
print(f"reported N = {reported_n}; reported N / {hospitals} = {reported_n / hospitals:.3f} years per hospital")
print(f"reported - balanced = {reported_n - balanced_n}")
if reported_n in (balanced_n, lagged_n):
    print("VERDICT: REFUTED-BY-CHECK - the reported N matches the stated design.")
elif reported_n % hospitals != 0:
    print(f"VERDICT: DEMONSTRATED - 4,712 is not a multiple of 412, so it cannot be a balanced 412-hospital panel; "
          f"expected {balanced_n} (all years) or at most {lagged_n} for models with Peer(t-1).")
else:
    print("VERDICT: INCONCLUSIVE - N is a multiple of 412 but matches neither expected count.")
```

### p09:chk:2

```json
{"CheckSpec": {"id": "p09:chk:2", "finding_ids": ["p09:fnd:2"], "probe_type": "P-NUM", "method": "recompute |t| and two-sided p for every Table 2 cell; star range allowed by rounding of printed coefficient and SE, under normal and t(411) references", "premises": ["ms:T2 coefficients, SEs, stars", "ms:T2 note: *** p<0.001; ** p<0.01; * p<0.05", "ms:T2: 412 hospital clusters"], "verdict_rule": "DEMONSTRATED if any cell's printed stars lie outside the range attainable under rounding; REFUTED-BY-CHECK if none"}}
```

```python
# p09:chk:2 -- stars against coefficient/SE for every cell of Table 2 (P-NUM)
from scipy import stats

# ms:T2 as printed: (row, model, coefficient, SE, number of stars)
cells = [
    ("Peer outsourcing (t-1)", "M1", 0.137, 0.031, 3),
    ("Peer outsourcing (t-1)", "M2", 0.042, 0.038, 0),
    ("Peer outsourcing (t-1)", "M3", 0.039, 0.037, 0),
    ("Peer outsourcing (t-1)", "M4", 0.036, 0.036, 0),
    ("Modularity", "M2", 0.112, 0.024, 3),
    ("Modularity", "M3", 0.118, 0.025, 3),
    ("Modularity", "M4", 0.097, 0.023, 3),
    ("Environmental uncertainty", "M3", 0.084, 0.051, 3),
    ("Environmental uncertainty", "M4", 0.079, 0.050, 0),
    ("Modularity x uncertainty", "M3", -0.061, 0.019, 2),
    ("Modularity x uncertainty", "M4", -0.058, 0.019, 2),
    ("Asset specificity", "M1", -0.094, 0.027, 3),
    ("Asset specificity", "M2", -0.091, 0.027, 3),
    ("Asset specificity", "M3", -0.090, 0.026, 3),
    ("Asset specificity", "M4", -0.088, 0.026, 3),
    ("In-house IT staffing (log)", "M4", -0.143, 0.029, 3),
]
DF = 412 - 1      # ms:T2: 412 hospital clusters; t(G-1) reference
HALF = 0.0005     # printed values are rounded to three decimals


def stars(p):
    return 3 if p < 0.001 else 2 if p < 0.01 else 1 if p < 0.05 else 0


def p_two(t, dist):
    return 2 * (stats.norm.sf(t) if dist == "normal" else stats.t.sf(t, DF))


mismatches = []
print(f"{'row':28s} {'mod':3s} {'coef':>7s} {'se':>6s} {'|t|':>6s} {'p(t411)':>9s} {'printed':>7s} {'attainable':>11s}")
for row, mod, b, se, st in cells:
    t = abs(b) / se
    p = p_two(t, "t")
    t_lo = (abs(b) - HALF) / (se + HALF)
    t_hi = (abs(b) + HALF) / (se - HALF)
    ok = set()
    for dist in ("normal", "t"):
        s_lo, s_hi = stars(p_two(t_lo, dist)), stars(p_two(t_hi, dist))
        ok |= set(range(min(s_lo, s_hi), max(s_lo, s_hi) + 1))
    flag = ""
    if st not in ok:
        mismatches.append(f"{row} {mod}: {b} ({se}) printed {'*' * st}, |t|={t:.2f}, p={p:.4f}")
        flag = "  <-- MISMATCH"
    print(f"{row:28s} {mod:3s} {b:7.3f} {se:6.3f} {t:6.2f} {p:9.5f} {st:7d} {str(sorted(ok)):>11s}{flag}")

print(f"cells checked: {len(cells)}; mismatches: {len(mismatches)}")
if mismatches:
    print("VERDICT: DEMONSTRATED - stars inconsistent with coefficient/SE (robust to rounding) in: " + "; ".join(mismatches))
else:
    print("VERDICT: REFUTED-BY-CHECK - all printed stars are attainable from the printed coefficients and SEs.")
```

### p09:chk:3

```json
{"CheckSpec": {"id": "p09:chk:3", "finding_ids": ["p09:fnd:3"], "probe_type": "P-NUM", "method": "interval, TOST equivalence, and bounds on the test of the coefficient change, from printed estimates", "premises": ["ms:T2.M1.peer 0.137 (0.031)", "ms:T2.M2.peer 0.042 (0.038)", "Abstract / ms:§5: 'rule out mimetic isomorphism'"], "verdict_rule": "DEMONSTRATED (claim of absence not entitled) if TOST at margin 0.5 x Model 1 estimate fails (p >= .05) and the 95% CI upper bound exceeds that margin; else REFUTED-BY-CHECK"}}
```

```python
# p09:chk:3 -- does Table 2 license 'no longer predicts' / 'rule out'? (P-NUM)
from scipy import stats

b1, se1 = 0.137, 0.031   # ms:T2, Peer, Model 1
b2, se2 = 0.042, 0.038   # ms:T2, Peer, Model 2
DF = 411                 # 412 hospital clusters (ms:T2)
t975, t95 = stats.t.ppf(0.975, DF), stats.t.ppf(0.95, DF)

lo, hi = b2 - t975 * se2, b2 + t975 * se2
print(f"Model 2 peer: 95% CI = [{lo:.4f}, {hi:.4f}]; upper bound = {hi / b1:.2f} x Model 1 estimate")

delta_min = abs(b2) + t95 * se2
print(f"smallest symmetric margin at which TOST declares equivalence (alpha=.05): {delta_min:.4f} "
      f"= {delta_min / b1:.2f} x Model 1 estimate")

margin = 0.5 * b1
p_upper = stats.t.cdf((b2 - margin) / se2, DF)   # H0: beta >= +margin
p_lower = stats.t.sf((b2 + margin) / se2, DF)    # H0: beta <= -margin
p_tost = max(p_upper, p_lower)
print(f"TOST, margin = 0.5 x Model 1 estimate = {margin:.4f}: p = {p_tost:.3f}")

print(f"change M1 - M2 = {b1 - b2:.3f}; the covariance of the two estimates is not reported, so the test is bounded:")
for rho in (0.0, 0.5, 0.8, 0.9):
    sd = (se1 ** 2 + se2 ** 2 - 2 * rho * se1 * se2) ** 0.5
    z = (b1 - b2) / sd
    print(f"  assumed rho={rho:.1f}: se={sd:.4f}, z={z:.2f}, p={2 * stats.norm.sf(abs(z)):.4f}")

if p_tost >= 0.05 and hi > margin:
    print(f"VERDICT: DEMONSTRATED - the Model 2 peer estimate is not shown equivalent to zero (TOST p={p_tost:.3f} at margin "
          f"{margin:.3f}); its 95% CI reaches {hi:.3f}. Non-significance does not license 'rule out'.")
else:
    print("VERDICT: REFUTED-BY-CHECK - the Model 2 peer estimate is statistically equivalent to zero at the stated margin.")
```

### p09:chk:4

```json
{"CheckSpec": {"id": "p09:chk:4", "finding_ids": ["p09:fnd:4"], "probe_type": "P-NUM", "method": "arithmetic recomputation of reported magnitudes; zero-crossing of the marginal effect of m", "premises": ["ms:T2.M2 modularity 0.112", "ms:§3.2 SD(m)=0.24, SD(Phi)=0.17", "ms:T2 peer 0.137 -> 0.042", "ms:T2.M3-M4 modularity and interaction", "ms:§3.2 u standardized"], "verdict_rule": "REFUTED-BY-CHECK (arithmetic sound) if 2.7 pp, about one-sixth SD (within 0.02) and a fall of more than two-thirds all reproduce; else DEMONSTRATED"}}
```

```python
# p09:chk:4 -- H1 magnitude, the 'two-thirds' fall, and where the modularity effect crosses zero (P-NUM)
from scipy import stats

b_m2, sd_m, sd_phi = 0.112, 0.24, 0.17      # ms:T2.M2 modularity; ms:§3.2 SDs (pooled)
eff = b_m2 * sd_m
ratio = eff / sd_phi
drop = (0.137 - 0.042) / 0.137              # ms:T2 peer, Model 1 -> Model 2
print(f"one-SD effect = {b_m2} x {sd_m} = {eff:.4f} ({eff * 100:.2f} pp); reported 2.7 pp")
print(f"as share of SD(Phi): {ratio:.3f}; one-sixth = {1 / 6:.3f}")
print(f"fall in peer coefficient: {drop:.3f}; two-thirds = {2 / 3:.3f}")
ok = (round(eff * 100, 1) == 2.7) and (abs(ratio - 1 / 6) <= 0.02) and (drop > 2 / 3)

# informational: marginal effect of m = beta1 + beta3*u, u standardized (ms:§3.2)
for label, b1, b3 in (("Model 3", 0.118, -0.061), ("Model 4", 0.097, -0.058)):
    u0 = -b1 / b3
    print(f"{label}: marginal effect of m is zero at u = {u0:.2f} SD; "
          f"share of hospital-years above it if u ~ N(0,1) [ASSUMPTION]: {stats.norm.sf(u0):.3f}")
print("note: SDs are pooled (ms:§3.2); within-hospital SDs, which govern the FE estimand, are not reported.")
if ok:
    print("VERDICT: REFUTED-BY-CHECK - the reported magnitudes (2.7 pp, about one-sixth SD, fall > two-thirds) are arithmetically correct.")
else:
    print("VERDICT: DEMONSTRATED - at least one reported magnitude does not follow from Table 2 and the ms:§3.2 moments.")
```

### p09:chk:5

```json
{"CheckSpec": {"id": "p09:chk:5", "finding_ids": ["p09:fnd:5"], "probe_type": "P-ID", "method": "Monte Carlo from a DGP built from the manuscript's own stated relations; two-way FE OLS, SEs clustered by hospital", "premises": ["ms:§3.3: unobserved time-varying capability drives modularity and outsourcing", "ms:§3.3 eq.: m -> Phi", "ms:§3.2: outsourcing transfers or eliminates in-house IT staff (Phi -> staffing)", "ms:§3.2: staffing tracks internal IT capability (C -> staffing)", "ms:§3.1: 412 hospitals x 11 years"], "scenarios": {"A": "beta=0 (no causal effect), capability confounding present", "B": "beta=0.11 (as ms:T2.M2), no confounding"}, "verdict_rule": "DEMONSTRATED if in A the Model 4 analogue gives a positive coefficient with p<.05 in >=80% of replications (survival is compatible with pure confounding), or if in B Model 4 is biased by >=5% and >3 MC SEs (the control itself biases); INCONCLUSIVE otherwise"}}
```

```python
# p09:chk:5 -- is 'survives the in-house staffing control' informative about capability confounding? (P-ID)
# Model 3/Model 4 analogues: Phi on m (FE), and Phi on m + staffing (FE). Other ms:T2 regressors (u, m x u, Peer,
# controls) are omitted; by construction they are independent of the variables simulated here.
import numpy as np
import statsmodels.api as sm

rng = np.random.default_rng(2026102305)
N, T = 412, 11            # ms:§3.1: 412 hospitals, 2009-2019, balanced
REPS = 200
groups = np.repeat(np.arange(N), T)


def demean2(X):
    """Two-way (hospital, year) within transformation; exact for a balanced panel."""
    return X - X.mean(axis=1, keepdims=True) - X.mean(axis=0, keepdims=True) + X.mean()


def simulate(beta, c, d, a=1.5, b=0.2, rho=0.7):
    # C: unobserved, time-varying internal IT capability, the confounder named in ms:§3.3. ASSUMPTION: AR(1), rho=0.7
    C = np.empty((N, T))
    C[:, 0] = rng.normal(size=N)
    for t in range(1, T):
        C[:, t] = rho * C[:, t - 1] + np.sqrt(1 - rho ** 2) * rng.normal(size=N)
    yr = np.arange(T)[None, :]
    # C -> m (ms:§3.3). ASSUMPTION: capability raises modularity (d >= 0)
    m = rng.normal(0, 0.15, (N, 1)) + 0.03 * yr + d * C + rng.normal(0, 0.10, (N, T))
    # m -> Phi (ms:§3.3 equation) and C -> Phi (ms:§3.3). ASSUMPTION: capability raises outsourcing (c >= 0)
    phi = rng.normal(0, 0.10, (N, 1)) + 0.02 * yr + beta * m + c * C + rng.normal(0, 0.06, (N, T))
    # Phi -> staffing: ms:§3.2 "outsourcing a function transfers its staff to the vendor or eliminates the positions"
    # C -> staffing:   ms:§3.2 staffing "also tracks the scale of the hospital's internal IT capability"
    staff = rng.normal(0, 0.30, (N, 1)) - 0.01 * yr - a * phi + b * C + rng.normal(0, 0.10, (N, T))
    return demean2(phi).ravel(), demean2(m).ravel(), demean2(staff).ravel()


def fit(y, cols):
    r = sm.OLS(y, np.column_stack(cols)).fit(cov_type="cluster", cov_kwds={"groups": groups})
    return r.params[0], r.pvalues[0]


def run(beta, c, d):
    out = np.empty((REPS, 4))
    for i in range(REPS):
        y, m, s = simulate(beta, c, d)
        b3, p3 = fit(y, [m])        # Model 3 analogue
        b4, p4 = fit(y, [m, s])     # Model 4 analogue (adds in-house staffing)
        out[i] = (b3, p3, b4, p4)
    return out


A = run(beta=0.0, c=0.03, d=0.06)
B = run(beta=0.11, c=0.0, d=0.0)

for name, R, beta in (("A: beta=0, capability confounding", A, 0.0), ("B: beta=0.11, no confounding", B, 0.11)):
    print(f"Scenario {name}")
    print(f"  Model 3 analogue: mean b = {R[:, 0].mean():.4f} (MC SE {R[:, 0].std(ddof=1) / np.sqrt(REPS):.4f}); "
          f"share b>0 & p<.05 = {np.mean((R[:, 0] > 0) & (R[:, 1] < 0.05)):.2f}")
    print(f"  Model 4 analogue: mean b = {R[:, 2].mean():.4f} (MC SE {R[:, 2].std(ddof=1) / np.sqrt(REPS):.4f}); "
          f"share b>0 & p<.05 = {np.mean((R[:, 2] > 0) & (R[:, 3] < 0.05)):.2f}; true beta = {beta}")

survive_A = np.mean((A[:, 2] > 0) & (A[:, 3] < 0.05))
bias_B = B[:, 2].mean() - 0.11
mcse_B = B[:, 2].std(ddof=1) / np.sqrt(REPS)
biased_B = abs(bias_B) / 0.11 >= 0.05 and abs(bias_B) > 3 * mcse_B
print(f"A: share of replications in which the modularity effect 'survives' Model 4 with zero true effect = {survive_A:.2f}")
print(f"B: Model 4 bias = {bias_B:+.4f} ({bias_B / 0.11:+.1%} of true beta), MC SE {mcse_B:.4f}")

if survive_A >= 0.8:
    print(f"VERDICT: DEMONSTRATED - under the manuscript's own relations, a modularity coefficient with no causal content "
          f"survives the staffing control (positive, p<.05) in {survive_A:.0%} of replications; survival cannot rule out "
          f"capability confounding." + (f" The control also biases a true effect by {bias_B / 0.11:+.0%}." if biased_B else ""))
elif biased_B:
    print(f"VERDICT: DEMONSTRATED - the staffing control biases the modularity coefficient by {bias_B / 0.11:+.0%} even "
          f"without confounding; Model 4 is not a valid robustness test.")
else:
    print("VERDICT: INCONCLUSIVE - with these parameters the staffing control neither preserves a spurious effect nor "
          "biases a true one; the finding stands as argued only.")
```

### p09:chk:6

```json
{"CheckSpec": {"id": "p09:chk:6", "finding_ids": ["p09:fnd:6", "p09:fnd:7"], "probe_type": "P-ID", "method": "Monte Carlo state-hospital panel; Model 1 and Model 2 analogues (two-way FE, SEs clustered by hospital as in ms:§3.3); test whether DGPs with real mimetic effects reproduce the Table 2 pattern", "premises": ["ms:§3.1: 412 sample hospitals, 2009-2019", "ms:§3.2: Peer = mean of other sample hospitals in the state, t-1", "ms:§4: standards diffuse in common across hospitals in a state; state requirements staggered 2011-2016", "ms:§3.3 eq.: m -> Phi (beta=0.11 as ms:T2.M2)", "ms:§2.4 H3: peers' prior outsourcing -> own outsourcing (the rival)", "ms:§2.4 last paragraph and ms:§4: the pattern taken as discriminating"], "pattern": "M1 peer > 0 with p<.05; M2 peer p>=.05 and <= one-third of M1 peer; M2 modularity > 0 with p<.05", "scenarios": {"i": "economizing only", "ii": "mimicry through modularity (field prevalence -> own m), kappa in {1,2}", "iii": "direct mimicry of field prevalence, observed through the sample-based Peer, theta in {0.10,0.20,0.30}"}, "verdict_rule": "Per finding: DEMONSTRATED if scenario i reproduces the pattern in >=50% of replications and some scenario of the finding's family (ii for fnd:6, iii for fnd:7) also does; INCONCLUSIVE otherwise"}}
```

```python
# p09:chk:6 -- does the Model 1 -> Model 2 peer pattern discriminate economizing from mimicry? (P-ID)
import numpy as np
import statsmodels.api as sm

rng = np.random.default_rng(2026102306)
S = 50                                   # ASSUMPTION: 50 states (the number is not reported)
NPOP = 40                                # ASSUMPTION: hospitals per state in the field (sample + non-sample)
n_s = np.full(S, 412 // S)
n_s[: 412 % S] += 1                      # 412 sample hospitals (ms:§3.1): 12 states with 9, 38 with 8
BURN = list(range(2004, 2009))           # unobserved burn-in years
OBS = list(range(2009, 2020))            # ms:§3.1 observation window
REPS = 100

state = np.repeat(np.arange(S), NPOP)
in_sample = np.concatenate([np.arange(NPOP) < n_s[s] for s in range(S)])
NP = S * NPOP
samp = np.where(in_sample)[0]
samp_state = state[samp]
NS = samp.size
assert NS == 412


def field_mean(x):
    """True field prevalence: mean over all hospitals in the state (sample and non-sample)."""
    return np.bincount(state, weights=x, minlength=S) / NPOP


def demean2(X):
    return X - X.mean(axis=1, keepdims=True) - X.mean(axis=0, keepdims=True) + X.mean()


def simulate(beta, lam, kappa, theta, sig_zeta=0.01):
    adopt = np.full(S, 9999)
    adopters = rng.permutation(S)[:40]                    # ASSUMPTION: 40 of 50 states adopt a requirement
    adopt[adopters] = rng.integers(2011, 2017, size=40)   # ms:§4: requirements adopted 2011-2016
    a = rng.normal(0, 0.10, NP)                           # hospital effects in Phi
    am = rng.normal(0, 0.15, NP)                          # hospital effects in m
    w = np.zeros(S)
    e = rng.normal(0, 0.12, NP)
    phi_prev = a.copy()
    F_prev = field_mean(phi_prev)
    PHI, M, PEER = [], [], []
    for yr in BURN + OBS:
        w = w + rng.normal(0, 0.10, S)
        R = (yr >= adopt).astype(float) + w               # state standards diffusion (ms:§4 'common diffusion of standards')
        e = 0.5 * e + np.sqrt(0.75) * rng.normal(0, 0.12, NP)
        # kappa > 0: field prevalence of outsourcing prompts own adoption of certified interfaces (mimicry via m)
        m = am + 0.03 * (yr - 2009) + lam * R[state] + kappa * F_prev[state] + e
        zeta = rng.normal(0, sig_zeta, S)                 # state-year outsourcing shock (serially independent here)
        # beta: H1 (ms:§3.3 eq.); theta > 0: direct imitation of the field (H3, ms:§2.4)
        phi = (a + 0.02 * (yr - 2009) + beta * m + theta * F_prev[state] + zeta[state]
               + rng.normal(0, 0.06, NP))
        # observed Peer: mean of the OTHER SAMPLE hospitals in the same state in t-1 (ms:§3.2)
        ps = phi_prev[samp]
        ssum = np.bincount(samp_state, weights=ps, minlength=S)
        peer = (ssum[samp_state] - ps) / (n_s[samp_state] - 1)
        if yr in OBS:
            PHI.append(phi[samp]); M.append(m[samp]); PEER.append(peer)
        F_prev = field_mean(phi)
        phi_prev = phi
    # 2009 is dropped: Peer(t-1) would need 2008 data outside the window (see p09:fnd:1)
    PHI, M, PEER = (np.column_stack(z)[:, 1:] for z in (PHI, M, PEER))
    return PHI, M, PEER


def run(beta, lam, kappa, theta):
    out = np.empty((REPS, 7))
    for i in range(REPS):
        PHI, M, PEER = simulate(beta, lam, kappa, theta)
        g = np.repeat(np.arange(NS), PHI.shape[1])
        y, m, p = (demean2(Z).ravel() for Z in (PHI, M, PEER))
        r1 = sm.OLS(y, p[:, None]).fit(cov_type="cluster", cov_kwds={"groups": g})                 # Model 1 analogue
        r2 = sm.OLS(y, np.column_stack([p, m])).fit(cov_type="cluster", cov_kwds={"groups": g})   # Model 2 analogue
        b1, p1 = r1.params[0], r1.pvalues[0]
        b2, p2 = r2.params[0], r2.pvalues[0]
        bm, pm = r2.params[1], r2.pvalues[1]
        pattern = (b1 > 0) and (p1 < 0.05) and (p2 >= 0.05) and (b2 <= b1 / 3) and (bm > 0) and (pm < 0.05)
        out[i] = (b1, p1, b2, p2, bm, pm, float(pattern))
    return out


scenarios = [
    ("i", "economizing only (no mimicry)", dict(beta=0.11, lam=0.25, kappa=0.0, theta=0.0), "none"),
    ("ii", "mimicry through modularity, kappa=1", dict(beta=0.11, lam=0.25, kappa=1.0, theta=0.0), "indirect 0.11"),
    ("ii", "mimicry through modularity, kappa=2", dict(beta=0.11, lam=0.25, kappa=2.0, theta=0.0), "indirect 0.22"),
    ("iii", "direct mimicry, theta=0.10", dict(beta=0.11, lam=0.25, kappa=0.0, theta=0.10), "direct 0.10"),
    ("iii", "direct mimicry, theta=0.20", dict(beta=0.11, lam=0.25, kappa=0.0, theta=0.20), "direct 0.20"),
    ("iii", "direct mimicry, theta=0.30", dict(beta=0.11, lam=0.25, kappa=0.0, theta=0.30), "direct 0.30"),
]
rates = {"i": [], "ii": [], "iii": []}
print("Table 2 for reference: M1 peer 0.137 (0.031)***; M2 peer 0.042 (0.038); M2 modularity 0.112 (0.024)***")
for fam, label, par, true_mim in scenarios:
    R = run(**par)
    rate = R[:, 6].mean()
    rates[fam].append((label, rate))
    print(f"[{fam}] {label} (true mimetic effect of field prevalence: {true_mim})")
    print(f"    M1 peer mean {R[:, 0].mean():.3f}, share p<.05 {np.mean(R[:, 1] < 0.05):.2f} | "
          f"M2 peer mean {R[:, 2].mean():.3f}, share p<.05 {np.mean(R[:, 3] < 0.05):.2f} | "
          f"M2 modularity mean {R[:, 4].mean():.3f}, share p<.05 {np.mean(R[:, 5] < 0.05):.2f} | "
          f"pattern reproduced in {rate:.2f} of replications")

rate_i = rates["i"][0][1]
best_ii = max(rates["ii"], key=lambda x: x[1])
best_iii = max(rates["iii"], key=lambda x: x[1])
if rate_i < 0.5:
    print(f"VERDICT: INCONCLUSIVE - the economizing-only DGP reproduces the Table 2 pattern in only {rate_i:.2f} of "
          f"replications with these parameters, so the comparison is not informative (p09:fnd:6, p09:fnd:7).")
else:
    overall = best_ii[1] >= 0.5 or best_iii[1] >= 0.5
    print(("VERDICT: DEMONSTRATED - " if overall else "VERDICT: INCONCLUSIVE - ")
          + f"economizing-only reproduces the pattern in {rate_i:.2f} of replications; best mimicry DGPs: "
          f"'{best_ii[0]}' {best_ii[1]:.2f}, '{best_iii[0]}' {best_iii[1]:.2f}. "
          + ("The Model 1 -> Model 2 pattern does not discriminate economizing from mimicry." if overall else ""))
    print(("VERDICT: DEMONSTRATED - p09:fnd:6: " if best_ii[1] >= 0.5 else "VERDICT: INCONCLUSIVE - p09:fnd:6: ")
          + f"mimicry operating through modularity reproduces the pattern in {best_ii[1]:.2f} of replications ({best_ii[0]}).")
    print(("VERDICT: DEMONSTRATED - p09:fnd:7: " if best_iii[1] >= 0.5 else "VERDICT: INCONCLUSIVE - p09:fnd:7: ")
          + f"direct mimicry seen through the sample-based Peer reproduces the pattern in {best_iii[1]:.2f} of "
          f"replications ({best_iii[0]}).")
```

### p09:chk:7

```json
{"CheckSpec": {"id": "p09:chk:7", "finding_ids": ["p09:fnd:8"], "probe_type": "P-ID", "method": "Monte Carlo of a simultaneous system with same-year feedback Phi -> m; FE OLS (Model 2 analogue), FE OLS on lagged m, FE 2SLS with state requirements as instrument", "premises": ["ms:§3.1-3.2: m and Phi are same-year CIO reports", "ms:§1: a vendor taking over a function builds its interfaces (basis for the feedback edge, inferred)", "ms:§3.3: two-way FE, SEs clustered by hospital", "ms:§4: staggered state requirements for certified interfaces, 2011-2016"], "scenarios": {"A": "beta=0 (no modularity effect), feedback pi=0.5", "B": "beta=0.11, no feedback (the manuscript's model)"}, "verdict_rule": "DEMONSTRATED if in A the FE OLS coefficient is positive with p<.05 in >=80% of replications; INCONCLUSIVE otherwise. Lagged-m and IV results are reported as information on repairs"}}
```

```python
# p09:chk:7 -- reverse timing: does within-hospital FE exclude same-year feedback from outsourcing to modularity? (P-ID)
import numpy as np
import statsmodels.api as sm

rng = np.random.default_rng(2026102307)
N, S, REPS = 412, 50, 200                # ms:§3.1: 412 hospitals. ASSUMPTION: 50 states
years = np.arange(2009, 2020)            # ms:§3.1
T = years.size
state = np.arange(N) % S


def demean2(X):
    return X - X.mean(axis=1, keepdims=True) - X.mean(axis=0, keepdims=True) + X.mean()


def simulate(beta, pi):
    adopt = np.full(S, 9999)
    adopters = rng.permutation(S)[:40]                    # ASSUMPTION: 40 of 50 states adopt
    adopt[adopters] = rng.integers(2011, 2017, size=40)   # ms:§4: 2011-2016
    Z = (years[None, :] >= adopt[state][:, None]).astype(float)
    eps = np.empty((N, T))
    eps[:, 0] = rng.normal(0, 0.06, N)
    for t in range(1, T):                                 # ASSUMPTION: serially correlated outsourcing shocks
        eps[:, t] = 0.5 * eps[:, t - 1] + np.sqrt(0.75) * rng.normal(0, 0.06, N)
    yr = (years - 2009)[None, :]
    base_m = rng.normal(0, 0.15, (N, 1)) + 0.03 * yr + 0.2 * Z + rng.normal(0, 0.10, (N, T))
    a = rng.normal(0, 0.10, (N, 1))
    # Simultaneous system: Phi = a + .02*yr + beta*m + eps (ms:§3.3 eq.);  m = base_m + pi*Phi (feedback, inferred from ms:§1)
    phi = (a + 0.02 * yr + beta * base_m + eps) / (1 - beta * pi)
    m = base_m + pi * phi
    return phi, m, Z


def ols(y, x, groups):
    r = sm.OLS(y, x[:, None]).fit(cov_type="cluster", cov_kwds={"groups": groups})
    return r.params[0], r.pvalues[0], r.tvalues[0]


def iv(y, m, z, groups):
    b = (z @ y) / (z @ m)
    u = y - b * m
    scores = np.bincount(groups, weights=z * u)
    se = np.sqrt(np.sum(scores ** 2)) / abs(z @ m)
    return b, se


def run(beta, pi):
    out = np.empty((REPS, 7))
    gh_all = np.repeat(np.arange(N), T)
    gs_all = np.repeat(state, T)
    gh_lag = np.repeat(np.arange(N), T - 1)
    for i in range(REPS):
        phi, m, Z = simulate(beta, pi)
        y, x, z = demean2(phi).ravel(), demean2(m).ravel(), demean2(Z).ravel()
        b_ols, p_ols, _ = ols(y, x, gh_all)                                     # Model 2 analogue
        b_lag, p_lag, _ = ols(demean2(phi[:, 1:]).ravel(), demean2(m[:, :-1]).ravel(), gh_lag)   # m at t-1
        _, _, t_fs = ols(x, z, gs_all)                                          # first stage, clustered by state
        b_iv, se_iv = iv(y, x, z, gs_all)
        out[i] = (b_ols, p_ols, b_lag, p_lag, b_iv, se_iv, t_fs)
    return out


A = run(beta=0.0, pi=0.5)
B = run(beta=0.11, pi=0.0)
for name, R, beta in (("A: beta=0, feedback pi=0.5", A, 0.0), ("B: beta=0.11, no feedback", B, 0.11)):
    print(f"Scenario {name} (true beta = {beta})")
    print(f"  FE OLS on m_t:      mean b = {R[:, 0].mean():.4f}; share b>0 & p<.05 = {np.mean((R[:, 0] > 0) & (R[:, 1] < 0.05)):.2f}")
    print(f"  FE OLS on m_(t-1):  mean b = {R[:, 2].mean():.4f}; share b>0 & p<.05 = {np.mean((R[:, 2] > 0) & (R[:, 3] < 0.05)):.2f}")
    print(f"  FE 2SLS (state requirement as instrument): mean b = {R[:, 4].mean():.4f}; mean SE = {R[:, 5].mean():.4f}; "
          f"mean first-stage t = {R[:, 6].mean():.1f}")

spurious = np.mean((A[:, 0] > 0) & (A[:, 1] < 0.05))
lag_spurious = np.mean((A[:, 2] > 0) & (A[:, 3] < 0.05))
if spurious >= 0.8:
    print(f"VERDICT: DEMONSTRATED - with no effect of modularity and same-year feedback from outsourcing to reported "
          f"modularity, the within-hospital FE estimate is positive and significant in {spurious:.0%} of replications "
          f"(mean {A[:, 0].mean():.3f}); lagging m still gives {lag_spurious:.0%}; 2SLS on state requirements gives mean "
          f"{A[:, 4].mean():.3f} (a valid repair only if requirements satisfy exclusion, which ms does not argue).")
else:
    print(f"VERDICT: INCONCLUSIVE - feedback produced a significant positive FE estimate in only {spurious:.0%} of replications.")
```

### p09:chk:8

```json
{"CheckSpec": {"id": "p09:chk:8", "finding_ids": ["p09:fnd:9"], "probe_type": "P-ID", "method": "Monte Carlo of staggered state requirements with cohort-heterogeneous dynamic effects and zero pre-trends; TWFE event study (hospital and year FE, leads and lags) in two specifications: fully saturated relative time, and binned endpoints; compare with the true hospital-year-weighted effects", "premises": ["ms:§4: staggered state requirements 2011-2016; 'two-way fixed effects with leads and lags'", "ms:§3.1: 412 hospitals, 2009-2019"], "assumptions": ["50 states, 40 adopters (6-7 per cohort), 10 never-treated", "effect on Phi grows with time since adoption and is larger for earlier cohorts", "window and binning are not reported; both common choices are run"], "verdict_rule": "DEMONSTRATED if, in either specification, some lead has |mean| > max(3 MC SE, 0.005) or rejects at > 10%, or some lag misses the true weighted effect by > max(3 MC SE, 10%); REFUTED-BY-CHECK for part (a) otherwise. Parts (b)-(c) of p09:fnd:9 are argued and not tested here"}}
```

```python
# p09:chk:8 -- TWFE event study under staggered adoption with heterogeneous dynamic effects (P-ID)
import numpy as np
import statsmodels.api as sm

rng = np.random.default_rng(2026102308)
N, S, REPS = 412, 50, 100                 # ms:§3.1: 412 hospitals. ASSUMPTION: 50 states
years = np.arange(2009, 2020)             # ms:§3.1
T = years.size
state = np.arange(N) % S
NEVER = 9999
groups = np.repeat(state, T)              # cluster by state (the level of treatment)


def demean2(X):
    return X - X.mean(axis=1, keepdims=True) - X.mean(axis=0, keepdims=True) + X.mean()


def draw_adoption():
    adopt = np.full(S, NEVER)
    adopters = rng.permutation(S)[:40]                 # ASSUMPTION: 40 adopting states, 10 never-treated
    adopt[adopters] = 2011 + (np.arange(40) % 6)       # ms:§4: cohorts 2011-2016, each non-empty
    return adopt[state]


def true_effect(adopt_h):
    rel = years[None, :] - adopt_h[:, None]
    treated = (adopt_h < NEVER)[:, None] & (rel >= 0)
    slope = 0.003 * (2017 - adopt_h)[:, None]          # ASSUMPTION: earlier cohorts gain more per year
    return np.where(treated, slope * (rel + 1), 0.0), rel


def dummies(rel, never, spec):
    ever = ~never[:, None]
    cols, labels = [], []
    if spec == "saturated":                            # every relative period except -1
        for k in range(-7, 9):
            if k != -1:
                cols.append(((rel == k) & ever).astype(float)); labels.append(str(k))
    else:                                              # binned endpoints: <=-5, -4..-2, 0..4, >=5
        cols.append(((rel <= -5) & ever).astype(float)); labels.append("<=-5")
        for k in (-4, -3, -2, 0, 1, 2, 3, 4):
            cols.append(((rel == k) & ever).astype(float)); labels.append(str(k))
        cols.append(((rel >= 5) & ever).astype(float)); labels.append(">=5")
    return cols, labels


def truth(eff, rel, never, labels):
    ever = ~never[:, None]
    out = []
    for lab in labels:
        if lab == "<=-5":
            mask = (rel <= -5) & ever
        elif lab == ">=5":
            mask = (rel >= 5) & ever
        else:
            mask = (rel == int(lab)) & ever
        out.append(eff[mask].mean() if mask.any() else np.nan)
    return np.array(out)


flags = []
for spec in ("saturated", "binned"):
    est, pv, tru = [], [], []
    for _ in range(REPS):
        adopt_h = draw_adoption()
        never = adopt_h == NEVER
        eff, rel = true_effect(adopt_h)
        y = rng.normal(0, 0.10, (N, 1)) + 0.02 * (years - 2009)[None, :] + eff + rng.normal(0, 0.06, (N, T))
        cols, labels = dummies(rel, never, spec)
        X = np.column_stack([demean2(c).ravel() for c in cols])
        r = sm.OLS(demean2(y).ravel(), X).fit(cov_type="cluster", cov_kwds={"groups": groups})
        est.append(r.params); pv.append(r.pvalues); tru.append(truth(eff, rel, never, labels))
    est, pv, tru = np.array(est), np.array(pv), np.array(tru)
    mean, mcse, t_mean = est.mean(0), est.std(0, ddof=1) / np.sqrt(REPS), np.nanmean(tru, 0)
    print(f"Specification: {spec}")
    print(f"  {'rel':>5s} {'TWFE mean':>10s} {'MC SE':>7s} {'truth':>7s} {'bias':>8s} {'rej5%':>6s}")
    for j, lab in enumerate(labels):
        bias = mean[j] - t_mean[j]
        rej = np.mean(pv[:, j] < 0.05)
        is_lead = lab.startswith("-") or lab.startswith("<=")
        if is_lead:
            bad = abs(mean[j]) > max(3 * mcse[j], 0.005) or rej > 0.10
        else:
            bad = abs(bias) > max(3 * mcse[j], 0.10 * abs(t_mean[j]))
        if bad:
            flags.append(f"{spec} rel {lab}: mean {mean[j]:.4f} vs truth {t_mean[j]:.4f}")
        print(f"  {lab:>5s} {mean[j]:10.4f} {mcse[j]:7.4f} {t_mean[j]:7.4f} {bias:8.4f} {rej:6.2f}{'  <--' if bad else ''}")

if flags:
    print("VERDICT: DEMONSTRATED - part (a) of p09:fnd:9: with zero pre-trends and cohort-heterogeneous dynamic effects, "
          "TWFE event-study coefficients do not recover the true effects (or show non-zero leads): " + "; ".join(flags))
else:
    print("VERDICT: REFUTED-BY-CHECK - part (a) of p09:fnd:9: under these DGPs, TWFE leads are null and lags recover the "
          "true weighted effects in both specifications; parts (b)-(c) (estimand, exclusion, reporting) remain argued.")
```

### p09:chk:9

```json
{"CheckSpec": {"id": "p09:chk:9", "finding_ids": ["p09:fnd:10", "p09:fnd:11"], "probe_type": "P-ID", "method": "Monte Carlo with no peer effect and no modularity; Model 1 analogue (two-way FE); SEs clustered by hospital (ms:§3.3) versus by state", "premises": ["ms:§3.2: Peer = mean of other sample hospitals in the state, t-1", "ms:§3.3: year FE absorb national shocks; SEs clustered by hospital", "ms:§4: state requirements are state-year events (so state-year shocks exist)", "ms:§3.1: 412 hospitals, 2009-2019"], "parts": {"a": "iid state-year shocks: size of a 5% test of the peer coefficient", "b": "persistent state-year shocks (AR(1), rho=0.7): bias of the peer coefficient under zero imitation"}, "verdict_rule": "fnd:10 DEMONSTRATED if hospital-clustered rejection rate >= 0.08 and exceeds the state-clustered rate by >= 0.03; fnd:11 DEMONSTRATED if, in b, the mean peer coefficient > 0 and the state-clustered rejection rate >= 0.5; INCONCLUSIVE otherwise"}}
```

```python
# p09:chk:9 -- state-level regressor, hospital clustering, and persistent state shocks (P-ID)
import numpy as np
import statsmodels.api as sm

rng = np.random.default_rng(2026102309)
S = 50                                   # ASSUMPTION: 50 states
n_s = np.full(S, 412 // S)
n_s[: 412 % S] += 1                      # 412 sample hospitals (ms:§3.1)
st = np.repeat(np.arange(S), n_s)
NS = st.size
BURN = list(range(2004, 2009))
OBS = list(range(2009, 2020))            # ms:§3.1


def demean2(X):
    return X - X.mean(axis=1, keepdims=True) - X.mean(axis=0, keepdims=True) + X.mean()


def simulate(rho_z, sig_z=0.03):
    a = rng.normal(0, 0.10, NS)
    z = rng.normal(0, sig_z, S)
    phi_prev = a + z[st] + rng.normal(0, 0.06, NS)
    PHI, PEER = [], []
    for yr in BURN + OBS:
        z = rho_z * z + np.sqrt(1 - rho_z ** 2) * rng.normal(0, sig_z, S)   # state-year shock (not absorbed by year FE)
        phi = a + 0.02 * (yr - 2009) + z[st] + rng.normal(0, 0.06, NS)      # NO imitation, NO modularity
        ssum = np.bincount(st, weights=phi_prev, minlength=S)
        peer = (ssum[st] - phi_prev) / (n_s[st] - 1)                         # ms:§3.2 Peer, t-1
        if yr in OBS:
            PHI.append(phi); PEER.append(peer)
        phi_prev = phi
    return np.column_stack(PHI)[:, 1:], np.column_stack(PEER)[:, 1:]       # drop 2009 (lag; see p09:fnd:1)


def run(rho_z, reps):
    out = np.empty((reps, 3))
    for i in range(reps):
        PHI, PEER = simulate(rho_z)
        T = PHI.shape[1]
        y, p = demean2(PHI).ravel(), demean2(PEER).ravel()
        rh = sm.OLS(y, p[:, None]).fit(cov_type="cluster", cov_kwds={"groups": np.repeat(np.arange(NS), T)})
        rs = sm.OLS(y, p[:, None]).fit(cov_type="cluster", cov_kwds={"groups": np.repeat(st, T)})
        out[i] = (rh.params[0], rh.pvalues[0], rs.pvalues[0])
    return out


Ra = run(rho_z=0.0, reps=300)
rej_h, rej_s = np.mean(Ra[:, 1] < 0.05), np.mean(Ra[:, 2] < 0.05)
print(f"(a) iid state-year shocks, true peer effect 0: mean b = {Ra[:, 0].mean():.4f}; "
      f"5% rejection rate: hospital-clustered {rej_h:.3f}, state-clustered {rej_s:.3f}")
Rb = run(rho_z=0.7, reps=100)
rej_b = np.mean((Rb[:, 0] > 0) & (Rb[:, 2] < 0.05))
print(f"(b) persistent state shocks (rho=0.7), true peer effect 0: mean b = {Rb[:, 0].mean():.4f}; "
      f"share b>0 & p<.05 (state-clustered) = {rej_b:.2f}; hospital-clustered = {np.mean((Rb[:, 0] > 0) & (Rb[:, 1] < 0.05)):.2f}")
print("reference: ms:T2.M1 peer = 0.137 (0.031)")

if rej_h >= 0.08 and rej_h - rej_s >= 0.03:
    print(f"VERDICT: DEMONSTRATED - p09:fnd:10: hospital-clustered SEs reject a true null for Peer at {rej_h:.1%} "
          f"(nominal 5%; state-clustered {rej_s:.1%}).")
else:
    print(f"VERDICT: INCONCLUSIVE - p09:fnd:10: hospital-clustered rejection {rej_h:.1%} vs state-clustered {rej_s:.1%}.")
if Rb[:, 0].mean() > 0 and rej_b >= 0.5:
    print(f"VERDICT: DEMONSTRATED - p09:fnd:11: with persistent state shocks and no imitation, lagged Peer predicts "
          f"own outsourcing (mean b = {Rb[:, 0].mean():.3f}; significant in {rej_b:.0%} with state clustering).")
else:
    print(f"VERDICT: INCONCLUSIVE - p09:fnd:11: persistent state shocks did not produce a reliable spurious peer coefficient.")
```

## 8. Hand-off to the harness

```json
{"HarnessRequest": {"run": "p09", "part": 1, "checks": ["p09:chk:1", "p09:chk:2", "p09:chk:3", "p09:chk:4", "p09:chk:5", "p09:chk:6", "p09:chk:7", "p09:chk:8", "p09:chk:9"], "independent": true, "libraries": ["numpy", "scipy", "statsmodels"], "expected_runtime": "chk:1-4 instant; chk:5, chk:7, chk:8, chk:9 under a minute each; chk:6 the longest (600 simulated panels)", "return": "full stdout of each check, including every VERDICT line"}}
```

In Part 2 (step 4) each bound finding will be set to `demonstrated`, `refuted-by-check` or `inconclusive` from the harness output, and severities revised.

- `p09:fnd:4`'s arithmetic is expected to be refuted, which counts as a strength.
- `p09:fnd:6` and `p09:fnd:7` share `p09:chk:6`; `p09:fnd:10` and `p09:fnd:11` share `p09:chk:9`. Each of these findings has its own VERDICT line.
- Parts (b) and (c) of `p09:fnd:9` stay `asserted` whatever the result, because they are argued, not bound.
- The simulation checks show that a pattern is *possible* under the manuscript's own relations. They cannot show that it is what happened in the data. A `demonstrated` verdict means "the manuscript's inference is not entitled". It does not mean "the rival is true".

## 9. Decisions for the reviewer

1. **Perspective defaults.** Confirm or replace the working defaults. MI6 is endorsed only with its proviso and MI7 is not endorsed. Intervals and equivalence count for more than significance (EPI.5). `p09:fnd:3` and `p09:fnd:6` depend on these.
2. **Severity of `p09:fnd:6`.** Choose fatal (the central claim is the adjudication in the title, Abstract and `ms:§5`) or damaging (the central claim is H1, and "rule out mimicry" is an overreach).
3. **Simulation assumptions.** Accept or amend the assumptions in `p09:chk:6`–`p09:chk:9`: 50 states, a 40-hospital field per state, 40 adopting states, and all variance and effect parameters. Alternatively, ask the authors for the number of states and the hospitals per state.
4. **Premise of `p09:fnd:8`.** The feedback edge (outsourcing → reported modularity) is *inferred* from `ms:§1`. Decide whether to keep the finding or put it to the authors as a question.
5. **Forward `p09:ref:1`.** Decide whether to send the Proposition 2 sign issue to the P-DER probe before Part 2. If confirmed, it changes how the Table 2 interaction and the `ms:§5` legitimacy account should be read.
6. **How to send `p09:fnd:1` and `p09:fnd:2`.** Send them to the authors as table corrections, or to the editor as a data-integrity flag (N cannot match the stated panel).
7. **Which repairs to request.** Choose among:
   - state-level clustering (`p09:fnd:10`);
   - a population-based or referent-based peer measure (`p09:fnd:7`);
   - an instrumented design on state requirements with a reported first stage (`p09:fnd:5`, `p09:fnd:8`, `p09:fnd:9`);
   - an equivalence test with a stated smallest effect of interest (`p09:fnd:3`).
8. **Run the checks.** Authorize the harness to run `p09:chk:1`–`p09:chk:9`. Part 2 follows on the results.

---

## Part 2: disposition after the harness

**Inputs read:** `09_checks/p09_chk_1.out.txt` to `p09_chk_9.out.txt` in full, and `09_checks/results.json`. All nine checks exited 0, with empty stderr, on 2026-10-23 between 20:42:09Z and 20:42:19Z. Part 1 above is unchanged.

**How to read the verdicts.**
- A `demonstrated` P-ID verdict means the manuscript's inference is not entitled under its own stated relations and my simulation parameters. It does not estimate what happened in the hospitals' data.
- Statuses follow each check's pre-stated verdict rule. Where the full output says more than the verdict line, I report it below under "Results that reach beyond their checks". I do not re-score a finding on that basis.

### P2.1 Disposition of bound findings

| Finding | Check | Status | Reason (from the output) | Severity, Part 1 → Part 2 |
|---|---|---|---|---|
| `p09:fnd:1` | `p09:chk:1` | **demonstrated** | Expected 412 × 11 = 4,532, or at most 4,120 with Peer(t−1). Reported 4,712 = 11.437 years per hospital, 180 more than balanced | fixable → fixable |
| `p09:fnd:2` | `p09:chk:2` | **demonstrated** | "Environmental uncertainty M3 0.084 0.051 1.65 0.10031, printed 3, attainable [0]", a mismatch robust to rounding. The other 15 of 16 cells are consistent | minor → minor |
| `p09:fnd:3` | `p09:chk:3` | **demonstrated** | 95% CI [−0.0327, 0.1167], whose upper bound is 0.85 × Model 1. TOST p = 0.243 at margin 0.0685. Smallest margin at which equivalence could be declared: 0.1046 (0.76 × Model 1) | damaging → damaging |
| `p09:fnd:4` | `p09:chk:4` | **refuted-by-check** (arithmetic) | 2.69 pp; 0.158 against one-sixth (0.167); fall 0.693 > 0.667. The manuscript's arithmetic is right. The residual scope remarks stay `asserted` | minor → none for the arithmetic; residual remarks minor |
| `p09:fnd:5` | `p09:chk:5` | **demonstrated** | (A) with true β = 0, Model 4 gives b = 0.146 (Model 3: 0.099), positive with p < .05 in 1.00 of replications. (B) with true β = 0.11 and no confounding, Model 4 gives 0.090, a bias of −18% | damaging → damaging |
| `p09:fnd:6` | `p09:chk:6` | **inconclusive** | The economizing benchmark (i) reproduces the pattern in only 0.28 of replications (its Model 1 peer coefficient is significant in only 0.37), so the pre-stated rule cannot fire. The check was too weak (see P2.2) | fatal → **damaging (provisional)**; fatal again if a recalibrated check demonstrates it |
| `p09:fnd:7` | `p09:chk:6` | **inconclusive** | Best direct-mimicry rate 0.31 (θ = 0.10). The Model 2 peer coefficient stays significant at θ = 0.20 (0.40) and θ = 0.30 (0.86) | damaging → **fixable (provisional)**; partly undercut (P2.2) |
| `p09:fnd:8` | `p09:chk:7` | **demonstrated**, conditional on the feedback edge, which is inferred from `ms:§1`, not stated | (A) with β = 0 and feedback 0.5, FE b = 0.107 (Table 2: 0.112), significant in 1.00 of replications. 2SLS on state requirements: 0.002 in (A) and 0.111 in (B); first-stage t ≈ 36–38 | damaging → damaging |
| `p09:fnd:9` | `p09:chk:8` | part (a) **demonstrated**, but with limited bearing on the reported result (P2.2). Parts (b) and (c) stay `asserted` | Saturated specification: leads −7 to −3 run from 0.024 to 0.008, rejecting in 0.37–0.81 of replications; lags 0–1 biased −10% to −20%. Binned specification: all leads flagged; the ≥5 bin is 0.095 against a truth of 0.107 | fixable → fixable |
| `p09:fnd:10` | `p09:chk:9` (a) | **demonstrated**, with a caveat | Under a true null, rejection is 0.560 with hospital clustering and 0.317 with state clustering. But the mean b under the null is −0.063, so part of both rates is bias, not understated SEs (P2.2) | fixable → fixable |
| `p09:fnd:11` | `p09:chk:9` (b) | **demonstrated** | Persistent state shocks (ρ = 0.7) and no imitation: mean b = 0.270, about twice Table 2's Model 1 coefficient of 0.137, significant in 1.00 of replications even with state clustering | damaging → damaging |

Unbound items stay `asserted`: parts (b) and (c) of `p09:fnd:9`, the residual remarks under `p09:fnd:4`, and the referrals `p09:ref:1`–`p09:ref:5`.

```json
{"Disposition": {"run": "p09", "part": 2, "source": "09_checks/*.out.txt, results.json", "findings": [
  {"id": "p09:fnd:1", "check": "p09:chk:1", "status": "demonstrated", "severity": "fixable"},
  {"id": "p09:fnd:2", "check": "p09:chk:2", "status": "demonstrated", "severity": "minor"},
  {"id": "p09:fnd:3", "check": "p09:chk:3", "status": "demonstrated", "severity": "damaging"},
  {"id": "p09:fnd:4", "check": "p09:chk:4", "status": "refuted-by-check", "severity": "none (arithmetic); residual remarks minor, asserted"},
  {"id": "p09:fnd:5", "check": "p09:chk:5", "status": "demonstrated", "severity": "damaging"},
  {"id": "p09:fnd:6", "check": "p09:chk:6", "status": "inconclusive", "severity": "damaging (provisional; was fatal)"},
  {"id": "p09:fnd:7", "check": "p09:chk:6", "status": "inconclusive", "severity": "fixable (provisional; was damaging)"},
  {"id": "p09:fnd:8", "check": "p09:chk:7", "status": "demonstrated", "condition": "feedback edge inferred from ms:§1", "severity": "damaging"},
  {"id": "p09:fnd:9", "check": "p09:chk:8", "status": "demonstrated (part a); asserted (parts b, c)", "severity": "fixable"},
  {"id": "p09:fnd:10", "check": "p09:chk:9", "status": "demonstrated", "caveat": "null rejection partly due to bias of -0.063", "severity": "fixable"},
  {"id": "p09:fnd:11", "check": "p09:chk:9", "status": "demonstrated", "severity": "damaging"},
  {"id": "p09:fnd:12", "check": null, "status": "asserted", "origin": "unanticipated result in p09:chk:9 (a)", "severity": "damaging if confirmed (provisional)"}
]}}
```

### P2.2 Results that reach beyond their checks

Each item below says plainly whether it strengthens or undercuts a finding. None of it changes a status in P2.1.

1. **`p09:chk:6` was too weak to be informative (my design fault).**
   - **Why it failed.** Its verdict rule needed the economizing-only benchmark to reproduce Table 2's pattern. Under my parameters, that benchmark yields a Model 1 peer coefficient of only 0.056 (significant in 0.37 of replications), against Table 2's 0.137. I set the state-standards channel too weak relative to the noise in the sample-based Peer. So the check could not compare the rivals, and both `p09:fnd:6` and `p09:fnd:7` stay unestablished.
   - **What the output still shows (descriptive, not a verdict).** In every scenario without a direct peer term, the Model 2 peer coefficient is about zero (−0.012 to −0.018) and rejects at the nominal rate (0.05–0.07). That includes κ = 2, where field prevalence has a true indirect effect of 0.22 on outsourcing. This is the regression logic of `p09:fnd:6` in numbers: Model 2's null coexists with a real mimetic effect that runs through modularity.
   - **What not to infer.** The κ = 2 scenario happens to match Table 2's Model 1 peer coefficient (0.143) and reproduces the full pattern in 0.91 of replications, more often than economizing-only does. This is **not** evidence for mimicry. The gap comes from my calibration, and a stronger standards channel would raise the economizing benchmark.
   - **Proposed follow-up.** A recalibrated check (`p09:chk:6b`) would tune the benchmark so that scenario (i) reproduces a significant Model 1 peer coefficient in at least 80% of replications, then re-run scenarios (ii) and (iii).
2. **`p09:fnd:7` is partly undercut.**
   - Through the noisy sample-based Peer, Model 2 recovers about a third of a true direct effect: 0.030 for θ = 0.10, 0.065 for θ = 0.20, and 0.110 for θ = 0.30. That supports the attenuation mechanism.
   - But direct effects of 0.20 or more remain detectable (significant in 0.40 and 0.86 of replications). The noisy proxy blinds the test to modest direct imitation, not to large direct imitation. I therefore downgrade `p09:fnd:7` to fixable.
   - The same output **strengthens `p09:fnd:3`**. Under this data-generating process, Table 2's 0.042 lies between the means for θ = 0.10 and θ = 0.20. So it is what a direct effect of roughly 0.13, about three times the estimate, would produce. This is parameter-dependent and illustrative.
3. **`p09:chk:9` (a) turned up something I did not anticipate.**
   - With iid state-year shocks and no peer effect, the mean Peer coefficient is **−0.063**, not zero.
   - **It tempers the `p09:fnd:10` verdict line.** The 0.560 rejection rate mixes this bias with understated SEs. Only the gap from state clustering (0.560 against 0.317) is attributable to clustering, and state clustering with about 50 clusters still over-rejects here because of the bias. The finding stands, but the verdict line overstated the clustering share.
   - **It changes how `p09:fnd:11` bears on the claim.** Persistent shocks bias Peer upward (+0.270 in (b)). Serially independent shocks bias it downward (−0.063 in (a)). Had only the upward bias been possible, the Model 2 null would be conservative, which would favour the authors. With either sign possible, Model 2's peer coefficient is uninterpretable as evidence about imitation. That strengthens `p09:fnd:3`.
   - I record the downward bias as a new finding, `p09:fnd:12` (below). It is `asserted`, because no check was designed to test it.
4. **`p09:chk:8` bites less on the reported result than Part 1 implied.**
   - The contamination it demonstrates produces spurious *positive* leads, significant in up to 0.98 of replications. The authors report small, insignificant leads. So this particular heterogeneity (earlier cohorts, larger and growing effects) is, if anything, not what their data show.
   - The masking case (contamination hiding a real pre-trend) was not simulated.
   - The lags are biased *downward* by 10–20%, which is conservative for the authors.
   - The force of `p09:fnd:9` now lies in its asserted parts: (b) the estimand is the effect of mandates, and no first stage or exclusion argument is given; (c) nothing is reported. Severity stays fixable.
5. **`p09:chk:7` undercuts one of my own Part 1 repairs.**
   - Lagging modularity is not a repair. Under feedback, m(t−1) still gives 0.036, significant in 0.99 of replications. Under the manuscript's own model with no feedback, it gives 0.008 (significant in 0.20) against a true effect of 0.11.
   - I withdraw "use m at t−1" from the `p09:fnd:8` repair.
   - 2SLS on state requirements recovers the truth in both scenarios (0.002 and 0.111). It is the repair to request, provided the authors argue exclusion. `p09:ref:3` (mandates as coercive pressure) is the main threat to that argument.
   - Strengthening, illustrative only: a modest feedback (10 pp more outsourcing leading to 5 pp more certified interfaces) reproduces Table 2's modularity estimate (0.107 against 0.112) with no true effect at all.
6. **`p09:chk:5`: two magnitudes are illustrative only.**
   - Scenario (B)'s −18% bias equals the fall in Table 2 from 0.118 to 0.097 (−17.8%). This is a coincidence of my parameters and not evidence about the data.
   - Scenario (A) shows the coefficient can *rise* under the control (0.099 → 0.146).
   - So Model 4 is uninformative in either direction, which is the point of `p09:fnd:5`. The check fixed the signs of the capability paths (c, d ≥ 0); with other signs the direction changes but the uninformativeness does not.
7. **Strengths confirmed.**
   - The H1 magnitude and the "more than two-thirds" fall are arithmetically correct (`p09:chk:4`).
   - The stars are consistent in 15 of 16 cells (`p09:chk:2`).
   - The fall in the peer coefficient is probably a real change. With any plausible positive correlation between the two estimates (ρ ≥ 0.5), the 0.095 change is significant (p ≤ 0.0067; `p09:chk:3`). What the data do not show is that the remaining peer effect is zero.

### P2.3 New finding from the harness output

```json
{
  "id": "p09:fnd:12", "probe_type": "P-ID", "status": "asserted", "check": null,
  "origin": "p09:chk:9 part (a) output: 'iid state-year shocks, true peer effect 0: mean b = -0.0632'",
  "locus": "ms:§3.3 (hospital FE); ms:§3.2 Peer (lagged state mean); ms:T2.M2 peer",
  "commitment": "p09:cmt:1 and p09:cmt:7, applied to beta4",
  "missing_entitlement": "inferred from the output: with hospital FE and a lagged state-mean regressor, state-year shocks that enter both Peer(t-1) and own Phi(t) through the within-transformation bias Peer's coefficient downward when shocks are serially independent (consistent with Nickell 1981-type bias; to verify). In the simulation the bias (-0.063) is larger than Table 2's Model 2 point estimate (0.042) and about 1.7 of its SEs. Its real size depends on the share of state-year variance in outsourcing, which is not reported.",
  "severity": "damaging if confirmed (provisional)",
  "repair": "Report the state-year variance share; estimate in first differences or with Peer lagged two periods; or use an external instrument for peer prevalence; a bound check (p09:chk:10) should be written in a later run."
}
```

### P2.4 Where the manuscript stands after the harness

- **No fatal finding is demonstrated.** The only Part 1 fatal (`p09:fnd:6`) is inconclusive.
- **The adjudication claim is overstated on demonstrated grounds.** "Rule out mimetic isomorphism" and "Not Mimicry" fail on `p09:fnd:3` (absence not shown; interval up to 0.85 × Model 1) and `p09:fnd:11` (the peer coefficient does not identify imitation). `p09:fnd:12` (asserted) adds that its bias can take either sign.
- **The causal reading of H1 is unprotected on demonstrated grounds.** Model 4 is uninformative (`p09:fnd:5`), and same-year feedback alone can reproduce Table 2's modularity estimate (`p09:fnd:8`, conditional on an inferred edge).
- **H1 as an association, and the reported arithmetic, stand.**
- **What the authors are left with, by my reading** (which the reviewer may reject): a defensible within-hospital association between modularity and outsourcing, and a peer coefficient that cannot adjudicate. Whether that is fatal for the paper's title claim is the reviewer's call.

### P2.5 Findings to put in front of the reviewer, in order

| Rank | Finding | Status | Severity | One line |
|---|---|---|---|---|
| 1 | `p09:fnd:3` | demonstrated | damaging | Model 2's peer null is not evidence of absence. 95% CI reaches 0.117; TOST fails; "rule out" must go |
| 2 | `p09:fnd:11` | demonstrated | damaging | Persistent state shocks alone yield a peer coefficient twice Table 2's. The H3 design cannot identify imitation either way |
| 3 | `p09:fnd:5` | demonstrated | damaging | In-house staffing is caused by outsourcing (`ms:§3.2`), so Model 4 cannot rule out capability confounding |
| 4 | `p09:fnd:8` | demonstrated (inferred edge) | damaging | Same-year feedback can produce Table 2's modularity estimate with no true effect. Ask for 2SLS on state requirements with an exclusion argument |
| 5 | `p09:fnd:6` | inconclusive | damaging (provisional) | Model 2 cannot see mimicry that runs through modularity. Put it as a challenge: estimate peers → own m. Re-check with `p09:chk:6b` |
| 6 | `p09:fnd:1` | demonstrated | fixable | N = 4,712 cannot be the stated balanced panel (4,532), nor fit lagged Peer (≤ 4,120) |
| 7 | `p09:fnd:10` | demonstrated (caveat) | fixable | Cluster by state; hospital clustering over-rejects (0.56 against 0.32) |
| 8 | `p09:fnd:9` | (a) demonstrated, limited bite; (b) and (c) asserted | fixable | The event study estimates the effect of mandates on outsourcing. Ask for coefficients, a robust estimator, the first stage and an exclusion argument |
| 9 | `p09:fnd:12` | asserted (new) | damaging if confirmed | The FE/lagged-Peer construction can bias β4 downward. Ask for the state-year variance share or a first-difference estimate |
| 10 | `p09:fnd:7` | inconclusive | fixable (provisional) | Peer comes from about 8 respondents per state. It attenuates modest direct effects; ask for a population or referent-based peer measure |
| 11 | `p09:fnd:2` | demonstrated | minor | Model 3 uncertainty is starred *** at p ≈ 0.10. Correct the cell |
| — | `p09:fnd:4` | refuted-by-check | none | Strength: the H1 magnitude and the "two-thirds" fall are correct. The residual remarks (pooled SDs; effect zero above u ≈ 1.7–1.9 SD) are minor |
| — | `p09:ref:1` | referral (asserted) | — | Proposition 2's sign appears reversed under A3. If P-DER confirms, the "contrary" H2 result is what the model predicts |

## Decisions for the reviewer (Part 2)

1. **Severity of `p09:fnd:6`.** Accept the downgrade to damaging (provisional), or keep fatal on the argued regression logic alone. Authorize `p09:chk:6b` to settle it.
2. **Withdrawn repair.** Accept that "m at t−1" is removed from the repair for `p09:fnd:8` (`p09:chk:7`), and that 2SLS on state requirements with an argued exclusion restriction is the repair to request.
3. **New finding.** Admit `p09:fnd:12`, an unanticipated harness result (asserted), and authorize a bound check (`p09:chk:10`); or hold it back until checked.
4. **Reading of `p09:chk:8`.** Accept that part (a) of `p09:fnd:9` has limited bearing on the authors' flat leads, and that the finding goes forward mainly on (b) estimand/exclusion and (c) reporting.
5. **Is the title claim fatal?** Decide whether `p09:fnd:3` + `p09:fnd:11` (demonstrated) together make the adjudication claim fatal or damaging-and-repairable by restatement.
6. **Simulation assumptions.** Confirm that the parameter-dependent magnitudes (−18% in `p09:chk:5`, 0.107 in `p09:chk:7`, 0.270 in `p09:chk:9`) are cited to the authors only as illustrations, not as estimates.
7. **Still open from Part 1.** Decisions 1 (perspective defaults), 4 (premise of `p09:fnd:8`), 5 (forward `p09:ref:1` to P-DER) and 6 (route for `p09:fnd:1`/`p09:fnd:2`) remain open.

