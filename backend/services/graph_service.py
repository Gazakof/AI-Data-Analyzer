import matplotlib.pyplot as plt
import os

UPLOAD_DIR = "uploads"

def generate_graph(df, graph_type, column):
    file_path = f"{UPLOAD_DIR}/{column}_{graph_type}.png"

    plt.figure()

    if graph_type == "histogram":
        df[column].dropna().hist()
    elif graph_type == "bar":
        df[column].value_counts().plot(kind = "bar")

    plt.title(f"{graph_type} of {column}")
    plt.tight_layout()

    plt.savefig(file_path)
    plt.close()

    return file_path