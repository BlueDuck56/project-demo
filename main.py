import extract
import transform

def main():
    raw_data = extract.fetch_ebay_listing(query="chessboard")
    
    transformer = transform.DataTransformer(raw_data)
    transformed_data = transformer.transform()
    print(transformed_data)
if __name__ == "__main__":
    main()
