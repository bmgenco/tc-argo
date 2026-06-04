# TC-Argo Development Roadmap

Adapting Hu et al. (arXiv:2012.15130) tropical cyclone-ocean analysis pipeline from core Argo temperature to BGC Argo dissolved oxygen for ETNP OMZ dissertation research.

---

## Phase 1: Pipeline Portability and Organization

Make the pipeline reproducible across machines and clearly documented.

- [x] Document directory structure (`STRUCTURE.md`)
- [x] Add conda environment spec (`environment.yml`)
- [x] Add machine-specific path template (`.env.example`)
- [x] Make `current_settings.py` read paths from environment variables
- [ ] Verify `environment.yml` creates working conda env on a clean machine
- [ ] Document data acquisition: where to download core Argo DAC files and TC track CSVs
- [ ] Ensure `.gitignore` covers data, runs, and environment files

---

## Phase 2: Core Argo Reproduction Test

Run Hu's pipeline end-to-end on core Argo (temperature) in ETNP to verify it reproduces expected results before modifying anything.

- [ ] Get A00 through A12 (MATLAB scripts) running in sequence
  - Known blocker: MATLAB NetCDF issues documented in `notes/20230807_matlab_error_notes`
- [ ] Run B00-B36 (Python scripts) in sequence
- [ ] Generate output figures (TPS three-panel, kernel smoothing, etc.)
- [ ] Compare to Hu's published results; document deviations
- [ ] Fix any pipeline breaks and commit working state

**Running order** (from Hu's README):
```
B00 -> B01 -> A00-A04 -> B02 -> B03 -> A05-A09 -> A11 -> A12
  -> B04-B10 -> B32 -> B35 -> B34 -> B36 -> B21-B27
```

---

## Phase 3: Evaluate MATLAB Alternatives (Deferred)

Assess feasibility of replacing MATLAB A-series scripts with Python.

- [ ] Audit each A-series script for Python equivalent:
  - `gsw` (Python TEOS-10) for oceanographic calculations
  - `scipy.interpolate.PchipInterpolator` for A01 gridding
  - `scikit-learn.gaussian_process` for A11 GP fitting
  - `netCDF4` / `xarray` for A00 data reading
- [ ] Decision: full Python replacement vs. keep MATLAB for GP scripts
- [ ] If replacing: implement and validate against MATLAB outputs

---

## Phase 4: BGC Argo Transition

Switch the analysis variable from core Argo temperature to BGC Argo dissolved oxygen.

### 4a. Data Access Review

The GO-BGC tutorial scripts in `scripts/GO_BGC/` use HTTP downloads from USGODAE. Evaluate whether these are still current or if newer tools are preferable:

- [ ] Review current state of GO-BGC tutorial scripts (last updated ~2023)
- [ ] Evaluate [argopy](https://argopy.readthedocs.io/) -- actively maintained Python library for Argo data access (supports BGC)
- [ ] Evaluate BGC-Argo GDAC synthetic profiles (Sprof files) from [data-argo.ifremer.fr](https://data-argo.ifremer.fr/)
- [ ] Evaluate [OneArgo-Mat](https://github.com/NOAA-PMEL/OneArgo-Mat) / [OneArgo-R](https://github.com/NOAA-PMEL/OneArgo-R) toolboxes
- [ ] Decide on data access method and document acquisition steps

### 4b. Pipeline Modifications

- [ ] Modify A00 (or Python replacement) to read `DOXY` / `DOXY_ADJUSTED` from synthetic profiles
- [ ] Update QC filters for oxygen-specific quality flags (different from TEMP QC)
- [ ] Adjust depth range: OMZ typically 100-900m vs. current 10-200 dbar for upper-ocean temperature
- [ ] Update `current_settings.py` with BGC-specific parameters (depth range, variable name)
- [ ] Update visualization scripts: color scales, units (umol/kg instead of deg C), axis labels

### 4c. Extended Analysis (Future)

- [ ] Cokriging with explanatory variables (see [BGC-Argo measured variables](https://biogeochemical-argo.org/measured-variables-general-context.php))
- [ ] Multi-variable analysis: DOXY + CHLA + NITRATE correlations with TC passage

---

## References

- Hu, A., Bates, S., Holt, J., et al. "Tropical cyclone-induced ocean thermal response." arXiv:2012.15130
- Genco, B. (2022). Dissertation Proposal. See `documents/BGenco_2022_Dissertation_Proposal.pdf`
- BGC-Argo: https://biogeochemical-argo.org/
- Beman Lab: https://bemanlab.org/
