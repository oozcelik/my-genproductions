import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(0.026),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    crossSection = cms.untracked.double(30560000.0),
    comEnergy = cms.double(13000.0),
    maxEventsToPrint = cms.untracked.int32(0),
    PythiaParameters = cms.PSet(
         pythia8CommonSettingsBlock,
         pythia8CUEP8M1SettingsBlock,
         processParameters = cms.vstring(
             'Bottomonium:all = on',                      # Quarkonia, MSEL=62, including feed-down as well
             'PhaseSpace:pTHatMin = 2.'                   # be aware of this ckin(3) equivalent
         ),
         parameterSets = cms.vstring(
             'pythia8CommonSettings',
             'pythia8CUEP8M1Settings',
             'processParameters',
         )
    )
)

# match one single particle of a list
oniafilter = cms.EDFilter("MCSingleParticleFilter",
    ParticleID = cms.untracked.vint32(553, 100553, 200553),
    MinPt = cms.untracked.vdouble(6.0, 6.0, 6.0),
    MinEta = cms.untracked.vdouble(-99., -99., -99.),
    MaxEta = cms.untracked.vdouble(99., 99., 99.),
    Status = cms.untracked.vint32(2, 2, 2)
)

# two muons with invariant mass in the J/psi and Psi(2s) mass range
mumugenfilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(1, 1),
    MinPt = cms.untracked.vdouble(0.5, 0.5),
    MinP = cms.untracked.vdouble(0., 0.),
    MaxEta = cms.untracked.vdouble(2.5, 2.5),
    MinEta = cms.untracked.vdouble(-2.5, -2.5),
    MinInvMass = cms.untracked.double(8.0),
    MaxInvMass = cms.untracked.double(11.0),
    ParticleCharge = cms.untracked.int32(-1),
    ParticleID1 = cms.untracked.vint32(13),
    ParticleID2 = cms.untracked.vint32(13)
)

ProductionFilterSequence = cms.Sequence(generator*oniafilter*mumugenfilter)

