import pandas as pd

def input_from_console():
    """
    Receives user input from the console.

    Returns:
        str: The text entered by the user.
    """
    return input("Enter text: ")

def input_from_file(filepath):
    """
    Reads the content of a text file using python's built-in capabilities.

    Parameters:
        filepath (str): Path to the file.

    Returns:
        str: The content of the file as a string.
    """
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()

def input_from_file_pandas(filepath):
    """
    Reads the content of a file using the panda's library.

    Parameters:
        filepath (str): Path to the file.

    Returns:
        pd.DataFrame: Data read from the file in a DataFrame format.
    """
    return pd.read_csv(filepath)
