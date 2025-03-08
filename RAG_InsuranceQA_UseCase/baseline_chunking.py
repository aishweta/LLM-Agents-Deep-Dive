import os
import pandas as pd 
import uuid

def create_chunk_id(file_name):
    # Generate a UUID
    unique_id = uuid.uuid4().hex[:5]
    # Extract file name without extension
    base_name = os.path.splitext(os.path.basename(file_name))[0]
    # Concatenate file name and UUID
    chunk_id = f"{base_name}_{unique_id}"
    return chunk_id

# Function to perform operations on each file
def process_file(file_path, filename):
    with open(file_path, 'r', encoding='utf-8') as input_file:
        # Read the content of the input file
        content = input_file.read()
        # Split the content into paragraphs using newline characters
        paragraphs = content.split('\n')
        
        chunks = []
        chunk_ids = []
        chunk_dataframe = pd.DataFrame()
        for i, paragraph in enumerate(paragraphs, start=1):
            # Remove leading and trailing whitespace
            paragraph = paragraph.strip()
            chunks.append(paragraph)
            chunk_id = create_chunk_id(filename)
            chunk_ids.append(chunk_id)
            # Skip empty paragraphs
            if not paragraph:
                continue
            
        # Append the paragraph as a chunk  
        chunk_dataframe['Chunk_id'] = chunk_ids
        chunk_dataframe['Chunk'] = chunks
        chunk_dataframe['File'] = filename
              
    return chunk_dataframe    

# function to create .csv file containg filename, chunk_id and chunk
def final_df(directory):
    # list to store dataframe of individual files
    lst_temp_df = []
    # Iterate through each file in the directory
    for filename in os.listdir(directory):   
        if filename.endswith(".txt"):
            filename = filename
            temp_df = pd.DataFrame()
            file_path = os.path.join(directory, filename)
            temp_df = process_file(file_path,filename)
            lst_temp_df.append(temp_df)
    
    final_df = pd.concat(lst_temp_df, ignore_index=True)
    final_df.to_csv("final_version.csv", index=False)
    print(" Final chunking file stored in a local directory named as final_version.csv ")
    
    return final_df
