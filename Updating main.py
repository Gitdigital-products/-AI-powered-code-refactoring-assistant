# Inside main.py, update the run_refactor_pipeline function:

from src.engine.sandbox import RefactorSandbox

def run_refactor_pipeline(file_path):
    # ... (existing AST and LLM logic here) ...
    
    refactored_code = get_refactor_suggestion(original_code, issues)

    # NEW: Safety Verification
    sandbox = RefactorSandbox(project_root=os.getcwd())
    is_safe, message = sandbox.verify_refactor(file_path, refactored_code)

    if is_safe:
        output_path = f"{file_path}.refactored"
        with open(output_path, "w") as f:
            f.write(refactored_code)
        print(f"✨ Safe refactor generated: {output_path}")
    else:
        print(f"🛑 Refactor rejected: Tests failed in sandbox.\n{message}")
