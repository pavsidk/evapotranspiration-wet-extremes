import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
et = pd.read_csv(
    "runs/RF/RF_run_with_lagged_et02/events_iqr.csv",
    low_memory=False
)

gpp = pd.read_csv(
    "gpp_paper/revision_lagged_gpp_12_remove_medium/events_iqr.csv",
    low_memory=False
)

gpp_sites = set(gpp[gpp["R2"] > 0.7]["SITE_ID"].unique())
et_sites  = set(et[et["R2"]  > 0.7]["SITE_ID"].unique())
shared_sites = gpp_sites & et_sites

gpp = gpp[gpp["SITE_ID"].isin(shared_sites)]
et  = et[et["SITE_ID"].isin(shared_sites)]

merged = pd.merge(
    gpp,
    et,
    on=["SITE_ID", "day"],
    how="inner",
    suffixes=("_gpp", "_et")
)

if "IGBP_gpp" in merged.columns:
    igbp_col = "IGBP_gpp"
elif "IGBP_et" in merged.columns:
    igbp_col = "IGBP_et"
else:
    raise ValueError("No IGBP column found")

merged = merged.dropna(subset=["anomaly_norm_gpp", "anomaly_norm_et", igbp_col])

merged["diff"] = merged["anomaly_norm_et"] - merged["anomaly_norm_gpp"]

igbp_full_names = {
    "ENF": "Evergreen Needleleaf Forest",
    "DBF": "Deciduous Broadleaf Forest",
    "EBF": "Evergreen Broadleaf Forest",
    "MF":  "Mixed Forest",
    "GRA": "Grasslands",
    "SAV": "Savannas",
    "WSA": "Woody Savannas",
    "CSH": "Closed Shrubland",
    "OSH": "Open Shrubland"
}

merged["biome"] = merged[igbp_col].map(igbp_full_names)

merged = merged.dropna(subset=["biome"])

plt.figure(figsize=(10, 6))

palette = sns.color_palette("PuBuGn", n_colors=merged["biome"].nunique())

sns.violinplot(
    data=merged,
    x="biome",
    y="diff",
    palette=palette
)

plt.xticks(rotation=45, ha="right")
plt.ylabel("ET - GPP Anomaly")
plt.xlabel("IGBP Category")
plt.title("Difference Between ET and GPP Across International Geosphere-Biosphere Programme (IGBP) Categories")

plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()

plt.savefig(
    "figs/NEW_FIGS/et_minus_gpp_by_biome_violin.png",
    dpi=300
)

plt.show()