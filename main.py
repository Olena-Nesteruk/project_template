import os
from app.io.input import input_from_console, input_from_file, input_from_file_pandas
from app.io.output import output_to_console, output_to_file


def main():
    text_console = input_from_console()

    file_path = os.path.join("data", "input.txt")
    text_file = input_from_file(file_path)

    file_path_pandas = os.path.join("data", "input.csv")
    data_pandas = input_from_file_pandas(file_path_pandas)

    output_to_console(text_console)
    output_to_console(text_file)
    output_to_console(str(data_pandas))

    output_file_path = os.path.join("data", "output.txt")
    output_to_file(output_file_path, text_console)
    output_to_file(output_file_path, text_file)
    output_to_file(output_file_path, str(data_pandas))

if __name__ == "__main__":
    main()
