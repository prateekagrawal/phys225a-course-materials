# PHYS 225A practicals

Status: notebook drafts and generation recipes, not yet a validated sample release.
No new simulation datasets are included. Black-box physics and jet clustering are
not implemented by this teaching pack.

## Sequence
1. Reconstruct a collision (lectures 1–4): kinematics and event records.
2. Cross sections and event yields (lecture 5): normalization and acceptance.
3. From particles to detector objects (lectures 6–7): compare simulation stages.
4. Define a lepton (lecture 7): vary supplied object selections.
5. Design a cut and count: freeze cuts before pseudo-data release.
6. Test the QED prediction (lectures 16–18): angular shape and energy dependence.
7. Characterize the Z (lectures 19–20): diagnostic line-shape fit and optional asymmetry.

Pair 1–2, 3–4 and 6–7 if fewer assignments are preferred. Start with 1000-event
pilots, then judge whether larger samples are needed; every job stays within 10000.
Student notebooks are under notebooks/exercises. Empty selectors are intentional;
they run setup but do not silently choose an inappropriate sample.

## Deployment
Install FindingZ in hep; sync course materials separately. Keep student-edited
copies in persistent storage. Configure the FindingZ course catalog and variables
paths in BOTH Streamlit and Jupyter kernel environments. Choose the course Python
kernel. These notebooks use existing numpy/pandas/matplotlib/awkward dependencies.

See datasets/225a-sample-plan.json and scripts/prepare_225a_samples.py.
The recipe file is an instructor planning input, NOT the live application catalog.
Nothing becomes visible in the dropdown just by adding a recipe.
See exercises/RELEASE-CHECKLIST.md before registering or assigning samples.

In the hep environment, from this checkout:

```bash
python scripts/check_225a_exercises.py
python scripts/prepare_225a_samples.py
python scripts/prepare_225a_samples.py --sample born-mumu-91p2 --execute --run-root /YOUR/PERSISTENT/INSTRUCTOR/RUNS
```

The first command uses artificial fixtures; the second only validates/lists recipes.
Replace the run-root placeholder before the third command. It starts one real job.
Do not use a student-submission directory as instructor generation storage.
