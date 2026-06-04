# Repository Structure

Cloned from [Addison Hu's tc-ocean-methods](https://github.com/huisaddison/tc-ocean-methods/), adapted for ETNP OMZ dissolved oxygen analysis. See the [ROADMAP](ROADMAP.md) for development goals.

## Directories

```
tc-argo/
├── original/                    Git submodule of Hu's unmodified repo (reference only)
├── scripts/
│   ├── tc_ocean_methods/        Working copy of the pipeline
│   │   ├── pipeline-gridded/    A-series (MATLAB) + B-series (Python) scripts
│   │   ├── pipeline-integrated/ Integrated heat content variant (mostly softlinks)
│   │   ├── implementations/     Regressors (TPS, kernel smoother) and utilities
│   │   └── tests/               Pipeline configuration tests
│   ├── current_runs/            Machine-specific settings and pipeline runner
│   │   ├── current_settings.py  Master configuration (paths, parameters)
│   │   └── current_pipeline.py  Sequential execution of A/B scripts
│   ├── GO_BGC/                  GO-BGC workshop tutorial for BGC Argo data access
│   ├── older_misc/              Legacy scripts from earlier development
│   └── temp/                    Temporary/scratch scripts
├── documents/                   Dissertation proposal, 4D Argo proposal (PDFs)
├── notes/                       Dev notes, checklists, MATLAB error logs
├── log_history/                 Archived run configurations and logs
├── wd/                          Working directory for pipeline runs (gitignored)
└── data/                        Data directory (gitignored, see .env.example)
```

## Pipeline Script Naming

- **A-series** (A00-A13): MATLAB oceanographic processing (gridding, mean field, Gaussian Process)
- **B-series** (B00-B36): Python TC matching, pairing, statistics, and visualization

## Configuration

Copy `.env.example` to `.env` and set paths for your machine. See `scripts/current_runs/current_settings.py` for all pipeline parameters.
