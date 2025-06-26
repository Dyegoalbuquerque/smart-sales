import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()



def extract_data():
    DATA_URL = os.getenv("SALES_DATA_URL")
    df = pd.read_csv(DATA_URL, encoding='utf-8')
    return df

def transform_data(df):
    # Values standards of column 'Item_Fat_Content'
    df['Item_Fat_Content'] = df['Item_Fat_Content'].replace({
        'LF': 'Low Fat',
        'low fat': 'Low Fat',
        'reg': 'Regular'
    })

    # Converts columns to appropriate types
    df['Item_Weight'] = pd.to_numeric(df['Item_Weight'], errors='coerce')
    df['Item_Visibility'] = pd.to_numeric(df['Item_Visibility'], errors='coerce')
    df['Item_MRP'] = pd.to_numeric(df['Item_MRP'], errors='coerce')
    df['Outlet_Establishment_Year'] = pd.to_numeric(df['Outlet_Establishment_Year'], errors='coerce')
    df['Item_Outlet_Sales'] = pd.to_numeric(df['Item_Outlet_Sales'], errors='coerce')

    # Remove lines with null values
    df = df.dropna()

    return df

def load_data(df, output_path="../output/sales.parquet"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_parquet(output_path, index=False)

def run_etl():
    df = extract_data()
    df = transform_data(df)
    load_data(df)

if __name__ == "__main__":
    run_etl()
