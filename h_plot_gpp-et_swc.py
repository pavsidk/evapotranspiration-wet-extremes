import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import seaborn as sns
from scipy.stats import linregress


et = pd.read_csv(
    "runs/RF/RF_run_with_lagged_et02/events_iqr.csv",
    low_memory=False
)

gpp = pd.read_csv(
    "gpp_paper/revision_lagged_gpp_12_remove_medium/events_iqr.csv",
    low_memory=False
)

# FILTERING SITES TO HAVE ABOVE 0.7 PERFORMANCE
gpp_sites = set(gpp[gpp["R2"] > 0.7]["SITE_ID"].unique())
et_sites  = set(et[et["R2"]  > 0.7]["SITE_ID"].unique())


shared_sites = gpp_sites & et_sites
gpp_shared = gpp[gpp["SITE_ID"].isin(shared_sites)]
et_shared  = et[et["SITE_ID"].isin(shared_sites)]

#MERGING BOTH SHARED SITES DATA
merged = pd.merge(
    gpp_shared,
    et_shared,
    on=["SITE_ID", "day"],
    how="inner"
)


#DIFFERENCE VAR
merged["gpp_minus_et"] = (
    merged["anomaly_norm_gpp"]
    - merged["anomaly_norm_et"]
)

x = merged["SWC_F_MDS_1_x"]
y = merged["gpp_minus_et"]
valid = x.notna() & y.notna()
x = x[valid]
y = y[valid]



#PLOT
plt.figure(figsize=(8,6))

hb = plt.hist2d(
    x, y,
    bins=40,
    cmap="Blues"
)


cbar = plt.colorbar()
cbar.set_label("Number of days")


slope, intercept, r_value, _, _ = linregress(x, y)
x_line = np.linspace(x.min(), x.max(), 100)
y_line = slope * x_line + intercept
plt.plot(x_line, y_line, color="black", linewidth=2)

plt.text(
    0.95, 0.95,
    f"r = {r_value:.2f}",
    transform=plt.gca().transAxes,
    ha="right",
    va="top",
    fontsize=12
)

plt.xlabel("Soil moisture [m³/m³]")
plt.ylabel("Normalized GPP − ET anomaly [-]")
plt.title("GPP − ET vs Soil Moisture")

plt.tight_layout()
plt.savefig("figs/NEW_FIGS/gpp-et_swc.png")