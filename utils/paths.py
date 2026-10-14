import os

# General file dirs
USER = 'ericamcc' # Stanford Desktop
#USER = 'ericamccormick' # Laptop

GDRIVE_PATH = '/Users/' + USER + '/Library/CloudStorage/GoogleDrive-ericamcc@stanford.edu/My Drive/'

METADATA_PATH = os.path.join(GDRIVE_PATH, 'DATASETS/FLUXNET15/FLX_AA-Flx_BIF_ALL_20200501/FLX_AA-Flx_BIF_DD_20200501.csv')
FLUXNET_RAW_DIR = '/Users/pavan/Documents/ERICA RESEARCH/testing/dir_fluxnet_raw'

GENERATED_CSVS_FOR_INPUT = 'inputs'
CHOSEN_SITES_FILENAME = '/Users/pavan/Documents/ERICA RESEARCH/testing/wet-extremes-photosynthesis-main/inputs/unzip_chosensites.csv'
FLUXNET_HH_DIR = '/Users/pavan/Documents/ERICA RESEARCH/testing/dir_fluxnet_hh_selected'
FLUXNET_DD_DIR = '/Users/pavan/Documents/ERICA RESEARCH/testing/dir_fluxnet_dd_selected'

#LE ANALYSIS RELATED DIRECTORIES
FLUXNET_HH_DIR_LE = '/Users/pavan/Documents/ERICA RESEARCH/testing/dir_fluxnet_hh_selected_le' #not needed?
PATH_TO_SWC_SITES_LE = '/Users/pavan/Documents/ERICA RESEARCH/testing/wet-extremes-photosynthesis-main/inputs/le_selected_swc_sites_from_hh_processing.txt'

# Names for specific output files 
PATH_TO_SWC_SITES = '/Users/pavan/Documents/ERICA RESEARCH/testing/wet-extremes-photosynthesis-main/inputs/selected_swc_sites_from_hh_processing.txt'

FIG_DIR = 'figs'

DATA_DIR = '/Users/pavan/Documents/ERICA RESEARCH/testing'
