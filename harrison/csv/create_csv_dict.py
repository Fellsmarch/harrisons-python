from typing import List, Callable, Dict


def create_csv_dict(headers: List[str], lines: List[str], break_condition: Callable[[List], bool] = None) -> Dict:
    """
    Maps a list of CSV content into a dictionary.

    Args:
        headers: The headers of the CSV file.
        lines: The non-header lines of the CSV file.
        break_condition: A function that is called to check if lines should
                            stop being added to the dictionary
    """
    # Could do this as a default argument, but this is nicer.
    if not break_condition:
        def break_condition(line): return not line[0]

    csv_dict = {header: [] for header in headers}
    for line in lines:
        line = line.split(",")
        if break_condition(line):
            break

        for index, header in enumerate(headers):
            csv_dict[header].append(line[index])

    return csv_dict
