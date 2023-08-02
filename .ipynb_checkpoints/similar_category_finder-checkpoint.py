from global_imports import *

###### ADD MOST SIMILAR CATEGORY BASED ON OFFER/BRAND

class SimilarCategoryFinder:
    def __init__(self, index_file_path, unique_category, get_embeddings_func, brand_category_dict):
        self.f = 768
        self.category_annoy_index = AnnoyIndex(self.f, 'angular')
        self.category_annoy_index.load(index_file_path)
        self.unique_category = unique_category
        self.get_embeddings = get_embeddings_func
        self.brand_category_dict = brand_category_dict

    def get_index_from_category(self, category):
        return self.unique_category[self.unique_category['Category'] == category].index[0]

    def get_most_similar_category(self, offer_embedding, brand):
        # Retrieve the category indices for the brand from the brand-category dictionary
        category_indices_for_brand = self.brand_category_dict.get(brand, [])

        # If there are no category indices for the brand, return None
        if not category_indices_for_brand:
            return None

        # Initialize most similar category and highest similarity score
        most_similar_category = None
        highest_similarity_score = -1

        # Iterate over each category index for the brand
        for category_name in category_indices_for_brand:
            # Retrieve the category embedding from the category Annoy index
            category_index = self.get_index_from_category(category_name)
            category_embedding = self.category_annoy_index.get_item_vector(category_index)

            # Calculate the cosine similarity between the offer and category embeddings
            similarity_score = np.dot(offer_embedding, category_embedding) / (np.linalg.norm(offer_embedding) *             np.linalg.norm(category_embedding))

            # If this score is higher than the current highest, update most similar category and highest score
            if similarity_score > highest_similarity_score:
                most_similar_category = category_index
                highest_similarity_score = similarity_score

        return self.unique_category.loc[most_similar_category, 'Category']

    def apply_func(self, row):
        # Retrieve the brand from the row
        brand = row['BRAND']

        if brand not in self.brand_category_dict:
            return None

        # Retrieve the BERT embedding for the offer
        offer_embedding = self.get_embeddings(row['OFFER'])[0]  # Adjust this function call to suit your implementation

        # Get the most similar category
        most_similar_category = self.get_most_similar_category(offer_embedding, brand)

        return most_similar_category

    def update_dataframe(self, df, output_file):
        df['MOST_SIMILAR_CATEGORY'] = df.apply(self.apply_func, axis=1)
        df.to_csv(os.path.join("Updated_Files/", output_file), index=False, mode='w')
        



