#!/usr/bin/env python3 
#
# combine by key example 
# traditional implementation
#
# 2018 (c) Juan Carlos Maureira
# Center for Mathematical Modeling
# University of Chile

from __future__ import print_function

import os
import csv 
import itertools
from operator import itemgetter

#
# Main routine
#
if __name__ == "__main__":
 
    trxs = []

    #input_file = 'trx-sampled-28k.csv'
    #input_file = 'trx-big.csv'
    input_file = 'trx-really-big.cvs'

    # create the input list of tuples (tr_id, item)
    with open(input_file,'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            trxs.append((row[0],row[1]))

    # sort transactions
    trxs_sorted = sorted(trxs, key=lambda x: int(itemgetter(0)(x)))
    trxs = trxs_sorted

    # combine by key
    items = {}
 
    for tr_id, its in itertools.groupby(trxs, lambda x: x[0]):
        items[tr_id] = [i[1] for i in its]

    # remove keys and items duplicates
    its=[]
    for k,v in items.items():
        its.append((k,list(set(v))))

    # write output
    output_file='tx-joined-serial.csv'
    with open(output_file, 'w',) as f_out:
        writer = csv.writer(f_out, delimiter=',')
        for tx in its:
            writer.writerow([tx[0],tx[1]])
