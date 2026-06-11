import sys
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).parent / "src"))

from extract.extract import fetch_ebay_listing
from transform.transform import DataTransformer
from load.load import upload_file

def main():
    print("Starting ETL pipeline...")
    
    print("Extracting data from eBay API...")
    raw_data = fetch_ebay_listing(query="chessboard")
    
    print("Transforming data...")
    transformer = DataTransformer(raw_data)
    df = transformer.transform()
    print(f"Transformed {len(df)} items")
    print(df)
    
    raw_dir = Path(__file__).parent / "raw"
    raw_dir.mkdir(exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    parquet_filename = f"ebay_chessboard_{timestamp}.parquet"
    parquet_path = raw_dir / parquet_filename
    
    print(f"Saving to parquet: {parquet_path}")
    df.to_parquet(path=str(parquet_path))
    print(f"Successfully saved parquet file")
    
    print(f"Uploading to B2 bucket...")
    object_key = parquet_filename
    upload_file(str(parquet_path), object_key, content_type="application/octet-stream")
    print("ETL pipeline completed successfully!")

if __name__ == "__main__":
    main()
