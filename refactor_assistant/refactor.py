"""
Module responsible for applying refactoring suggestions.
"""
import ast
import astor
from pathlib import Path
from .safety_checker import SafetyChecker

class RefactoringEngine:
    def __init__(self):
        self.safety_checker = SafetyChecker()
        
    def apply_refactoring(self, suggestions):
        for suggestion in suggestions:
            if self.safety_checker.is_safe(suggestion):
                self._apply_suggestion(suggestion)
                
    def _apply_suggestion(self, suggestion):
        file_path = Path(suggestion['file_path'])
        
        # Parse the code
        with open(file_path, 'r') as f:
            code = f.read()
        tree = ast.parse(code)
        
        # Apply the transformation (simplified example)
        # In a real implementation, this would use more sophisticated AST manipulation
        transformer = self._get_transformer(suggestion)
        new_tree = transformer.visit(tree)
        
        # Write the modified code back
        new_code = astor.to_source(new_tree)
        with open(file_path, 'w') as f:
            f.write(new_code)
    
    def _get_transformer(self, suggestion):
        # Return appropriate AST transformer based on suggestion type
        # This is a simplified example
        class RenameTransformer(ast.NodeTransformer):
            def visit_FunctionDef(self, node):
                if node.name == suggestion['old_name']:
                    node.name = suggestion['new_name']
                return node
                
        return RenameTransformer()