# PHYS 225A — Problem Set 0

Start with [Problem Set 0, Question 4: compare QED with MARK II and FindingZ](exercises/00_pset0_q4_qed_comparison.ipynb).

1. Generate your sample in FindingZ using the settings given in the notebook.
2. Copy the notebook into a `work` folder in your JupyterLab home directory.
   Name your copy `pset0_q4_<name>.ipynb`. Leave the course original unchanged.
3. Select **Python (hep)** on CIT, run the cells in order, and choose your sample
   from the table. Complete the exercise in your copy.
4. Save with the outputs and plots, download the `.ipynb` file from JupyterLab,
   and include it with your problem-set submission.

Keep the simulation run used by your notebook: event files are stored separately
and are not embedded in the notebook. See [sample storage](datasets/README.md).

The `config` directory and `notebooks/templates` support FindingZ; they are not
additional assignments. Course updates do not update your personal copy in `work`.

Optional run, parameter, shower and detector card editing is demonstrated in
[card_customization.example.yaml](config/card_customization.example.yaml).
This `codex/testing` branch enables these editors with schema 2. It requires
FindingZ commit `c58d13a` or a compatible later build; the version label `0.2.0`
alone does not identify that build. The student branch `codex/initial-layout`
is unchanged. Validate on the CIT test server before promoting these changes.
The `run_card`, `param_card`, `shower_card` and
`detector_card` blocks control available edits; a process can override a course
policy, and model entries can supply their own parameter policy. Card paths are
relative to the catalogue. Detailed configuration and scripted-run examples live
in FindingZ's `deploy/EXTERNAL-COURSE-CONTENT.md`.

[License](LICENSE) · [Attribution](PROVENANCE.md)

## Problem Set 2: W transverse mass

Generate 1,000 MadGraph-only events for each of `w_enu` and `wj_enu`.
For the W + jet sample set `ptj = 30` GeV in the run card; keep other cuts
consistent and record them. Use the saved LHE or compressed LHE files in
[the companion notebook](notebooks/templates/02_w_transverse_mass.ipynb).

Students implement transverse mass, compare the electron pT distribution with
an isotropic Jacobian reference, and test mass estimators when the W recoils.
The notebook handles file loading and plotting with numpy and matplotlib.
It reads electron and neutrino momenta directly, with no Delphes or FindingZ
code update required. FindingZ's course plot menu exposes existing electron
observables; the transverse-mass and truth-mass plots are made in the notebook.
