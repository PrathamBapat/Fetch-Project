from global_imports import *

##### CREATE BRAND-CATEGORY DICT
  
def create_brand_category_dict(df, brand_col, category_col):
    grouped = df.groupby(brand_col)[category_col].apply(list)

    # Convert the grouped Series object to a dictionary
    brand_dc = grouped.to_dict()
    
    return brand_dc