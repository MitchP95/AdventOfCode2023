def read_lines_from_file(file_path):
    """
    Reads all lines from the specified file and returns them as a list of strings.

    :param file_path: Path to the file to be read.
    :return: List of strings, where each string is a line from the file.
    """
    lines = []
    try:
        with open(file_path, 'r') as file:
            lines = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return lines