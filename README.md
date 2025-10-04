# ngs-variant-ai

NGS variant curation & analysis template.

## Steps to run locally
1. Build Docker image:
   ```bash
   docker build -t ngs-variant-analysis .
   ```
2. Run container with mounted repo:
   ```bash
   docker run -it -v $(pwd):/workspace ngs-variant-analysis
   ```
3. Inside container, run scripts:
   ```bash
   python3 scripts/03_annotation.py
   python3 scripts/05_ml_model.py
   ```
