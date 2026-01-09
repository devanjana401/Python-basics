# The sys module gives access to system-specific parameters and functions — things like:
# ---- The Python version
# ---- Command-line arguments
# ---- System path (where Python looks for modules)
# ---- Exiting the program
# ---- Standard input/output

import sys
print(sys.version)  # shows Python version
print("Version Info:", sys.version_info)

# Get the Python Executable Path
print("Python Executable:", sys.executable)

# Exit from Python Script
import sys
print("This will print.")
sys.exit()
print("This will NOT print.")

#Get Platform Information
print("Platform:", sys.platform)

# Maximum and Minimum Integer Values
print("Max size of int:", sys.maxsize)

#Get Default Encoding
print("Default Encoding:", sys.getdefaultencoding())

#Memory and Recursion Limit
print("Recursion Limit:", sys.getrecursionlimit())


# sys.version -- Python version info
# sys.executable -- Path of Python interpreter
# sys.path -- List of module search paths
# sys.argv -- Command-line arguments
# sys.exit() -- Exit the program
# sys.platform -- Operating system name
# sys.maxsize -- Maximum int size
# sys.getdefaultencoding() -- Get encoding used
# sys.getrecursionlimit() -- Check recursion depth
# sys.stdout / sys.stderr -- Output & error streams