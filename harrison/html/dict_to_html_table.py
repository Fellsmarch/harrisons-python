from typing import List
from bs4 import BeautifulSoup
from .create_html_table_header import create_html_table_header


def dict_to_html_table(dict: [str, List[str]], table_id: str = "tableId") -> str:
    """
    Takes a dictionary mapping strings (the table headers) to lists of 
    strings (the table rows) and returns a valid HTML table as a string.

    Each list should be of the same length.
    Requires BeautifulSoup.

    Args:
        dict: The dictionary to map to an HTML table.
        table_id: The id of the table.
    """
    headers = list(dict.keys())
    num_rows = len(dict[headers[0]])
    html_table = f"<table id={table_id}>{create_html_table_header(headers)}"
    for index in range(num_rows):
        new_row = "<tr>"

        for header in headers:
            new_row += f"<td>{dict[header][index]}</td>"

        new_row += "</tr>"
        html_table += new_row

    html_table += "</table>"

    soup = BeautifulSoup(html_table, features="lxml")

    return soup.prettify()
