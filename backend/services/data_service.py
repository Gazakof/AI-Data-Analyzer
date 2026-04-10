import pandas as pd

def load_file(file_path: str):
    try:
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        elif file_path.endswith(".xlsx"):
            df = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format")
        
        return df
    
    except Exception as e:
        raise Exception(f"Error reading file: {str(e)}")
    
def basic_analysis(df):
    return {
        "num_rows": df.shape[0],
        "num_columns": df.shape[1],
        "columns": list(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict()
    }