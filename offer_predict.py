import streamlit as st
from global_imports import *
from get_embeddings import get_embeddings
from annoy import AnnoyIndex
import pandas as pd

def find_offers(user_input):
    # Generate BERT embedding for user input
    user_input_embedding = get_embeddings(user_input)[0]

    ### OFFER FILE
    # Path where your file is saved
    file_path = 'Annoy_Files/Final.ann'

    f = 768  # This depends on the dimension of your embeddings, for bert-base-uncased it's 768
    t = AnnoyIndex(f, 'angular')
    t.load(file_path)  # Load the Annoy index

    # Get the most similar item in the Annoy index
    index_of_most_similar, distances = t.get_nns_by_vector(user_input_embedding, 10, include_distances=True)

    # Retrieve the offer from the DataFrame using the index
    most_similar_offers = offer_retailer_latest['OFFER'].iloc[index_of_most_similar]

    data = {'Offer': most_similar_offers, 'Similarity Score': distances}
    df = pd.DataFrame(data)

    return df.reset_index(drop=True)

# Load the Data
offer_retailer_latest = pd.read_csv('Updated_Files/updated_offer_retailer.csv')

# Main
st.title('Offers Recommender')

user_input = st.text_input("Please input your query here:", '')
if user_input:
    st.write("Query:", user_input)
    result_df = find_offers(user_input)
    st.write("Results:")
    st.dataframe(result_df)
