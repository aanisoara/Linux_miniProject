#!/bin/shell
# -*- coding: utf-8 -*-
Number=$1

echo "Numero candidature: " ${Number}


source ~/miniconda3/etc/profile.d/conda.sh
conda activate
python ~/Projets_1_Master2/Data_preprocess/data_result.py ${Number}
conda deactivate