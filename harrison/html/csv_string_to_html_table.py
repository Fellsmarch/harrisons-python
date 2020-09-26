from .dict_to_html_table import dict_to_html_table
from ..csv.create_csv_dict import create_csv_dict


def csv_string_to_html_table(csv_string: str) -> str:
    """
    Formats a CSV file represented as a string to an HTML table
    represented as a string.
    """
    csv_list = csv_string.split("\r\n")
    headers = csv_list[0].split(",")
    csv_dict = create_csv_dict(headers, csv_list[1:])
    return dict_to_html_table(csv_dict)
