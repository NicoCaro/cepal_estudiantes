#!/usr/bin/env python3 
#
# combine by key example 
# pandas implementation
#
# 2018 (c) Juan Carlos Maureira
# Center for Mathematical Modeling
# University of Chile

from __future__ import print_function

import os
import csv 
import pandas as pd

#
# Main routine
#
if __name__ == "__main__":
 
    trxs = []

    #input_file = 'trx-test.csv'
    #input_file = 'trx-sampled-28k.csv'
    #input_file = 'trx-big.csv'
    input_file = 'trx-really-big.cvs'

    trxs = pd.read_csv(input_file, header=None, names=("tr_id","items"))

    items = trxs.groupby("tr_id")
    its = items['items'].apply(list)

    # write output
    output_file='tx-joined-pandas.csv'
    with open(output_file, 'w',) as f_out:
        writer = csv.writer(f_out, delimiter=',')
        for k,v in its.items():
            l = list(map(str,list(set(v))))
            writer.writerow([k,l])
