from utils import fluxnet_tools
from utils import paths


fluxnet_tools.extract_zipped_timestep_files(
    dir_fluxnet_raw = paths.FLUXNET_RAW_DIR,
    path_selected_sites = paths.CHOSEN_SITES_FILENAME,
    freq = "HH", 
    out_dir = paths.FLUXNET_HH_DIR,
    verbose = True, 
    )