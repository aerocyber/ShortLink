import os # PATH operations.
from urllib.parse import urlparse # URL validation and others.
import webbrowser # Open link in new tab.
import ShorLinklib.validate_url as v


def url_validate(url):
    return v.url_validate(url)
