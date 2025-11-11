import json
from pathlib import Path

ROOT = Path(__file__).parent

def fix_notebook_json(path: Path):
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    changed = False
    
    # Fix top-level metadata.widgets
    if "metadata" not in nb:
        nb["metadata"] = {}
    meta = nb["metadata"]
    if "widgets" in meta and isinstance(meta["widgets"], dict):
        if "state" not in meta["widgets"]:
            meta["widgets"]["state"] = {}
            changed = True
    
    # Fix cell-level metadata.widgets
    for cell in nb.get("cells", []):
        if "metadata" not in cell:
            cell["metadata"] = {}
        cell_meta = cell["metadata"]
        if "widgets" in cell_meta and isinstance(cell_meta["widgets"], dict):
            if "state" not in cell_meta["widgets"]:
                cell_meta["widgets"]["state"] = {}
                changed = True
    
    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1)
        print(f"Fixed: {path}")
        return True
    else:
        print(f"No change: {path}")
        return False

def main():
    for ipynb in ROOT.rglob("*.ipynb"):
        try:
            fix_notebook_json(ipynb)
        except Exception as e:
            print(f"Error: {ipynb} — {e}")

if __name__ == "__main__":
    main()