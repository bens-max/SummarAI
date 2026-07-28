from pypdf import PdfReader

def extract_text_from_pdf(file_name):
    try:
        reader = PdfReader(file_name)                                                  #reading pages in a file
    except FileNotFoundError:
        print("File doesn't exist.")
        return None
    else:
        extracted_text = ""                                                            #empty string for extracting whole file
        for page in reader.pages:                                                      #looping through each pages
            extracted_text += page.extract_text(extraction_mode="layout") + "\n"       #extracting each page
        if extracted_text.strip() == "":
            return None
    return extracted_text                                                              #returining extracted text
