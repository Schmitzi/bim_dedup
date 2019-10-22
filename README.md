# Deduplicate rsIDs in BIM Files

Multiallelic SNPs are encoded as multiple SNPs with the same rsID but different alleles in BIM files used by PLINK.
This can lead to problems with downstream analyses because other tools expect these IDs to be unique.
This script identifies duplicated rsIDs and appends a serial number to make them unique.

## Usage
```
bim_dedup.py [-h] [input]

positional arguments:
  input       The BIM file to read in. Defaults to STDIN if '-' or no value is
              passed

optional arguments:
  -h, --help  show help message and exit
```

The output is always written to STDOUT.