### 16s
 16s sequnce analysis

#### 16s与宏基因区别
16s
 * 数据来源细菌
 * 分析群落的物种组成, 物种间的进化关系以及群落的多样性
 * 采用Mothur分析

宏基因组
 * 数据来源环境中全部微生物的总DNA
 * 在16s的基础上研究基因和功能
 * 采用Metaphlan, kneaddata分析

#### [Mothur标准流程](https://mothur.org/wiki/miseq_sop/)
1. 构建数据
    fastq数据
   ```make.file(inputdir=., type=fastq, prefix=stability)```

   fastq.gz数据
   ```make.file(inputdir=., type=gz, prefix=stability)```
2. 质量(>25)控制
   ```make.contigs(file=stability.files)```
3. 

