# Copyright 2021 Aditya Ajay
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os # PATH operations.
import webbrowser # Open link in new tab.
import validators # Validation of URL.
import json # Data saving and reading.


class NotURLError(Exception):
    """Error raised when URL Validation fails.

    Args:
        Exception (string): Error Text.
    """
    pass

class EntryExistsError(Exception):
    """Error raised when Nickname of Url and Url Exists.

    Args:
        Exception (string): Error Text.
    """
    pass

def url_validate(url: str):
    """Validate a url.

    Args:
        url (string): Checks whether url is a valid URL.

    Returns:
        bool: True if url is a valid URL else False.
    """
    isValid = validators.url(url) # Call validators.url() with url as the value.
    if isValid == True:
        return True # If True is the output of the function call, return call...
    else:
        return False # If anything else is the output, return False (validation fail).

def open_in_browser(url : str):
    """Open the link in (default) browser.

    Args:
        url (string): URL to be opened
    """
    val = url_validate(url)
    if val == True:
        webbrowser.open_new_tab(url) # Use built-in module to open url in new tab.
    else:
        errors = "[ERROR]:: " + url + ":: is not a valid URL."
        raise NotURLError(errors) # If url validation fail, raise error.

def save_(db_path,data: dict):
    """Save data to db_path.

    Args:
        db_path (PATH): An existing file. File will be overwritten and the data will be in JSON format.
        data (dict): Data to be written.
    """
    if os.path.exists(db_path) == False: # If file do not exist,
        f = open(db_path, 'w') # Open it!
        f.write(json.dumps(data)) # Write it!
        f.close() # Close it!
    
    x = open(db_path,'r') # open file for reading.
    x_dat = json.loads(x.read()) # Get data in dict format.
    x.close() # Close it!
    dat_ = x_dat.update(data) # Update data!
    f = open(db_path,'w') # Open file for writing
    f.write(json.dumps(dat_)) # Write it!
    f.close() # Close it!

def read_(db_path):
    """Read data from db_path.

    Args:
        db_path (PATH): Path to file.

    Raises:
        FileNotFoundError: If file is not found.

    Returns:
        [type]: Associated data.
    """
    exist = os.path.exists(db_path) # Check for existance.
    if exist == True:
        x = open(db_path, 'r')
        dat = json.loads(x.read()) # Can have error if the data is not JSON formatted.
        x.close()
        return dat # Return read data.
    else:
        errors = db_path+":: does not exist."
        raise FileNotFoundError(errors)

def return_url(db, name,  open_in_browsers=True):
    """Return URL of the nickname name.

    Args:
        db (dict): The database where data is stored.
        name (string): The nickname of url.
        open_in_browsers (bool, optional): Open in browser?. Defaults to True.

    Returns:
        url: URL associated with nickname name.
    """
    if open_in_browsers == False:
        return db[name]
    else:
        open_in_browser(db[name])
        return db[name] # To prevent error.

def new_entry(db, name, url, db_path, auto_save = True):
    """Add a new entry to database.

    Args:
        db (dict): The database.
        name (string): Nickname to be assigned.
        url (URL): URL which is to be called name.
        db_path (PATH): PATH to file where database is to be saved.
        auto_save (bool, optional): Save on adding the entry?. Defaults to True.

    Raises:
        EntryExistsError: If both name and url exist in the database.
        KeyError: If name exist in database.
        ValueError: If url exist in database.

    Returns:
        dict: Updated database.
    """
    if name in db.keys():
        if url in db.values():
            errors = "[ERROR]::" + name + ":"+ url+":: exists." # url and name exist.
            raise EntryExistsError(errors)
        else:
            errors = "[ERROR]::" + name + "::exists." # name exist.
            raise KeyError(errors)
    elif url in db.values():
        errors = "[ERROR]::" + url + "::exists." # url exist.
        raise ValueError(errors)
    else:
        db[name] = url # Add the entry.
        if auto_save == True:
            save_(db_path=db_path)
        return db

def del_entry(db_path, db, name, auto_save=True):
    """Delete an entry.

    Args:
        db_path (PATH): Path to file to which data is to be saved.
        db (dict): Database.
        name (string): Nickname.
        auto_save (bool, optional): Save data upon deletion of data. Defaults to True.

    Raises:
        KeyError: Raised when name do not exist.

    Returns:
        dict: Updated database. 
    """
    if name in db.keys():
        del db[name]
        if auto_save == True:
            save_(db_path,db)
        return db
    else:
        errors = "[ERROR]::" + name + ":: do NOT exist."
        raise KeyError(errors)

def mod_url(name, url, db, db_path, auto_save=True):
    """Modify the url of the entry.

    Args:
        name (string): Nickname in which url is to be modified.
        url (URL): New URL.
        db (dict): Database.
        db_path (PATH): PATH to the file to which data is to be saved.
        auto_save (bool, optional): Autosave on modification?. Defaults to True.

    Returns:
        dict: Updated database.
    """
    db[name] = url # Modify the entry.
    if auto_save == True:
        save_(db_path=db_path)
    return db

def mod_name(name, url, db, db_path, name_old, auto_save=True):
    """Modify the name of the entry.

    Args:
        name (string): New nickname.
        url (URL): URL which name is to be assigned.
        db (dict): Database.
        db_path (PATH): PATH to the file to which data is to be saved.
        name_old(string): The old nickname.
        auto_save (bool, optional): Autosave on modification?. Defaults to True.

    Returns:
        dict: Updated database.
    """
    del db[name_old]
    db[name] = url
    if auto_save == True:
        save_(db_path=db_path)
    return db