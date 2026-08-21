# 1. Python Installation
'''
Python needs to be installed on your computer before you can write and execute Python programs.

Python is available for major operating systems:
    - Windows
    - macOS
    - Linux

After installation, you should verify that Python is working correctly from the terminal.

On Windows, you can install Python from the official Python website: [python.org](https://www.python.org/?utm_source=chatgpt.com)

During Windows installation, make sure to enable:

```
Add python.exe to PATH
```

This allows you to run Python commands directly from the terminal.
'''

# 2. Python Executable

'''
The Python executable is the program that runs Python code.

On Windows, it is commonly:
```
python.exe
```

On Linux and macOS, it is commonly:
```
python3
```

For example:
```
python hello.py
```

The `python` command tells the operating system to find the Python executable and use it to run your program.

You can find which Python executable is being used with:
Windows:
```
where python
```

Linux/macOS:

```
which python3
```
'''

# 3. PATH

'''
PATH is an environment variable that contains a list of directories where the operating system looks for executable programs.

For example, when you type:
```
python --version
```

your operating system searches the directories listed in `PATH` to find the Python executable.

If Python is correctly added to PATH, you can run:
```
python
```

from any directory.

If Python is not in PATH, you may get an error such as:
```text
'python' is not recognized as an internal or external command
```

On Windows, you can add Python to PATH during installation by selecting:
```text
Add python.exe to PATH
```
'''

# 4. Python Terminal

'''
The Python terminal allows you to interact with Python directly without creating a `.py` file.

Open your terminal and run:
```bash
python
```

You may see:
```text
Python 3.x.x
>>>
```
The `>>>` symbol is the Python prompt.

Now you can execute Python code directly:
```python
>>> print("Hello, Python!")
Hello, Python!
```

You can also perform calculations:
```python
>>> 10 + 20
30
```

To exit the Python terminal:
```python
>>> exit()
```

You can also use:
```text
Ctrl + Z
```

on Windows, followed by Enter, or:
```text
Ctrl + D
```
on Linux/macOS.
'''

# 5. `python --version`

'''
The `python --version` command displays the installed Python version.

```bash
python --version
```

Example:
```text
Python 3.14.0
```

This is useful for checking whether Python is installed and which version is currently being used.

You can also use:
```bash
python -V
```
`-V` is a shorter form of `--version`.

On systems where Python is invoked as `python3`:
```bash
python3 --version
```
'''

# 6. `pip --version`

'''
pip is Python's package installer.
It is used to install and manage third-party Python packages.

For example:
```bash
python -m pip install package_name (python -m pip install requests)
```

To check the installed pip version:

```bash
pip --version
```

Example output:
```text
pip 25.x.x from C:\Python\Lib\site-packages\pip
```

This confirms that pip is installed and shows its location.
You can also use:
```bash
python -m pip --version
```

Using `python -m pip` is often a good practice because it explicitly runs pip through the Python interpreter you specified.

# Quick Verification
After installing Python, you can verify your setup with:
```bash
python --version
pip --version
```

Then test Python:
```bash
python
```

And run:
```python
print("Python is working!")
```

If all of these work correctly, your basic Python environment is ready for development.
'''