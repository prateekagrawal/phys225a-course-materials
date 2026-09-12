"""Offline software checks only; artificial fixtures are NOT released physics samples."""
import contextlib
import io
import json
import tempfile
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import awkward as ak
from findingz.hypotheses import AnalysisSample

ROOT = Path(__file__).resolve().parents[1]
notebooks = sorted(path for path in (ROOT / "notebooks/exercises").glob("*.ipynb")
                   if not path.name.startswith("."))

def execute(path, replacements=None):
    document = json.loads(path.read_text())
    assert document["nbformat"] == 4
    ns = {"display": lambda *_: None}
    with contextlib.redirect_stdout(io.StringIO()):
        for index, cell in enumerate(document["cells"]):
            if cell["cell_type"] == "code":
                assert not cell["outputs"] and cell["execution_count"] is None
                source = cell["source"]
                for before, after in (replacements or {}).items():
                    source = source.replace(before, after)
                exec(compile(source, f"{path.name}:cell{index}", "exec"), ns)
    plt.close("all")
    return ns

def main():
    with tempfile.TemporaryDirectory(prefix="findingz-exercise-tests-") as folder:
        root = Path(folder)
        frame = pd.DataFrame({
            "l1_pt":[30.,35.], "l2_pt":[30.,35.],
            "l1_eta":[.8,.7], "l2_eta":[-.8,-.7],
            "l1_phi":[0.,0.], "l2_phi":[np.pi,np.pi],
            "l1_mass":[0.,0.], "l2_mass":[0.,0.],
            "l1_charge":[-1,-1], "l2_charge":[1,1],
            "l1_flavor":["mu","mu"], "l2_flavor":["mu","mu"],
            "channel":["mumu","mumu"], "weight":[1.,1.]})
        sample_file = root / "fixture.csv"
        frame.to_csv(sample_file,index=False)
        config = {"collider":"ee","collider_id":"lep91","beam_energy_gev":45.6,
                  "run_mode":"madgraph","min_mass_gev":10.,"max_mass_gev":250.}
        samples = {key:AnalysisSample(key,key,"generated",sample_file,"artificial software fixture",
                                     config,2,1.) for key in ("signal","background")}
        objects = ak.Array([[{"pt":25.,"eta":.2,"charge":-1,"isolation":.1},
                             {"pt":30.,"eta":-.2,"charge":1,"isolation":.05}],
                            [{"pt":8.,"eta":1.,"charge":-1,"isolation":.2}]])
        fake_root = SimpleNamespace(collection=lambda _:objects)
        scan = [{"sqrt_s_gev":e,"sigma_pb":1e6*e**2/((e**2-91.2**2)**2+91.2**2*2.5**2),
                 "error_pb":1.,"integration_error_pb":1.} for e in [88.,89.,90.,91.,92.,93.,94.]]
        overrides = {
            "sample_id = None":'sample_id = "signal"',
            "sample_ids = []":'sample_ids = ["signal","background"]',
            "run_ids = []":'run_ids = ["fixture"]',
            "signal_id = None":'signal_id = "signal"',
            "background_ids = []":'background_ids = ["background"]',
            "scan = []":"scan = "+repr(scan),
            "angular_sample_id = None":'angular_sample_id = "signal"',
        }
        with patch("findingz.hypotheses.build_sample_library",return_value={}):
            for path in notebooks:
                execute(path)
        with patch("findingz.hypotheses.build_sample_library",return_value=samples), patch(
                "findingz.delphes.open_run",return_value=fake_root), patch("matplotlib.pyplot.show"):
            for path in notebooks:
                result = execute(path,overrides)
                if path.name.startswith("07"):
                    assert abs(result["mass"]-91.2)<.051
                    assert abs(result["width"]-2.5)<.051
                if path.name.startswith("05"):
                    assert result["result"].signal_yield >= 0
                print("PASS",path.name,"(setup and artificial-data branches)")
    assert len(notebooks)==7
    print("Seven notebooks passed offline software checks. Real sample/CIT validation remains required.")

if __name__ == "__main__":
    main()
