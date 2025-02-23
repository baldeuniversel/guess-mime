import pytest
from guess_mime.guess_mime import GuessMime
import os





# Set paths to test files
TXT_FILE = os.path.join(os.path.dirname(__file__), "../assets/media/txt/txt_test.txt")
IMG_JPG_FILE = os.path.join(os.path.dirname(__file__), "../assets/media/images/image_test.jpg")
IMG_PNG_FILE = os.path.join(os.path.dirname(__file__), "../assets/media/images/image_test.png")
PDF_FILE = os.path.join(os.path.dirname(__file__), "../assets/media/pdf/pdf_test.pdf")
VIDEO_FILE = os.path.join(os.path.dirname(__file__), "../assets/media/videos/video_test.mp4")

# Initialize GuessMime class
guesser = GuessMime()





"""
Test the detection of MIME type for a text file.

This test checks that the correct MIME type is detected for a file
with a .txt extension. The expected MIME type is 'text/plain'.
The test ensures that the file is found and the MIME type is correctly
returned as 'text/plain'.
"""
def test_mime_txt_file():

    mime, found = guesser.guess_mime(TXT_FILE)
    assert mime == "text/plain", f"Expected 'text/plain' but got {mime}"
    assert found is True, "MIME type should be found"



"""
Test the detection of MIME type for a JPEG image.

This test checks that the correct MIME type is detected for a file
with a .jpg extension. The expected MIME type is 'image/jpeg'.
The test ensures that the file is found and the MIME type is correctly
returned as 'image/jpeg'.
"""
def test_mime_jpg_file():
 
    mime, found = guesser.guess_mime(IMG_JPG_FILE)
    assert mime == "image/jpeg", f"Expected 'image/jpeg' but got {mime}"
    assert found is True, "MIME type should be found"



"""
Test the detection of MIME type for a PNG image.

This test checks that the correct MIME type is detected for a file
with a .png extension. The expected MIME type is 'image/png'.
The test ensures that the file is found and the MIME type is correctly
returned as 'image/png'.
"""
def test_mime_png_file():

    mime, found = guesser.guess_mime(IMG_PNG_FILE)
    assert mime == "image/png", f"Expected 'image/png' but got {mime}"
    assert found is True, "MIME type should be found"



"""
Test the detection of MIME type for a PDF file.

This test checks that the correct MIME type is detected for a file
with a .pdf extension. The expected MIME type is 'application/pdf'.
The test ensures that the file is found and the MIME type is correctly
returned as 'application/pdf'.
"""
def test_mime_pdf_file():

    mime, found = guesser.guess_mime(PDF_FILE)
    assert mime == "application/pdf", f"Expected 'application/pdf' but got {mime}"
    assert found is True, "MIME type should be found"



"""
Test the detection of MIME type for a video file.

This test checks that the correct MIME type is detected for a file
with a .mp4 extension. The expected MIME type is 'video/mp4'.
The test ensures that the file is found and the MIME type is correctly
returned as 'video/mp4'.
"""
def test_mime_video_file():

    mime, found = guesser.guess_mime(VIDEO_FILE)
    assert mime == "video/mp4", f"Expected 'video/mp4' but got {mime}"
    assert found is True, "MIME type should be found"



"""
Test the detection of MIME type for a non-existent file.

This test checks that when an invalid or non-existent file is passed
to the guess_mime function, the MIME type returned should be 'unknown/unknown'.
The test ensures that the function behaves correctly in case of an invalid file path.
"""
def test_mime_unknown_file():
    
    unknown_file = "assets/media/unknown_file.txt"
    mime, found = guesser.guess_mime(unknown_file)
    assert mime == "unknown/unknown", f"Expected 'unknown/unknown' but got {mime}"
    assert found is False, "MIME type should not be found"
