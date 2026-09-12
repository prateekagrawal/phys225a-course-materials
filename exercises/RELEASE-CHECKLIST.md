# Release gates

## Notebook checks
- Compile every code cell and execute all notebooks with no selection.
- Exercise each sample-dependent branch with approved data, including ROOT objects.
- Check conservation and energy conventions in 01; detector samples must not be used for the Born conservation test.
- Check event weights and the denominator in 02 and 04.
- Confirm the paired samples in 03 have identical hard-process and generator settings.
- In 04 inspect fields and card-level isolation; loosen notebook cuts only within what the stored collections permit.
- In 05 validate counting compatibility and normalization; record cut choices BEFORE data release.
- In 06 inspect the generated diagrams and parameter card for the photon-only preset; use its coupling convention.
- In 07 inspect scan residuals. Full SM scans need photon/interference modeling for a serious fit; the starter resonance fit is explicitly approximate.
- Confirm electron beam is +z before assigning charge-defined angular observables.
- Numerical tests with artificial fixtures are software checks, not physics validation.

## Reference sample release
Run recipes serially on the instructor environment; never auto-launch a batch at notebook startup.
Inspect MadGraph cross sections and integration errors, cards, event counts, detector ROOT
branches, and run manifests. Label all samples clearly and retain their provenance.
Register complete run directories in config/course_catalog.yaml only AFTER approval.
Use actual shared-storage paths; do not commit event files or placeholder paths.
Check the same files are readable by each student's Jupyter kernel.

For counting use the 240-GeV ZH(mumu) and WW(mumu) pair with identical detector,
mass window, beam energy and output profile. This is a defined simplified hypothesis
comparison, not a claim to contain all experimental backgrounds. Check other
backgrounds/interference before interpreting it as a realistic measurement.
For object selection start with muons from these runs; add a separately validated
electron sample pair if electron identification is to be assigned.

## Pseudo-data (not provided yet)
Choose luminosity AFTER inspecting expected rates and available MC statistics.
For each process draw a Poisson event count from the normalized expected yield,
then sample unit-weight event records from an independent pool. Use a documented
finite-MC/resampling policy. Do not give students a fixed-size generator sample
and call its row count experimental data.
Release a JSON object with an events array containing flat analysis columns
(mll, l1_pt, l2_pt, l1_eta, l2_eta, etc.) and no per-event signal labels.
The starter uses the background column schema for a zero-count events array.
Keep truth composition, random seeds, unreleased data and solutions OUTSIDE this
student repository. A disabled catalog entry is not access control.
Student observed p-values currently assume a known background mean; do not imply
the background-uncertainty slider is propagated into them.

## CIT smoke test
Check imports, sample discovery, one matrix-element and one full-pipeline run,
ROOT object access, plotting, save/reopen and persistence in hep. Configure the
notebook destination; URL prefix is optional and used only for the explicit link.
No FastJet Python interface is required for 225A.
