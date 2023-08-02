from global_imports import *

from annoy_index import create_annoy_index
from brand_category_dict import create_brand_category_dict
from finaldata_cleaner import clean_and_prepare_dataframe
from get_embeddings import get_embeddings
from similar_category_finder import SimilarCategoryFinder
from unique_category import get_unique_categories


print('1 - Load the Data')
# Load the Data
brand_category = pd.read_csv('Data/brand_category.csv')
categories = pd.read_csv('Data/categories.csv')
offer_retailer = pd.read_csv('Data/offer_retailer.csv')


print('2 - Get Unique Categories')
# Get unique categories
unique_categories_df = get_unique_categories(brand_category, 'BRAND_BELONGS_TO_CATEGORY')


print('3 - Create Annoy Index Embeddings for Categories')
# Create annoy index for unique categories
create_annoy_index(unique_categories_df, 'Category', get_embeddings, 'Annoy_Files/', 'category.ann')


print('4 - Create Brand - Category Dict')
# Create brand - Category dictionary
brand_dc = create_brand_category_dict(brand_category, 'BRAND', 'BRAND_BELONGS_TO_CATEGORY')


print('5 - Add relevant category to the offer retailor table')
# Add relevent category and its's parent to the offer table
finder = SimilarCategoryFinder('Annoy_Files/category.ann', unique_categories_df , get_embeddings, brand_dc)
finder.update_dataframe(offer_retailer, 'updated_offer_retailer.csv')


print('6 - Final data processing')
# Data cleaning the final offer table
df_cleaned = clean_and_prepare_dataframe('updated_offer_retailer.csv', brand_category, categories)

print('7 - Create Annoy index embedding for the combined text')
# Create annoy index for combined text
create_annoy_index(df_cleaned, 'combined', get_embeddings, 'Annoy_Files/', 'Final.ann')

print('DONE!')