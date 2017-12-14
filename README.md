# sstmap_test_suite
Test systems for SSTMap


Thank you for helping us test SSTMap.   This short guide will step you through the installation and how to run the test cases.   If you don't have any problems, this should take less than half an hour.   If anything does fail, please post here so we can address it. You can let us know of any issues either via email or by raising an issue at this issue tracker.


## Install Anaconda
Follow the instructions at:
http://sstmap.org/2017/05/02/getting-started/
or
https://www.continuum.io/downloads

## Install SSTMap using conda
Note: If you have a previous inatallation of sstmap, make sure to run 'conda remove sstmap' prior to installation.
```
conda config --add channels omnia
conda config --add channels solvationtools
conda install sstmap
```
## Obtain the test suite
This has a number of short trajectories in different MD packages as well as testing scripts.  It is quite large (500Mb).

https://www.dropbox.com/sh/hrijgk8n5z12bgi/AABSigcBf9PN_7-Z26VCCPePa?dl=0

Download the entire directory as a `zip` file and unzip into a new directory, e.g.,
```
mkdir my_tests
cd my_tests
unzip sstmap_test_suite
```
##  Run testing scripts
Make sure you clean up the test suite so that previously stored test results are removed.
```
make clean
```
### Quick Test
This command will run a quick test calculation and will output if the calculated quantities pass the tests against validated outputs.
```
make test_quick
```
### Test different MD platforms
These will test if the SSTMap installation works smoothly when given inputs from different MD packages.
```
make test_hsa
make test_gist
```
### Test different water models
These will test if the SSTMap installation works smoothly when different water models are used in an MD simulation. In the root test suite folder, do the following:
```
make test_water
```
## Test on your own trajectories

Most importantly, please test this on any trajectories you happen to have.   Instructions for running SSTMap for a popular MD packages (Amber, OpenMM, NAMD, CHARMM, DESMOND, Gromacs) can be found at:

http://sstmap.org/2017/05/03/simple-examples/

Any feedback you have on any aspect of this would be much appreciated.  Thanks for your time.

