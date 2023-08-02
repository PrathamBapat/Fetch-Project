from global_imports import *

# GET UNIQUE CATEGORIES
def get_unique_categories(brand_category, column_name):
    unique_values = brand_category[column_name].unique()

    # Create a DataFrame from the unique values
    unique_category = pd.DataFrame(unique_values, columns=['Category'])

    unique_category.reset_index(inplace=True)

    return unique_category