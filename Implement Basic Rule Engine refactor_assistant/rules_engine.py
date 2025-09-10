"""
Rule engine for code refactoring suggestions.
"""
import ast
import astor
from typing import List, Dict, Any
import yaml
from pathlib import Path

class RulesEngine:
    def __init__(self, config_path=None):
        self.rules = self._load_rules(config_path)
        
    def _load_rules(self, config_path):
        # Load default rules
        default_rules = {
            'python': [
                {
                    'name': 'simplify_if_else',
                    'description': 'Simplify nested if-else statements',
                    'pattern': 'if-else',
                    'action': 'simplify'
                },
                {
                    'name': 'rename_variables',
                    'description': 'Rename variables to follow naming conventions',
                    'pattern': 'naming',
                    'action': 'rename'
                },
                {
                    'name': 'extract_method',
                    'description': 'Extract repeated code into methods',
                    'pattern': 'repetition',
                    'action': 'extract'
                }
            ]
        }
        
        # Load custom rules if config path is provided
        if config_path and Path(config_path).exists():
            with open(config_path, 'r') as f:
                custom_rules = yaml.safe_load(f)
                default_rules.update(custom_rules)
                
        return default_rules
    
    def analyze_code(self, code: str, file_path: Path, language: str) -> List[Dict[str, Any]]:
        """Analyze code and return refactoring suggestions."""
        suggestions = []
        
        if language == 'python':
            suggestions = self._analyze_python(code, file_path)
            
        return suggestions
    
    def _analyze_python(self, code: str, file_path: Path) -> List[Dict[str, Any]]:
        """Analyze Python code for refactoring opportunities."""
        suggestions = []
        
        try:
            tree = ast.parse(code)
            
            # Check for nested if-else statements
            nested_if_else = self._find_nested_if_else(tree)
            for node in nested_if_else:
                suggestions.append({
                    'type': 'simplify_if_else',
                    'description': 'Nested if-else statements can be simplified',
                    'line': node.lineno,
                    'file_path': str(file_path),
                    'code_snippet': astor.to_source(node),
                    'confidence': 0.8
                })
                
            # Check for poor variable naming
            poor_naming = self._find_poor_naming(tree)
            for old_name, new_name, node in poor_naming:
                suggestions.append({
                    'type': 'rename_variables',
                    'description': f'Variable "{old_name}" should be renamed to "{new_name}"',
                    'line': node.lineno,
                    'file_path': str(file_path),
                    'old_name': old_name,
                    'new_name': new_name,
                    'code_snippet': astor.to_source(node),
                    'confidence': 0.9
                })
                
        except SyntaxError:
            # Skip files with syntax errors
            pass
            
        return suggestions
    
    def _find_nested_if_else(self, tree: ast.AST) -> List[ast.If]:
        """Find nested if-else statements in the AST."""
        nested_if_else = []
        
        for node in ast.walk(tree):
            if isinstance(node, ast.If):
                # Check if this if statement has nested if statements
                for child in ast.walk(node):
                    if isinstance(child, ast.If) and child != node:
                        nested_if_else.append(node)
                        break
                        
        return nested_if_else
    
    def _find_poor_naming(self, tree: ast.AST) -> List[tuple]:
        """Find variables with poor naming conventions."""
        poor_naming = []
        
        # Simple rule: variables should not be single letters (except for loop variables)
        for node in ast.walk(tree):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and len(target.id) == 1 and target.id not in ['i', 'j', 'k']:
                        # Suggest a more descriptive name
                        new_name = f"descriptive_{target.id}"
                        poor_naming.append((target.id, new_name, node))
                        
        return poor_naming