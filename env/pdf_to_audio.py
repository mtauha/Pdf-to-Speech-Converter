import subprocess as sb

try:
    # Attempt to import required modules
    import traceback
    import sys
    import os
    import re
    import pyttsx3
    import PyPDF2
except ImportError or NameError as e:
    # If import fails, extract module name from the error message
    error = traceback.format_exc()
    regex = r"import\s+[\w+]*"
    result = re.search(regex, error)
    result = result.group(0)
    module_name = result.removeprefix("import ")

    # Install the missing module using pip
    try:
        sb.run(["python", "-m", "pip", "-r", "install", "requirements.txt"])
    except ConnectionError as e:
        print(str(e))

# Get the file path from command-line arguments or user input
if len(sys.argv) > 1:
    file_path = sys.argv[1]
else:
    file_path = str(input("Enter file path: "))

# Extract the file name from the file path
pdf_file = os.path.basename(file_path)

try:
    # Check if the file exists and is not a directory
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"'{file_path}' does not exist at the path '{file_path}'"
        )
    elif os.path.isdir(file_path):
        raise IsADirectoryError(f"{pdf_file} is a directory.")
except (FileNotFoundError, IsADirectoryError) as e:
    print(str(e))

# Initialize PDF reader
pdf_reader = PyPDF2.PdfFileReader(open(file_path, "rb"))

# Initialize text-to-speech engine
speaker = pyttsx3.init()

# Iterate through each page of the PDF
for page_num in range(pdf_reader.numPages):
    # Extract text from the page
    text = pdf_reader.getPage(pageNumber=page_num).extract_text()
    # Clean up the extracted text
    clean_text = text.strip().replace("\n", " ")

# Save the cleaned text to an MP3 file
speaker.save_to_file(clean_text, f"{pdf_file}.mp3")
# Run the text-to-speech engine to convert the text to speech
speaker.runAndWait()

# Stop the text-to-speech engine
speaker.stop()
