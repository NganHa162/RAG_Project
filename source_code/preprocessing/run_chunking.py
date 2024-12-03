from llama_index.core import SimpleDirectoryReader
from llama_index.packs.node_parser_semantic_chunking.base import SemanticChunker
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.openai import OpenAIEmbedding
import openai
import pickle
import os

openai.api_key = " "

embed_model = OpenAIEmbedding()
splitter = SemanticChunker(
    buffer_size=1, breakpoint_percentile_threshold=95, embed_model=embed_model
)

base_splitter = SentenceSplitter(chunk_size=5000, chunk_overlap=350)

txt_folder = '/mnt/disk1/HaNTN/Hydrogen_RAG/Document_txt'

def process_txt_files(txt_folder, splitter):
    # Loop through all the files in the folder
    nodes_all = []
    for filename in os.listdir(txt_folder):
        if filename.endswith('.txt'):  # Only process .txt files
            txt_path = os.path.join(txt_folder, filename)
            print(f"Processing file: {filename}")
            
            # Load data from the txt file
            documents = SimpleDirectoryReader(input_files=[txt_path]).load_data()
            base_chunks = base_splitter(documents)
            # Process the documents into nodes using the splitter
            for chunk in base_chunks:
                with open('/mnt/disk1/HaNTN/Hydrogen_RAG/code/source_code/intermediary.txt', 'w') as file:
                    file.write(chunk.text)
                
                documents = SimpleDirectoryReader(input_files=['/mnt/disk1/HaNTN/Hydrogen_RAG/code/source_code/intermediary.txt']).load_data()
                    
                nodes = splitter.get_nodes_from_documents(documents)
                nodes_all = nodes_all + nodes
                
                with open('/mnt/disk1/HaNTN/Hydrogen_RAG/code/source_code/intermediary.txt', 'w') as file:
                    file.write('')

            # You can now work with the nodes (e.g., print, save, etc.)
            print(f"Processed nodes from {filename}")
    
    return nodes_all


nodes_all = process_txt_files(txt_folder, splitter)

with open("/mnt/disk1/HaNTN/Hydrogen_RAG/code/source_code/chunkers_5000_350.pkl", 'wb') as file:
    pickle.dump(nodes_all, file, protocol=pickle.HIGHEST_PROTOCOL)
