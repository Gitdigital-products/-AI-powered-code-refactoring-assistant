import os
import argparse
from src.engine.ast_analyzer import analyze_file
from src.utils.llm_client import get_refactor_suggestion
from src.engine.sandbox import RefactorSandbox
from src.utils.diff_tool import generate_github_diff

def main(file_path):
    # 1. READ
    with open(file_path, "r") as f:
        original_code = f.read()

    # 2. ANALYZE (Local AST)
    issues = analyze_file(file_path)
    if not issues:
        print("✅ Code looks clean. No refactor needed.")
        return

    # 3. GENERATE (AI Call)
    print(f"🤖 Consulting AI for {len(issues)} issues...")
    refactored_code = get_refactor_suggestion(original_code, issues)

    # 4. VERIFY (Sandbox)
    sandbox = RefactorSandbox(project_root=os.getcwd())
    is_safe, error_msg = sandbox.verify_refactor(file_path, refactored_code)

    if not is_safe:
        print(f"🛑 Refactor rejected: {error_msg}")
        return

    # 5. REPORT (Diff)
    diff_report = generate_github_diff(original_code, refactored_code, file_path)
    
    # Save the report to a file so the GitHub Action can post it
    with open("refactor_report.md", "w") as f:
        f.write(diff_report)
    
    print("✨ Refactor complete! Report generated in refactor_report.md")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    args = parser.parse_args()
    main(args.file)
