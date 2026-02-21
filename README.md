# README.md (The "Face" of the Project)
We'll use a dense block of badges to show off the stack and the project's health.
# 🤖 AI-Powered Code Refactoring Assistant

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Build](https://img.shields.io/badge/build-passing-brightgreen.svg)
![PRs](https://img.shields.io/badge/PRs-welcome-orange.svg)
![OpenAI](https://img.shields.io/badge/AI-GPT--4o-blueviolet.svg)
![Security](https://img.shields.io/badge/Safety-Sandboxed-success.svg)
![Solana](https://img.shields.io/badge/Web3-Solana%20Compatible-black.svg)

> **Automated Code Governance.** This assistant uses AST analysis and LLMs to identify technical debt, suggest refactors, and verify them in a safe sandbox before they ever touch your main branch.

---

## 🚀 How it Works

1. **Static Analysis**: Uses `ast_analyzer.py` to find complex/messy functions locally (saving tokens).
2. **AI Refactoring**: Sends problematic snippets to GPT-4o with context-aware prompts.
3. **Sandbox Verification**: Runs your existing `pytest` suite against the new code in an isolated environment.
4. **GitHub Integration**: Posts a clean `diff` report directly to your Pull Request.

---

## 🛠️ Installation

1. **Clone the Repo**
   ```bash
   git clone [https://github.com/Gitdigital-products/-AI-powered-code-refactoring-assistant.git](https://github.com/Gitdigital-products/-AI-powered-code-refactoring-assistant.git)
   cd -AI-powered-code-refactoring-assistant

 * Setup Environment
   python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

 * Configure API Keys
   Create a .env file:
   OPENAI_API_KEY=your_key_here

🤖 Usage
Local CLI
Refactor a specific file and see the diff locally:
python main.py --file src/engine/messy_code.py

GitHub Action
Simply comment /refactor on any Pull Request, and the bot will:
 * Analyze the changes.
 * Verify the logic in the sandbox.
 * Reply with a suggested diff.
🏛️ Governance & Compliance
Designed for GitDigital standards, this tool ensures that refactors adhere to:
 * Dry Principles: Reducing code duplication.
 * Security: Avoiding common sinkholes in Web3/Solana (Anchor) logic.
 * Readability: Maintaining a clean codebase for decentralized teams.
🤝 Contributing
Feel free to open an issue or submit a PR. Let's build the future of automated code quality together!

---

### Final Project Status
* **`src/engine/ast_analyzer.py`**: ✅ Done
* **`src/engine/refactor_engine.py`**: ✅ Done
* **`src/engine/sandbox.py`**: ✅ Done
* **`src/utils/diff_tool.py`**: ✅ Done
* **`.github/workflows/refactor-bot.yml`**: ✅ Done
* **`requirements.txt` & `README.md`**: ✅ Done

# -AI-powered-code-refactoring-assistant
   AI-powered code refactoring assistant: A bot that automatically suggests and applies code refactors based on best practices and performance improvements.
AI-Powered Code Refactoring Assistant 🤖

An intelligent bot that automatically suggests and applies code refactoring improvements based on best practices, performance metrics, and maintainability standards. This tool leverages machine learning to analyze code patterns and provide context-aware recommendations.

Features

· Automated Code Analysis: Scans your codebase for anti-patterns and improvement opportunities
· Context-Aware Suggestions: Provides language-specific recommendations based on best practices
· Safe Refactoring: Applies changes with built-in safety checks and backup systems
· Multi-Language Support: Works across multiple programming languages
· Customizable Rules: Configure refactoring rules to match your team's standards
· Version Control Integration: Works seamlessly with Git and other VCS

Supported Languages

· Python
· JavaScript/TypeScript
· Java
· C#
· Go
· Ruby
· PHP
· And more through extensible architecture

Installation

```bash
# Clone the repository
git clone https://github.com/RickCreator87/ai-refactoring-assistant.git

# Install dependencies
cd ai-refactoring-assistant
pip install -r requirements.txt
```

Usage

```bash
# Analyze code without applying changes
refactor analyze --path /your/code/path

# Apply suggested refactoring
refactor apply --path /your/code/path

# Custom rules configuration
refactor --config ./custom_rules.yaml
```

Example

Before:

```python
def calculate(a,b):
    x = a + b
    y = x * 2
    return y
```

After Refactoring:

```python
def calculate_double_sum(a: int, b: int) -> int:
    """Calculate the double of the sum of two integers."""
    return 2 * (a + b)
```

Configuration

Create a .refactorrc file to customize behavior:

```yaml
rules:
  - complexity
  - performance
  - naming
  - documentation
  
ignore:
  - tests/
  - vendor/
  
language: python
strict: false
```

Contributing

We welcome contributions! Please see our Contributing Guidelines for details.

License

MIT License - see LICENSE file for details.

Roadmap

· Add plugin system for custom rules
· Integrate with popular IDEs
· Add CI/CD integration
· Support for additional languages
· Interactive refactoring mode

---

For the gist language selection: Python would be an excellent choice as it's widely used in AI/ML projects and has strong ecosystem support for code analysis tools. Alternatively, TypeScript would be great if you're focusing on web development ecosystems.
