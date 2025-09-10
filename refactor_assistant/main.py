#!/usr/bin/env python3
"""
Main entry point for the AI Refactoring Assistant.
"""
import argparse
import logging
from pathlib import Path
from .analyzer import CodeAnalyzer
from .refactor import RefactoringEngine

def setup_logging(verbose=False):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def main():
    parser = argparse.ArgumentParser(description='AI-powered code refactoring assistant')
    parser.add_argument('path', help='Path to the code to analyze')
    parser.add_argument('--apply', action='store_true', help='Apply suggested refactoring')
    parser.add_argument('--config', help='Path to custom configuration file')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    setup_logging(args.verbose)
    
    # Initialize components
    analyzer = CodeAnalyzer(config_path=args.config)
    refactor_engine = RefactoringEngine()
    
    # Analyze code
    suggestions = analyzer.analyze(Path(args.path))
    
    if args.apply:
        refactor_engine.apply_refactoring(suggestions)
    else:
        for suggestion in suggestions:
            print(suggestion)

if __name__ == '__main__':
    main()