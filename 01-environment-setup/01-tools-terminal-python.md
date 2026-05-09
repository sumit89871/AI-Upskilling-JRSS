# Tools, Terminal, Python, and VS Code

## 1. What It Is

This topic explains the basic tools used in the course:

- Python: programming language
- VS Code: code editor
- terminal: place where commands are typed
- PowerShell: default Windows terminal shell
- Command Prompt: older Windows shell
- bash: common Linux/macOS shell

## 2. Why It Matters

AI engineering work is not only writing code. You also run commands to install libraries, start servers, test APIs, use Git, build Docker images, and deploy Kubernetes YAML.

## 3. How It Works

You write code in VS Code and run commands in a terminal.

The terminal always has a current folder. Commands usually run relative to that folder.

Check current folder:

```powershell
Get-Location
```

Command breakdown:

- `Get-Location` is a PowerShell command.
- It prints the folder where the terminal is currently working.

List files:

```powershell
Get-ChildItem
```

Command breakdown:

- `Get-ChildItem` lists files and folders in the current location.
- It is similar to `dir` in Command Prompt and `ls` in bash.

## 4. How I Use It

Before running project commands, check location:

```powershell
Get-Location
Get-ChildItem
```

If you are not inside the project folder, move into it:

```powershell
cd ai-engineer-jrss-reskilling-course
```

Command breakdown:

- `cd` means change directory.
- `ai-engineer-jrss-reskilling-course` is the folder name to enter.

## 5. Syntax Breakdown

### Paths In Windows

Windows paths usually use backslashes:

```text
C:\Users\Sumit\Desktop\project
```

PowerShell also accepts many forward-slash paths, but Windows examples in this course use backslashes when appropriate.

### Relative Path

```text
.\.venv\Scripts\Activate.ps1
```

- `.` means current folder.
- `\` separates folders on Windows.
- `.venv` is a hidden-style project environment folder.
- `Scripts` contains activation scripts on Windows.
- `Activate.ps1` is the PowerShell activation script.

## 6. Small Examples

Create and run a Python file.

File name: `practice/hello_setup.py`

Where to create it: inside `01-environment-setup/practice/`

```python
print("Environment setup is working")
```

Important line:

- `print(...)` displays text in the terminal.
- The text inside quotes is a string.

Run it from the module folder:

```powershell
python .\practice\hello_setup.py
```

Command breakdown:

- `python` runs Python.
- `.\practice\hello_setup.py` points to the file inside the `practice` folder.

## 7. Expected Output

```text
Environment setup is working
```

## 8. Quick Practice

- Open PowerShell.
- Print your current location.
- List files.
- Create a folder named `sandbox`.
- Move into `sandbox`.
- Move back to the previous folder.

Useful commands:

```powershell
mkdir sandbox
cd sandbox
cd ..
```

- `mkdir sandbox` creates a folder.
- `cd sandbox` enters it.
- `cd ..` moves one folder up.

Expected output:

- `mkdir sandbox` usually prints no output if the folder is created.
- `cd sandbox` usually prints no output, but your terminal location changes.
- `cd ..` usually prints no output, but your terminal moves back to the parent folder.

How to verify:

```powershell
Get-Location
Get-ChildItem
```

- `Get-Location` confirms your current folder.
- `Get-ChildItem` confirms whether `sandbox` exists.

Expected output:

- `Get-Location` prints the folder path where your terminal currently is.
- `Get-ChildItem` prints a list of files/folders. You should see `sandbox` when you are in its parent folder.

Common error:

```text
Cannot find path
```

This usually means the folder name was typed incorrectly or you are in the wrong parent folder.

## 9. Common Mistakes

- Running commands from the wrong folder.
- Typing Linux commands in PowerShell without knowing the equivalent.
- Opening VS Code but using a different terminal folder.
- Installing Python but not selecting "Add Python to PATH" during installation.

## 10. Where Used In AI Engineer Work

Terminal commands appear when you:

- install FastAPI
- run `uvicorn`
- run tests with `pytest`
- start Streamlit
- run Docker commands
- use `kubectl`
- run MCP servers

## 11. Beginner Deep Dive

The terminal is not a separate programming language. It is a place where you give instructions to your operating system.

Beginner mental model:

```text
terminal current folder -> command runs there -> files/processes change there
```

Before running any command, ask:

- What folder am I in?
- What file or folder will this command affect?
- What output should I expect?
- How can I verify it worked?

PowerShell vs Command Prompt vs bash:

- PowerShell is common on modern Windows.
- Command Prompt is older Windows shell.
- bash is common on Linux/macOS and Git Bash.

The same goal may use different commands in different shells. For example, PowerShell uses `Get-ChildItem`, while bash commonly uses `ls`.

Common beginner confusion:

- VS Code being open does not guarantee the terminal is in the correct folder.
- A command may succeed but create files in the wrong folder.
- `.` means current folder.
- `..` means parent folder.

Where this appears in AI Engineer work:

- running Python scripts
- activating virtual environments
- starting FastAPI with Uvicorn
- running Streamlit
- executing Git, Docker, and Kubernetes commands
