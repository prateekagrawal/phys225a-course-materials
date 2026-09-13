# Analysis notebook template

Edit analysis_template.ipynb to change explanations, imports, analysis code or
object-definition exercises. Finding Z reads it fresh for each new notebook.
Set FINDINGZ_NOTEBOOK_TEMPLATE to this file in the course checkout.

Keep exactly one code cell tagged findingz-settings. Finding Z replaces that cell
with an editable analysis dictionary containing separate plot and count settings.
The exporter writes a readable Python dictionary into that cell; no json import
is needed. The cell is collapsed by default to keep provenance out of the main
analysis flow. Expand it to inspect the original settings.
A blank template receives empty selections.
Other cell sources are preserved; execution counts and outputs are cleared.
Do not put secrets or student outputs in the template.

Use the same supported settings schema as the packaged template in the Finding Z
application. Changing the exported schema itself requires an app update.
Saved notebooks refer to existing samples, not embedded event files. Preserve those
samples to reproduce results. Changes here never overwrite saved student notebooks.

The short analysis cells use findingz.notebook_analysis for sample loading,
normalization and plotting. Student choices (sample IDs, variable, cuts, channels,
luminosity and counting roles) remain editable in the notebook. This template
requires the accompanying FindingZ helper module: update the app before deploying
the new template. Existing old templates still work with the updated app.

07_simple_analysis.ipynb is the clean standalone starter. Historical exercise
notebooks are retained; do not overwrite students' edited copies during rollout.
