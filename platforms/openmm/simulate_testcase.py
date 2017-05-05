#!/usr/bin/env python
from __future__ import division, print_function

import sys

# OpenMM Imports
import simtk.openmm as mm
import simtk.openmm.app as app

# ParmEd Imports
from parmed import load_file, unit as u
from parmed.openmm import StateDataReporter, NetCDFReporter

# Load the Amber files
print('Loading AMBER files...')
testcase = load_file('testcase.parm7', 'testcase.rst7')

# Create the OpenMM system
print('Creating OpenMM System')
system = testcase.createSystem(nonbondedMethod=app.PME,
                                nonbondedCutoff=8.0*u.angstroms,
                                constraints=app.HBonds,
)

force = mm.CustomExternalForce("k*((x-x0)^2+(y-y0)^2+(z-z0)^2)")
force.addGlobalParameter("k", 5.0*u.kilocalories_per_mole/u.angstroms**2)
force.addPerParticleParameter("x0")
force.addPerParticleParameter("y0")
force.addPerParticleParameter("z0")
for i, atom_crd in enumerate(testcase.positions):
    if testcase.atoms[i].name in ('CA', 'C', 'N'):
        force.addParticle(i, atom_crd.value_in_unit(u.nanometers))
system.addForce(force)

# Create the integrator to do Langevin dynamics
integrator = mm.LangevinIntegrator(
                        300*u.kelvin,       # Temperature of heat bath
                        1.0/u.picoseconds,  # Friction coefficient
                        2.0*u.femtoseconds, # Time step
)

# Define the platform to use; CUDA, OpenCL, CPU, or Reference. Or do not specify
# the platform to use the default (fastest) platform
platform = mm.Platform.getPlatformByName("OpenCL")
#platform = mm.Platform.getPlatform()
#prop = dict(CudaPrecision='mixed') # Use mixed single/double precision

# Create the Simulation object
sim = app.Simulation(testcase.topology, system, integrator, platform)

# Set the particle positions
sim.context.setPositions(testcase.positions)

# Minimize the energy
print('Minimizing energy')
sim.minimizeEnergy(maxIterations=500)

# Set up the reporters to report energies and coordinates every 100 steps
sim.reporters.append(
        StateDataReporter(sys.stdout, 100, step=True, potentialEnergy=True,
                          kineticEnergy=True, temperature=True, volume=True,
                          density=True)
)
sim.reporters.append(NetCDFReporter('testcase.nc', 100, crds=True))

# Run dynamics
print('Running dynamics')
sim.step(10000)
