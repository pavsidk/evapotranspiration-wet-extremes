import pandas as pd

et = pd.read_csv("runs/RF/RF_run_with_lagged_et02/events_iqr.csv", low_memory=False)
gpp  = pd.read_csv("gpp_paper/revision_lagged_gpp_12_remove_medium/events_iqr.csv",  low_memory=False)

gpp_sites = set(gpp[gpp["R2"] > 0.7]["SITE_ID"].unique())
et_sites  = set(et[et["R2"]  > 0.7]["SITE_ID"].unique())

shared   = gpp_sites & et_sites   # these were in both GPP and ET analysis
new      = et_sites - gpp_sites   # in ET study but not GPP
removed  = gpp_sites - et_sites   # in GPP study but not ET
dfShared = pd.DataFrame(shared)
dfNew = pd.DataFrame(new)
dfRemoved = pd.DataFrame(removed)
dfShared.to_csv('questions/sharedSites.csv')
dfNew.to_csv('questions/newSites.csv')
dfRemoved.to_csv('questions/removedSites.csv')


print(f"Question 1: How many of the sites in our current study (with RF R2>0.7) were also in the GPP study?")
print(f"Shared sites:  {len(shared)}")

print(f"Question 2: How many ‘new’ sites do we have and how many ‘old’ sites do we no longer have?")
print(f"New sites:     {len(new)}")
print(f"Removed sites: {len(removed)}")
print(f"\nNew:     {sorted(new)}")
print(f"Removed: {sorted(removed)}")

# Question 1: How many of the sites in our current study (with RF R2>0.7) were also in the GPP study?
# Shared sites:  37

# Question 2: How many ‘new’ sites do we have and how many ‘old’ sites do we no longer have?
# New sites:     14
# Removed sites: 17
