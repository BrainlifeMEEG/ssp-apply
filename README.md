<h1 align="center">Apply SSP projectors</h1>

<p align="center">
  Applies precomputed signal-space projection (SSP) projectors (for example ECG or EOG) to continuous MEG/EEG data with MNE-Python and saves the cleaned raw FIF.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/brainlife.app.674"><img src="https://img.shields.io/badge/Brainlife-brainlife.app.674-blue.svg" alt="Run on brainlife.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-see_LICENSE-lightgrey.svg" alt="License"></a>
</p>

## At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Applies precomputed signal-space projection (SSP) projectors (for example ECG or EOG) to continuous MEG/EEG data with MNE-Python and saves the cleaned raw FIF.**

Adds the projectors from the projection file to the raw data with add_proj and applies them with apply_proj, saving raw.fif, and makes a joint plot of the projectors against an ECG-evoked response. Use it after an App that computes SSP projectors to remove the artefact components from the data.

| | |
|---|---|
| **Inputs** | `neuro/meeg/mne/raw` · `neuro/meeg/mne/projection` |
| **Outputs** | `generic/image/png` · `neuro/meg/fif` |
| **Container** | `brainlifemeeg/mne:1.12.1` |
| **Resources** | 8 CPUs |
| **Run it** | [doi.org/10.25663/brainlife.app.674](https://doi.org/10.25663/brainlife.app.674) |

#### Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `fif` | `neuro/meeg/mne/raw` | yes | Continuous MEG/EEG data (MNE raw FIF). |
| `projection` | `neuro/meeg/mne/projection` | yes | Precomputed SSP projector file (.fif), for example from an ECG/EOG SSP App. |

#### Outputs

| Output | Datatype | Description |
|---|---|---|
| `out_figs` | `generic/image/png` | Joint plot (PNG) of the projectors and the ECG-evoked response. |
| `out_dir` | `neuro/meg/fif` | Raw data (raw.fif) with the SSP projectors applied. |

<!-- brainlife-app:end -->

## Running the App

### On brainlife.io

Open the App at [doi.org/10.25663/brainlife.app.674](https://doi.org/10.25663/brainlife.app.674), choose `neuro/meeg/mne/raw`, `neuro/meeg/mne/projection` from your project and press **Execute**. The results are saved to your project as `generic/image/png`, `neuro/meg/fif`.

### Locally

You need [Singularity/Apptainer](https://apptainer.org/) (the App runs in `brainlifemeeg/mne:1.12.1`), [`jq`](https://jqlang.github.io/jq/).

1. Clone this repository.
2. Create `config.json` with the paths to your inputs and the parameters:

   ```json
   {
       "mne": "/path/to/fif/mne",
       "projection": "/path/to/projection/projection"
   }
   ```

3. Run `./main`.

## Configuration Parameters

This app reads no configuration parameters beyond its input files (see Inputs above).

## Local Testing

```bash
git clone <this-repo>
cd SSP-apply
# edit config.json with paths to your own mne and projection files
./main
```

## Citing

If you use this App, please cite it, the software it builds on and brainlife.io:

- Apply SSP projectors. brainlife.io App. [doi:10.25663/brainlife.app.674](https://doi.org/10.25663/brainlife.app.674)
- Gramfort A et al. MEG and EEG data analysis with MNE-Python. Frontiers in Neuroscience 7:267 (2013). [doi:10.3389/fnins.2013.00267](https://doi.org/10.3389/fnins.2013.00267)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Authors

- Saeed Zahran (https://github.com/zahransa)

## Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io, which runs this App, is publicly funded by Wellcome, the U.S. National Institutes of Health and the U.S. National Science Foundation; acknowledging that support helps keep it running.</sub>

## License

See [LICENSE](LICENSE).
