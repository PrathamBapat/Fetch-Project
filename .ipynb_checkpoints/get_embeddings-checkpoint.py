from global_imports import *

# Create a function to get embeddings
def get_embeddings(text):
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    embeddings = outputs.pooler_output.detach().numpy()  # use pooler_output as sentence embedding
    return embeddings