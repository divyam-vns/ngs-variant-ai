FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    wget curl git build-essential python3 python3-pip bwa samtools bcftools tabix \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir pandas numpy scikit-learn matplotlib seaborn pysam pyvcf

WORKDIR /workspace
CMD ["/bin/bash"]
