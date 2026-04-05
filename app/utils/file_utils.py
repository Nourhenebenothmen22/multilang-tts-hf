from pathlib import Path

def ensure_dir(path: str) -> None:
    Path(path).mkdir(parents=True, exist_ok=True)

def build_output_path(output_dir: str, filename: str) -> str:
    ensure_dir(output_dir)
    return str(Path(output_dir) / filename)