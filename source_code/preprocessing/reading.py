import PyPDF2
import os

def extract_text_from_pdf(pdf_path):
    # Mở tệp PDF và trích xuất văn bản
    with open(pdf_path, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def save_to_txt(text, output_file):
    # Ghi văn bản vào tệp .txt
    with open(output_file, 'a') as f:  # 'a' mode để thêm vào tệp đã có
        f.write(text + '\n')
        
        