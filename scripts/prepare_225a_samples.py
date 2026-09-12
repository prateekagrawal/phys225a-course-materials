"""Validate/list recipes by default; run explicitly selected jobs serially with --execute."""
import argparse
import json
from pathlib import Path
from findingz.hep_pipeline import HepSimulationConfig, run_hep_simulation

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, default=Path(__file__).resolve().parents[1] / "datasets/225a-sample-plan.json")
    parser.add_argument("--sample", action="append", default=[], help="Recipe ID; repeat for multiple jobs")
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--run-root", type=Path, help="Persistent instructor run storage (required for execution)")
    args = parser.parse_args()
    plan = json.loads(args.plan.read_text())
    recipes = {item["id"]: item for item in plan["recipes"]}
    if len(recipes) != len(plan["recipes"]):
        parser.error("Duplicate recipe IDs")
    unknown = set(args.sample)-recipes.keys()
    if unknown:
        parser.error(f"Unknown recipes: {sorted(unknown)}")
    if args.execute and (not args.sample or args.run_root is None):
        parser.error("--execute requires explicit --sample selections and --run-root")
    chosen = args.sample or list(recipes)
    for key in chosen:
        config = HepSimulationConfig(**recipes[key]["config"])
        print(key, config.run_mode, 2*config.beam_energy_gev, "GeV", config.events, "events", flush=True)
        if args.execute:
            result = run_hep_simulation(config, args.run_root)
            print("Generated; physics approval still required:", result.manifest_path, flush=True)
    if not args.execute:
        print("Dry run only: no simulations launched or catalog entries changed.")

if __name__ == "__main__":
    main()

