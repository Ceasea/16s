/mnt/d/huawei/tmp/2auto-ncbi/usearch11.0.667_i86linux32 -makeudb_usearch rdp_16s_v18.fa -output rdp_16s.udb
dir="../fasta/"
for i in $(ls $dir)
do
echo $i
/mnt/d/huawei/tmp/2auto-ncbi/usearch11.0.667_i86linux32  -fastx_uniques $dir/$i -fastaout uni/$i.uniques.fa --sizeout --relabel Uniq
if [ $? -ne 0 ]
then
  echo "$i uni error " >> log
  continue
fi
/mnt/d/huawei/tmp/2auto-ncbi/usearch11.0.667_i86linux32  --cluster_otus uni/$i.uniques.fa -otus otus/$i.otus.fa -relabel Otu
if [ $? -ne 0 ]
then
  echo "$i otus error " >> log
  continue
fi
/mnt/d/huawei/tmp/2auto-ncbi/usearch11.0.667_i86linux32 -otutab $dir/$i  -otus otus/$i.otus.fa -otutabout tabs/$i.otubab.txt
if [ $? -ne 0 ]
then
  echo "$i tab error " >> log
  continue
fi

# taxa
java -Xmx1g -jar /mnt/d/huawei/tmp/2auto-ncbi/rdp_classifier/rdp_classifier-2.0.jar  otus/$i.otus.fa taxa/$i.taxa.txt -f fixrank
if [ $? -ne 0 ]
then
  echo "$i taxa error " >> log
  continue
fi
done



