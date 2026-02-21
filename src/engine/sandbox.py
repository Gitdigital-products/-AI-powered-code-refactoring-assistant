import subprocess
import os
import shutil
from tempfile import TemporaryDirectory

class RefactorSandbox:
    def __init__(self, project_root):
        self.project_root = project_root

    def verify_refactor(self, file_path, refactored_content):
        """
        Validates refactored code by running existing tests in a temp directory.
        """
        with TemporaryDirectory() as tmpdir:
            # 1. Copy the entire project to the sandbox
            # This ensures dependencies and local imports are available
            sandbox_path = os.path.join(tmpdir, "project")
            shutil.copytree(self.project_root, sandbox_path)

            # 2. Overwrite the specific file with the AI's refactored version
            relative_path = os.path.relpath(file_path, self.project_root)
            target_file = os.path.join(sandbox_path, relative_path)
            
            with open(target_file, "w") as f:
                f.write(refactored_content)

            # 3. Run Pytest
            print(f"🧪 Running tests in sandbox for {relative_path}...")
            try:
                result = subprocess.run(
                    ["pytest", sandbox_path],
                    capture_output=True,
                    text=True,
                    timeout=60  # Prevent infinite loops
                )
                
                if result.returncode == 0:
                    print("✅ Sandbox verification PASSED.")
                    return True, "All tests passed."
                else:
                    print("❌ Sandbox verification FAILED.")
                    return False, result.stdout
            except subprocess.TimeoutExpired:
                return False, "Tests timed out (possible infinite loop in refactor)."
            except Exception as e:
                return False, str(e)
