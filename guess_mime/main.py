"""
@overview A main file
"""

import sys
import argparse
from .guess_mime import GuessMime





def main():
    """
    The main entry point for the command-line interface (CLI) of the guess-mime tool.

    This function sets up the argument parser to accept a file path as input. It is required 
    to provide **only one file path at a time** for analysis. The program initializes a 
    `GuessMime` object with the provided file path, and outputs the MIME type of the file. 
    It provides feedback to the user regarding whether the MIME type was successfully found 
    (based on the detection method's reliability).

    The result is printed in the format (not exactly, but the pattern will be of this nature):
        MIME: <mime_type> | Confidence: Yes/No

    **Usage:**
    1. Provide **exactly one file path** to analyze. For example:
        `guess-mime <file_path>`
    2. Use `-h` or `--help` to get more information about usage.

    :note: Only **one file path** can be provided at a time.
    """

    # Check if there are no argument (just the program name)
    if len(sys.argv) == 1:

        print("\U0001F6AB Error: You have to provide a file as an argument \U0001F9D0", flush=True)
        sys.exit(1)  # Exit the program with an error code

    # Check if there are more than 2 arguments (program name + 1 file)
    if len(sys.argv) != 2:

        print("\U000026D4 Error: Only one file path is allowed at a time.", flush=True)
        print("Please provide a single file path.", flush=True)
        
        sys.exit(1)  # Exit the program with an error code


    # Initialize argument parser with description of usage
    parser = argparse.ArgumentParser(
        description="Detect the MIME type of a file. Provide exactly one file path as input."
    )

    # Define the 'file' argument, which is the path to the file to analyze
    parser.add_argument(
        "file", 
        help="The path of the file to analyze. Only one file path is accepted at a time."
    )

    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Create an instance of the GuessMime class using the provided file path
    guess_mime_instance = GuessMime(args.file)
    
    # Call the guess_mime method to determine the MIME type and confidence
    mime, found = guess_mime_instance.guess_mime()
    
    # Output the result to the user, indicating the MIME type and whether it was found with confidence
    print(f"\U0001F389 MIME Type: {mime} | Confidence: {'YES' if found else 'NO'} {'\U00002705' if found else '\U0000274C'}", flush=True)



if __name__ == "__main__":
    main()
