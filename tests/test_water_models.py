import sys
import os
import shutil
from sstmap.grid_water_analysis import GridWaterAnalysis
from sstmap.testing.test_gist_output import run_all_gist_tests

water_models = ["tip3p", "tip4p", "tip4pew", "tip5p", "opc"]
curr_dir = os.getcwd()


for water_model in water_models:
    print("Testing: %s" % water_model)
    data_dir = os.path.abspath("../water_models/" + water_model + "/output")
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    else:
        shutil.rmtree(data_dir)           #removes all the subdirectories!
        os.makedirs(data_dir)
    top = os.path.abspath("../water_models/" + water_model + "/" + water_model + ".prmtop")
    traj = os.path.abspath("../water_models/" + water_model + "/md100ps.nc")
    supp = None
    #clusters = os.path.abspath(water_model + "/test_points.pdb")
    ligand = os.path.abspath("../water_models/" + water_model + "/test_points.pdb")
    #clusters = None
    s = 0
    n = 100
    os.chdir(data_dir)
    gist = GridWaterAnalysis(top, traj, start_frame=s, num_frames=n, 
                        ligand_file=ligand, supporting_file=supp,
                        grid_dimensions=[20, 20, 20],
                        prefix="testcase")
    gist.print_system_summary()
    gist.calculate_grid_quantities()
    gist.write_data()
    gist.print_calcs_summary()
    gist.generate_dx_files()
    os.chdir(curr_dir)
