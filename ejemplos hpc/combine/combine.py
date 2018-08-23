#!/usr/bin/env python3
#
# Spark 2.3 combine by key example
#
# 2018 (c) Juan Carlos Maureira
# Center for Mathematical Modeling
# University of Chile

from __future__ import print_function
from pyspark import SparkContext,SparkConf

from pyspark.mllib.fpm import FPGrowth

import os
import csv

#
# Main routine
#
if __name__ == "__main__":

    conf = SparkConf()
    conf.setAppName("Combine example")
    sc = SparkContext(conf=conf)

    # reduce logging
    log4j = sc._jvm.org.apache.log4j
    log4j.LogManager.getRootLogger().setLevel(log4j.Level.ERROR)

    #input_file = './trx-sampled-28k.csv'
    #input_file = 'trx-big.csv'
    input_file = 'trx-really-big.cvs'

    data = sc.textFile(input_file)
    pairs_id_items = data.map(lambda line: line.strip().split(',')).map(lambda x: (x[0].encode('ascii'), x[1].encode('ascii')))
    trxs = pairs_id_items.combineByKey(lambda x: [ x ],
                                       lambda x, y: x + [y],
                                       lambda x, y: x + y )

    # remove duplicates
    items = trxs.map(lambda trx : (trx[0], list(set(trx[1]))))

    # write the output file
    its = items.collect()
    num_trxs = len(its)
    print("Number of Transactions: %d " % num_trxs)
    output_file='tx-joined.csv'
    with open(output_file, 'w',) as f_out:
        writer = csv.writer(f_out, delimiter=',')
        for tx in its:
            writer.writerow([tx[0],tx[1]])

    # run a fpgrowth for the grouped transactions
    #trx_data = sc.textFile(output_file)
    #trx_items = trx_data.map(lambda line: line.strip().split(','))

    #min_support=(1/float(num_trxs))*3
     
    #model = FPGrowth.train(trx_items, minSupport=min_support, numPartitions=4)
    #result = model.freqItemsets().collect()
 
    #for fi in result:
    #    if len(fi.items)>1:
    #        print(fi)

    sc.stop()

    print("done")
