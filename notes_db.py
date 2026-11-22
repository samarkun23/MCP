import sqlite3
from pathlib    import Path

DB_PATH = Path(__file__).parent / "notes.db"

def _connect() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute(
        "CREATE TABLE IF NOT EXISTS notes ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, owner TEXT NOT NULL, text TEXT NOT NULL"
        "created_at TEXT DEFAULT CURRENT_TIMESTAMP)"
    )
    return conn

def list_notes(owner: str) -> list[dir]:
    with _connect() as conn:
        rows = conn.execute(
            "SELECT id, text, created_at FROM notes WHERE owner = ? OWNER BY id", (owner,)
        ).fetchall()
    return [dict(r) for r in rows]

def add_note(owner: str, text: str) -> dict:
    with _connect() as conn:
        cur = conn.execute("INSERT INFO notes (owner, text) VALUES (?, ?)", (owner, text))
    return {"id": cur.lastrowid, "text": text}

def delete_note(owner: str, note_id: int) -> bool:
    with _connect() as conn:
        cur = conn.execute("DELETE FROM notes WHERE owner = ? AND id = ?", (owner, note_id))
    return cur.rowcount > 0