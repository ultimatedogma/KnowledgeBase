# GTDB

[Database website](https://gtdb.ecogenomic.org/) | [NatBiotech paper](https://www.nature.com/articles/nbt.4229)

GTDB used a concatenated protein phylogeny as the basis for a bacterial taxonomy that conservatively removes polyphyletic groups and normalizes taxonomic ranks on the basis of relative evolutionary divergence. Under this approach, 58% of the 94,759 genomes comprising the Genome Taxonomy Database had changes to their existing taxonomy. This result includes the description of 99 phyla, including six major monophyletic units from the subdivision of the Proteobacteria, and amalgamation of the Candidate Phyla Radiation into a single phylum. 


## Reference Tree

GTDB has a reference tree that is used to classify the genomes.

[Path to the latest release](https://data.ace.uq.edu.au/public/gtdb/data/releases/latest/)

Files including:

- `ar53.tree`
- `ar53_metadata.tsv.gz`
- `ar53_taxonomy.tsv`
- `bac120.tree`
  - Bacterial reference tree inferred from the concatenation of 120 proteins and spanning the representative genomes for each bacterial species cluster. This tree is used to curate the GTDB taxonomy. The provided tree is in Newick format, decorated with the GTDB taxonomy.
- `bac120_metadata.tsv.gz`
  - Metadata for all bacterial genomes including GTDB and NCBI taxonomies, completeness and contamination estimates, assembly statistics, and genomic properties.
- `bac120_taxonomy.tsv`
  - GTDB taxonomy for all bacterial genomes assigned to a GTDB species cluster.

    


## Method

Refer to this file: [METHOD](https://data.ace.uq.edu.au/public/gtdb/data/releases/latest/METHODS.txt)

