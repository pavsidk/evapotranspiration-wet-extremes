import pandas as pd
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--gpp"); parser.add_argument("--et")
parser.add_argument("--out", default="out.png")
args = parser.parse_args()

frames = []
if args.gpp:
    gpp = pd.read_csv(args.gpp, low_memory=False)
    gpp["var"] = "GPP"; gpp["anom"] = gpp["anomaly_norm_gpp"]
    frames.append(gpp)
if args.et:
    et = pd.read_csv(args.et, low_memory=False)
    et["var"] = "ET"; et["anom"] = et["anomaly_norm_et"]
    frames.append(et)

df = pd.concat(frames)
df = df[df["storm_length_so_far"].notna()]
df["day_in_storm"] = df["storm_length_so_far"].astype(int)
df["row_label"] = df["SITE_ID"] + ", Day " + df["day_in_storm"].astype(str)

row_order = (df[["SITE_ID","day_in_storm","row_label"]].drop_duplicates()
               .sort_values(["SITE_ID","day_in_storm"])["row_label"].tolist())

fig, ax = plt.subplots(figsize=(9, len(row_order) * 0.4 + 1))
for i, label in enumerate(row_order):
    sub = df[df["row_label"] == label]
    ax.scatter(sub["anom"], [i]*len(sub),
               c=sub["var"].map({"GPP":"#2e7d32","ET":"#e65100"}), s=50, alpha=0.8)

ax.set_yticks(range(len(row_order))); ax.set_yticklabels(row_order, fontsize=7)
ax.invert_yaxis(); ax.axvline(0, color="gray"); ax.set_xlabel("Normalized Anomaly")
ax.margins(y=0.01)
plt.tight_layout(); plt.savefig(args.out, dpi=150)