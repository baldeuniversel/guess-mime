"""
@overview The class of the `guess-mime` program
"""

from pathlib import Path
import mimetypes
import magic
from typing import Optional





class GuessMime:
    """
    A class to determine the MIME type of a file using multiple methods.

    This class attempts to determine the MIME type of a given file. It uses the
    `python-magic` library for a reliable MIME type detection based on file content.
    If that fails, it falls back to using `mimetypes` based on file extension.

    Attributes:
        file_path (str): The path of the file whose MIME type is to be determined.
        file (Path): A Path object representing the file.
    """



    def __init__(self, file_path: Optional[str] = None):
        """
        Initializes the GuessMime instance with the file path.

        :param file_path: The path of the file to analyze.

        @constructor
        """
       
        self.file_path = file_path

        # Optional[Path] means it can either be a Path or None
        self.file: Optional[Path] = Path(file_path) if file_path else None



    def guess_mime(self, file_path: Optional[str] = None) -> tuple[str, bool]:
        """
        Guesses the MIME type of the file.

        This method first tries to determine the MIME type using the `magic` library,
        which is based on the file's content. If this fails, it attempts to determine the MIME
        type based on the file extension using the `mimetypes` library.

        :param file_path: The path to the file to analyze. If None, it will use the instance's file path.
        :return: A tuple containing the MIME type and a boolean indicating if the MIME
                type was found (`True` if found, `False` if not).
        :rtype: tuple
        """

        # Use the passed file_path or the instance's file_path if no argument is provided
        file_path = file_path or self.file_path

        # Return "unknown/unknown" MIME type if no file path is provided
        if not file_path:
            return ("unknown/unknown", False)

        # Use the instance's file attribute if it exists, otherwise use the provided file_path
        file = self.file or Path(file_path)

        # Check if the file exists and is a valid file
        if not file.exists() or not file.is_file():
            return ("unknown/unknown", False)

        # Try detecting MIME type using the `magic` library (more reliable, based on content)
        try:

            mime = magic.Magic(mime=True)
            mime_type: Optional[str] = mime.from_file(str(file))  # mime_type can be Optional[str]

            #
            if mime_type:
                return (mime_type, True)
            
        except Exception:
            pass  # If `magic` fails, proceed to use `mimetypes`

        # Detect MIME type using file extension (`mimetypes`)
        mime_type, _ = mimetypes.guess_type(str(file) if file else '')   # Convert Path object to string

        # Return MIME type if found, otherwise return "unknown/unknown"
        return (mime_type if mime_type and mime_type != '' else "unknown/unknown", mime_type is not None)
