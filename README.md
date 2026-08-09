# 🚗 UK Automotive Market: Electrification & Chinese New Entrants

**A public-data market analysis: how close is the UK to its ZEV Mandate target, and how fast are Chinese-origin brands growing?**

[![Data](https://img.shields.io/badge/Data-Public%20%2F%20OGL-blue)]() [![Python](https://img.shields.io/badge/Python-3.11-blue)]() [![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-yellow)]()

## 📌 Overview

This project tracks two of the most talked-about trends in the UK car market right now:

1. **Electrification vs. the ZEV Mandate** — the UK requires an escalating share of
   zero-emission new car sales each year, reaching 80% by 2030. How does the real
   market compare to that legal curve?
2. **Chinese-origin brands' market entry** — GWM, BYD, Omoda, Jaecoo, Leapmotor and
   others have gone from a standing start in 2022 to a genuinely material share of
   UK registrations. How fast, exactly?

## ⚠️ A note on data sourcing

Every figure in this repository is compiled **by hand, from public sources**, and
cited individually in `data/compile_dataset.py`. Nothing here is scraped or
bulk-redistributed from a licensed/proprietary market-research database (e.g.
GlobalData, JATO). This makes the project fully safe to publish and reuse.

**Primary sources:**
- UK Department for Transport / DVLA, *Vehicle Licensing Statistics* — official,
  accredited government statistics, © Crown copyright, [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/)
  → https://www.gov.uk/government/collections/vehicles-statistics
- Society of Motor Manufacturers and Traders (SMMT) new car registration data, as
  reported in public press coverage:
  - Car Dealer Magazine, *"How did Chinese car brands fare in the UK in 2025?"*
  - Zapmap, *UK EV market share* tracker (citing SMMT)
  - GB News, Regit, DriveElectric, ChinaEVHome — Chinese-brand coverage (see inline
    citations in `data/compile_dataset.py`)

Where public reporting is approximate, or figures are compiled by a third party from
SMMT's underlying data rather than published by SMMT directly as a headline stat,
this is flagged in the dataset's `note` column. Chinese-brand market share in
particular is **not** an official standalone SMMT statistic.

## 🗂️ Repository structure

```
├── data/
│   ├── compile_dataset.py          # source-by-source data compilation (read this first)
│   ├── bev_share_by_year.csv
│   ├── zev_mandate_target.csv
│   └── chinese_brand_share.csv
├── notebooks/
│   ├── analysis.py                 # chart-generation pipeline
│   └── uk_auto_market_analysis.ipynb
├── assets/                         # exported chart images
├── dashboard/
│   └── POWERBI_GUIDE.md
└── README.md
```

## 📊 Key findings

- Actual UK BEV share tracked the ZEV Mandate closely through 2022–2023, but has
  **fallen behind from 2024 onward** — 23.4% actual vs. 28% target in 2025.
- Chinese-origin new entrants (excluding the longer-established MG) grew from
  **negligible in 2022 to roughly 12% of new registrations by 2026**.

## 🛠️ Tech stack

`Python` · `pandas` · `matplotlib` · `Power BI`

## ▶️ Run it yourself

```bash
pip install -r requirements.txt
python data/compile_dataset.py
python notebooks/analysis.py
```

## 📈 Dashboard

A companion Power BI dashboard turns this into a live-refreshable, stakeholder-facing
view. See [`dashboard/POWERBI_GUIDE.md`](dashboard/POWERBI_GUIDE.md).
