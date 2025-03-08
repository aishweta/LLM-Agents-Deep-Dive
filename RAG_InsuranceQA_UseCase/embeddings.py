import pandas as pd
from sentence_transformers import SentenceTransformer

# Load BGE embedding model
model = SentenceTransformer("BAAI/bge-base-en")  # Change to "BAAI/bge-large-en" for better performance

# Generate sentence embeddings
def sentence_embedding(text):
    return model.encode(text, convert_to_numpy=True)

def main(input_path):
    df = pd.read_csv(input_path)
    df['Chunk_embeddings'] = df['Chunk'].apply(sentence_embedding)
    output_filepath = "Embeddings.csv"
    df.to_csv(output_filepath, index=False)
    return output_filepath
