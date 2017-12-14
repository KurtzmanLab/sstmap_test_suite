import sys
import os
import shutil
from sstmap.grid_water_analysis import GridWaterAnalysis
from sstmap.testing.test_gist_output import run_all_gist_tests

platforms = ["amber", "charmm", "desmond", "gromacs", "namd", "openmm"]
top_ext = [".prmtop", ".psf", ".pdb", ".gro", ".psf", ".parm7"]
trj_ext = [".nc", ".dcd", ".nc", ".xtc", ".dcd", ".nc"]
supp_ext = [None, "toppar", "params.txt", "params.top", "toppar", None]
curr_dir = os.getcwd()

for index, platform in enumerate(platforms):
    if platform in ["amber"]:
        print("Testing: %s" % platform)
        data_dir = os.path.abspath("../platforms/" + platform + "/gist_output")
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)
        else:
            shutil.rmtree(data_dir)           #removes all the subdirectories!
            os.makedirs(data_dir)
        top = os.path.abspath("../platforms/" + platform + "/" + "testcase" + top_ext[index])
        traj = os.path.abspath("../platforms/" + platform + "/" + "md100ps" + trj_ext[index])
        supp = None
        if supp_ext[index] is not None:
            supp = os.path.abspath("../platforms/" + platform + "/" + supp_ext[index])
        ligand = os.path.abspath("../platforms/" + platform + "/" + "ligand.pdb")
        s = 0
        n = 100
        os.chdir(data_dir)
        gist = GridWaterAnalysis(top, traj, start_frame=s, num_frames=n, 
                            ligand_file=ligand, supporting_file=supp,
                            grid_dimensions=[48, 48, 48],
                            prefix="testcase")
        gist.print_system_summary()
        gist.calculate_grid_quantities()
        gist.write_data()
        gist.print_calcs_summary()
        gist.generate_dx_files()
        os.chdir(curr_dir)
        run_all_gist_tests(data_dir, "../ref_calcs/")
