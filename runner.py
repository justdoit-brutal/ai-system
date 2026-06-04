import subprocess
import tempfile

def run_code(code):
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        f.write(code)
        path = f.name

    result = subprocess.run(
        ["python", path],
        capture_output=True,
        text=True,
        timeout=5
    )

    return {
        "success": result.returncode == 0,
        "output": result.stdout,
        "error": result.stderr
    }
