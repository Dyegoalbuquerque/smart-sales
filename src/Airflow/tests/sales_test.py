import pytest
import pandas as pd
from unittest.mock import patch
from scripts import sales_etl

# DataFrame fake para mockar extract_data
fake_df = pd.DataFrame({
    "Item_Identifier": ["FDT36", "FDT36"],
    "Item_Weight": [12.3, 12.3],
    "Item_Fat_Content": ["LF", "Low Fat"],
    "Item_Visibility": [0.111447593, 0.111904005],
    "Item_Type": ["Baking Goods", "Baking Goods"],
    "Item_MRP": [33.4874, 33.9874],
    "Outlet_Identifier": ["OUT049", "OUT017"],
    "Outlet_Establishment_Year": [1999, 2007],
    "Outlet_Size": ["Medium", "Medium"],
    "Outlet_Location_Type": ["Tier 1", "Tier 2"],
    "Outlet_Type": ["Supermarket Type1", "Supermarket Type1"],
    "Item_Outlet_Sales": [436.6087212, 443.1277212]
})

@patch('scripts.sales_etl.extract_data', return_value=fake_df)
def test_extract_data(mock_extract):
    df = sales_etl.extract_data()
    assert not df.empty
    expected_columns = [
        "Item_Identifier", "Item_Weight", "Item_Fat_Content", "Item_Visibility",
        "Item_Type", "Item_MRP", "Outlet_Identifier", "Outlet_Establishment_Year",
        "Outlet_Size", "Outlet_Location_Type", "Outlet_Type", "Item_Outlet_Sales"
    ]
    for col in expected_columns:
        assert col in df.columns

@patch('scripts.sales_etl.extract_data', return_value=fake_df)
def test_transform_data(mock_extract):
    raw_df = sales_etl.extract_data()
    clean_df = sales_etl.transform_data(raw_df)
    
    # Sem valores nulos
    assert clean_df.isnull().sum().sum() == 0

    # Tipos numéricos
    assert pd.api.types.is_numeric_dtype(clean_df["Item_Weight"])
    assert pd.api.types.is_numeric_dtype(clean_df["Item_Visibility"])
    assert pd.api.types.is_numeric_dtype(clean_df["Item_MRP"])
    assert pd.api.types.is_numeric_dtype(clean_df["Outlet_Establishment_Year"])
    assert pd.api.types.is_numeric_dtype(clean_df["Item_Outlet_Sales"])

    # Padronização 'Item_Fat_Content'
    valid_fat_contents = {"Low Fat", "Regular"}
    assert set(clean_df["Item_Fat_Content"].unique()).issubset(valid_fat_contents)

@patch('scripts.sales_etl.extract_data', return_value=fake_df)
def test_load_data(mock_extract, tmp_path):
    df = sales_etl.extract_data()
    df = sales_etl.transform_data(df)
    output_file = tmp_path / "sales.parquet"
    sales_etl.load_data(df, output_file)
    assert output_file.exists()
    loaded_df = pd.read_parquet(output_file)
    assert len(loaded_df) > 0
