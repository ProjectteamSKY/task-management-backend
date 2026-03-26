import toml
from pathlib import Path

# Cache loaded files (performance)
_query_cache = {}


def load_queries(file_name: str):
    """
    Load TOML file and cache it

    Example:
    queries = load_queries("worker")
    sql = queries["create_worker"]
    """
    if file_name in _query_cache:
        return _query_cache[file_name]

    base_path = Path(__file__).resolve().parent.parent / "queries"
    file_path = base_path / f"{file_name}.toml"

    if not file_path.exists():
        raise FileNotFoundError(f"{file_name}.toml not found")

    queries = toml.load(file_path)
    _query_cache[file_name] = queries

    return queries