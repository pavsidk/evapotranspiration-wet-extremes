# AppEEARS Point Sample Extraction Readme  

## Table of Contents  

1. Request Parameters  
2. Request File Listing  
3. Point Sample Extraction Process  
4. Data Quality  
    4.1. Moderate Resolution Imaging Spectroradiometer (MODIS)  
    4.2. NASA MEaSUREs Shuttle Radar Topography Mission (SRTM) Version 3 (v3)  
    4.3. NASA Visible Infrared Imaging Radiometer Suite (VIIRS)  
    4.4. Soil Moisture Active Passive (SMAP)  
    4.5. Daymet (v4R1)
    4.6.1. Ecosystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) Swath V2  
    4.6.2. Ecosystem Spaceborne Thermal Radiometer Experiment on Space Station (ECOSTRESS) Tiled V2
    4.7. Advanced Spaceborne Thermal Emission and Reflection Radiometer (ASTER) Global Digital Elevation Model (GDEM) Version 3 (v3) and Global Water Bodies Database (WBD) Version 1 (v1)  
    4.8. NASA MEaSUREs NASA Digital Elevation Model (DEM) Version 1 (v1)  
    4.9. Harmonized Landsat Sentinel-2 (HLS) Version 2.0
    4.10. Landsat Collection 2 (C2) U.S. Analysis Ready Data (ARD)  
    4.11. US National Park Service (NPS) Historical Water Balance for the Continental United States (CONUS)
    4.12. Earth surface Mineral dust source InvesTigation (EMIT) L1B Radiance and L2A Reflectance Collections
    4.13. Earth surface Mineral dust source InvesTigation (EMIT) L2B Estimated Mineral Identification, Band Depth and Uncertainty Collection
5. Data Caveats  
6. Documentation  
7. Sample Request Retention  
8. Data Product Citations  
9. Software Citation  
10. Feedback  

## 1. Request Parameters  

    Name: LE_sites  

    Date Completed:** 2026-01-19T01:37:08.242906  

    ID: 79173e83-7412-436b-b94a-a3bb7ab7c1e4  

    Details:  

        Start Date: 01-01-2000  

        End Date: 01-17-2026
    
        Layers:  

            Lai_500m (MOD15A2H.061)  
    
        Coordinates:  

            AR-SLu, , -33.4648, -66.4598  
            AR-Vir, , -28.2395, -56.1886  
            AT-Neu, , 47.1167, 11.3175  
            AU-ASM, , -22.283, 133.249  
            AU-Ade, , -13.0769, 131.1178  
            AU-Cpr, , -34.0021, 140.5891  
            AU-Cum, , -33.6152, 150.7236  
            AU-DaP, , -14.0633, 131.3181  
            AU-DaS, , -14.1593, 131.3881  
            AU-Dry, , -15.2588, 132.3706  
            AU-Emr, , -23.8587, 148.4746  
            AU-Fog, , -12.5452, 131.3072  
            AU-GWW, , -30.1913, 120.6541  
            AU-Gin, , -31.3764, 115.7138  
            AU-How, , -12.4943, 131.1523  
            AU-Lox, , -34.4704, 140.6551  
            AU-RDF, , -14.5636, 132.4776  
            AU-Rig, , -36.6499, 145.5759  
            AU-Rob, , -17.1175, 145.6301  
            AU-Stp, , -17.1507, 133.3502  
            AU-TTE, , -22.287, 133.64  
            AU-Tum, , -35.6566, 148.1517  
            AU-Wac, , -37.4259, 145.1878  
            AU-Whr, , -36.6732, 145.0294  
            AU-Wom, , -37.4222, 144.0944  
            AU-Ync, , -34.9893, 146.2907  
            BE-Bra, , 51.3076, 4.5198  
            BE-Lon, , 50.5516, 4.7462  
            BE-Vie, , 50.3049, 5.9981  
            BR-Npw, , -16.498, -56.412  
            BR-Sa1, , -2.8567, -54.9589  
            BR-Sa3, , -3.018, -54.9714  
            BW-Gum, , -18.9647, 22.3711  
            BW-Nxr, , -19.5481, 23.1792  
            CA-Gro, , 48.2167, -82.1556  
            CA-Man, , 55.8796, -98.4808  
            CA-NS1, , 55.8792, -98.4839  
            CA-NS2, , 55.9058, -98.5247  
            CA-NS3, , 55.9117, -98.3822  
            CA-NS4, , 55.9144, -98.3806  
            CA-NS5, , 55.8631, -98.485  
            CA-NS6, , 55.9167, -98.9644  
            CA-NS7, , 56.6358, -99.9483  
            CA-Oas, , 53.6289, -106.1978  
            CA-Obs, , 53.9872, -105.1178  
            CA-Qfo, , 49.6925, -74.3421  
            CA-SCB, , 61.3089, -121.2984  
            CA-SCC, , 61.3079, -121.2992  
            CA-SF1, , 54.485, -105.8176  
            CA-SF2, , 54.2539, -105.8775  
            CA-SF3, , 54.0916, -106.0053  
            CA-TP1, , 42.6609, -80.5595  
            CA-TP2, , 42.7744, -80.4588  
            CA-TP3, , 42.7068, -80.3483  
            CA-TP4, , 42.7102, -80.3574  
            CA-TPD, , 42.6353, -80.5577  
            CG-Tch, , -4.2892, 11.6564  
            CH-Cha, , 47.2102, 8.4104  
            CH-Dav, , 46.8153, 9.8559  
            CH-Fru, , 47.1158, 8.5378  
            CH-Lae, , 47.4783, 8.3644  
            CH-Oe1, , 47.2858, 7.7319  
            CH-Oe2, , 47.2864, 7.7337  
            CN-Cha, , 42.4025, 128.0958  
            CN-Cng, , 44.5934, 123.5092  
            CN-Dan, , 30.4978, 91.0664  
            CN-Din, , 23.1733, 112.5361  
            CN-Du2, , 42.0467, 116.2836  
            CN-Du3, , 42.0551, 116.2809  
            CN-Ha2, , 37.6086, 101.3269  
            CN-HaM, , 37.37, 101.18  
            CN-Hgu, , 32.8453, 102.59  
            CN-Qia, , 26.7414, 115.0581  
            CN-Sw2, , 41.7902, 111.8971  
            CZ-BK1, , 49.5021, 18.5369  
            CZ-BK2, , 49.4944, 18.5429  
            CZ-wet, , 49.0247, 14.7704  
            DE-Akm, , 53.8662, 13.6834  
            DE-Dgw, , 53.1514, 13.0543  
            DE-Geb, , 51.0997, 10.9146  
            DE-Gri, , 50.95, 13.5126  
            DE-Hai, , 51.0792, 10.4522  
            DE-Hte, , 54.2103, 12.1761  
            DE-Kli, , 50.8931, 13.5224  
            DE-Lkb, , 49.0996, 13.3047  
            DE-Lnf, , 51.3282, 10.3678  
            DE-Obe, , 50.7867, 13.7213  
            DE-RuR, , 50.6219, 6.3041  
            DE-RuS, , 50.8659, 6.4471  
            DE-Seh, , 50.8706, 6.4497  
            DE-SfN, , 47.8064, 11.3275  
            DE-Spw, , 51.8922, 14.0337  
            DE-Tha, , 50.9626, 13.5651  
            DE-Zrk, , 53.8759, 12.889  
            DK-Eng, , 55.6905, 12.1918  
            DK-Fou, , 56.4842, 9.5872  
            DK-Sor, , 55.4859, 11.6446  
            ES-Amo, , 36.8336, -2.2523  
            ES-LJu, , 36.9266, -2.7521  
            ES-LgS, , 37.0979, -2.9658  
            ES-Ln2, , 36.9695, -3.4758  
            FI-Hyy, , 61.8474, 24.2948  
            FI-Jok, , 60.8986, 23.5134  
            FI-Let, , 60.6418, 23.9595  
            FI-Lom, , 67.9972, 24.2092  
            FI-Si2, , 61.8372, 24.1967  
            FI-Sii, , 61.8327, 24.1928  
            FI-Sod, , 67.3624, 26.6386  
            FR-Fon, , 48.4764, 2.7801  
            FR-Gri, , 48.8442, 1.9519  
            FR-LBr, , 44.7171, -0.7693  
            FR-LGt, , 47.3229, 2.2841  
            FR-Pue, , 43.7413, 3.5957  
            GF-Guy, , 5.2788, -52.9249  
            GH-Ank, , 5.2685, -2.6942  
            GL-NuF, , 64.1308, -51.3861  
            GL-ZaF, , 74.4814, -20.5545  
            GL-ZaH, , 74.4733, -20.5503  
            HK-MPM, , 22.4982, 114.0292  
            ID-Pag, , -2.32, 113.9  
            IT-BCi, , 40.5237, 14.9574  
            IT-CA1, , 42.3804, 12.0266  
            IT-CA2, , 42.3772, 12.026  
            IT-CA3, , 42.38, 12.0222  
            IT-Cas, , 45.07, 8.7175  
            IT-Col, , 41.8494, 13.5881  
            IT-Cp2, , 41.7043, 12.3573  
            IT-Cpz, , 41.7052, 12.3761  
            IT-Isp, , 45.8126, 8.6336  
            IT-La2, , 45.9542, 11.2853  
            IT-Lav, , 45.9562, 11.2813  
            IT-MBo, , 46.0147, 11.0458  
            IT-Noe, , 40.6062, 8.1517  
            IT-PT1, , 45.2009, 9.061  
            IT-Ren, , 46.5869, 11.4337  
            IT-Ro1, , 42.4081, 11.93  
            IT-Ro2, , 42.3903, 11.9209  
            IT-SR2, , 43.732, 10.2909  
            IT-SRo, , 43.7279, 10.2844  
            IT-Tor, , 45.8444, 7.5781  
            JP-BBY, , 43.323, 141.8107  
            JP-MBF, , 44.3869, 142.3186  
            JP-Mse, , 36.0539, 140.0269  
            JP-SMF, , 35.2617, 137.0788  
            JP-SwL, , 36.0466, 138.1084  
            KR-CRK, , 38.2013, 127.2506  
            MY-MLM, , 1.4536, 111.1495  
            MY-PSO, , 2.973, 102.3062  
            NL-Hor, , 52.2403, 5.0713  
            NL-Loo, , 52.1666, 5.7436  
            NZ-Kop, , -37.3879, 175.5539  
            PA-SPn, , 9.3181, -79.6346  
            PA-SPs, , 9.3138, -79.6314  
            PH-RiF, , 14.1412, 121.2653  
            RU-Ch2, , 68.6169, 161.3509  
            RU-Che, , 68.613, 161.3414  
            RU-Cok, , 70.8291, 147.4943  
            RU-Fy2, , 56.4476, 32.9019  
            RU-Fyo, , 56.4615, 32.9221  
            RU-Ha1, , 54.7252, 90.0022  
            RU-Sam, , 72.3738, 126.4958  
            RU-SkP, , 62.255, 129.168  
            RU-Tks, , 71.5943, 128.8878  
            RU-Vrk, , 67.0547, 62.9405  
            SD-Dem, , 13.2829, 30.4783  
            SE-Deg, , 64.182, 19.5565  
            SE-St1, , 68.3541, 19.0503  
            SJ-Adv, , 78.186, 15.923  
            SJ-Blv, , 78.9216, 11.8311  
            SN-Dhr, , 15.4028, -15.4322  
            UK-LBT, , 51.5215, -0.1389  
            US-A03, , 70.4953, -149.8823  
            US-A10, , 71.3242, -156.6149  
            US-AR1, , 36.4267, -99.42  
            US-AR2, , 36.6358, -99.5975  
            US-ARM, , 36.6058, -97.4888  
            US-ARb, , 35.5497, -98.0402  
            US-ARc, , 35.5465, -98.04  
            US-Atq, , 70.4696, -157.4089  
            US-BZB, , 64.6955, -148.3208  
            US-BZF, , 64.7013, -148.3121  
            US-BZS, , 64.6963, -148.3235  
            US-Beo, , 71.281, -156.6123  
            US-Bes, , 71.2809, -156.5965  
            US-Bi1, , 38.0992, -121.4993  
            US-Bi2, , 38.1091, -121.5351  
            US-Blo, , 38.8953, -120.6328  
            US-CRT, , 41.6285, -83.3471  
            US-Cop, , 38.09, -109.39  
            US-DPW, , 28.0521, -81.4361  
            US-EDN, , 37.6156, -122.114  
            US-EML, , 63.8784, -149.2536  
            US-GBT, , 41.3658, -106.2397  
            US-GLE, , 41.3665, -106.2399  
            US-Goo, , 34.2547, -89.8735  
            US-HRA, , 34.5852, -91.7517  
            US-HRC, , 34.5888, -91.7517  
            US-Ha1, , 42.5378, -72.1715  
            US-Ho1, , 45.2041, -68.7402  
            US-IB2, , 41.8406, -88.241  
            US-ICs, , 68.6058, -149.311  
            US-Ivo, , 68.4865, -155.7503  
            US-KS1, , 28.4583, -80.6709  
            US-KS2, , 28.6086, -80.6715  
            US-LA1, , 29.5013, -90.4449  
            US-LA2, , 29.8587, -90.2869  
            US-LWW, , 34.9604, -97.9789  
            US-Lin, , 36.3566, -119.0922  
            US-Los, , 46.0827, -89.9792  
            US-MAC, , 27.1632, -81.1873  
            US-MMS, , 39.3232, -86.4131  
            US-MRM, , 40.8164, -74.0435  
            US-Me1, , 44.5794, -121.5  
            US-Me2, , 44.4526, -121.5589  
            US-Me3, , 44.3154, -121.6078  
            US-Me4, , 44.4992, -121.6224  
            US-Me5, , 44.4372, -121.5668  
            US-Me6, , 44.3233, -121.6078  
            US-Myb, , 38.0499, -121.765  
            US-NC4, , 35.7879, -75.9038  
            US-NGB, , 71.28, -156.6092  
            US-NGC, , 64.8618, -163.7002  
            US-NR1, , 40.0329, -105.5464  
            US-Ne1, , 41.1651, -96.4766  
            US-Ne2, , 41.1649, -96.4701  
            US-Ne3, , 41.1797, -96.4397  
            US-ORv, , 40.0201, -83.0183  
            US-OWC, , 41.3795, -82.5125  
            US-Oho, , 41.5545, -83.8438  
            US-PFa, , 45.9459, -90.2723  
            US-Prr, , 65.1237, -147.4876  
            US-SRC, , 31.9083, -110.8395  
            US-SRG, , 31.7894, -110.8277  
            US-SRM, , 31.8214, -110.8661  
            US-Snd, , 38.0366, -121.754  
            US-Sne, , 38.0369, -121.7547  
            US-Srr, , 38.2006, -122.0264  
            US-StJ, , 39.0882, -75.4372  
            US-Sta, , 41.3966, -106.8024  
            US-Syv, , 46.242, -89.3477  
            US-Ton, , 38.4309, -120.966  
            US-Tw1, , 38.1074, -121.6469  
            US-Tw2, , 38.0969, -121.6365  
            US-Tw3, , 38.1152, -121.6469  
            US-Tw4, , 38.1027, -121.6413  
            US-Tw5, , 38.1072, -121.6426  
            US-Twt, , 38.1087, -121.6531  
            US-UMB, , 45.5598, -84.7138  
            US-UMd, , 45.5625, -84.6975  
            US-Uaf, , 64.8663, -147.8555  
            US-Var, , 38.4133, -120.9508  
            US-WCr, , 45.8059, -90.0799  
            US-WPT, , 41.4646, -82.9962  
            US-Whs, , 31.7438, -110.0522  
            US-Wi0, , 46.6188, -91.0814  
            US-Wi1, , 46.7305, -91.2329  
            US-Wi2, , 46.6869, -91.1528  
            US-Wi3, , 46.6347, -91.0987  
            US-Wi4, , 46.7393, -91.1663  
            US-Wi5, , 46.6531, -91.0858  
            US-Wi6, , 46.6249, -91.2982  
            US-Wi7, , 46.6491, -91.0693  
            US-Wi8, , 46.7223, -91.2524  
            US-Wi9, , 46.7385, -91.0746  
            US-Wkg, , 31.7365, -109.9419  
            ZA-Kru, , -25.0197, 31.4969  
            ZM-Mon, , -15.4391, 23.2525  
    
    Version: This request was processed by AppEEARS version 3.107  

## 2. Request File Listing  

- Comma-separated values file with data extracted for a specific product
  - LE-sites-MOD15A2H-061-results.csv
- Text file with data pool URLs for all source granules used in the extraction
  - LE-sites-granule-list.txt
- JSON request file which can be used in AppEEARS to create a new request
  - LE-sites-request.json
- xml file
  - LE-sites-MOD15A2H-061-metadata.xml  

## 3. Point Sample Extraction Process  

Datasets available in AppEEARS are served via OPeNDAP (Open-source Project for a Network Data Access Protocol) services. OPeNDAP services allow users to concisely pull pixel values from datasets via HTTPS requests. A middleware layer has been developed to interact with the OPeNDAP services. The middleware make it possible to extract scaled data values, with associated information, for pixels corresponding to a given coordinate and date range.

**NOTE:**  

- Requested date ranges may not match the reference date for multi-day products. AppEEARS takes an inclusive approach when extracting data for sample requests, often returning data that extends beyond the requested date range. This approach ensures that the returned data includes records for the entire requested date range.  
- For multi-day (8-day, 16-day, Monthly, Yearly) MODIS and Suomi NPP VIIRS datasets, the date field in the data tables reflects the first day of the composite period.  
- If selected, the SRTM v3, ASTER GDEM v3 and Global Water Bodies Database v1, and NASADEM v1 product will be extracted regardless of the time period specified in AppEEARS because it is a static dataset. The date field in the data tables reflects the nominal SRTM date of February 11, 2000.  
- If the visualizations indicate that there are no data to display, proceed to downloading the .csv output file. Data products that have both categorical and continuous data values (e.g. MOD15A2H) are not able to be displayed within the visualizations within AppEEARS.  

## 4. Data Quality  

When available, AppEEARS extracts and returns quality assurance (QA) data for each data file returned regardless of whether the user requests it. This is done to ensure that the user possesses the information needed to determine the usability and usefulness of the data they get from AppEEARS. Most data products available through AppEEARS have an associated QA data layer. Some products have more than one QA data layer to consult. See below for more information regarding data collections/products and their associated QA data layers.  

### 4.1. MODIS (Terra, Aqua, & Combined)

All MODIS land products, as well as the MODIS Snow Cover Daily product, include quality assurance (QA) information designed to help users understand and make best use of the data that comprise each product. Results downloaded from AppEEARS and/or data directly requested via middleware services contain not only the requested pixel/data values but also the decoded QA information associated with each pixel/data value extracted.  

- See the MODIS Land Products QA Tutorials: <https://lpdaac.usgs.gov/resources/e-learning/> for more QA information regarding each MODIS land product suite.  
- See the MODIS Snow Cover Daily product user guide for information regarding QA utilization and interpretation.  

### 4.2. NASA MEaSUREs SRTM v3 (30m & 90m)  

SRTM v3 products are accompanied by an ancillary "NUM" file in place of the QA/QC files. The "NUM" files indicate the source of each SRTM pixel, as well as the number of input data scenes used to generate the SRTM v3 data for that pixel.  

- See the user guide: <https://lpdaac.usgs.gov/documents/179/SRTM_User_Guide_V3.pdf> for additional information regarding the SRTM "NUM" file.  

### 4.3. NASA VIIRS (Suomi National Polar-orbiting Partnership (Suomi NPP) & NOAA-20)  

All NASA VIIRS land products include quality information designed to help users understand and make best use of the data that comprise each product. For product-specific information, see the link to the NASA VIIRS products table provided in section 5.  

**NOTE:**  

- The version 2 Suomi NPP NASA VIIRS Surface Reflectance data products VNP09A1 and VNP09H1 contain two quality layers: `SurfReflect_State` and `SurfReflect_QC`. 

### 4.4. SMAP  

SMAP products provide multiple means to assess quality. Each data product contains bit flags, uncertainty measures, and file-level metadata that provide quality information. Results downloaded from AppEEARS and/or data directly requested via middleware services contain not only the requested pixel/data values, but also the decoded bit flag information associated with each pixel/data value extracted. For additional information regarding the specific bit flags, uncertainty measures, and file-level metadata contained in this product, refer to the Quality Assessment section of the user guide for the specific SMAP data product in your request: <https://nsidc.org/data/smap/smap-data.html>  

### 4.5. Daymet v4R1

Daymet station-level daily weather observation data and the corresponding Daymet model predicted data for three Daymet model parameters: minimum temperature (tmin), maximum temperature (tmax), and daily total precipitation (prcp) are available. These data provide information into the regional accuracy of the Daymet model for the three station-level input parameters. Corresponding comma separated value (.csv) files that contain metadata for every surface weather station for the variable-year combinations are also available. <https://doi.org/10.3334/ORNLDAAC/2129>

### 4.6 ECOSTRESS

#### 4.6.1. ECOSTRESS Swath V2  

Quality information varies by product for the ECOSTRESS product suite. Quality Assurance (QA) information for ECO_L2_LSTE.002, including the bit definition index for the quality layer, is provided in section 2.4 of the User Guide: <https://lpdaac.usgs.gov/documents/1574/ECOL2_User_Guide_V2.pdf>. For Land Surface Temperature and Emissivity (LSTE) product, the quality flags of the source data are available in the ECO_L2_LSTE.002 data product. Please note that unlike V1, the V2 LSTE product does not incorporate cloud cover into the Pixel Produced QA bit flag. This flag now relates to other variables only (See Table 6 in User Guide). Users should apply the cloud mask separately to account for pixels with cloud when using ECO_L2_LSTE.002 data product.  Cloud mask derived from ECO_L2_CLOUD.002 is and Water mask derived from the Shuttle Radar Topography Mission (SRTM) Digital Elevation Model are available as separate science dataset (SDS) layers in the ECO_L2_LSTE.002 data product. Additionally, cloud and cloud confidence layers are available in the ECO_L2_CLOUD.002 product. Results downloaded from AppEEARS contain requested pixel/data values, decoded Quality Assurance (QA), and cloud information associated with each pixel/data value extracted.

#### 4.6.2. ECOSTRESS Tiled V2  

Quality information varies by product for the ECOSTRESS product suite. Quality information for ECO_L2T_LSTE.002, including the bit definition index for the quality layer, is provided in section 2.4 of the User Guide: <https://lpdaac.usgs.gov/documents/1574/ECOL2_User_Guide_V2.pdf>. Results downloaded from AppEEARS contain requested pixel/data values and decoded QA information associated with each pixel/data value extracted. For Land Surface Temperature and Emissivity (LSTE) product, the quality flags of the source data are available as a separate SDS layer in the ECO_L2T_LSTE.002 collection, however this Pixel Produced QA bit flags do not account for cloud cover. Users should apply the cloud mask separately to account for pixels with cloud when using ECO_L2T_LSTE.002 collection. In addition to decoded quality information, AppEEARS returns the cloud mask information for requests including layers from ECO_L2T_LSTE.002.

For high-level products, Cloud mask derived from ECO_L2_CLOUD.002 and Water mask derived from the Shuttle Radar Topography Mission (SRTM) Digital Elevation Model are available as separate science dataset (SDS) layers in the ECO_L2T_LSTE.002 data product.

### 4.7. ASTER GDEM v3 and Global Water Bodies Database v1  

ASTER GDEM v3 data are accompanied by an ancillary "NUM" file in place of the QA/QC files. The "NUM" files refer to the count of ASTER Level-1A scenes that were processed for each pixel or the source of reference data used to replace anomalies. The ASTER Global Water Bodies Database v1 products do not contain QA/QC files.  

- See Section 7 of the ASTER GDEM user guide: <https://lpdaac.usgs.gov/documents/434/ASTGTM_User_Guide_V3.pdf> for additional information regarding the GDEM "NUM" file.  
- See Section 7 of the ASTER Global Water Bodies Database user guide: <https://lpdaac.usgs.gov/documents/436/ASTWBD_User_Guide_V1.pdf> for a comparison with the SRTM Water Body Dataset.  

### 4.8. NASA MEaSUREs NASADEM v1 (30m)  

NASADEM v1 products are accompanied by an ancillary "NUM" file in place of the QA/QC files. The "NUM" files indicate the source of each NASADEM pixel, as well as the number of input data scenes used to generate the NASADEM v1 data for that pixel.  

- See the NASADEM user guide: <https://lpdaac.usgs.gov/documents/592/NASADEM_User_Guide_V1.pdf> for additional information regarding the NASADEM "NUM" file.  

### 4.9. HLS v2.0  

HLS v2.0 Operational Land Imager (OLI) Surface Reflectance and TOA Brightness Daily Global 30m (HLSL30 v002) and Sentinel-2 Multi-spectral Instrument (MSI) Surface Reflectance Daily Global 30m (HLSS30 v002) products have a quality assessment layer enabling per-pixel masking of cloud, cloud shadow, snow, water, and aerosol optical thickness levels. Quality information for HLSL30 v002 and HLSS30 v002 products, including bit definitions for the quality layer can be found in section 6.4 of the User Guide: <https://lpdaac.usgs.gov/documents/1326/HLS_User_Guide_V2.pdf>.  

### 4.10. Landsat Collection 2 ARD

Landsat C2 U.S. Analysis Ready Data (ARD) products are available for conterminous United States (CONUS)(1982-Present), Alaska (1984-present), and Hawaii (1989-1993, 1999-present). These data are products of Landsat 8/9 Operational Land Imager 2 (OLI-2) / Thermal Infrared Sensor 2 (TIRS-2), Landsat 7 Enhanced Thematic Mapper Plus (ETM+) and Landsat 4-5 Thematic Mapper (TM). The ARD significantly reduces the magnitude of data processing for application scientists. These data contain a quality assessment derived from Fmask version 3.3.1, Aerosol and Cloud QA derived from atmospheric compensation algorithms, and radiometric saturation QA derived from detector's input signal level. More details can be found in the Landsat Collection 2 U.S. ARD DFCB: <https://d9-wret.s3.us-west-2.amazonaws.com/assets/palladium/production/s3fs-public/media/files/LSDS-1435%20Landsat%20C2%20US%20ARD%20Data%20Format%20Control%20Book-v3.pdf>

### 4.11. US NPS Water Balance

The US NPS Historical Water Balance products do not have associated QA files or layers.

### 4.12. EMIT L1B Radiance and L2A Reflectance

The functionality of AppEEARS surrounding EMIT data is somewhat unique. There are currently no visualizations included within the AppEEARS UI, these will be added at a later date. Point requests return a comma separated variable (.csv) file organized in long format, rather than wide format to improve readability, resulting in some duplicate data for non-wavelength associated dimensions.  EMIT L1B At-Sensor Calibrated Radiance and Geolocation Data 60m (EMITL1BRAD) collection does not include quality information. EMIT L2A Estimated Surface Reflectance and Uncertainty and Masks 60m (EMITL2ARFL) collection does not have a direct quality assessment, but has a `good_wavelengths` flag associated with atmospheric water absorption features indicating where reflectance was not calculated. Additionally, the Reflectance Uncertainty product (EMIT_L2A_RFLUNCERT) contains uncertainty estimates about the reflectance captured as per-pixel, per-band posterior standard deviations, and the EMIT L2A Mask (EMIT_L2A_Mask) contains atmospheric state estimates and binary flags that can be used for quality filtering. By default the `good_wavelengths` layer is included with all requests that include the L2A Reflectance Product. More details about the EMIT_L2A_Mask can be found in the EMITL2ARFL User Guide: <https://lpdaac.usgs.gov/documents/1569/EMITL2ARFL_User_Guide_v1.pdf>

### 4.13. EMIT L2B Estimated Mineral Identification, Band Depth and Uncertainty

Similarly to the EMIT L1B Radiance and L2A Reflectance products, AppEEARS functionality for the EMIT L2B Mineralogy is also unique. The EMIT L2B Estimated Mineral Identification, Band Depth and Uncertainty 60m ([EMITL2BMIN](https://doi.org/10.5067/EMIT/EMITL2BMIN.001)) collection is generated using the [Tetracorder system](https://www.usgs.gov/publications/tetracorder-user-guide-version-44?_gl=1*1eoj33d*_ga*MTU3MTA3ODgxNS4xNjQ5MTg1MDgx*_ga_0YWDZEJ295*MTY4NjkyNTg0Mi40NC4xLjE2ODY5MjU4NzMuMC4wLjA.) ([code](https://github.com/PSI-edu/spectroscopy-tetracorder)). Point requests return a comma separated variable (.csv) file organized in long format, rather than wide format to improve readability, resulting in some duplicate data for non-group associated dimensions. These outputs also include quality data from the EMITL2BMINUNCERT product by default. This quality data includes the band depth uncertainty estimates and a fit score for the mineral identification. Band depth uncertainties are presented as standard deviations and the fit score is provided as the coefficient of determination (r^2) of the match between the continuum normalized library reference and the continuum normalized observed spectrum. There are currently no visualizations included within the AppEEARS UI, these will be added at a later date. More info can be found on the [EMITL2BMIN collection page](https://doi.org/10.5067/EMIT/EMITL2BMIN.001).

## 5. Data Caveats  

### 5.1.1. ECOSTRESS Swath V2

- ECOSTRESS Swath data products are natively stored in swath format. To fulfill AppEEARS requests for ECOSTRESS Swath products, the data are first resampled from the native swath format to a georeferenced output. This requires the use of the requested ECOSTRESS product files and the corresponding ECO1BGEO: <https://doi.org/10.5067/ECOSTRESS/ECO1BGEO.001> files for all ECOSTRESS Swath products. To do this conversion, an index array and distance array are created, then the nearest area pixel is located. Next, the Euclidean distance to that area pixel plus all surrounding pixels is measured within a 210 meter search radius (+/- a 3 pixels). This results in 49 pixels measured for every swath pixel. If the distance measured is less than what's currently present in any distance array, then the new distance as well as the swath index value are recorded into the index array used to convert to an area output.

### 5.1.2. ECOSTRESS Tiled V2

- It is not uncommon for many .csv cells returned to contain NaN values. If any layer requested or the QC layer contains valid data, the remaining requested layers will be returned even if only NaN values are present.

### 5.2. Suomi NPP VIIRS Land Surface Phenology Product (VNP22Q2)

- A subset of the science datasets/variables for VNP22Q2 are returned in their raw, unscaled form. That is, these variables are returned without having their scale factor and offset applied. AppEEARS visualizations and output summary files are derived using the raw data value, and consequently do not characterize the intended information ("day of year") for the impacted variables. The variables returned in this state include:  

    1. Date_Mid_Greenup_Phase (Cycle 1 and Cycle 2)  
    2. Date_Mid_Senescence_Phase (Cycle 1 and Cycle 2)  
    3. Onset_Greenness_Increase (Cycle 1 and Cycle 2)  
    4. Onset_Greenness_Decrease (Cycle 1 and Cycle 2)  
    5. Onset_Greenness_Maximum (Cycle 1 and Cycle 2)  
    6. Onset_Greenness_Minimum (Cycle 1 and Cycle 2)  

- To convert the raw data to "day of year" (doy) for the above variables, use the following equation:  

      doy = Raw_Data_Value * 1 – (Given_Year - 2000) * 366

### 5.3 SMAP

#### 5.3.1. SMAP Enhanced L3 Radiometer Global and Polar Grid Daily 9 km EASE-Grid Soil Moisture (SPL3SMP_E)

- The SPL3SMP_E includes additional layers for AM and PM north-polar grid soil moisture retrievals. These additional layers are not supported in AppEEARS.

#### 5.3.2. SMAP L4 Global 3-hourly 9 km EASE-Grid Surface and Root Zone Soil Moisture Geophysical Data (SPL4SMGP)

- The SPL4SMGP provides 3-hourly data within a single day. AppEEARS specify the observation date and time in the output CSV file.

### 5.4. HLS v2.0

- When requesting HLS timeseries, note that Sentinel-2 launched after Landsat was already active. Landsat OLI (HLSL30 v002) products are available from 2013-04-11 to present, while Sentinel-2 MSI products (HLSS30 v002) are available from  2015-11-30 to present.
- Point requests are returned in geographic coordinates.  
- Extra granules may appear in the granule list output file if the target point is close to an area where MGRS tiles overlap.
- Historical processing of the HLS Vegetation Indices (VI) products (HLSS30_VI v002 and HLSL30_VI v002) has not started as of May 9, 2025. Data currently available in AppEEARS is from February 6, 2025 to present. 

### 5.5. MOD44B V6.1

- Value zero in the Cloud and Quality layers from MOD44B Version 6.1 Vegetation Continuous Fields (VCF) yearly product is assigned to Fill Value in the source file while value zero is meaningful for those layers. If comparing Cloud and Quality layers outputs with source files, users may notice that within the source files zero is assigned to fill value, however zero is within the valid range. Thus, AppEEARS outputs Use -999 as a fill value for those layers.

### 5.6. EMIT L1B Radiance and L2A Reflectance

- Elevation data is always included in requests. For API users there is an additional 'elev' layer listed, but that layer cannot be requested. This has to be present due to some constraints of AppEEARS' backend.
- For L1B Radiance and L2A reflectance products, the default included quality layer is 'good bands' which denotes where radiance/reflectance data were not estimated due to atmospheric water absorption features. This is included with all requests.
- The EMIT mission is focused on collecting data from land arid dust source regions, meaning that coverage is limited to those regions based upon a mask. You can explore coverage and forecasted coverage using Jet Propulsion Laboratory's [Visions: EMIT Open Data Portal](https://earth.jpl.nasa.gov/emit/data/data-portal/coverage-and-forecasts/)

### 5.7. EMIT L2B Estimated Mineral Identification, Band Depth and Uncertainty

- The EMIT_L2B_MIN product is generated to support the EMIT mission objectives of constraining the sign of dust-related radiative forcing. Ten mineral types are the core focus of this work: Calcite, Chlorite, Dolomite, Goethite, Gypsum, Hematite, Illite+Muscovite, Kaolinite, Montmorillonite, and Vermiculite. Additional minerals are included in this product for transparency but were not the focus of this product. Further validation is required to use these additional mineral maps, particularly in the case of resource exploration. Similarly, the separation of minerals with similar spectral features, such as a fine-grained goethite and hematite, is an active research area. The results presented here are an initial offering, but the precise categorization is likely to evolve, and the limits of what can and cannot be separated on a global scale are still being explored. The user is encouraged to read the Algorithm Theoretical Basis Document ([ATBD](https://lpdaac.usgs.gov/documents/1659/EMITL2B_ATBD_v1.pdf)) for more details.  
- "no_match" was added to the mineral library constituents for cases where no match was found via the tetracorder system (this has a value of 0 in the original data, but there is not an entry with an index of 0 in the "mineral_metadata" group).
- Elevation data is always included in requests. For API users there is an additional 'elev' layer listed, but that layer cannot be requested. This has to be present due to some constraints of AppEEARS' backend.

## 6. Documentation  

Documentation for data products available through AppEEARS are listed below.  

### 6.1. MODIS Land Products(Terra, Aqua, & Combined)  

- <https://lpdaac.usgs.gov/product_search/?collections=Combined+MODIS&collections=Terra+MODIS&collections=Aqua+MODIS&view=list>  

### 6.2. MODIS Snow Products (Terra and Aqua)  

- <https://nsidc.org/data/modis/data_summaries>  

### 6.3. NASA MEaSUREs SRTM v3  

- <https://doi.org/10.5067/MEASURES/SRTM/SRTMGL1.003>  
- <https://doi.org/10.5067/MEASURES/SRTM/SRTMGL1N.003>  
- <https://doi.org/10.5067/MEaSUREs/SRTM/SRTMGL3.003>  
- <https://doi.org/10.5067/MEASURES/SRTM/SRTMGL3N.003>  

### 6.4. NASA VIIRS Land Products  

- <https://www.earthdata.nasa.gov/data/catalog?keyword=VIIRS%20LP%20DAAC>  

### 6.5. SMAP Products  

- <http://nsidc.org/data/smap/smap-data.html>  

### 6.6. Daymet v4R1

- <https://doi.org/10.3334/ORNLDAAC/2129>
- <https://daymet.ornl.gov/>

### 6.7. ECOSTRESS  

- <https://www.earthdata.nasa.gov/data/catalog?keyword=ECOSTRESS&page_num=4>  

### 6.8. ASTER GDEM v3 and Global Water Bodies Database v1  

- <https://doi.org/10.5067/ASTER/ASTGTM.003>  
- <https://doi.org/10.5067/ASTER/ASTWBD.001>  

### 6.9. NASADEM  

- <https://doi.org/10.5067/MEaSUREs/NASADEM/NASADEM_NC.001>  
- <https://doi.org/10.5067/MEaSUREs/NASADEM/NASADEM_NUMNC.001> 

### 6.10. HLS v2.0  
 
- <https://doi.org/10.5067/HLS/HLSL30.002>  
- <https://doi.org/10.5067/HLS/HLSS30.002>  

### 6.11. Landsat ARD

- <https://doi.org/10.5066/P960F8OC>

### 6.12. EMIT L1B Radiance and L2A Reflectance

- <https://doi.org/10.5067/EMIT/EMITL1BRAD.001>
- <https://doi.org/10.5067/EMIT/EMITL2ARFL.001>

### 6.13. EMIT L2B Estimated Mineral Identification, Band Depth and Uncertainty

- <https://doi.org/10.5067/EMIT/EMITL2BMIN.001>

### 6.14.  NASA VIIRS Snow Products (Includes Suomi NPP & NOAA-20)

- <https://doi.org/10.5067/45VDCKJBXWEE>

## 7. Sample Request Retention  

AppEEARS sample request outputs are available to download for a limited amount of time after completion. Please visit <https://appeears.earthdatacloud.nasa.gov/help?section=sample-retention> for details.  

## 8. Data Product Citations  

- Myneni, R., Knyazikhin, Y., & Park, T. (2021). MODIS/Terra Leaf Area Index/FPAR 8-Day L4 Global 500m SIN Grid V061. NASA Land Processes Distributed Active Archive Center. https://doi.org/10.5067/MODIS/MOD15A2H.061

Kern, S. (2024). MODIS Collection 6.1 global 8-daily LAI and FAPAR (Version 2024_fv0.01). Universität Hamburg. https://doi.org/10.25592/UHHFDM.14185

Kern, S. (2025). MODIS Collection 6.1 global 8-daily LAI and FAPAR (Version 2025_fv0.01). Universität Hamburg. https://doi.org/10.25592/UHHFDM.8584

Kern, S. (2022). MODIS Collection 6.1 global 8-daily LAI and FAPAR (Version 2022_fv0.03). Universität Hamburg. https://doi.org/10.25592/UHHFDM.10863

Kern, S. (2025). MODIS Collection 6.1 global 8-daily LAI and FAPAR (Version 2025_fv0.01). Universität Hamburg. https://doi.org/10.25592/UHHFDM.16752

Kern, S. (2023). MODIS Collection 6.1 Sinusoidal Tiles 8-daily LAI and FAPAR (Version 2023_fv0.01). Universität Hamburg. https://doi.org/10.25592/UHHFDM.11776

Kern, S. (2025). MODIS Collection 6.1 Sinusoidal Tiles 8-daily LAI and FAPAR (Version 2025_fv0.01). Universität Hamburg. https://doi.org/10.25592/UHHFDM.10866

Kern, S. (2022). MODIS Collection 6.1 Sinusoidal Tiles 8-daily LAI and FAPAR (Version 2022_fv0.01). Universität Hamburg. https://doi.org/10.25592/UHHFDM.10867

Kern, S. (2024). MODIS Collection 6.1 Sinusoidal Tiles 8-daily LAI and FAPAR (Version 2024_fv0.01). Universität Hamburg. https://doi.org/10.25592/UHHFDM.14184

Kern, S. (2025). MODIS Collection 6.1 Sinusoidal Tiles 8-daily LAI and FAPAR (Version 2025_fv0.01). Universität Hamburg. https://doi.org/10.25592/UHHFDM.16751

Kern, S. (2023). MODIS Collection 6.1 global 8-daily LAI and FAPAR (Version 2023_fv0.01). Universität Hamburg. https://doi.org/10.25592/UHHFDM.11777. Accessed January 19, 2026.

## 9. Software Citation  

AppEEARS Team. (2026). Application for Extracting and Exploring Analysis Ready Samples (AppEEARS). Ver. 3.107. NASA EOSDIS Land Processes Distributed Active Archive Center (LP DAAC), USGS/Earth Resources Observation and Science (EROS) Center, Sioux Falls, South Dakota, USA. Accessed January 19, 2026. https://appeears.earthdatacloud.nasa.gov

## 10. Feedback  

We value your opinion. Please help us identify what works, what doesn't, and anything we can do to make AppEEARS better by submitting your feedback at https://appeears.earthdatacloud.nasa.gov/feedback or to LP DAAC User Services at <https://lpdaac.usgs.gov/lpdaac-contact-us/>
