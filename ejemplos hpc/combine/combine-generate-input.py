#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

num_trx      = 150000
max_trx_len  = 50
mean_trx_len = 3
p_trx_len    = 1/float(mean_trx_len)

# generate transactions lenghts
trx_lens = []
while len(trx_lens)<num_trx:
    trx_len = np.random.geometric(p=p_trx_len)
    if trx_len <= max_trx_len:
        trx_lens.append(trx_len)
        
print("Total number of transactons : %d " % len(trx_lens))
print("Total number of items       : %d " % sum(trx_lens))

plt.hist(trx_lens, bins=range(1,max_trx_len), density=True)
plt.show()

trx_h = np.histogram(trx_lens, bins=range(1,max(trx_lens)))
total_trxs = sum(trx_h[0])
trx_probs = [ x/float(total_trxs) for x in trx_h[0]]

print(trx_probs)

# generate items occurence in transactions

num_skus          = 28000
p_sku_occur       = num_trx/float(sum(trx_lens))
sku_ids           = range(1,num_skus+1)

print("Probability of occurrence for a SKU in a transaction : %f " % p_sku_occur)

# generate transactions lenghts
sku_counts = np.random.geometric(p=p_sku_occur,size=num_skus)

total_skus = sum(sku_counts)
sku_probs = [ x/float(total_skus) for x in sku_counts ]

print("Average number of transactions for a SKU" % np.mean(sku_counts))
plt.hist(sku_counts, bins=range(1,num_skus), density=True)
plt.show()

# generate transactions 
import csv
from timeit import default_timer as timer

output_file = 'trx-sampled-28k.csv'

start = timer()
trx_sampled_id = 0

emp_trx_lens = trx_h[1]

with open(output_file, 'w',) as f_out:
    sampled_trx_lens = []
    writer = csv.writer(f_out, delimiter=',')
    for i in range(num_trx):
        trx_sampled_id+=1
        trx_len = np.random.choice(emp_trx_lens[:-1], 1, p=trx_probs)
        sampled_trx_lens.append(trx_len[0])
        sampled_skus = np.random.choice(sku_ids,trx_len[0], p=sku_probs)        
        for item in sampled_skus:
            writer.writerow([trx_sampled_id,item])

end = timer()
print("Time elapsed in generation: %f seconds" % (end-start))

# plot the sampled and the empirical distributions
plt.figure( figsize=(15, 6))
plt.hist([sampled_trx_lens,trx_lens],bins=range(1,max(trx_lens)),density=True)
plt.legend(["sampled","empirical"])
plt.show()

