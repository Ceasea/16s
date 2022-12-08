#!/usr/bin/env python3
import os

trim = '/mnt/d/huawei/tmp/2auto-ncbi/Trimmomatic-0.39'
result= '1quality_merge'
with open("./fastq/stability.files",'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip().split()
        one, two = line[1],line[2]
        one, two = one[:-9], two[:-9]
        info = f"java -jar {trim}/trimmomatic-0.39.jar PE fastq/{one}.fastq.gz fastq/{two}.fastq.gz {result}/{one}_paired.fastq.gz \
            {result}/{one}_unpaired.fastq.gz {result}/{two}_paired.fastq.gz {result}/{two}_unpaired.fastq.gz \
            ILLUMINACLIP:{trim}/adapters/TruSeq3-PE.fa:2:30:10:2:True SLIDINGWINDOW:50:20"
        #print(info)
        os.system(info)
