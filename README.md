# Python Sumatra Darklight

For those who uses [SumatraPDF](https://www.sumatrapdfreader.org/free-pdf-reader) and feels annoying with it rough way to switch from light to dark mode and vice-versa. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
**This project was made to  Windows only!!**

What things you need to install the software and how to install them

```
Python 3.x
```
### Getting the code

Clone this repository or download the zip file by clicking the green button on the top right. 

### Installing

A step by step series of examples that tell you how to get a development env running

First of all, move inside the directory where the code is.

Make a venv with:
```
python -m venv venv
```

To activate the venv:
```
venv/Scripts/activate
```

With venv activated install PyInstaller, to generate .exe file (for Windows):

```
pip install pyinstaller
```

## Running the tests

To run a test, call the script inside a folder with photos:

```
python sumatra-darklight.py
```

## For Windows in Context Menu:

1. Change the value of the variable below in *sumatra-darklight.py*:
```
SUMATRA_SETTINGS_PATH = r'C:\Users\<your_user>\path\to\SumatraPDF\SumatraPDF-settings.txt'
```

2. Then to generate *sumatra-darklight.exe* file to run on Windows:

```
pyinstaller -w -F sumatra-darklight.py
```

3. Add the keys on Registry or run *sumatra-darklight.reg*.
4. Copy *.exe* file and the *.ico* image on *C:\Program Files\Sumatra Darklight*
5. Add *C:\Program Files\Sumatra Darklight* in the *Path* on Windows Environment Variable.

## Contributing

Feel free to submitting pull requests to us.