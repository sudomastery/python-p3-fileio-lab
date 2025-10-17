def write_file(file_name, file_content):

    # Support pathlib.Path or str and ensure .txt extension
    try:
        # Works if file_name is a pathlib.Path-like object
        file_path = file_name.with_suffix('.txt')
        parent = file_path.parent
        if str(parent) and str(parent) != '.':
            parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, 'w') as f:
            f.write(file_content)
    except AttributeError:
        # Fallback for plain strings
        file_path = f"{file_name}.txt" if not str(file_name).endswith('.txt') else str(file_name)
        with open(file_path, 'w') as f:
            f.write(file_content)

def append_file(file_name, append_content):
    """Append content to a .txt file, creating it if it doesn't exist."""
    try:
        file_path = file_name.with_suffix('.txt')
        parent = file_path.parent
        if str(parent) and str(parent) != '.':
            parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, 'a') as f:
            f.write(append_content)
    except AttributeError:
        file_path = f"{file_name}.txt" if not str(file_name).endswith('.txt') else str(file_name)
        with open(file_path, 'a') as f:
            f.write(append_content)

def read_file(file_name):
    """Read and return the content of a .txt file."""
    try:
        file_path = file_name.with_suffix('.txt')
        with open(file_path, 'r') as f:
            return f.read()
    except AttributeError:
        file_path = f"{file_name}.txt" if not str(file_name).endswith('.txt') else str(file_name)
        with open(file_path, 'r') as f:
            return f.read()
