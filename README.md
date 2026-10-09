# Apply SSP Projectors

[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.674-blue.svg)](https://doi.org/10.25663/brainlife.app.674)

## Description

This Brainlife App applies a pre-computed set of signal-space projection (SSP) vectors (e.g. for ECG or EOG artifacts) to continuous MEG/EEG data, using MNE-Python's [`mne.io.Raw.add_proj`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.add_proj) and [`apply_proj`](https://mne.tools/stable/generated/mne.io.Raw.html#mne.io.Raw.apply_proj) methods. For quality control, it also builds an ECG-evoked response (via [`mne.preprocessing.create_ecg_epochs`](https://mne.tools/stable/generated/mne.preprocessing.create_ecg_epochs.html)) and plots the projectors against it with [`mne.viz.plot_projs_joint`](https://mne.tools/stable/generated/mne.viz.plot_projs_joint.html).

The app generates:
- A raw `.fif` file with the SSP projectors applied
- A joint plot of the projectors and the ECG-evoked response
- A `product.json` summary reporting how many projectors were applied

## Inputs

- **`mne`** (`neuro/meeg/mne/raw`): continuous MEG/EEG data to which the projectors will be applied (required)
- **`projection`** (`neuro/meeg/mne/projection`): pre-computed SSP projector file (`.fif`), e.g. produced by the "Compute ECG artifact SSP projectors" app (required)

## Outputs

- **`out_dir/raw.fif`** (`neuro/meg/fif`, tag `ssp-applied`): raw data with the SSP projectors applied
- **`out_figs/joint-plot.png`** (`generic/image/png`): joint plot of the projectors and the ECG-evoked response
- **`product.json`**: summary message with the number of projectors applied, plus the joint plot image

## Configuration Parameters

This app reads no configuration parameters beyond its input files (see Inputs above).

## Usage

### Running on Brainlife.io

1. Go to the [Apply SSP Projectors app page](https://brainlife.io/app/63341bd2db978c79919bff74) on Brainlife.io.
2. Select your project, the continuous MEG/EEG data as the `mne` input, and a pre-computed SSP projector file as the `projection` input.
3. Submit the process, then download `out_dir/raw.fif` and review the joint plot in the output viewer.

### Local Testing

```bash
git clone <this-repo>
cd SSP-apply
# edit config.json with paths to your own mne and projection files
./main
```

## Authors
- Saeed Zahran (https://github.com/zahransa)

## Citations

We kindly ask that you cite the following articles when publishing papers and code using this app.

Hayashi, S., Caron, B.A., Heinsfeld, A.S. et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. Nat Methods 21, 809–813 (2024). https://doi.org/10.1038/s41592-024-02237-2

Gramfort, A. et al. MEG and EEG data analysis with MNE-Python. Front. Neurosci. 7, 267 (2013). https://doi.org/10.3389/fnins.2013.00267

## Funding Acknowledgement

brainlife.io is publicly funded and for the sustainability of the project it is helpful to acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your publications and code reusing this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://grantome.com/grant/NIH/R01-EB030896-01)

## License

Copyright (c) 2026 MEEG Brainlife team. Licensed under AGPL-3.0, see [license.txt](license.txt) for details.
