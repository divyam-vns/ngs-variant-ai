#!/usr/bin/env python3
import sys
import csv
from pathlib import Path
import pysam

input_vcf = Path("data/processed/sample.vcf")
output_csv = Path("reports/variant_summary.csv")

def summarize_vcf(vcf_path, csv_path):
    if not vcf_path.exists():
        print(f"VCF not found: {vcf_path}. Place a sample.vcf in data/processed/ to test.")
        return

    vcf_in = pysam.VariantFile(str(vcf_path))
    with open(csv_path, "w", newline='') as fh:
        writer = csv.writer(fh)
        writer.writerow(["CHROM","POS","ID","REF","ALT","QUAL","FILTER","DP","INFO"])
        for rec in vcf_in:
            dp = rec.info.get("DP", "")
            alt = ",".join(str(a) for a in rec.alts) if rec.alts else ""
            info_str = ";".join([f"{k}={rec.info[k]}" for k in rec.info.keys()])
            writer.writerow([rec.chrom, rec.pos, rec.id, rec.ref, alt, rec.qual, ";".join(rec.filter.keys()) if rec.filter else "PASS", dp, info_str])
    print(f"Wrote summary to {csv_path}")

if __name__ == "__main__":
    summarize_vcf(input_vcf, output_csv)
