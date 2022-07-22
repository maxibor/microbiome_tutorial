.PHONY: run_pipeline
run_pipeline:
	nextflow run maxibor/eager -r dev \
	-profile eva,archgen \
	--fasta '/home/maxime_borry/SDAG_old/04_genomes/Homo_sapiens/NCBI/GRCh38/Sequence/BWAIndex/genome.fa' \
	--bwa_index '/home/maxime_borry/SDAG_old/04_genomes/Homo_sapiens/NCBI/GRCh38/Sequence/BWAIndex/' \
	--input '/home/maxime_borry/13_spaam_summerschool/microbiome_tutorial/data/raw/*_{1,2}.fastq.gz' \
	--complexity_filter_poly_g \
	--hostremoval_input_fastq \
	-resume \
	-with-tower
