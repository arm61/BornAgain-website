"""
Cosine ripple on a 2D lattice
"""
import numpy
import bornagain as ba
from bornagain import deg, angstrom, nm


def get_sample():
    """
    Returns a sample with cosine ripples on a substrate.
    The structure is modelled as a 2D Lattice.
    """
    # defining materials
    m_vacuum = ba.HomogeneousMaterial("Vacuum", 0.0, 0.0)
    m_substrate = ba.HomogeneousMaterial("Substrate", 6e-6, 2e-8)
    m_particle = ba.HomogeneousMaterial("Particle", 6e-4, 2e-8)

    # collection of particles
    ff = ba.FormFactorCosineRippleBox(100*nm, 20*nm, 4*nm)
    particle = ba.Particle(m_particle, ff)

    particle_layout = ba.ParticleLayout()
    particle_layout.addParticle(particle, 1.0)

    interference = ba.InterferenceFunction2DLattice(
        ba.BasicLattice2D(200.0*nm, 50.0*nm, 90.0*deg, 0.0*deg))
    pdf = ba.FTDecayFunction2DCauchy(160*nm, 16*nm, 0)
    interference.setDecayFunction(pdf)
    particle_layout.setInterferenceFunction(interference)

    # assemble the sample
    vacuum_layer = ba.Layer(m_vacuum)
    vacuum_layer.addLayout(particle_layout)
    substrate_layer = ba.Layer(m_substrate)
    multi_layer = ba.MultiLayer()
    multi_layer.addLayer(vacuum_layer)
    multi_layer.addLayer(substrate_layer)

    return multi_layer


def get_simulation():
    """
    characterizing the input beam and output detector
    """
    simulation = ba.GISASSimulation()
    simulation.setDetectorParameters(100, -1.5*deg, 1.5*deg, 100, 0.0*deg,
                                     2.5*deg)
    simulation.setBeamParameters(1.6*angstrom, 0.3*deg, 0.0*deg)
    return simulation


def run_simulation():
    """
    Runs simulation and returns intensity map.
    """
    simulation = get_simulation()
    simulation.setSample(get_sample())
    simulation.runSimulation()
    return simulation.result()


if __name__ == '__main__':
    result = run_simulation()
    ba.plot_simulation_result(result, cmap='jet', aspect='auto')
