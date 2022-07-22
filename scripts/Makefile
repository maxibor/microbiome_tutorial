metaphlan:
	metaphlan ../results/fastp/ERR5766177.merged.fastq.gz  \
    --input_type fastq \
    --bowtie2out ../results/metaphlan/ERR5766177.bt2.out  \
    --nproc 8 \
    > ../results/metaphlan/ERR5766177.metaphlan_profile.txt

sourcetracker:
	sourcetracker2 gibbs \
    -i ../results/sourcetracker2/all_species_counts.biom \
    -m ../results/sourcetracker2/labels_st2.tsv \
    -o ../results/sourcetracker2/st2 \
    --source_rarefaction_depth 95327810 \
    --sink_rarefaction_depth 95327810 \
    --jobs 10