import pandas as pd
import matplotlib.pyplot as plt
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("--gpp")
parser.add_argument("--et")
parser.add_argument("--out_dir", default="plots")
args = parser.parse_args()

gpp = pd.read_csv(args.gpp)
et  = pd.read_csv(args.et)

gpp_sites = set(gpp[gpp["R2"] > 0.7]["SITE_ID"])
et_sites  = set(et[et["R2"]  > 0.7]["SITE_ID"])

shared_sites = gpp_sites & et_sites

gpp = gpp[gpp["SITE_ID"].isin(shared_sites)]
et  = et[et["SITE_ID"].isin(shared_sites)]

gpp["var"] = "GPP"
gpp["anom"] = gpp["anomaly_norm_gpp"]

et["var"] = "ET"
et["anom"] = et["anomaly_norm_et"]

df = pd.concat([gpp, et], ignore_index=True)

if "DATE" in df.columns:
    df["DATE"] = pd.to_datetime(df["DATE"], errors="coerce")
else:
    df["DATE"] = pd.to_datetime(df["day"], errors="coerce")

df = df.dropna(subset=["DATE"])

counts = df.groupby(["SITE_ID", "DATE"])["var"].nunique().reset_index()
valid = counts[counts["var"] == 2][["SITE_ID", "DATE"]]
df = df.merge(valid, on=["SITE_ID", "DATE"])

os.makedirs(args.out_dir, exist_ok=True)

for site in sorted(shared_sites):

    site_df = df[df["SITE_ID"] == site]

    if site_df.empty:
        continue

    dates = sorted(site_df["DATE"].unique())[:150]

    fig, ax = plt.subplots(figsize=(8, min(len(dates)*0.25, 12)))

    for i, d in enumerate(dates):
        sub = site_df[site_df["DATE"] == d]

        ax.scatter(
            sub["anom"],
            [i]*len(sub),
            c=sub["var"].map({"GPP":"green", "ET":"orange"}),
            s=40
        )

    ax.set_yticks(range(len(dates)))
    ax.set_yticklabels([str(d)[:10] for d in dates], fontsize=6)
    ax.axvline(0)
    ax.set_title(site)
    ax.set_xlabel("Anomaly")

    plt.subplots_adjust(left=0.3, right=0.95, top=0.95, bottom=0.05)

    fname = site.replace("/", "_")
    plt.savefig(f"{args.out_dir}/{fname}.png", dpi=150, bbox_inches="tight")
    plt.close()

    print("saved", fname)