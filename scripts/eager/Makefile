.PHONY: run_pipeline
run_pipeline:
	nextflow run nf-core/eager -r 2.3.5 \
	-profile eva,archgen \
	--fasta '/projects1/users/borry/04_genomes/Homo_sapiens/NCBI/GRCh38/Sequence/BWAIndex/genome.fa' \
	--bwa_index '/projects1/users/borry/04_genomes/Homo_sapiens/NCBI/GRCh38/Sequence/BWAIndex/' \
	--input '/home/maxime_borry/07_mpi_shh_summerschool/dag-material/Hands on Introduction to Ancient Microbiome Analysis/tutorial/data/subsampled/*_R{1,2}_subsample_1000000.fastq.gz' \
	--complexity_filter_poly_g \
	--hostremoval_input_fastq
