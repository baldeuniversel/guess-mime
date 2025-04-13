# guess-mime

`guess-mime` is a Python project that detects the MIME type of a file. It utilizes both the `python-magic` library for more accurate 
detection and the built-in `mimetypes` module as a fallback.

## Features
- Detects MIME type of a given file.
- Uses `python-magic` for reliable MIME type detection.
- Falls back to `mimetypes` if `python-magic` fails.
- Provides a simple command-line interface (CLI).

## Installation

### Install dependencies
To install all required dependencies, create a virtual environment and use the following command (once in the **guess-mime** directory) :
```bash
pip install -r requirements.txt 
```

### Install program
To install the program after cloning the repo `https://github.com/baldeuniversel/guess-mime.git`, execute 
this command (be sure to specify the **correct path** ~ once in the **guess-mime** directory) : 
```bash
pip install dist/guess_mime-1.0.0-py3-none-any.whl
```

## About the Author

**Amadou Baldé**  
*Developer/Programmer ... | Open Source Contributor*

### Connect with Me:
- [GitHub](https://github.com/baldeuniversel)  
- [Email](mailto:baldeuniversel@protonmail.com)

Feel free to reach out if you'd like to collaborate on a project or discuss Python development !

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit) file for details.
