import os
import argparse
from src.engine.ast_analyzer import analyze_file
from src.utils.llm_client import get_refactor_suggestion # We'll build this next

def run_refactor_pipeline(file_path):
    print(f"🔍 Analyzing {file_path} for code smells...")
    
    # 1. Local AST Analysis (Saves tokens/cost)
    issues = analyze_file(file_path)
    
    if not issues:
        print("✅ No major structural issues found by AST. Skipping AI call.")
        return

    print(f"⚠️ Found {len(issues)} issues. Consulting AI for refactoring...")

    with open(file_path, "r") as f:
        original_code = f.read()

    # 2. AI Refactoring Call
    # We pass the issues found by AST as "hints" to the AI
    refactored_code = get_refactor_suggestion(original_code, issues)

    # 3. Output the result
    # In a real PR, this would write to a new branch or a diff file
    output_path = f"{file_path}.refactored"
    with open(output_path, "w") as f:
        f.write(refactored_code)
    
    print(f"✨ Refactored code written to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="Path to the file to refactor")
    args = parser.parse_args()
    
    if args.file:
        run_refactor_pipeline(args.file)
