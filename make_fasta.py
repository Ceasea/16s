#!/usr/bin/env python

import os

def merger():
    for i in os.listdir("2merger"):
        if "extend" in i:
            re = i.split(".")[0]
            os.system(f"fastq_to_fasta -Q33 -i 2merger/{i} -o 3fasta/{re}.fasta")

def direct_merger():
    result = '6direc_fasta'
    if not os.path.exists(result):
        os.mkdir(result)
    for i in os.listdir("5direct_merge"):
        if "extend" in i:
            re = i.split(".")[0]
            os.system(f"fastq_to_fasta -Q33 -i 5direct_merge/{i} -o {result}/{re}.fasta")

direct_merger()