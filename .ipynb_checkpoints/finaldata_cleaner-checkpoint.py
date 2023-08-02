from global_imports import *

##### CLEAN THE FINAL DF

def clean_and_prepare_dataframe(input_file, brand_category, categories):
    # Load the DataFrame
    offer_retailer = pd.read_csv(os.path.join("Updated_Files", input_file))
    
    # Merge on brand and most similar category
    df = offer_retailer.merge(brand_category, left_on=['BRAND', 'MOST_SIMILAR_CATEGORY'], 
                              right_on=['BRAND', 'BRAND_BELONGS_TO_CATEGORY'], how='left')
    df['RECEIPTS'] = df['RECEIPTS'].where(pd.notnull(df['RECEIPTS']), None)
    
    # Further merge on most similar category
    df1 = df.merge(categories, left_on='MOST_SIMILAR_CATEGORY', right_on='PRODUCT_CATEGORY', how='left')
    df1 = df1.fillna('[UNK]')
    df1 = df1.drop(['BRAND_BELONGS_TO_CATEGORY', 'CATEGORY_ID', 'PRODUCT_CATEGORY'], axis=1)
    
    # Combine necessary fields
    df1['combined'] = df1.apply(lambda row: f"Offer: {row['OFFER']}, Retailer: {row['RETAILER']}, Brand: {row['BRAND']}, Category: {row['MOST_SIMILAR_CATEGORY']}, Parent Category: {row['IS_CHILD_CATEGORY_TO']}, Receipts: {row['RECEIPTS']}", axis=1)

    # Rearranging columns and keeping only 'OFFER' and 'combined'
    df1 = df1[['OFFER', 'combined']]
    df1.loc[:, 'combined'] = df1['combined'].str.lower()

    return df1