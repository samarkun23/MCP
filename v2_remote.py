from fastmcp import FastMCP
from notes_db import list_notes, add_note, delete_note

mcp = FastMCP("notes")

@mcp.tool()
def list_my_notes() -> list[dict]:
    """List all saved notes"""
    return list_notes(owner="local")

@mcp.tool()
def add_a_note(text: str) -> dict: 
    """Save a new note"""
    return add_note(owner="local", text=text)

@mcp.tool()
def delete_a_note(note_id: int) -> str:
    """Delete a node by id."""
    return "deleted" if delete_note(owner="local", note_id=note_id) else "nothing delete"

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)