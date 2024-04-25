# PDF to Speech Converter

This Python script converts text from a PDF file into speech and saves it as an MP3 file.

## Requirements

- Python 3.x
- PyPDF2 library (`pip install PyPDF2`)
- pyttsx3 library (`pip install pyttsx3`)

## Usage

1. Clone this repository or download the `pdf_to_speech.py` script.
2. Install the required libraries using pip:
   `pip install -r requirements.txt`
3. Run the script:
   `python pdf_to_speech.py [file_path]`

Replace `[file_path]` with the path to the PDF file you want to convert. If no file path is provided, the script will prompt you to enter one.
4. The script will convert the text from each page of the PDF file into speech and save it as an MP3 file named after the input PDF file.

## Example

python pdf_to_speech.py my_document.pdf

This will convert the text from `my_document.pdf` into speech and save it as `my_document.mp3`.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
