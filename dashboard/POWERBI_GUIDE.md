# Power BI Dashboard — Build Guide

Three small CSVs in this folder — `bev_share_by_year.csv`, `zev_mandate_target.csv`,
`chinese_brand_share.csv` — plus the steps below to build the dashboard. Budget ~30 minutes
(this dataset is much smaller than a full registration-level file, so it's quick).

## 1. Import data
Power BI Desktop → **Get Data → Text/CSV** → import all three files. Close & Apply.

## 2. Create a relationship
In Model view, join `bev_share_by_year` and `zev_mandate_target` on `year` (both are
small, one-row-per-year tables — a simple 1:1 relationship is fine).

## 3. Pages & visuals

### Page 1 — Electrification vs. ZEV Mandate
- **Line chart**: `year` (axis) × `bev_share_pct` and `target_pct` (two lines) —
  reproduces the notebook's headline chart, now interactive
- **Card visuals**: latest actual BEV share; latest year's gap to target (calculated
  column: `target_pct - bev_share_pct`)
- **Text box**: note that 2026 is Q1 only, not a full-year figure

### Page 2 — Chinese-brand entrants
- **Clustered column chart**: `year` (axis) × `new_entrants_excl_mg_pct` and
  `all_chinese_owned_incl_mg_pct`
- **Text box**: the MG inclusion/exclusion caveat from the README — important for
  credibility with anyone who knows the market

### Page 3 — Sources
- A simple table or text page listing every source cited in `compile_dataset.py`.
  This page matters more than it looks — it's what makes the dashboard defensible
  in an interview setting when someone asks "where does this data come from?"

## 4. Formatting tips
- Use red (`#C62828`) consistently for anything ZEV-Mandate/compliance-risk related,
  and green (`#2E7D32`) for actual BEV performance, matching the notebook charts
- Publish to **Power BI Service** and share the link from your GitHub README and
  LinkedIn featured section

## 5. Why this is a stronger portfolio piece than a static PDF chart
Because the underlying figures are cited per-row, a recruiter or interviewer can
trace every number back to its source — showing not just chart-building skill but
data governance instinct, which is exactly what the original interview task (Part 2)
asked about.
