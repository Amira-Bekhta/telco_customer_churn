import pandas as pd 

def load_data(dataset: str, path: str, isRoot: bool) -> pd.DataFrame:
    """
    Loads a CSV dataset from a specified path.

    Args:
    dataset (str): The name of the dataset (CSV file).
    path (str): The subdirectory where the dataset is located.
    isRoot (bool): A flag indicating whether the current directory is the root 
                   of the project (True) or not (False).

    Returns:
    pd.DataFrame: The loaded dataset as a pandas DataFrame.

    Example:
    load_data("data.csv", "raw", True)
    """
    if isRoot:
        return pd.read_csv(f"data/{path}/{dataset}")
    return pd.read_csv(f"../data/{path}/{dataset}")


def save_data(df: pd.DataFrame, name: str, isRoot: bool) -> None:
    """
    Saves a pandas DataFrame to a CSV file in the preprocessed data directory.

    Args:
    df (pd.DataFrame): The DataFrame to be saved.
    name (str): The name of the CSV file containing the dataset.
    isRoot (bool): A flag indicating whether the current directory is the root 
                   of the project (True) or not (False).

    Returns:
    None

    Example:
    save_data(df, "processed_data.csv", False)
    """
    if isRoot:
        df.to_csv("data/preprocessed/" + name, index=False)
    df.to_csv("../data/preprocessed/" + name, index=False)

    