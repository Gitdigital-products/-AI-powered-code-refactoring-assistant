# Inside main.py
def main(file_path):
    ext = file_path.split('.')[-1]
    
    if ext == "py":
        issues = analyze_file(file_path) # Our Python AST
        prompt = PYTHON_PROMPT
    elif ext == "rs":
        with open(file_path, "r") as f:
            issues = analyze_rust_solana(f.read())
        prompt = SOLANA_REFACTOR_PROMPT
    else:
        print("Unsupported language.")
        return

    # Proceed with LLM call and Sandbox...
