1. tests/test_subject.py (The "Messy" Code)
Save this as a test file. It’s functional, but it’s a maintenance nightmare.
def process_data(data, user_type, bypass_validation=False):
    # Issue 1: Deep Nesting (3+ levels)
    if data:
        if isinstance(data, list):
            for item in data:
                if item.get("active"):
                    if user_type == "admin":
                        print("Processing admin item")
                        # Imagine 15 more lines of logic here...
                    else:
                        print("Processing standard item")
                else:
                    print("Skipping inactive")
        else:
            print("Data is not a list")
    else:
        print("No data provided")

    # Issue 2: Redundant conditional logic
    result = []
    if user_type == "admin":
        result.append("Access Granted")
    if user_type != "admin":
        result.append("Access Denied")
        
    return result

def test_process_data():
    # Simple test to ensure the sandbox has something to run
    assert process_data([{"active": True}], "admin") == ["Access Granted"]
    assert process_data([{"active": True}], "user") == ["Access Denied"]

2. How to Run Your First End-to-End Test
Now that you have the full stack, here is the sequence to verify everything is working:
 * Set your API Key:
   export OPENAI_API_KEY='your-key-here'
 * Run the Orchestrator:
   python main.py --file tests/test_subject.py

 * Observe the Pipeline:
   * AST will flag the if/if/for/if nesting.
   * LLM will suggest "Guard Clauses" to flatten the code.
   * Sandbox will run test_process_data() to make sure the "Access Granted" logic still works.
   * Diff Tool will generate the refactor_report.md.
3. Verification Diagram
