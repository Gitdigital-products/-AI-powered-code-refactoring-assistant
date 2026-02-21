import ast

class RefactorAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.suggestions = []

    def visit_FunctionDef(self, node):
        # 1. Check Function Length
        if len(node.body) > 20:
            self.suggestions.append({
                "line": node.lineno,
                "name": node.name,
                "issue": "Long Function",
                "message": f"Function '{node.name}' is over 20 lines. Consider breaking it down."
            })

        # 2. Check for Deep Nesting (Nested Ifs/Loops)
        for child in ast.walk(node):
            if isinstance(child, (ast.If, ast.For, ast.While)):
                for grandchild in ast.iter_child_nodes(child):
                    if isinstance(grandchild, (ast.If, ast.For, ast.While)):
                        self.suggestions.append({
                            "line": grandchild.lineno,
                            "name": node.name,
                            "issue": "Deep Nesting",
                            "message": "Nested logic detected. Consider guard clauses or sub-functions."
                        })
        
        self.generic_visit(node)

def analyze_file(file_path):
    with open(file_path, "r") as source:
        tree = ast.parse(source.read())
    
    analyzer = RefactorAnalyzer()
    analyzer.visit(tree)
    return analyzer.suggestions

# Example usage:
# print(analyze_file("your_script.py"))
