import pandas as pd
import os

def preprocess_data(input_file="Flipkart_mobile_brands_data.csv", output_file="Flipkart_mobile_brands_cleaned.csv"):
    """
    Preprocess mobile phone dataset by cleaning and transforming data.
    
    Args:
        input_file (str): Path to input CSV file
        output_file (str): Path to save cleaned CSV file
    """
    try:
        # Check if input file exists
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file not found: {input_file}")

        # Load the dataset
        df = pd.read_csv(input_file)
        print(f"Loaded {len(df)} records from dataset")

        # Data Preprocessing
        # Drop rows with missing critical values
        df_cleaned = df.dropna(subset=['Model', 'Memory', 'Storage', 'Selling Price'])
        print(f"Removed {len(df) - len(df_cleaned)} rows with missing critical values")

        # Convert Memory & Storage to numeric values
        df_cleaned['Memory'] = df_cleaned['Memory'].str.extract(r'(\d+)').fillna(0).astype(float)
        df_cleaned['Storage'] = df_cleaned['Storage'].str.extract(r'(\d+)').fillna(0).astype(float)

        

        # Fill missing colors
        df_cleaned['Color'] = df_cleaned['Color'].fillna('Unknown')

        # Remove duplicates
        initial_len = len(df_cleaned)
        df_cleaned = df_cleaned.drop_duplicates()
        print(f"Removed {initial_len - len(df_cleaned)} duplicate entries")

        # Save cleaned dataset
        df_cleaned.to_csv(output_file, index=False)
        print(f"Data preprocessing completed. Cleaned dataset saved to {output_file}")
        print(f"Final dataset contains {len(df_cleaned)} records")

    except Exception as e:
        print(f"Error during data preprocessing: {str(e)}")
        raise

if __name__ == "__main__":
    preprocess_data()