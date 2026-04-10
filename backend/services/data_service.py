import pandas as pd

def load_file(file_path: str):
    try:
        if file_path.endswith(".csv"):
            try:
                df = pd.read_csv(file_path, encoding = "utf-8")
            except:
                df = pd.read_csv(file_path, encoding = "latin-1")
        elif file_path.endswith(".xlsx"):
            df = pd.read_excel(file_path, engine = "openpyxl")
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

def statistical_analysis(df):
    try:
        stats = df.describe().to_dict()
        return stats
    except Exception: 
        return {}
    
def clean_data(df):
    df = df.drop_duplicates()

    #remplir valeurs nulles numériques avec moyenne
    for col in df.select_dtypes(include = ['float64', 'int64']).columns:
        df[col].fillna(df[col].mean(), inplace = True)

    #remplir texte avec "Unknown"
    for col in df.select_dtypes(include = ['object']).columns:
        df[col].fillna("Unknown", inplace = True)

    return df