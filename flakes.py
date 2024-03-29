import subprocess

def check_flake8_version():
  """
  Checks the installed Flake8 version using subprocess.run.

  Returns:
      str: The Flake8 version string or an error message if not found.
  """

  try:
    # Execute `flake8 --version` to get the version information
    result = subprocess.run(["flake8", "--version"], capture_output=True, text=True)
    # Check for successful execution
    if result.returncode == 0:
      # Extract the version string from the output (may need adjustments based on flake8 output format)
      
      version_line = result.stdout
      return version_line  # Assuming "flake8 X.Y.Z" format
    else:
      return f"Error: Flake8 execution failed (code: {result.returncode})"
  except FileNotFoundError:
    return "Flake8 not found. Please install it using 'pip install flake8'."

if __name__ == "__main__":
  version = check_flake8_version()
  print(f"Flake8 version: {version}")
