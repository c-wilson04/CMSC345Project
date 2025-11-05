# CMSC 435 Group Project - Protein Interaction Prediction

## Team Information

- **Team Name:** Column Crushers
- **Members:**
  - Connor Fair
  - Charles Wilson

## Project Overview

This project involves developing and evaluating models for predicting proteins that interact with DNA and RNA. The classification task involves four outcomes:

- **DNA**: Interacts with DNA
- **RNA**: Interacts with RNA
- **DRNA**: Interacts with both DNA and RNA
- **nonDRNA**: Does not interact with DNA or RNA

## Dataset

- **Training Dataset:** `sequences_training.txt` (8,795 proteins)
  - 391 DNA proteins
  - 523 RNA proteins
  - 22 DRNA proteins
  - 7,859 nonDRNA proteins
- **Test Dataset:** `sequences_test.txt` (8,794 proteins) - will be provided later

## Development Setup

### Environment and Package Management

This project uses **uv** as the environment and package manager.

**Python Version:** Python 3.12.8

### Setup Instructions

1. Install uv (if not already installed):

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Create a virtual environment with Python 3.12.8 and install dependencies:

   ```bash
   uv venv --python 3.12.8
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate  # On Windows
   ```

3. Install project dependencies:

   ```bash
   uv pip install -r requirements.txt
   ```

4. Install Quarto (required for PDF report generation):
   - Download from: https://quarto.org/docs/get-started/
   - Or via Homebrew: `brew install --cask quarto`
   - Verify installation: `quarto --version`

## Project Structure

```
.
├── README.md
├── sequences_training.txt    # Training dataset (original sequences)
├── training_dataset.csv       # Training dataset with features (tracked via Git LFS)
├── protein_classifier.ipynb   # Jupyter notebook with classifier implementation
└── progress_report.qmd        # Quarto document for progress report
```

### Downloading the Training Dataset

The `training_dataset.csv` file is tracked using **Git LFS** (Large File Storage). To download it:

1. **Clone with LFS** (recommended):
   ```bash
   git lfs clone https://github.com/c-wilson04/CMSC345Project.git
   ```
   
2. **Or if you already cloned**, install LFS and pull:
   ```bash
   git lfs install
   git lfs pull
   ```

The file will be automatically downloaded when you clone or pull the repository.

## Evaluation Metrics

Models will be evaluated using:

- Sensitivity (SENS)
- Specificity (SPEC)
- Accuracy
- Matthews Correlation Coefficient (MCC)
- Average MCC across all four classes
- 4-label accuracy

## Deliverables

1. Team project contract
2. Progress report (November 6, 2025)
3. Final report (December 2, 2025)
4. Test predictions (December 2, 2025)

## Notes

- 5-fold cross-validation must be performed on the training dataset
- All design activities should be completed using only the training dataset
- The test dataset should be used only once for final evaluation
