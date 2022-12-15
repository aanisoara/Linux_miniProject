#!/bin/shell
# -*- coding: utf-8 -*-
Number=$1

echo "Numero candidature: " ${Number}


source /root/miniconda3/etc/profile.d/conda.sh
conda activate
python /root/projet_linux/Data_preprocess/data_result.py ${Number}
conda deactivate

