import pandas as pd

et = pd.read_csv("runs/RF/RF_run_with_lagged_et02/events_iqr.csv", low_memory=False)
gpp  = pd.read_csv("gpp_paper/revision_lagged_gpp_12_remove_medium/events_iqr.csv",  low_memory=False)

gpp_sites = set(gpp[gpp["R2"] > 0.7]["SITE_ID"].unique())
et_sites  = set(et[et["R2"]  > 0.7]["SITE_ID"].unique())

table = pd.concat([gpp, et])
table = table[table["R2"] > 0.7].groupby("SITE_ID").agg(
    total       = ("event_percentileof_test", "count"),
    outside_iqr = ("event_percentileof_test", lambda x: (x > 75).sum())
).reset_index()

table["meets_threshold"] = table["outside_iqr"] > 4

print(f"Question 4: How many anomalies are there for each of our sites?")
print(table.sort_values("outside_iqr", ascending=False).to_string(index=False))

print(f"\nQuestion 5: How many of the anomalies at each site are outside of the 25th-75th percentile?")
print(f"Total sites:                  {len(table)}")
print(f"Sites with >4 outside IQR:    {table['meets_threshold'].sum()}")
print(f"Sites without >4 outside IQR: {(~table['meets_threshold']).sum()}")


# Question 4: How many anomalies are there for each of our sites?
# SITE_ID  total  outside_iqr  meets_threshold
#  US-Wkg    219          143             True
#  US-Var    230          112             True
#  US-Ton    149           95             True
#  US-Whs    102           68             True
#  JP-SMF     64           52             True
#  AU-TTE     55           45             True
#  US-SRM     66           43             True
#  AU-ASM     52           43             True
#  IT-SRo    112           41             True
#  NL-Loo     51           39             True
#  RU-Ha1     41           36             True
#  AU-Stp     78           34             True
#  ES-Amo     40           34             True
#  AU-Cpr     43           34             True
#  AU-Rig     43           28             True
#  AU-Gin     36           27             True
#  US-AR1     35           26             True
#  IT-Noe     36           25             True
#  CN-Dan     22           22             True
#  US-Goo     39           21             True
#  US-SRC     31           21             True
#  AU-Dry     45           20             True
#  IT-Cpz     29           20             True
#  SD-Dem     34           19             True
#  IT-Ro1     46           19             True
#  CN-Qia     22           19             True
#  DE-Hai     30           18             True
#  CN-Cng     25           17             True
#  CA-Oas     18           16             True
#  AU-RDF     41           16             True
#  DK-Sor     18           16             True
#  AU-How     17           14             True
#  DE-Tha     15           14             True
#  US-ARc     17           12             True
#  CA-SF2     19           12             True
#  US-LWW     16           11             True
#  AU-Whr     12           11             True
#  US-KS2     32           10             True
#  PA-SPs     14           10             True
#  CA-SF1     17           10             True
#  AU-Ync      9            9             True
#  US-Syv     10            8             True
#  US-ARb     12            8             True
#  CA-NS4     10            8             True
#  IT-CA1     11            7             True
#  US-WCr     28            6             True
#  AU-Emr     19            6             True
#  US-KS1      9            5             True
#  US-Blo      4            4            False
#  US-Sta      4            4            False
#  CA-NS3      5            4            False
#  CN-Du3      7            3            False
#  BE-Vie      9            3            False
#  AU-Wom      5            3            False
#  FR-LBr     21            3            False
#  CN-Cha     33            2            False
#  CH-Cha      9            2            False
#  CA-NS1      4            2            False
#  SN-Dhr      4            1            False
#  CN-Din      4            1            False
#  CH-Oe1      7            1            False
#  CA-SF3      7            1            False
#  IT-Isp     14            0            False
#  US-SRG     11            0            False
#  US-IB2      5            0            False
#  US-AR2      8            0            False
#  CA-NS6     11            0            False
#  ES-LJu      4            0            False
#remove false for analysis

# Question 5: How many of the anomalies at each site are outside of the 25th-75th percentile?
# Total sites:                  68
# Sites with >4 outside IQR:    48 # THIS IS SIMILAR TO OUTPUT FROM GPP ANALYIS
# Sites without >4 outside IQR: 20