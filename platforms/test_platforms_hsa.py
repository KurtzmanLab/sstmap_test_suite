import sys
import os
#sys.path.append("/Users/kamranhaider/Dropbox/SSTMap/sstmap")

from sstmap.site_water_analysis import SiteWaterAnalysis

platforms = ["amber", "charmm", "desmond", "gromacs", "namd", "openmm"]
top_ext = [".prmtop", ".psf", ".pdb", ".gro", ".psf", ".parm7"]
trj_ext = [".nc", ".dcd", ".nc", ".xtc", ".dcd", ".nc"]
supp_ext = [None, "toppar", "params.txt", "params.top", "toppar", None]

for index, platform in enumerate(platforms):
    print("Testing: %s" % platform)
    os.chdir(platform)
    top = "testcase" + top_ext[index]
    traj = "md100ps" + trj_ext[index]
    supp = supp_ext[index]
    ligand = "ligand.pdb"
    s = 0
    n = 100
    hsa = SiteWaterAnalysis(top, traj, start_frame=s, num_frames=n, 
                        ligand_file=ligand, supporting_file=supp,
                        prefix="testcase")
    hsa.print_system_summary()
    hsa.initialize_hydration_sites()
    hsa.calculate_site_quantities()
    hsa.write_calculation_summary()
    hsa.write_data()
    os.chdir("../")

