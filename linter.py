import subprocess
import sys

def LintCode():
    try:
        # Write to test.py
        if len(sys.argv) < 2:
            print("Error: Please provide a value to write to the file.")
            print("Usage: python write_to_file.py <value>")
            exit(1)

        value = sys.argv[1]
        filename = "test.py"

        # print(value)
        
        with open(filename, "w") as file:
            file.write(value)
        print(f"Successfully wrote to {filename}")

        result = subprocess.run(["flake8", filename], capture_output=True, text=True)
        
        response = result.stdout
        return response

    except OSError as e:
        return "Error linting python code." + e

if __name__ == "__main__":
    res = LintCode()
    # print(res)