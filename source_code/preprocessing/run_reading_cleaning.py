import os
from pathlib import Path

from reading import extract_text_from_pdf, save_to_txt
from cleaning import text_cleaning



def process_pdfs(pdf_folder, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(pdf_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(pdf_folder, filename)
            print(f"Processing file: {filename}")
            
            # Extract and clean the text from the PDF
            text = extract_text_from_pdf(pdf_path)
            text = text_cleaning(text)
            
            # Define the output file path for the .txt file
            output_filename = Path(filename).stem + '.txt'
            output_file_path = os.path.join(output_folder, output_filename)
            
            # Save the cleaned text to the output .txt file
            save_to_txt(text, output_file_path)
            print(f"Saved to: {output_file_path}")

# Example usage
pdf_folder = '/mnt/disk1/HaNTN/Hydrogen_RAG/Document'
output_folder = '/mnt/disk1/HaNTN/Hydrogen_RAG/Document_txt'
process_pdfs(pdf_folder, output_folder)
