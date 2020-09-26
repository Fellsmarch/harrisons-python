from requests import get


def download_to_utf_string(url: str) -> str:
    """
    Makes a GET request to the given URL and returns a utf-8 encoded 
    string of the response body.

    Args:
        url: The URL to make the GET request to
    """
    request = get(url)
    content = request.content.decode("utf-8")
    return content
