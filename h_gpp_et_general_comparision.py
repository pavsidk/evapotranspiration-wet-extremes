import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math

gpp_run = sys.argv[1]
et_run  = sys.argv[2]

gpp = pd.read_csv(f"new_runs/RF/{gpp_run}/events_iqr.csv")
et  = pd.read_csv(f"runs/RF/{et_run}/events_iqr.csv")
gpp_iqr = pd.read_csv(f"output_anomalies/{gpp_run}_testuncertainty.csv")
et_iqr  = pd.read_csv(f"output_anomalies/{et_run}_testuncertainty.csv")

gpp = gpp[["SITE_ID","day","actual - predicted","category"]].rename(columns={"actual - predicted":"gpp"})
et = et[["SITE_ID","day","actual - predicted"]].rename(columns={"actual - predicted":"et"})

#merges both so we only keep sites present in both ET and GPP dfs
df = gpp.merge(et,on=["SITE_ID","day"])
sites = sorted(df["SITE_ID"].unique())


rows = 3
cols = math.ceil(len(sites) / rows)
fig, axs = plt.subplots(rows, cols, figsize=(4*cols, 3*rows))
axs = axs.flatten()

for i,site in enumerate(sites):

    ax = axs[i]
    cat = gpp[gpp["SITE_ID"]==site]["category"].iloc[0]
    gpp_thresh = gpp_iqr[gpp_iqr["SITE_ID"] == site].iloc[0]
    et_thresh  = et_iqr[et_iqr["SITE_ID"] == site].iloc[0]
    ax.fill_between(
        [-0.4,0.4],
        gpp_thresh["p25"],
        gpp_thresh["p75"],
        color="#D09621",
        alpha=0.5
    )
    ax.fill_between(
        [0.6,1.4],
        et_thresh["p25"],
        et_thresh["p75"],
        color="#98CA53",
        alpha=0.25
    )
    s = df[df["SITE_ID"]==site]
    sns.swarmplot(x=["GPP"]*len(s),y=s["gpp"],color="blue",ax=ax)
    sns.swarmplot(x=["ET"]*len(s),y=s["et"],color="red",ax=ax)
    
    ax.set_title(f"{site}\n({cat})")
    ax.axhline(0,color="gray")
    ax.set_ylim(-6,6)
    ax.set_ylabel("Anomaly")
    
for j in range(len(sites),len(axs)):
    axs[j].axis("off")


plt.tight_layout()
plt.savefig("gpp_et_compare.svg")