import re

def analyze_rust_solana(file_content):
    issues = []
    
    # 1. Check for missing inline on small functions
    functions = re.findall(r"fn\s+(\w+)\(.*\)\s*->", file_content)
    for fn in functions:
        if "inline" not in file_content.split(fn)[0][-50:]:
            issues.append({
                "issue": "Missing Inline",
                "message": f"Function '{fn}' could save CU with #[inline(always)]."
            })

    # 2. Check for Eager Loading of large accounts
    if "Account<'info," in file_content and "LazyAccount" not in file_content:
        issues.append({
            "issue": "Eager Loading",
            "message": "Consider using LazyAccount<'info, T> to reduce initial CU parse costs."
        })

    return issues
