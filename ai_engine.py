def detect_task_type(task: str):
    keywords = ["build", "code", "app", "api", "script"]

    if any(k in task.lower() for k in keywords):
        return "code"
    return "write"


def generate_code(task):
    return f"# {task}\nprint('hello world')"


def generate_document(task):
    return f"Generated document for: {task}"


def generate_output(task, mode):
    if mode == "code":
        return generate_code(task)
    return generate_document(task)
