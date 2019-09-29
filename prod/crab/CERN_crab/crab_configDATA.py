from CRABClient.UserUtilities import config

config = config()

config.General.requestName = 'GJet-Feb03-Run2016B'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/afs/cern.ch/work/h/hlattaud/private/production_GJet/Data_driven_QCD/V3/CMSSW_9_4_10/src/CMSDIJET/DijetRootTreeMaker/prod/Config_RunonMiniaod.py'
config.JobType.pyCfgParams = ['isRunonData=True']

config.Data.inputDataset = '/SinglePhoton/Run2016B-03Feb2017_ver2-v2/MINIAOD'
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/ReReco/Final/Cert_271036-284044_13TeV_23Sep2016ReReco_Collisions16_JSON.txt'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 50
config.Data.publication = False
config.Data.outLFNDirBase = '/store/user/hlattaud/GammaJet/GJetHF/'

config.Site.storageSite = 'T3_FR_IPNL'
