import shutil
from pathlib import Path
import nbformat

ROOT = Path(__file__).parent

def ensure_state(obj):
    # obj is a dict-like metadata; if it contains "widgets" ensure "state" exists
    if not isinstance(obj, dict):
        return False
    widgets = obj.get("widgets")
    if widgets is None:
        return False
    if "state" not in widgets:
        widgets["state"] = {}
        obj["widgets"] = widgets
        return True
    return False

def fix_notebook(path: Path):
    nb = nbformat.read(path, as_version=nbformat.NO_CONVERT)
    changed = False

    # top-level metadata
    if ensure_state(nb.metadata):
        changed = True

    # per-cell metadata
    for cell in nb.get("cells", []):
        if ensure_state(cell.get("metadata", {})):
            changed = True

    if changed:
        bak = path.with_suffix(path.suffix + ".bak")
        shutil.copy2(path, bak)
        nbformat.write(nb, path)
        print(f"Fixed: {path} (backup: {bak.name})")
    else:
        print(f"No change: {path}")

def main():
    for ipynb in ROOT.rglob("*.ipynb"):
        try:
            fix_notebook(ipynb)
        except Exception as e:
            print(f"Error processing {ipynb}: {e}")

if __name__ == "__main__":
    main()