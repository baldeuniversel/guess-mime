# guess-mime
`guess-mime` is a Python project that detects the MIME type of a file. It utilizes both the `python-magic` library for more accurate 
detection and the built-in `mimetypes` module as a fallback.

---

## 📚 Summary
- [Features](#features)  
- [Installation](#installation)   
- [Use cases (after installing the program)](#use-cases-after-installing-the-program)  
- [About the Author](#about-the-author)  
- [License](#license)

---

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

## Use cases (after installing the program)
### Use Case 1 — Detect a mp4 file
```
success:
    -> action : guess-mime video_file.mp4
    -> output : 🎉 MIME Type: video/mp4 | Confidence: YES ✅

error:
    -> action : guess-mime corrupted_video_file.mp4
    -> output : 🎉 MIME Type: unknown/unknown | Confidence: NO ❌
```

### Use Case 2 — Detect a text plain file 
```
success:
    -> action : guess-mime text_file.txt
    -> output : 🎉 MIME Type: text/plain | Confidence: YES ✅

error:
    -> action : guess-mime corrupted_text_file.txt
    -> output : 🎉 MIME Type: unknown/unknown | Confidence: NO ❌
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
