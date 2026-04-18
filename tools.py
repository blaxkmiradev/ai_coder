import os
from config import WORKSPACE_DIR

os.makedirs(WORKSPACE_DIR, exist_ok=True)

def _path(file):
    return os.path.join(WORKSPACE_DIR, file)

def write_file(file, content):
    path = _path(file)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"✅ Saved: {file}"

def read_file(file):
    path = _path(file)
    if not os.path.exists(path):
        return "❌ File not found"
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def list_files():
    return os.listdir(WORKSPACE_DIR)

# ⚠️ safety: disabled command execution
def run_command(cmd):
    return "⚠️ Disabled for safety"
