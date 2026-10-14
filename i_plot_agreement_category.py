import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

comp = pd.read_csv(
    "figs/NEW_FIGS/et_vs_gpp_site_comparison.csv"
)

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

comp["biome"] = comp["IGBP"].map(igbp_full_names)
comp = comp.dropna(subset=["biome"])
comp["agree"] = comp["MATCH"] == "match"

counts = comp.groupby("biome").size()
print("\nNumber of sites per biome:\n")
print(counts.sort_values(ascending=False))

agreement = (
    comp.groupby("biome")["agree"]
    .mean()
    .reset_index()
)
agreement["agree_percent"] = agreement["agree"] * 100
agreement = agreement.sort_values("agree_percent")

plt.figure(figsize=(10, 6))

sns.barplot(
    data=agreement,
    x="biome",
    y="agree_percent",
    palette=sns.color_palette("BuPu", n_colors=len(agreement))
)

plt.xticks(rotation=45, ha="right")
plt.ylabel("Agreement (%)")
plt.xlabel("Biome")
plt.title("Agreement Between ET and GPP Categories by Biome")

plt.ylim(0, 100)
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig(
    "figs/NEW_FIGS/agreement_by_biome_from_sites.png",
    dpi=300
)
plt.show()

# Grasslands                     14
# Deciduous Broadleaf Forest      5
# Evergreen Needleleaf Forest     4
# Woody Savannas                  4
# Mixed Forest                    3
# Savannas                        3
# Closed Shrubland                2
# Open Shrubland                  2