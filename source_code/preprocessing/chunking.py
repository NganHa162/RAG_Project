from llama_index.core import SimpleDirectoryReader
from llama_index.packs.node_parser_semantic_chunking.base import SemanticChunker
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.openai import OpenAIEmbedding
import openai


def semantic_chunking(input_txt_file):
    openai.api_key = " "
    documents = SimpleDirectoryReader(input_files=input_txt_file).load_data()
    embed_model = OpenAIEmbedding()
    splitter = SemanticChunker(
        buffer_size=1, breakpoint_percentile_threshold=95, embed_model=embed_model
    )

    # also baseline splitter
    base_splitter = SentenceSplitter(chunk_size=512)
    nodes = splitter.get_nodes_from_documents(documents)
    return nodes