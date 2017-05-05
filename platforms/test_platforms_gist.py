import sys
import os
#sys.path.append("/Users/kamranhaider/Dropbox/SSTMap/sstmap")

from sstmap.grid_water_analysis import GridWaterAnalysis

platforms = ["amber", "charmm", "desmond", "gromacs", "namd", "openmm"]
top_ext = [".prmtop", ".psf", ".pdb", ".gro", ".psf", ".parm7"]
trj_ext = [".nc", ".dcd", ".nc", ".xtc", ".dcd", ".nc"]
supp_ext = [None, "toppar", "params.txt", "params.top", "toppar", None]

for index, platform in enumerate(platforms):
    if platform == "charmm":
        print("Testing: %s" % platform)
        os.chdir(platform)
        top = "testcase" + top_ext[index]
        traj = "md100ps" + trj_ext[index]
        supp = supp_ext[index]
        ligand = "ligand.pdb"
        s = 0
        n = 100

        gist = GridWaterAnalysis(top, traj, start_frame=s, num_frames=n, 
                            ligand_file=ligand, supporting_file=supp,
                            grid_dimensions=[20.0, 20.0, 20.0],
                            prefix="testcase")
        gist.print_system_summary()
        gist.calculate_grid_quantities(num_frames=1000)
        gist.write_data()
        gist.generate_dx_files()
        os.chdir("../")

