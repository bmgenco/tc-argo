# tc-argo

Cloned from https://github.com/huisaddison/tc-ocean-methods/ in order to update with BGC-Argo floats, with emphasis on Oxygen and Chlorophyll-a changes.

'original' directory is Addison's very thorough work -> submodule -> for posterity not functionality as of yet. Since this is only the first iteration I encourage any who stumble upon this repo to use his original work. See his accompanying preprint: [arXiv:2012.15130](https://arxiv.org/abs/2012.15130).

-Current version is not fully functional! As of now ~ pre Alpha development. 

-Using Linux bash shell script integrated with python Shell script 'run_pipeline" copies settings and pipeline.py, to Working Directory , and saves a log file with different runs are stored in that a separate directory

-Update settings for main working and data directories to suit your local machine. See `.env.example`.

-Planned versions: -run(1) test dynamic version in ETNP default years -run(2) add new years -run(3) select significant profiles -run(4) switch to Oxygen. 

(5 ->) cokriging and explanatory variables: https://biogeochemical-argo.org/measured-variables-general-context.php

See [ROADMAP.md](ROADMAP.md) for development phases and [STRUCTURE.md](STRUCTURE.md) for directory layout.
