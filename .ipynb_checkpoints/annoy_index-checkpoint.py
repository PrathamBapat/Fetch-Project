from global_imports import *

###### ANNOY INDEX

def create_annoy_index(dataframe, column_name, get_embeddings, folder_path, file_name):
    embeddings = []
    for index, row in dataframe.iterrows():
        text = row[column_name]
        embedding = get_embeddings(text)
        embeddings.append(embedding[0])

    # Annoy index
    f = 768  # Length of item vector that will be indexed
    t = AnnoyIndex(f, 'angular')  # Length of item vector that will be indexed and angular for cosine similarity

    # Adding vectors to Annoy index
    for i, emb in enumerate(embeddings):
        t.add_item(i, emb)

    t.build(10)  # 10 trees
    t.save(file_name)

    # The source file path
    source_file_path = file_name  # assuming the file 'a.nn' is in the current working directory

    # Destination file path
    destination_file_path = os.path.join(folder_path, file_name)

    # Copy the file
    shutil.copy2(source_file_path, destination_file_path)
    
    #Delete the file from the main directory
    os.remove(file_name)
