import json
from pathlib import Path

ROOT = Path(__file__).parent

def remove_widgets(path: Path):
    with open(path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
    
    changed = False
    
    # Remove top-level metadata.widgets
    if "metadata" in nb and "widgets" in nb["metadata"]:
        del nb["metadata"]["widgets"]
        changed = True
    
    # Remove cell-level metadata.widgets
    for cell in nb.get("cells", []):
        if "metadata" in cell and "widgets" in cell["metadata"]:
            del cell["metadata"]["widgets"]
            changed = True
    
    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1)
        print(f"Removed widgets from: {path}")
        return True
    else:
        print(f"No widgets found: {path}")
        return False

def main():
    for ipynb in ROOT.rglob("*.ipynb"):
        try:
            remove_widgets(ipynb)
        except Exception as e:
            print(f"Error: {ipynb} — {e}")

if __name__ == "__main__":
    main()