from typing import List


def create_html_table_header(headers: List[str]) -> str:
    """
    Takes headers and maps them to a valid HTML table header.
    """
    total_chars = len("".join(headers))
    header_widths = {header: (len(header)/total_chars)
                     * 100 for header in headers}

    header_string = '<tr class="header">'

    for header in headers:
        header_string += f'<th style="width:{header_widths[header]}%">{header}</th>'

    header_string += '</tr>'

    return header_string
