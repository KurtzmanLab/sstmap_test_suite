import sys
import os
#sys.path.append("/Users/kamranhaider/Dropbox/SSTMap/sstmap")

from sstmap.site_water_analysis import SiteWaterAnalysis

water_models = ["tip3p", "tip4p", "tip4pew", "tip5p"]


for water_model in water_models:
    print("Testing: %s" % water_model)
    os.chdir(water_model)
    top = water_model + ".prmtop"
    traj = "md100ps.nc"
    clusters = "test_points.pdb"
    hsa = SiteWaterAnalysis(top, traj, start_frame=0, num_frames=100, 
                        clustercenter_file=clusters, ligand_file=clusters,
                        prefix=water_model)
    hsa.print_system_summary()
    hsa.initialize_hydration_sites()
    hsa.calculate_site_quantities(entropy=False)
    hsa.write_calculation_summary()

    os.chdir("../")

