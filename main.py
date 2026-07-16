"""
Apply SSP projectors to raw MEG/EEG data.

This app loads raw data and an SSP projector file, applies the
projectors, and generates a joint plot of the projectors against an
ECG-evoked response.

Inputs:
    - mne: Path to MNE raw .fif file
    - projection: Path to SSP projector file

Outputs:
    - out_dir/raw.fif: Raw data with SSP projectors applied
    - out_figs/joint-plot.png: Joint plot of projectors and ECG-evoked response
    - product.json: Metadata about the applied projectors
"""

# Copyright (c) 2026 brainlife.io

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'brainlife_utils'))

# Standard imports
import mne
import matplotlib.pyplot as plt

# Import shared utilities
from brainlife_utils import (
    load_config,
    setup_matplotlib_backend,
    ensure_output_dirs,
    create_product_json,
    add_info_to_product,
    add_image_to_product,
    require_config_keys
)

# Set up matplotlib for headless execution
setup_matplotlib_backend()

# Ensure output directories exist
ensure_output_dirs('out_dir', 'out_figs')

# Load configuration
config = load_config()
require_config_keys(config, ['mne', 'projection'])

# == LOAD DATA ==
fname = config['mne']
raw = mne.io.read_raw_fif(fname, verbose=False)
proj = mne.read_proj(config['projection'])
raw.add_proj(proj)
raw_cleaned = raw.copy().apply_proj()
raw_cleaned.save(os.path.join('out_dir', 'raw.fif'), overwrite=True)
n_applied = len(proj)

ecg_evoked = mne.preprocessing.create_ecg_epochs(raw).average()
ecg_evoked.apply_baseline((None, None))

proj = proj[3:]
# == FIGURE ==
plt.figure(1)
fig = mne.viz.plot_projs_joint(proj, ecg_evoked, picks_trace='MEG 0111')
fig.suptitle('Projectors')
fig_path = os.path.join('out_figs', 'joint-plot.png')
fig.savefig(fig_path)
plt.close(fig)

# == CREATE PRODUCT.JSON ==
product_items = []
add_info_to_product(product_items, f'Applied {n_applied} SSP projector(s) to raw data', 'success')
add_image_to_product(product_items, 'Projectors joint plot', filepath=fig_path)
create_product_json(product_items)
