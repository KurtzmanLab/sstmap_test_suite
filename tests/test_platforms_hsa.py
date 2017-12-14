import sys
import os
import shutil

from sstmap.site_water_analysis import SiteWaterAnalysis
platforms = ["amber", "charmm", "desmond", "gromacs", "namd", "openmm"]
top_ext = [".prmtop", ".psf", ".pdb", ".gro", ".psf", ".parm7"]
trj_ext = [".nc", ".dcd", ".nc", ".xtc", ".dcd", ".nc"]
supp_ext = [None, "toppar", "params.txt", "params.top", "toppar", None]
curr_dir = os.getcwd()

for index, platform in enumerate(platforms):
    print("Testing: %s" % platform)
    data_dir = os.path.abspath("../platforms/" + platform + "/hsa_output")
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
    hsa = SiteWaterAnalysis(top, traj, start_frame=s, num_frames=n,
                        ligand_file=ligand, supporting_file=supp,
                        prefix="testcase")
    hsa.print_system_summary()
    hsa.initialize_hydration_sites()
    hsa.calculate_site_quantities()
    hsa.write_calculation_summary()
    hsa.write_data()
    os.chdir(curr_dir)
