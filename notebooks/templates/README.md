# Analysis notebook template

Edit analysis_template.ipynb to change explanations, imports, analysis code or
object-definition exercises. Finding Z reads it fresh for each new notebook.
Set FINDINGZ_NOTEBOOK_TEMPLATE to this file in the course checkout.

Keep exactly one code cell tagged findingz-settings. Finding Z replaces that cell
with an editable analysis dictionary containing separate plot and count settings.
Keep the json import before that cell. A blank template receives null selections.
Other cell sources are preserved; execution counts and outputs are cleared.
Do not put secrets or student outputs in the template.

Use the same supported settings schema as the packaged template in the Finding Z
application. Changing the exported schema itself requires an app update.
Saved notebooks refer to existing samples, not embedded event files. Preserve those
samples to reproduce results. Changes here never overwrite saved student notebooks.
