#!/bin/bash
ini dctools
ini ROOT53000
gridinit
nohup for i in `dcls /pnfs/desy.de/cms/tier2/store/user/csander | grep noPrescaleCut_v19`; do; for j in `dcls /pnfs/desy.de/cms/tier2/store/user/csander/$i`; do; ~/Scripts/dc-cp.sh /pnfs/desy.de/cms/tier2/store/user/csander/$i/$j $i; hadd $i.root $i/*.root; done; done; > noPrescaleCut_v19.txt &
nohup for i in `dcls /pnfs/desy.de/cms/tier2/store/user/csander | grep withPrescaleCut_v19`; do; for j in `dcls /pnfs/desy.de/cms/tier2/store/user/csander/$i`; do; ~/Scripts/dc-cp.sh /pnfs/desy.de/cms/tier2/store/user/csander/$i/$j $i; hadd $i.root $i/*.root; done; done; > withPrescaleCut_v19.txt &
nohup for i in `dcls /pnfs/desy.de/cms/tier2/store/user/csander | grep withPrescaleCut_lowPU_v19`; do; for j in `dcls /pnfs/desy.de/cms/tier2/store/user/csander/$i`; do; ~/Scripts/dc-cp.sh /pnfs/desy.de/cms/tier2/store/user/csander/$i/$j $i; hadd $i.root $i/*.root; done; done; > withPrescaleCut_lowPUv19.txt &
nohup for i in `dcls /pnfs/desy.de/cms/tier2/store/user/csander | grep withPrescaleCut_mediumPU_v19`; do; for j in `dcls /pnfs/desy.de/cms/tier2/store/user/csander/$i`; do; ~/Scripts/dc-cp.sh /pnfs/desy.de/cms/tier2/store/user/csander/$i/$j $i; hadd $i.root $i/*.root; done; done; > withPrescaleCut_mediumPUv19.txt &
nohup for i in `dcls /pnfs/desy.de/cms/tier2/store/user/csander | grep withPrescaleCut_highPU_v19`; do; for j in `dcls /pnfs/desy.de/cms/tier2/store/user/csander/$i`; do; ~/Scripts/dc-cp.sh /pnfs/desy.de/cms/tier2/store/user/csander/$i/$j $i; hadd $i.root $i/*.root; done; done; > withPrescaleCut_highPUv19.txt &
