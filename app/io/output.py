def output_to_console(text):
    """
    Outputs text to the console.

    Parameters:
        text (str): The text to be displayed.
    """
    print(text)

def output_to_file(filepath, text):
    """
    Writes text to a file using python's built-in capabilities.

    Parameters:
        filepath (str): Path to the file.
        text (str): The text to be written to the file.
    """
    with open(filepath, "a", encoding="utf-8") as file:
        file.write(text + "\n")


