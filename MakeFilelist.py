#!/usr/bin/env python

import sys,glob,os

dir = os.path.abspath(sys.argv[1])

pattern = dir + "/*"
files = glob.glob(pattern)

# ---------- pythia --------#
#FILE = open("filelist_pythia_DR53X_chs_TuneZ2star_pt10_withoutPUReweighting_DoNotUseRebCorrection_v1_mc.txt","w")
#FILE = open("filelist_pythia_DR53X_chs_TuneZ2star_pt10_withoutPUReweighting_UseRebCorrection_v1_mc.txt","w")
#FILE = open("filelist_pythia_DR53X_chs_TuneZ2star_SmearedGenJets_withoutPUReweighting_v1_mc.txt","w")
#FILE = open("filelist_pythia_DR53X_chs_TuneZ2star_pt10_withoutPUReweighting_RebControlPlots_v1_mc.txt","w")
#FILE = open("filelist_pythia_DR53X_chs_TuneZ2star_pt10_withoutPUReweighting_RebControlPlots_NVtx0-10_v1_mc.txt","w")
#FILE = open("filelist_pythia_DR53X_chs_TuneZ2star_pt10_withoutPUReweighting_RebControlPlots_NVtx11-20_v1_mc.txt","w")
#FILE = open("filelist_pythia_DR53X_chs_TuneZ2star_pt10_withoutPUReweighting_RebControlPlots_NVtx21-Inf_v1_mc.txt","w")

# ---------- madgraph --------#
#FILE = open("filelist_madgraph_DR53X_chs_pt10_withoutPUReweighting_HT100-250_RebControlPlots_v1_mc.txt","w")
#FILE = open("filelist_madgraph_DR53X_chs_pt10_withoutPUReweighting_HT250-500_RebControlPlots_v1_mc.txt","w")
#FILE = open("filelist_madgraph_DR53X_chs_pt10_withoutPUReweighting_HT500-1000_RebControlPlots_v1_mc.txt","w")
#FILE = open("filelist_madgraph_DR53X_chs_pt10_withoutPUReweighting_HT1000-Inf_RebControlPlots_v1_mc.txt","w")

#FILE = open("filelist_madgraph_DR53X_chs_pt10_withoutPUReweighting_HT100-250_UseRebCorrection_v1_mc.txt","w")
#FILE = open("filelist_madgraph_DR53X_chs_pt10_withoutPUReweighting_HT250-500_UseRebCorrection_v1_mc.txt","w")
#FILE = open("filelist_madgraph_DR53X_chs_pt10_withoutPUReweighting_HT500-1000_UseRebCorrection_v1_mc.txt","w")
#FILE = open("filelist_madgraph_DR53X_chs_pt10_withoutPUReweighting_HT1000-Inf_UseRebCorrection_v1_mc.txt","w")

#FILE = open("filelist_madgraph_DR53X_chs_pt10_withoutPUReweighting_HT100-250_DoNotUseRebCorrection_v1_mc.txt","w")
#FILE = open("filelist_madgraph_DR53X_chs_pt10_withoutPUReweighting_HT250-500_DoNotUseRebCorrection_v1_mc.txt","w")
#FILE = open("filelist_madgraph_DR53X_chs_pt10_withoutPUReweighting_HT500-1000_DoNotUseRebCorrection_v1_mc.txt","w")
#FILE = open("filelist_madgraph_DR53X_chs_pt10_withoutPUReweighting_HT1000-Inf_DoNotUseRebCorrection_v1_mc.txt","w")

#FILE = open("filelist_madgraph_DR53X_chs_pt10_withPUReweighting_HT100-250_RebControlPlots_v1_mc.txt","w")
#FILE = open("filelist_madgraph_DR53X_chs_pt10_withPUReweighting_HT250-500_RebControlPlots_v1_mc.txt","w")
#FILE = open("filelist_madgraph_DR53X_chs_pt10_withPUReweighting_HT500-1000_RebControlPlots_v1_mc.txt","w")
#FILE = open("filelist_madgraph_DR53X_chs_pt10_withPUReweighting_HT1000-Inf_RebControlPlots_v1_mc.txt","w")

#FILE = open("filelist_madgraph_DR53X_chs_pt10_withPUReweighting_HT100-250_UseRebCorrection_v1_mc.txt","w")
#FILE = open("filelist_madgraph_DR53X_chs_pt10_withPUReweighting_HT250-500_UseRebCorrection_v1_mc.txt","w")
#FILE = open("filelist_madgraph_DR53X_chs_pt10_withPUReweighting_HT500-1000_UseRebCorrection_v1_mc.txt","w")
#FILE = open("filelist_madgraph_DR53X_chs_pt10_withPUReweighting_HT1000-Inf_UseRebCorrection_v1_mc.txt","w")

#FILE = open("filelist_madgraph_DR53X_chs_withoutPUReweighting_HT100-250_SmearedGenJets_v1_mc.txt","w")
#FILE = open("filelist_madgraph_DR53X_chs_withoutPUReweighting_HT250-500_SmearedGenJets_v1_mc.txt","w")
#FILE = open("filelist_madgraph_DR53X_chs_withoutPUReweighting_HT500-1000_SmearedGenJets_v1_mc.txt","w")
#FILE = open("filelist_madgraph_DR53X_chs_withoutPUReweighting_HT1000-Inf_SmearedGenJets_v1_mc.txt","w")

# ---------- data --------#
#FILE = open("filelist_prediction_535_Run2012A-13Jul2012-v1_pt10_withUncertainties_UseRebCorrection_data_v5.txt","w")
#FILE = open("filelist_prediction_535_Run2012A-recover-06Aug2012-v1_pt10_withUncertainties_UseRebCorrection_data_v5.txt","w")
#FILE = open("filelist_prediction_535_Run2012B-13Jul2012-v1_pt10_withUncertainties_UseRebCorrection_data_v5.txt","w")
#FILE = open("filelist_prediction_535_Run2012C-24Aug2012-v1_pt10_withUncertainties_UseRebCorrection_data_v5.txt","w")
#FILE = open("filelist_prediction_535_Run2012C-PromptReco-v2_pt10_withUncertainties_UseRebCorrection_data_v5.txt","w")
FILE = open("filelist_prediction_535_Run2012D-PromptReco-v1_pt10_withUncertainties_UseRebCorrection_data_v5.txt","w")

for file in files:
    FILE.write(file + "\n")

FILE.close()
