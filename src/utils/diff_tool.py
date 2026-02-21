import difflib

def generate_github_diff(original_code, refactored_code, filename):
    """
    Generates a unified diff string formatted for GitHub Markdown.
    """
    original_lines = original_code.splitlines(keepends=True)
    refactored_lines = refactored_code.splitlines(keepends=True)

    # Generate the diff
    diff = difflib.unified_diff(
        original_lines, 
        refactored_lines, 
        fromfile=f"a/{filename}", 
        tofile=f"b/{filename}"
    )

    diff_text = "".join(diff)

    if not diff_text:
        return "No changes detected."

    # Wrap it in Markdown code blocks for GitHub readability
    return f"### 🤖 AI Refactor Proposal for `{filename}`\n\n```diff\n{diff_text}\n```"
