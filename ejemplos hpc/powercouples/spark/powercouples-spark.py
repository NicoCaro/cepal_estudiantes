import os
import sys
import argparse
import csv
import itertools

from pyspark import SparkContext,SparkConf

import pew.pew as p

def pow(x):
    return x[0]**x[1]

def pewT(x):
    return p.pew(x[0],x[1])

def find_powerCouple(raw_row):

    row = raw_row.split(",")
    name = str(row[0])
    numbers = [int(i) for i in row[1:] ]
    tuples = itertools.permutations(numbers,2)
    pc =  max(tuples, key=pewT)
    return [name, pc[0], pc[1]]


if __name__ == "__main__":    
    parser = argparse.ArgumentParser(description='PowerCouples Serial native version') 
    parser.add_argument('-i','--input', dest="input_csv", help="input file in csv format", required=True)
    parser.add_argument('-o','--output', dest="output_csv", help="output file in csv format", default=sys.stdout, type=argparse.FileType('w'))

    args = parser.parse_args()

    # set the spark context
    conf = SparkConf()
    #conf.setMaster("local[4]")
    conf.setAppName("PowerCouples")
    sc = SparkContext(conf=conf)

    # compute power couples
    infile = sc.textFile(args.input_csv,40)
    result = infile.map(find_powerCouple).map(lambda elem: elem[0]+","+str(elem[1])+","+str(elem[2])).collect()

    # write results
    out = csv.writer(args.output_csv)
    for row in result:
        out.writerow([row])


