import FWCore.ParameterSet.Config as cms 

process = cms.Process('jetToolbox')


process.load('PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
qgDatabaseVersion = 'v1' # check https://twiki.cern.ch/twiki/bin/viewauth/CMS/QGDataBaseVersion

from CondCore.DBCommon.CondDBSetup_cfi import *
QGPoolDBESSource = cms.ESSource("PoolDBESSource",
      CondDBSetup,
      toGet = cms.VPSet(),
      connect = cms.string('frontier://FrontierProd/CMS_COND_PAT_000'),
)

for type in ['AK4PFchs','AK4PFchs_antib']:
  QGPoolDBESSource.toGet.extend(cms.VPSet(cms.PSet(
    record = cms.string('QGLikelihoodRcd'),
    tag    = cms.string('QGLikelihoodObject_'+qgDatabaseVersion+'_'+type),
    label  = cms.untracked.string('QGL_'+type)
  )))

## This local test conf is updated to match the grid production version
## 13 June 2016 by Juska.



## ----------------- Global Tag ------------------
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
#process.GlobalTag.globaltag = '74X_dataRun2_Prompt_v4'
process.GlobalTag.globaltag = '80X_dataRun2_2016SeptRepro_v7' #80X_mcRun2_asymptotic_2016_miniAODv2

#--------------------- Report and output ---------------------------
# Note: in grid runs this parameter is not used.
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(10000))

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 1


process.TFileService=cms.Service("TFileService",
                                 fileName=cms.string('mylocaltest_Run2017A_10.root'),
                                 #fileName=cms.string(THISROOTFILE),
                                 closeFileFast = cms.untracked.bool(True)
                                 )

## --- suppress long output ---> wantSummary = cms.untracked.bool(False) 

process.options = cms.untracked.PSet(
        allowUnscheduled = cms.untracked.bool(True),
        wantSummary = cms.untracked.bool(False),
)

############## output  edm format ###############
process.out = cms.OutputModule('PoolOutputModule',                                                                                                                  
                               fileName = cms.untracked.string('jettoolbox.root'),                                                                              
                               outputCommands = cms.untracked.vstring([                                                                 
                                                                      'keep *_slimmedJets_*_*',                                                                  
                                                                      'keep *_slimmedJetsAK8_*_*',                                                                  
                                                                       ])                                                                                           
                               )


# Added 'vertexRef().isNonnull() &&' check for 80X data compatibility. Juska
process.chs = cms.EDFilter('CandPtrSelector', src = cms.InputTag('packedPFCandidates'), cut = cms.string(' fromPV'))

from RecoJets.JetProducers.ak4GenJets_cfi import ak4GenJets
process.slimmedGenJetsAK8 = ak4GenJets.clone(src = 'packedGenParticles', rParam = 0.8)





#-------------------------------------------------------
# Gen Particles Pruner
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")


process.prunedGenParticlesDijet = cms.EDProducer('GenParticlePruner',
    src = cms.InputTag("prunedGenParticles"),
    select = cms.vstring(
    "drop  *  ", # by default
    "keep ( status = 3 || (status>=21 && status<=29) )", # keep hard process particles
    )
)



#------------- Recluster Gen Jets to access the constituents -------
#already in toolbox, just add keep statements

process.out.outputCommands.append("keep *_slimmedGenJets_*_*")
process.out.outputCommands.append("keep *_slimmedGenJetsAK8_*_*")

##-------------------- Define the source  ----------------------------



# Note: for grid running it does not matter what's here, as input data is
# handled separately there.

process.source = cms.Source("PoolSource",
    #  fileNames = cms.untracked.vstring("/store/data/Run2016H/SinglePhoton/MINIAOD/PromptReco-v3/000/284/036/00000/726BEBFC-619F-E611-862A-02163E0121A2.root")
    fileNames = cms.untracked.vstring("/store/data/Run2017D/SingleMuon/MINIAOD/PromptReco-v1/000/302/031/00000/2411F4EE-2D8F-E711-B514-02163E0134D6.root"),
    
    inputCommands =  cms.untracked.vstring("keep *","drop  *_isolatedTracks__*")
   # fileNames = cms.untracked.vstring("file:/afs/cern.ch/work/h/hlattaud/private/production_GJet/CMSSW_8_0_26_patch1/src/CMSDIJET/DijetRootTreeMaker/pickevents_oldreco.root")
  #  fileNames = cms.untracked.vstring("file:/afs/cern.ch/work/h/hlattaud/private/CMSSW_9_1_0/src/pickevents.root","file:/afs/cern.ch/work/h/hlattaud/private/CMSSW_9_1_0/src/pickevents_5.root","file:/afs/cern.ch/work/h/hlattaud/private/CMSSW_9_1_0/src/pickevents_6.root","file:/afs/cern.ch/work/h/hlattaud/private/CMSSW_9_1_0/src/pickevents_7.root","file:/afs/cern.ch/work/h/hlattaud/private/CMSSW_9_1_0/src/pickevents_8.root","file:/afs/cern.ch/work/h/hlattaud/private/CMSSW_9_1_0/src/pickevents_9.root","file:/afs/cern.ch/work/h/hlattaud/private/CMSSW_9_1_0/src/pickevents_10.root","file:/afs/cern.ch/work/h/hlattaud/private/CMSSW_9_1_0/src/pickevents_11.root","file:/afs/cern.ch/work/h/hlattaud/private/CMSSW_9_1_0/src/pickevents_12.root","file:/afs/cern.ch/work/h/hlattaud/private/CMSSW_9_1_0/src/pickevents_13.root","file:/afs/cern.ch/work/h/hlattaud/private/CMSSW_9_1_0/src/pickevents_14.root")
    
)

#process.source.eventsToProcess = cms.untracked.VEventRange("283884:599938894","283884:598913540","283884:608713271","283283:1732672268","283885:781824145")

#---keep un reg photon slimmed and before gx fix -------------

#process.slimmedPhotons_noreg = slimmedPhotonsclone()
#process.slimmedPhotonsBeforeGSFix_noreg = slimmedPhotonsBeforeGSFix.clone()
#------------------------------------------------------------
process.load("RecoEgamma/PhotonIdentification/PhotonIDValueMapProducer_cfi")
from PhysicsTools.SelectorUtils.tools.vid_id_tools import *

dataFormat = DataFormat.MiniAOD
switchOnVIDPhotonIdProducer(process, dataFormat)
my_id_modules = ['RecoEgamma.PhotonIdentification.Identification.cutBasedPhotonID_Spring16_V2p2_cff']
for idmod in my_id_modules:
         setupAllVIDIdsInModule(process,idmod,setupVIDPhotonSelection) 


process.load("RecoEgamma/PhotonIdentification/PhotonIDValueMapProducer_cfi")
#from EgammaAnalysis.ElectronTools.regressionWeights_cfi import regressionWeights
#process = regressionWeights(process)

#from EgammaAnalysis.ElectronTools.calibrationTablesRun2 import files

#process.load('EgammaAnalysis.ElectronTools.regressionApplication_cff')
#process.load('EgammaAnalysis.ElectronTools.calibratedPatPhotonsRun2_cfi')
#process.load('EgammaAnalysis.ElectronTools.calibratedPatbeforeGXPhotonsRun2_cfi')


#process.regressionApplication

#process.calibratedPatPhotons
#process.calibratedPatPhotons.isMC = cms.bool(False)# this is 74X
#process.calibratedPatPhotons.correctionFile = cms.string(files["Moriond2017_JEC"])

#process.calibratedPatPhotonsbeforeGS.correctionFile = cms.string(files["Moriond2017_JEC"])
#process.calibratedPatPhotonsbeforeGS.isMC = cms.bool(False)

#process.calibratedPatPhotons80X.isMC = cms.bool(False)


#process.calibratedPatbeforegxPhotons 
#process.calibratedPatbeforegxPhotons.isMC = cms.bool(False)


#process.EGMRegression = cms.Path(process.regressionApplication)

#process.EGMSmearerPhotons   = cms.Path(process.calibratedPatPhotons)



process.selectedPhotons = cms.EDFilter('PATPhotonSelector',
    src = cms.InputTag('slimmedPhotons'), # cms.InputTag('slimmedphoton74X'),# this is 74X regression 
    cut = cms.string('pt>5 && abs(eta)')
)
srcViD = "selectedPhotons"#"slimmedPhotons"
process.egmPhotonIDs.physicsObjectSrc = cms.InputTag(srcViD)
process.egmPhotonIsolation.srcToIsolate = cms.InputTag(srcViD)
process.photonIDValueMapProducer.srcMiniAOD = cms.InputTag(srcViD)
process.photonRegressionValueMapProducer.srcMiniAOD = cms.InputTag(srcViD)
process.photonMVAValueMapProducer.srcMiniAOD = cms.InputTag(srcViD)


##-------------------- User analyzer  --------------------------------


##-------------------- MET --------------------------------



#---------------NewMet ReminiAOD recipe ---------------------










##-------------Add quarkGluon tagging---------------------------



process.load('RecoJets.JetProducers.QGTagger_cfi')
process.QGTagger.srcJets          = cms.InputTag("slimmedJets")       # Could be reco::PFJetCollection or pat::JetCollection (both AOD and miniAOD)
process.QGTagger.jetsLabel        = cms.string('QGL_AK4PFchs')        # Other options: see https://twiki.cern.ch/twiki/bin/viewauth/CMS/QGDataBaseVersion









# Residue from AOD and RECO running
calo_collection=''
cluster_collection=''
pfcalo_collection=''
   

process.dijets     = cms.EDAnalyzer('DijetTreeProducer',

  # There's no avoiding this in Consumes era
  isData          = cms.bool(True),
  isreMiniAOD     = cms.bool(False),
  ## JETS/MET ########################################
  jetsAK4             = cms.InputTag('slimmedJets'), 
  jetsAK8             = cms.InputTag('slimmedJetsAK8'),
  jetsPUPPI           = cms.InputTag("slimmedJetsPuppi"),     
  rho              = cms.InputTag('fixedGridRhoFastjetAll'),
  met              = cms.InputTag('slimmedMETs'),
  metforggen       = cms.InputTag('slimmedMETs'),
  metEGcleaned     = cms.InputTag('slimmedMETs'),   
  metpuppi              = cms.InputTag('slimmedMETsPuppi'),
  PFCands = cms.InputTag('packedPFCandidates'),
  
 # QGT              = cms.InputTag('QGTagger'),
  vtx              = cms.InputTag('offlineSlimmedPrimaryVertices'),
  ptMinAK4         = cms.double(10),
  ptMinAK8         = cms.double(10),
  
  ## PHOTONS ########################################
  ptMinPhoton               = cms.double(10),
  Photon                    = cms.InputTag('selectedPhotons'),
  Photonsmeared             = cms.InputTag('selectedPhotons'),
  GenPhoton                 = cms.InputTag('slimmedGenPhotons'),
  full5x5SigmaIEtaIEtaMap   = cms.InputTag('photonIDValueMapProducer:phoFull5x5SigmaIEtaIEta'),
  phoChargedIsolation       = cms.InputTag('photonIDValueMapProducer:phoChargedIsolation'),
  phoNeutralHadronIsolation = cms.InputTag('photonIDValueMapProducer:phoNeutralHadronIsolation'),
  phoPhotonIsolation        = cms.InputTag('photonIDValueMapProducer:phoPhotonIsolation'),
  PhotonUncorr              = cms.InputTag('selectedPhotons'),
  eb               = cms.InputTag('reducedEgamma:reducedEBRecHits'),
  ee               = cms.InputTag('reducedEgamma:reducedEERecHits'),
  
  ## MC ########################################
  pu                        = cms.untracked.InputTag('slimmedAddPileupInfo'), # Updated from untracked to 80X by Juska
  ptHat                     = cms.untracked.InputTag('generator'), # Why do these need to be 'untracked' anyway?
  genParticles              = cms.InputTag('prunedGenParticlesDijet'),
  genJetsAK4                = cms.InputTag('slimmedGenJets'), 
  genJetsAK8                = cms.InputTag('slimmedGenJetsAK8'),  
 
 
   ## electrons ######################################## 

  Electrons                 = cms.InputTag('slimmedElectrons'),
  Electronssmeared          = cms.InputTag('slimmedElectrons'),
  ## muons ########################################

  Muons                     = cms.InputTag('slimmedMuons'),
  
  ## trigger ###################################
 
  ##### For single Photon ##### 
  triggerAlias     = cms.vstring('HLTPhoton30','HLTPhoton50','HLTPhoton75','HLTPhoton90','HLTPhoton120','HLTPhoton165','HLTPhoton200'),      #'HLTPhoton30',                          
  triggerSelection = cms.vstring(

     
     ###for SinglePhotons
     'HLT_Photon33_v*',
     'HLT_Photon50_R9Id90_HE10_IsoM_v*',
     'HLT_Photon75_R9Id90_HE10_IsoM_v*',
     'HLT_Photon90_R9Id90_HE10_IsoM_v*',
     'HLT_Photon120_R9Id90_HE10_IsoM_v*',
     'HLT_Photon165_R9Id90_HE10_IsoM_v*',
     'HLT_Photon200_v*'
     
  ),
  
  prescalesTag          = cms.InputTag("patTrigger"),
  triggerResultsTag = cms.InputTag("TriggerResults", "", "HLT"),
  triggerConfiguration = cms.PSet(
    hltResults            = cms.InputTag('TriggerResults','','HLT'),
    
    l1tResults            = cms.InputTag(''),
    daqPartitions         = cms.uint32(1),
    l1tIgnoreMask         = cms.bool(False),
    l1techIgnorePrescales = cms.bool(False),
    l1tIgnoreMaskAndPrescale = cms.bool(False),
    throw                 = cms.bool(False)
  ),
  triggerObjects = cms.InputTag('slimmedPatTrigger'),
  filters = cms.vstring(
        'hltEG33L1EG26HEFilter','hltEG50R9Id90HE10IsoMTrackIsoFilter', 'hltEG75R9Id90HE10IsoMTrackIsoFilter','hltEG90R9Id90HE10IsoMTrackIsoFilter','hltEG120R9Id90HE10IsoMTrackIsoFilter','hltEG165R9Id90HE10IsoMTrackIsoFilter','hltEG200HEFilter'),#

  ## JECs ################
  redoJECs  = cms.bool(True),

  
  L1corrAK4_DATA = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Summer16_23Sep2016HV4_DATA/Summer16_23Sep2016HV4_DATA_L1FastJet_AK4PFchs.txt'),
  L2corrAK4_DATA = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Summer16_23Sep2016HV4_DATA/Summer16_23Sep2016HV4_DATA_L2Relative_AK4PFchs.txt'),
  L3corrAK4_DATA = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Summer16_23Sep2016HV4_DATA/Summer16_23Sep2016HV4_DATA_L3Absolute_AK4PFchs.txt'),
  ResCorrAK4_DATA = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Summer16_23Sep2016HV4_DATA/Summer16_23Sep2016HV4_DATA_L2L3Residual_AK4PFchs.txt'),
  L1corrAK4PUPPI_DATA = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Summer16_23Sep2016HV4_DATA/Summer16_23Sep2016HV4_DATA_L1FastJet_AK4PFPuppi.txt'),
  L2corrAK4PUPPI_DATA = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Summer16_23Sep2016HV4_DATA/Summer16_23Sep2016HV4_DATA_L2Relative_AK4PFPuppi.txt'),
  L3corrAK4PUPPI_DATA = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Summer16_23Sep2016HV4_DATA/Summer16_23Sep2016HV4_DATA_L3Absolute_AK4PFPuppi.txt'),
  ResCorrAK4PUPPI_DATA = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Summer16_23Sep2016HV4_DATA/Summer16_23Sep2016HV4_DATA_L2L3Residual_AK4PFPuppi.txt'),
  L1corrAK8_DATA = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Summer16_23Sep2016HV4_DATA/Summer16_23Sep2016HV4_DATA_L1FastJet_AK8PFchs.txt'),
  L2corrAK8_DATA = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Summer16_23Sep2016HV4_DATA/Summer16_23Sep2016HV4_DATA_L2Relative_AK8PFchs.txt'),
  L3corrAK8_DATA = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Summer16_23Sep2016HV4_DATA/Summer16_23Sep2016HV4_DATA_L3Absolute_AK8PFchs.txt'),
  ResCorrAK8_DATA = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Summer16_23Sep2016HV4_DATA/Summer16_23Sep2016HV4_DATA_L2L3Residual_AK4PFchs.txt'),
  L1corrAK4_MC = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Summer16_23Sep2016V4_MC/Summer16_23Sep2016V4_MC_L1FastJet_AK4PFchs.txt'),
  L2corrAK4_MC = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Summer16_23Sep2016V4_MC/Summer16_23Sep2016V4_MC_L2Relative_AK4PFchs.txt'),
  L3corrAK4_MC = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Summer16_23Sep2016V4_MC/Summer16_23Sep2016V4_MC_L3Absolute_AK4PFchs.txt'),
  L1corrAK4PUPPI_MC = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Summer16_23Sep2016V4_MC/Summer16_23Sep2016V4_MC_L1FastJet_AK4PFPuppi.txt'),
  L2corrAK4PUPPI_MC = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Summer16_23Sep2016V4_MC/Summer16_23Sep2016V4_MC_L2Relative_AK4PFPuppi.txt'),
  L3corrAK4PUPPI_MC = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Summer16_23Sep2016V4_MC/Summer16_23Sep2016V4_MC_L3Absolute_AK4PFPuppi.txt'),
  L1corrAK8_MC = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Summer16_23Sep2016V4_MC/Summer16_23Sep2016V4_MC_L1FastJet_AK8PFchs.txt'),
  L2corrAK8_MC = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Summer16_23Sep2016V4_MC/Summer16_23Sep2016V4_MC_L2Relative_AK8PFchs.txt'),
  L3corrAK8_MC = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Summer16_23Sep2016V4_MC///Summer16_23Sep2016V4_MC_L3Absolute_AK8PFchs.txt'),
  L1RCcorr_DATA = cms.FileInPath('CMSDIJET/DijetRootTreeMaker/data/Summer16_23Sep2016HV4_DATA/Summer16_23Sep2016HV4_DATA_L1RC_AK4PFchs.txt')
)


# ------------------ path --------------------------


process.p = cms.Path()  
process.p +=                      process.chs
process.p +=                      process.selectedPhotons
process.p +=                      process.egmPhotonIDSequence
process.p +=                      process.QGTagger
process.p +=                      process.dijets
