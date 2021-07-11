import os # PATH operations.
from urllib.parse import urlparse # URL validation and others.
import webbrowser # Open link in new tab.
import validators


def url_validate(url):
    isValid = validators.url(url)
    if isValid == True:
        return True
    else:
        return False

def open_in_browser(url):
    webbrowser.new_taab(url)

def save_(db_path,data):
    x = open(db_path,'r')
    x_dat = x.read()
    x.close()
    dat_ = x_dat.update(data)
    f = open(db_path,'w')
    f.write(dat_)
    f.close()

def read_(db_path):
    x = open(db_path, 'r')
    dat = x.read()
    x.close()
    return dat


def export(format,data):
    pass