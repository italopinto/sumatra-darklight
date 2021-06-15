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

### Installing

A step by step series of examples that tell you how to get a development env running

Install Python 3.x with pip

Make a venv with
```
python -m venv venv
```

To activate the venv
```
venv/Scripts/activate
```

With venv activated install PyInstaller, to generate .exe file (for Windows)

```
pip install pyinstaller
```


## Running the tests

To run a test, call the script inside a folder with photos.

```
python sumatra-darklight.py
```

**For Windows in Context Menu:**

1. To generate *sumatra-darklight.exe* file to run on Windows.

```
pyinstaller -w -F sumatra-darklight.py
```

2. Add the keys on Registry or run *sumatra-darklight.reg*.
3. Copy .exe file on *C:\Program Files\Sumatra Darklight*
4. Add *C:\Program Files\Sumatra Darklight* in the *Path* on Windows Environment Variable.

## Contributing

Feel free to submitting pull requests to us.