"""
Code analysis module that identifies refactoring opportunities.
"""
import ast
from pathlib import Path
from typing import List
from .ai_model.pattern_detector import PatternDetector
from .rules_engine import RulesEngine

class CodeAnalyzer:
    def __init__(self, config_path=None):
        self.rules_engine = RulesEngine(config_path)
        self.pattern_detector = PatternDetector()
        
    def analyze(self, path: Path) -> List[dict]:
        suggestions = []
        
        # Process Python files
        for file_path in path.rglob('*.py'):
            with open(file_path, 'r') as f:
                code = f.read()
            
            # Get rule-based suggestions
            rule_suggestions = self.rules_engine.analyze_code(code, file_path)
            suggestions.extend(rule_suggestions)
            
            # Get AI-based suggestions
            ai_suggestions = self.pattern_detector.analyze(code, file_path)
            suggestions.extend(ai_suggestions)
        
        return suggestions