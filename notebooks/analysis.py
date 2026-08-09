"""
UK Automotive Market — Electrification & Chinese New Entrants
Built entirely from public, cited sources (see data/compile_dataset.py and README.md)
"""
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

plt.rcParams["figure.dpi"] = 110
ASSETS = "/home/claude/uk-auto-market/assets"

bev = pd.read_csv("/home/claude/uk-auto-market/data/bev_share_by_year.csv")
mandate = pd.read_csv("/home/claude/uk-auto-market/data/zev_mandate_target.csv")
chn = pd.read_csv("/home/claude/uk-auto-market/data/chinese_brand_share.csv")

# ---------------------------------------------------------------
# 1. BEV share vs ZEV Mandate target
# ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(bev["year"], bev["bev_share_pct"], marker="o", linewidth=2.5, color="#2E7D32", label="Actual BEV share (SMMT/DfT)")
ax.plot(mandate["year"], mandate["target_pct"], marker="o", linewidth=2, linestyle="--", color="#C62828", label="ZEV Mandate legal target")
ax.set_ylabel("% of new car registrations")
ax.set_title("UK BEV share vs. ZEV Mandate target, 2019-2030")
ax.legend()
ax.grid(axis="y", color="#E4E7EB")
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
plt.tight_layout()
plt.savefig(f"{ASSETS}/01_bev_vs_mandate.png")
plt.close()

# ---------------------------------------------------------------
# 2. Chinese brand share growth
# ---------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 4.5))
ax.bar(chn["year"] - 0.18, chn["new_entrants_excl_mg_pct"], width=0.36, color="#C62828", label="New entrants (excl. MG), since 2022")
mask = chn["all_chinese_owned_incl_mg_pct"].notna()
ax.bar(chn.loc[mask, "year"] + 0.18, chn.loc[mask, "all_chinese_owned_incl_mg_pct"], width=0.36, color="#8D8D8D", label="All Chinese-owned brands (incl. MG)")
ax.set_ylabel("% of UK new car registrations")
ax.set_title("Chinese-origin brand share of the UK new car market")
ax.legend()
ax.grid(axis="y", color="#E4E7EB")
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
plt.tight_layout()
plt.savefig(f"{ASSETS}/02_chinese_brand_share.png")
plt.close()

print("done")
