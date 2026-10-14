import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

et = pd.read_csv(
    "runs/RF/RF_run_with_lagged_et02/events_iqr.csv"
)

gpp = pd.read_csv(
    "gpp_paper/revision_lagged_gpp_12_remove_medium/events_iqr.csv"
)

et_sites = et.drop_duplicates(subset="SITE_ID")[[
    "SITE_ID", "LOCATION_LAT", "LOCATION_LONG", "category", "IGBP"
]]

gpp_sites = gpp.drop_duplicates(subset="SITE_ID")[[
    "SITE_ID", "category"
]]

merged = pd.merge(
    et_sites,
    gpp_sites,
    on="SITE_ID",
    suffixes=("_et", "_gpp")
)

merged = merged.dropna(subset=["LOCATION_LAT", "LOCATION_LONG"])


merged["agreement"] = merged["category_et"] == merged["category_gpp"]

# Convert to GeoDataFrame
gdf = gpd.GeoDataFrame(
    merged,
    geometry=gpd.points_from_xy(merged["LOCATION_LONG"], merged["LOCATION_LAT"]),
    crs="EPSG:4326"
)

#SAVING CSV
output_df = pd.DataFrame({
    "SITE_ID": merged["SITE_ID"],
    "IGBP": merged["IGBP"],
    "CATEGORY_GPP": merged["category_gpp"],
    "CATEGORY_ET": merged["category_et"],
    "MATCH": merged["agreement"].map({True: "match", False: "no match"})
})

output_df.to_csv(
    "figs/NEW_FIGS/et_vs_gpp_site_comparison.csv",
    index=False
)



world = gpd.read_file(
    "https://naturalearth.s3.amazonaws.com/110m_cultural/ne_110m_admin_0_countries.zip"
)

fig, ax = plt.subplots(figsize=(10, 6))


world.plot(ax=ax, color="#f5f5f5", edgecolor="gray", linewidth=0.5)

gdf[gdf["agreement"]].plot(
    ax=ax,
    color="#2ecc71",
    markersize=40,
    label="Matching Classification"
)

gdf[~gdf["agreement"]].plot(
    ax=ax,
    color="#e74c3c",
    markersize=40,
    label="Non-matching Classification"
)

ax.set_title("ET vs GPP Category Classification Agreement")
ax.set_xticks([])
ax.set_yticks([])

plt.legend()
plt.tight_layout()

plt.savefig(
    "figs/NEW_FIGS/et_vs_gpp_agreement_map.png",
    dpi=300
)

plt.show()