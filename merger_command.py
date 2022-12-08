#!/usr/bin/env python3
#!/usr/bin/env python3
import os

"""
flash = '/mnt/d/huawei/tmp/2auto-ncbi/FLASH-1.2.11-Linux-x86_64'
result= '2merger'
with open("./fastq/stability.files",'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip().split()
        one, two = line[1],line[2]
        one, two = one[:-9], two[:-9]
        info = f'{flash}/flash 1quality_merge/{one}_paired.fastq.gz 1quality_merge/{two}_paired.fastq.gz  -o {one} -d {result}'
        os.system(info)
"""

def direct_merger():
    # 不质控直接使用fastq
    flash = '/mnt/d/huawei/tmp/2auto-ncbi/FLASH-1.2.11-Linux-x86_64'
    result= '5direct_merge'
    if not os.path.exists(result):
        os.mkdir(result)
    with open("./fastq/stability.files",'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split()
            one, two = line[1],line[2]
            one, two = one[:-9], two[:-9]
            info = f'{flash}/flash fastq/{one}.fastq.gz fastq/{two}.fastq.gz  -o {one} -d {result}'
            os.system(info)
direct_merger()