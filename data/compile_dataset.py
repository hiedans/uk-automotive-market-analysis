"""
UK new car market — propulsion mix and Chinese-brand entrant share.

All figures in this file are compiled BY HAND from published, public statistics.
Nothing here is scraped or bulk-redistributed from a licensed/proprietary database.

Primary sources:
- UK Department for Transport / DVLA, "Vehicle licensing statistics" series
  (Crown copyright, Open Government Licence v3.0)
  https://www.gov.uk/government/collections/vehicles-statistics
- Society of Motor Manufacturers and Traders (SMMT) monthly new car registration
  figures, as reported in public SMMT press releases and press coverage
  (Car Dealer Magazine, Zapmap EV market data, GB News, Regit, DriveElectric,
  ChinaEVHome — see README.md for the full list of article URLs).

Where public reporting is approximate or a single named source could not be
verified precisely, this is flagged in the `note` column. Chinese-brand share
in particular is NOT an official standalone SMMT statistic; it is calculated
by third parties (journalists/analysts) from SMMT's underlying by-manufacturer
data, so treat those figures as indicative, not exact.
"""
import pandas as pd

# ---------------------------------------------------------------
# UK new car registrations: BEV (zero-emission) share by year
# Source: DfT Vehicle Licensing Statistics releases (VEH1153a series) and
# SMMT year-end figures as reported by Zapmap's EV market tracker.
# ---------------------------------------------------------------
bev_share = pd.DataFrame([
    {"year": 2019, "bev_share_pct": 1.6,  "source": "SMMT / DfT vehicle licensing statistics", "note": ""},
    {"year": 2020, "bev_share_pct": 6.6,  "source": "SMMT / DfT vehicle licensing statistics", "note": ""},
    {"year": 2021, "bev_share_pct": 11.6, "source": "SMMT, via Zapmap EV market data", "note": ""},
    {"year": 2022, "bev_share_pct": 16.6, "source": "SMMT, via Zapmap EV market data", "note": ""},
    {"year": 2023, "bev_share_pct": 16.5, "source": "SMMT year-end figures (widely reported)", "note": "approx., full-year"},
    {"year": 2024, "bev_share_pct": 19.6, "source": "DfT vehicle licensing statistics 2025 release", "note": ""},
    {"year": 2025, "bev_share_pct": 23.4, "source": "DfT vehicle licensing statistics 2025 release / Zapmap", "note": ""},
    {"year": 2026, "bev_share_pct": 21.8, "source": "DfT vehicle licensing statistics, Jan-Mar 2026 release", "note": "Q1 2026 only, not full year"},
])
bev_share.to_csv("/home/claude/uk-auto-market/data/bev_share_by_year.csv", index=False)

# ---------------------------------------------------------------
# ZEV Mandate legal targets (% of manufacturer new car sales that must be
# zero-emission each year) — for comparison with actual BEV share above.
# Source: UK ZEV Mandate legislation (DfT), as reported by AutoVista24 /
# WhatCar / gbnews coverage of the mandate.
# ---------------------------------------------------------------
zev_mandate_target = pd.DataFrame([
    {"year": 2024, "target_pct": 22.0},
    {"year": 2025, "target_pct": 28.0},
    {"year": 2026, "target_pct": 33.0},
    {"year": 2027, "target_pct": 38.0},
    {"year": 2028, "target_pct": 52.0},
    {"year": 2029, "target_pct": 66.0},
    {"year": 2030, "target_pct": 80.0},
])
zev_mandate_target.to_csv("/home/claude/uk-auto-market/data/zev_mandate_target.csv", index=False)

# ---------------------------------------------------------------
# Chinese-origin brand share of UK new car registrations.
# NOT an official SMMT headline statistic — compiled from public reporting
# that itself analyses SMMT's underlying by-manufacturer registration data.
# Two series are kept separate because "MG" has been sold in the UK since
# 1924 (Chinese-owned by SAIC since 2007) and is not a "new entrant" in the
# same sense as brands that launched from 2022 onwards.
# ---------------------------------------------------------------
chinese_brand_share = pd.DataFrame([
    {"year": 2022, "new_entrants_excl_mg_pct": 0.1, "all_chinese_owned_incl_mg_pct": None,
     "note": "GWM launches in UK 2022; volumes negligible"},
    {"year": 2023, "new_entrants_excl_mg_pct": 1.0, "all_chinese_owned_incl_mg_pct": None,
     "note": "BYD, Chery-group brands begin UK launch"},
    {"year": 2024, "new_entrants_excl_mg_pct": 4.5, "all_chinese_owned_incl_mg_pct": None,
     "note": "approx., compiled from press coverage of SMMT data"},
    {"year": 2025, "new_entrants_excl_mg_pct": 5.5, "all_chinese_owned_incl_mg_pct": 9.7,
     "note": "Car Dealer Magazine, citing SMMT: 10 Chinese brands (excl. MG) = 111,607 regs of ~2.02m; "
             "all Chinese-owned brands incl. MG = 9.7% of new cars"},
    {"year": 2026, "new_entrants_excl_mg_pct": 12.0, "all_chinese_owned_incl_mg_pct": 16.5,
     "note": "April 2026 single-month reading (ChinaEVHome, citing SMMT); not a full-year figure"},
])
chinese_brand_share.to_csv("/home/claude/uk-auto-market/data/chinese_brand_share.csv", index=False)

print(bev_share)
print()
print(zev_mandate_target)
print()
print(chinese_brand_share)
