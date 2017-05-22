import sys
import os
import shutil
from sstmap.site_water_analysis import SiteWaterAnalysis

water_models = ["tip3p", "tip4p", "tip4pew", "tip5p", "opc"]
curr_dir = os.getcwd()


for water_model in water_models:
    print("Testing: %s" % water_model)
    data_dir = water_model + "/output"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    else:
        shutil.rmtree(data_dir)           #removes all the subdirectories!
        os.makedirs(data_dir)
    top = os.path.abspath(water_model + "/" + water_model + ".prmtop")
    traj = os.path.abspath(water_model + "/md100ps.nc")
    clusters = os.path.abspath(water_model + "/test_points.pdb")
    s = 0
    n = 100
    os.chdir(data_dir)
    hsa = SiteWaterAnalysis(top, traj, start_frame=s, num_frames=n, 
                        clustercenter_file=clusters, ligand_file=clusters,
                        prefix=water_model)
    hsa.print_system_summary()
    hsa.initialize_hydration_sites()
    hsa.calculate_site_quantities(entropy=False)
    hsa.write_calculation_summary()
    os.chdir(curr_dir)
