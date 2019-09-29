#!/usr/bin/python
import argparse, os, tempfile, shutil, sys,math,pickle,itertools
parent = os.path.dirname(os.getcwd())
sys.path.append(parent)
from subprocess import call, PIPE, STDOUT, Popen
import argparse
import datetime
from ROOT import *

DirList = ["crab_GJet-07Aug17-Run2016B_ver2_v1_NEW_EG_systa_dded_V3","crab_GJet-07Aug17-Run2016C_NEW_EG_systa_dded_V3","crab_GJet-07Aug17-Run2016D_NEW_EG_systa_dded_V3","crab_GJet-07Aug17-Run2016E_NEW_EG_systa_dded_V3","crab_GJet-07Aug17-Run2016Fearly_NEW_EG_systa_dded_V3","crab_GJet-07Aug17-Run2016Flate__NEW_EG_systa_dded_V3","crab_GJet-07Aug17-Run2016G_NEW_EG_systa_dded_V3","crab_GJet-07Aug17-Run2016H_NEW_EG_systa_dded_V3","crab_GJets_HT-100To200_NEW_EG_systa_dded_V3","crab_GJets_HT-100To200_ext_NEW_EG_systa_dded_V3","crab_GJets_HT-200To400_NEW_EG_systa_dded_V3","crab_GJets_HT-200To400_ext_NEW_EG_systa_dded_V3","crab_GJets_HT-400To600_NEW_EG_systa_dded_V3","crab_GJets_HT-400To600_ext_NEW_EG_systa_dded_V3","crab_GJets_HT-40To100_NEW_EG_systa_dded_V3","crab_GJets_HT-40To100_ext_NEW_EG_systa_dded_V3","crab_GJets_HT-600ToInf_NEW_EG_systa_dded_V3","crab_GJets_HT-600ToInf_ext_NEW_EG_systa_dded_V3","crab_G1Jets_Pt-50To100_NEW_EG_systa_dded_V3","crab_G1Jets_Pt-50To100_ext_NEW_EG_systa_dded_V3","crab_G1Jets_Pt-100To250_NEW_EG_systa_dded_V3","crab_G1Jets__Pt-100To250_ext_NEW_EG_systa_dded_V3","crab_G1Jets_Pt-100To250_ext2_NEW_EG_systa_dded_V3","crab_G1Jets__Pt-250To400_NEW_EG_systa_dded_V3","crab_G1Jets__Pt-250To400_ext_NEW_EG_systa_dded_V3","crab_G1Jets__Pt-250To400_ext2_NEW_EG_systa_dded_V3","crab_G1Jets__Pt-400To650_NEW_EG_systa_dded_V3","crab_G1Jets__Pt-400To650_ext_NEW_EG_systa_dded_V3","crab_G1Jets__Pt-650ToInf_NEW_EG_systa_dded_V3","crab_G1Jets__Pt-650ToInf_ext_NEW_EG_systa_dded_V3"]

for iDir in DirList:
        env = "source /cvmfs/cms.cern.ch/crab3/crab.sh && export SCRAM_ARCH=slc6_amd64_gcc530 "
	cmd = "crab resubmit "+iDir
	print(cmd)
	os.system(env + "&&" + cmd)
	
	
	#"crab_GJet-07Aug17-Run2016B_ver2_v1_NEW_EG_systa_dded_V3","crab_GJet-07Aug17-Run2016C_NEW_EG_systa_dded_V3","crab_GJet-07Aug17-Run2016D_NEW_EG_systa_dded_V3","crab_GJet-07Aug17-Run2016E_NEW_EG_systa_dded_V3","crab_GJet-07Aug17-Run2016Fearly_NEW_EG_systa_dded_V3","crab_GJet-07Aug17-Run2016Flate__NEW_EG_systa_dded_V3","crab_GJet-07Aug17-Run2016G_NEW_EG_systa_dded_V3","crab_GJet-07Aug17-Run2016H_NEW_EG_systa_dded_V3",
