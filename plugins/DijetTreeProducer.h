#ifndef DijetTreeProducer_h
#define DijetTreeProducer_h

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "HLTrigger/HLTcore/interface/TriggerExpressionData.h"
#include "HLTrigger/HLTcore/interface/TriggerExpressionEvaluator.h"
#include "HLTrigger/HLTcore/interface/TriggerExpressionParser.h"
#include "DataFormats/JetReco/interface/Jet.h"

#include "DataFormats/PatCandidates/interface/Photon.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/JetReco/interface/JetCollection.h"
#include "TTree.h"
#include "TH1F.h"
#include "TParameter.h"

// For JECs
#include "FWCore/ParameterSet/interface/FileInPath.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "CondFormats/JetMETObjects/interface/FactorizedJetCorrector.h"

// For 80X updates (for consumes system)
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "DataFormats/Common/interface/ValueMap.h"
#include "CondFormats/JetMETObjects/interface/FactorizedJetCorrector.h"

#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/Common/interface/TriggerResults.h"
#include "DataFormats/PatCandidates/interface/PackedTriggerPrescales.h"

// EGM smearer package
#include "DataFormats/EcalRecHit/interface/EcalRecHitCollections.h"
#include "DataFormats/DetId/interface/DetId.h"
#include "DataFormats/EcalDetId/interface/EBDetId.h"
#include "DataFormats/EcalDetId/interface/EEDetId.h"

#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"
#include "Geometry/CaloTopology/interface/CaloTopology.h"
#include "FWCore/Framework/interface/ESHandle.h" 
#include "Geometry/CaloEventSetup/interface/CaloTopologyRecord.h"
#include "RecoEcal/EgammaCoreTools/interface/EcalClusterTools.h"

#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
enum JetAlgorithm {
  AK4,
  AK8,
  PUPPI
};

struct JetInfos {
  JetAlgorithm algo;
  edm::EDGetTokenT<pat::JetCollection> inputTag;

};


class DijetTreeProducer : public edm::EDAnalyzer 
{
  public:
    typedef reco::Particle::LorentzVector LorentzVector;
    explicit DijetTreeProducer(edm::ParameterSet const& cfg);
    virtual void beginJob();
    virtual void analyze(edm::Event const& iEvent, edm::EventSetup const& iSetup);
    virtual bool isValidPhotonLoose_Datadrivenpresel(const pat::PhotonRef& photonRef, const edm::Event& event, double generatorWeight);
    virtual bool isValidPhotonLoose(const pat::PhotonRef& photonRef,const edm::Event& event, double generatorWeight);
    virtual bool isValidPhotonMedium(const pat::PhotonRef& photonRef,const edm::Event& event, double generatorWeight);
    virtual bool isValidPhotonTight(const pat::PhotonRef& photonRef,const edm::Event& event, double generatorWeight); 
    virtual bool isValidEndcapPhotonLoose(const pat::PhotonRef& photonRef,const edm::Event& event, double generatorWeight);
    virtual bool isValidEndcapPhotonMedium(const pat::PhotonRef& photonRef,const edm::Event& event, double generatorWeight);
    virtual bool isValidEndcapPhotonTight(const pat::PhotonRef& photonRef,const edm::Event& event, double generatorWeight);
    virtual void endJob();
    virtual ~DijetTreeProducer();
    

  private: 
    
    void initialize();
    // For JECs
    bool redoJECs_;
    edm::FileInPath L1corrAK4_DATA_, L2corrAK4_DATA_, L3corrAK4_DATA_, ResCorrAK4_DATA_,L1corrPUPPI_DATA_, L2corrPUPPI_DATA_, L3corrPUPPI_DATA_, ResCorrPUPPI_DATA_, L1corrAK8_DATA_, L2corrAK8_DATA_, L3corrAK8_DATA_, ResCorrAK8_DATA_,L1RCcorr_DATA_;
    edm::FileInPath L1corrAK4_MC_, L2corrAK4_MC_, L3corrAK4_MC_,L1corrPUPPI_MC_, L2corrPUPPI_MC_, L3corrPUPPI_MC_, L1corrAK8_MC_, L2corrAK8_MC_, L3corrAK8_MC_;
    JetCorrectorParameters *L1ParAK4_DATA;
    JetCorrectorParameters *L2ParAK4_DATA;
    JetCorrectorParameters *L3ParAK4_DATA;
    JetCorrectorParameters *L2L3ResAK4_DATA;
    FactorizedJetCorrector *JetCorrectorAK4_DATA;
    JetCorrectorParameters *L1ParPUPPI_DATA;
    JetCorrectorParameters *L2ParPUPPI_DATA;
    JetCorrectorParameters *L3ParPUPPI_DATA;
    JetCorrectorParameters *L2L3ResPUPPI_DATA;
    FactorizedJetCorrector *JetCorrectorPUPPI_DATA;
    JetCorrectorParameters *L1JetParForTypeI;
    FactorizedJetCorrector *jetCorrectorForTypeI;    
    JetCorrectorParameters *L1ParAK4_MC;
    JetCorrectorParameters *L2ParAK4_MC;
    JetCorrectorParameters *L3ParAK4_MC;
    FactorizedJetCorrector *JetCorrectorAK4_MC;
    JetCorrectorParameters *L1ParPUPPI_MC;
    JetCorrectorParameters *L2ParPUPPI_MC;
    JetCorrectorParameters *L3ParPUPPI_MC;
    FactorizedJetCorrector *JetCorrectorPUPPI_MC;
    JetCorrectorParameters *L1ParAK8_DATA;
    JetCorrectorParameters *L2ParAK8_DATA;
    JetCorrectorParameters *L3ParAK8_DATA;
    JetCorrectorParameters *L2L3ResAK8_DATA;
    FactorizedJetCorrector *JetCorrectorAK8_DATA;
    JetCorrectorParameters *L1ParAK8_MC;
    JetCorrectorParameters *L2ParAK8_MC;
    JetCorrectorParameters *L3ParAK8_MC;
    FactorizedJetCorrector *JetCorrectorAK8_MC;
    //---- configurable parameters --------   
    double ptMinAK4_,ptMinAK8_;
    double ptMinPhoton_;
    bool mVerbose = false;
    bool isData_;
    bool isReminiAOD_;
    bool RunEndcapPhoton_;
    bool goodPVtx_;
    bool isSelected ;
    
    
    // Migrate to consumes-system for running in 80X

    

    edm::EDGetTokenT<pat::PhotonCollection> srcPhoton_;
    edm::EDGetTokenT<pat::PhotonCollection> srcPhotonsmeared_;
    edm::EDGetTokenT<pat::PhotonCollection> srcPhotonsnofix_;
    edm::EDGetTokenT<pat::PhotonCollection> srcPhotonUncorr_;
    edm::EDGetTokenT<pat::ElectronCollection> srcElectron_;
    edm::EDGetTokenT<pat::ElectronCollection> srcElectronsmeared_;
    edm::EDGetTokenT<pat::MuonCollection> srcMuon_;
    edm::EDGetTokenT<pat::PackedCandidateCollection> srcPfCands_;
    edm::EDGetTokenT<LHEEventProduct> lheToken_;
    
    edm::EDGetTokenT<edm::ValueMap<float>> full5x5SigmaIEtaIEtaMapToken_;
    edm::EDGetTokenT<edm::ValueMap<float>> phoChargedIsolationToken_;
    edm::EDGetTokenT<edm::ValueMap<float>> phoNeutralHadronIsolationToken_;
    edm::EDGetTokenT<edm::ValueMap<float>> phoPhotonIsolationToken_;
    edm::EDGetTokenT<edm::ValueMap<float>> phoFull5x5SigmaIEtaIPhiToken_;
    edm::EDGetTokenT<edm::ValueMap<float>> phoFull5x5E5x5Token_;
    edm::EDGetTokenT<edm::ValueMap<float>> phoFull5x5E2x2Token_;
    edm::EDGetTokenT<edm::ValueMap<float>> phoESEffSigmaRRToken_;
    edm::EDGetTokenT<edm::ValueMap<float>> phoFull5x5E2x5Token_;
    edm::EDGetTokenT<edm::ValueMap<float>> phoFull5x5E1x3Token_;
    edm::EDGetTokenT<edm::ValueMap<float>> phoWorstChargedIsolationToken_;
    edm::EDGetTokenT<edm::ValueMap<bool> > phoMediumIdBoolMapToken_;
    
    
    
    
    edm::InputTag barrelRecHitCollection_;
    edm::InputTag endcapRecHitCollection_;
    
    edm::Handle<EcalRecHitCollection> ecalRecHitsEBHandle_;
    edm::Handle<EcalRecHitCollection> ecalRecHitsEEHandle_;
    edm::EDGetTokenT<EcalRecHitCollection> ecalRecHitsEBToken_;
    edm::EDGetTokenT<EcalRecHitCollection> ecalRecHitsEEToken_;
    edm::ESHandle<CaloTopology> caloTopoHandle_;


    
    edm::EDGetTokenT<pat::JetCollection> srcJetsAK4_;
    edm::EDGetTokenT<edm::View<pat::Jet>> srcJetsAK4View_;
    edm::EDGetTokenT<edm::ValueMap<float>> qgToken ;
    edm::EDGetTokenT<pat::JetCollection> srcJetsAK8_;
    edm::EDGetTokenT<pat::JetCollection> srcJetsPUPPI_;
    edm::EDGetTokenT<edm::View<pat::Jet>> srcJetsAK4puppiView_;
    

    edm::EDGetTokenT<double> srcRho_;
    edm::EDGetTokenT<std::vector<pat::MET> > srcMET_      ;
    edm::EDGetTokenT<std::vector<pat::MET> > srcMETforgen_;
    edm::EDGetTokenT<std::vector<pat::MET> > srcMETpuppi_ ;
    edm::EDGetTokenT<std::vector<pat::MET> > srcMETEGcleaned_;

    edm::EDGetTokenT<reco::VertexCollection> srcVrtx_;

    edm::EDGetTokenT<reco::GenJetCollection> srcGenJetsAK4_;
    edm::EDGetTokenT<reco::GenJetCollection> srcGenJetsAK8_;
    edm::EDGetTokenT<pat::PackedGenParticleCollection> srcPrunedGenParticles_;
    
    edm::EDGetTokenT<std::vector<PileupSummaryInfo> > srcPU_;
    edm::EDGetTokenT<GenEventInfoProduct> srcGenInfo_;

    edm::Service<TFileService> fs_;
    TTree *outTree_;
    TTree *outTree_full_event_;
    
    
    
    std::vector<float> *weight_pdf_as_;
    //---- TRIGGER -------------------------
    edm::EDGetTokenT<edm::TriggerResults> srcTriggerResults_;
    edm::EDGetTokenT<pat::PackedTriggerPrescales> srcTriggerPrescale_;
    std::vector<bool>  *triggerResultfromToken_;
    std::vector<int> *triggerPrescale_; 
    std::vector<std::string> *triggerName_;
    
    edm::EDGetTokenT<edm::View<pat::TriggerObjectStandAlone>> triggerObjectsToken;
    std::vector<std::string> filters_name ;
    
    triggerExpression::Data triggerCache_;
    std::vector<triggerExpression::Evaluator*> vtriggerSelector_;
    std::vector<std::string> vtriggerAlias_,vtriggerSelection_;
    TH1F *triggerPassHisto_,*triggerNamesHisto_,*puHisto_;
    //---- output TREE variables ------
    //---- global event variables -----
    int   run_,evt_,nVtx_,lumi_,BXnumber_;
    int   nJetsAK4_,nJetsPUPPI_, nJetsAK8_, nGenJetsAK4_, nGenJetsAK8_;
    int   nPhotons_, nPhotonsLoose_,nPhotonsMedium_,nPhotonsTight_, nGenphotons_;
    int   nMuonsLoose_;
    TParameter<int>*  Nevent_tot;
    
    //-----egcleanned variables-----
    
    bool  isEGfixpropagated_, isEcalMulEGfixempty;
    

    float rho_,metEnergy_,metPt_,metPhi_,metEta_,metEnergypuppi_,metPtpuppi_,metPhipuppi_,metEtapuppi_,metSig_,metcorrected_;
    
    float PFmetX_, PFmetY_, EGmetX_, EGmetY_, CHSmetX_, CHSmetY_, deltaNHfootprintX_,deltaNHfootprintY_;
    
    float metEnergyGen_,metPtGen_,metPhiGen_,metEtaGen_,metEnergypuppiGen_,metPtpuppiGen_,metPhipuppiGen_,metEtapuppiGen_;
    float htAK4_;
    float htAK8_;
    std::vector<bool>  *triggerResult_;
        
    
    //---- photon variables --------------
    std::vector<float> *ptphoton_eff_, *etaphoton_eff_, *etaphoton_GEN_eff_, *ptphoton_GEN_eff_,*phiphoton_GEN_eff_ ;
    std::vector<float> *etajet_GEN_eff_, *ptjet_GEN_eff_,*phijet_GEN_eff_ ;
    double weighteff_;
    std::vector<bool> *isFake_eff_;
    std::vector<float> *ptphoton_,*etaphoton_,*phiphoton_,*energyphoton_,*full5x5SigmaIEtaIEtaMapTokenphoton_,*phoChargedIsolationTokenphoton_,*phoNeutralHadronIsolationTokenphoton_,*phoPhotonIsolationTokenphoton_,*hadTowOverEm_, *phoFull5x5SigmaIEtaIPhiTokenphoton_, *phoFull5x5E5x5Tokenphoton_, *phoFull5x5E2x2Tokenphoton_, *phoESEffSigmaRRTokenphoton_, *R9_, *etawidth_, *phiwidth_, *ES_energy_, *phoFull5x5E2x5Tokenphoton_, *phoFull5x5E1x3Tokenphoton_, *phoWorstChargedIsolationTokenphoton_;
    std::vector<float> *ptsmearedphoton_,*etasmearedphoton_,*phismearedphoton_,*energysmearedphoton_,*full5x5SigmaIEtaIEtaMapTokensmearedphoton_,*phoChargedIsolationTokensmearedphoton_,*phoNeutralHadronIsolationTokensmearedphoton_,*phosmearedphotonIsolationTokensmearedphoton_;
    std::vector<bool>  *isPhotonLoose_,*isPhotonMedium_,*isPhotonTight_,  *HaspixelSeed_ , *electronconvVeto_, *isFakephoton_,*isPhotonMedium_EG_MVA_;
    std::vector<float> *ptphotonSC_,*etaphotonSC_,*phiphotonSC_,*energyphotonSC_;
    std::vector<float> *ptGenphoton_,*etaGenphoton_,*phiGenphoton_,*energyGenphoton_;
    std::vector<double> *Ecorrbump_;
    
    std::vector<bool>  *isMatch30_,*isMatch50_,*isMatch75_,*isMatch90_,*isMatch120_,*isMatch165_, *isGenMatch_;
    
    std::vector<float> *photon_scaleUNC_gainup_,*photon_scaleUNC_gaindown_,*photon_scaleUNC_systup_,*photon_scaleUNC_systdown_,*photon_scaleUNC_statup_,*photon_scaleUNC_statdown_,*photon_scaleUNC_ETup_,*photon_scaleUNC_ETdown_,*photon_smearUNC_phiup_,*photon_smearUNC_rhodown_,*photon_smearUNC_rhoup_,*photon_smear_central_,*photon_scale_central_;
    
   
    
    
    std::vector<float> *elecPt_, *elecEta_, *elecPhi_, *elecEnergy_, *elecID_, *elecISO_;
    std::vector<float> *elecPtsmeared_, *elecEtasmeared_, *elecPhismeared_, *elecEnergysmeared_, *elecIDsmeared_, *elecISOsmeared_;    
    std::vector<float> *muPt_, *muEta_, *muPhi_, *muEnergy_;
    
    //------------variable for met correction--------
    FactorizedJetCorrector *jetCorrector;
  //  FactorizedJetCorrector *jetCorrectorForTypeI;
    
    //---- jet and genJet variables --------------
    std::vector<float> *ptAK4_,*jecAK4_,*etaAK4_,*phiAK4_,*massAK4_,*energyAK4_,*areaAK4_,*csvAK4_,*qgdAK4_, *deepcsv_probb_AK4_, *deepcsv_probbb_AK4_, *deepcsv_probc_AK4_, *deepcsv_probcc_AK4_,*chfAK4_,*nhfAK4_,*phfAK4_,*elfAK4_,*mufAK4_,*nemfAK4_,*cemfAK4_, *CvsL_taggerAK4_, *CvsB_taggerAK4_ ;
    std::vector<float> *ptAK4raw_,*etaAK4raw_,*phiAK4raw_,*massAK4raw_,*energyAK4raw_;
    
    std::vector<int> *idLAK4_,*idTAK4_, *chHadMultAK4_, *chMultAK4_, *neHadMultAK4_, *neMultAK4_, *phoMultAK4_,*pdgIDGenAK4_, *hadronflavour_, *hadron_flavor_jets_;
    std::vector<float> *hf_hfAK4_, *hf_emfAK4_, *hofAK4_;
    std::vector<float> *ptGenAK4_,*etaGenAK4_,*phiGenAK4_,*massGenAK4_,*energyGenAK4_;
    
    std::vector<float> *ptPUPPI_,*jecPUPPI_,*etaPUPPI_,*phiPUPPI_,*massPUPPI_,*energyPUPPI_,*areaPUPPI_,*csvPUPPI_,*qgdPUPPI_,*chfPUPPI_,*nhfPUPPI_,*phfPUPPI_,*elfPUPPI_,*mufPUPPI_,*nemfPUPPI_,*cemfPUPPI_;
    std::vector<float> *ptPUPPIraw_,*etaPUPPIraw_,*phiPUPPIraw_,*massPUPPIraw_,*energyPUPPIraw_;
    
    std::vector<int> *idLPUPPI_,*idTPUPPI_, *chHadMultPUPPI_, *chMultPUPPI_, *neHadMultPUPPI_, *neMultPUPPI_, *phoMultPUPPI_,*pdgIDGenPUPPI_;
    std::vector<float> *hf_hfPUPPI_, *hf_emfPUPPI_, *hofPUPPI_;
    std::vector<float> *ptGenPUPPI_,*etaGenPUPPI_,*phiGenPUPPI_,*massGenPUPPI_,*energyGenPUPPI_;
    
    std::vector<float>*ptAK8_,*jecAK8_,*etaAK8_,*phiAK8_,*massAK8_,*energyAK8_,*areaAK8_,*csvAK8_,*qgdAK8_,*chfAK8_,*nhfAK8_,*phfAK8_,*elfAK8_,*mufAK8_,*nemfAK8_,*cemfAK8_, *massPrunedAK8_, *massSoftDropAK8_, *dR_AK8_,*tau1AK8_,*tau2AK8_, *tau3AK8_ ;
    std::vector<int> *idLAK8_,*idTAK8_, *chHadMultAK8_, *chMultAK8_, *neHadMultAK8_, *neMultAK8_, *phoMultAK8_;
    std::vector<float> *hf_hfAK8_, *hf_emfAK8_, *hofAK8_;
    std::vector<float> *ptGenAK8_,*etaGenAK8_,*phiGenAK8_,*massGenAK8_,*energyGenAK8_;

    //---- MC variables ---------------
    std::vector<float> *npu_; 
    std::vector<int> *Number_interactions;
    std::vector <int> *OriginBX;
   
    //-----gen particles from hard scattering ------
  
    float ptHat_; 
    int processID_;
    float weight_;
    std::vector<float> *gen_eta, *gen_phi, *gen_p, *gen_px, *gen_py, *gen_pz, *gen_pt, *gen_energy,  *gen_vx, *gen_vy, *gen_vz;
    std::vector<int> *gen_numDaught, *gen_status, *gen_index, *gen_motherIndex, *gen_pdgId;  

};

#endif
