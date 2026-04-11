from pandas import read_csv, read_excel

def load_file(file_path: str):
    try:
        if file_path.endswith(".csv"):
            try:
                df = read_csv(file_path, encoding = "utf-8")
            except:
                df = read_csv(file_path, encoding = "latin-1")
        elif file_path.endswith(".xlsx"):
            df = read_excel(file_path, engine = "openpyxl")
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
    
#nombre de valeur manquant
def missing_values(df):
    return df.isnull().sum().to_dict()
    
def clean_data(df):
    df = df.drop_duplicates()

    #remplir valeurs nulles numériques avec moyenne
    for col in df.select_dtypes(include = ['float64', 'int64']).columns:
        df[col].fillna(df[col].mean())

    #remplir texte avec "Unknown"
    for col in df.select_dtypes(include = ['object']).columns:
        df[col].fillna("Unknown")

    return df

#choix graphique
def suggest_graphs(df):
    graphs = []

    for col in df.columns:
        if df[col].dtype in ["nt64", "float64"]:
            graphs.append({
                "type": "histogram",
                "column": col
            })
        elif df[col].dtype == "object":
            graphs.append({
                "type": "bar",
                "column": col
            })
    
    return graphs