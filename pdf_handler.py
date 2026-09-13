from pypdf import PdfReader
from pathlib import Path

def extract_text_from_pdf(uploaded_file):

    try:

        reader = PdfReader(uploaded_file)                                              #reading pages in a file


    except FileNotFoundError:

        print("File doesn't exist.")
        return None
    
    else:
        extracted_text = ""                                                            #empty string for extracting whole file

        for page in reader.pages:                                                      #looping through each pages
            page_text = page.extract_text(extraction_mode="layout")                    #extracting each page

            if page_text:
                extracted_text += page_text + "\n"

        if extracted_text.strip() == "":
            return None
        
        filename = Path(uploaded_file.filename).stem                                    #stem = remove extension

        text_directory = Path("extracted_text")

        text_directory.mkdir(exist_ok=True)

        text_file = text_directory/f"{filename}.txt"                                    #extracted_text = pointing to that location, / = join these path components

        text_file.write_text(extracted_text,encoding="utf-8")                           #text_file = path object
        
    return extracted_text, str(text_file)                                               #returning extracted text