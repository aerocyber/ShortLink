# Functions

## About this document

This document covers the usage of the functions in shortlink.

## del_entry(db_path, db, name, auto_save=True)

Delete an entry.

  Args:
    db_path (PATH): Path to file to which data is to be saved.
    db (dict): Database.
    name (string): Nickname which is to be deleted.
    auto_save (bool, optional): Save data upon deletion of data. Defaults to True.

  Raises:
    KeyError: Raised when name do not exist.

  Returns:
    dict: Updated database.

## mod_name(name, url, db, db_path, name_old, auto_save=True)

Modify the name of the entry.

Args:
    name (string): New nickname.
    url (URL): URL which name is to be assigned.
    db (dict): Database.
    db_path (PATH): PATH to the file to which data is to be saved.
    name_old(string): The old nickname.
    auto_save (bool, optional): Autosave on modification?. Defaults to True.

Returns:
    dict: Updated database.

## mod_url(name, url, db, db_path, auto_save=True)

  Modify the url of the entry.
  
  Args:
      name (string): Nickname in which url is to be modified.
      url (URL): New URL.
      db (dict): Database.
      db_path (PATH): PATH to the file to which data is to be saved.
      auto_save (bool, optional): Autosave on modification?. Defaults to True.
  
  Returns:
      dict: Updated database.

## new_entry(db, name, url, db_path, auto_save=True)

  Add a new entry to database.
  
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
      dict: Updated database

## open_in_browser(url: str)

  Open the link in (default) browser.
  
  Args:
      url (string): URL to be opened
  
  Raises:
      NorURLError: If the url is NOT a url.

## read_(db_path)

  Read data from db_path.
  
  Args:
      db_path (PATH): Path to file.
  
  Raises:
      FileNotFoundError: If file is not found.
  
  Returns:
      dict: Associated data.

## return_url(db, name, open_in_browsers=True)

  Return URL of the nickname name.
  
  Args:
      db (dict): The database where data is stored.
      name (string): The nickname of url.
      open_in_browsers (bool, optional): Open in browser?. Defaults to True.
  
  Returns:
      url: URL associated with nickname name.

## save_(db_path, data: dict)

  Save data to db_path.
  
  Args:
      db_path (PATH): An existing file. File will be overwritten and the data will be in JSON format.
      data (dict): Data to be written.

## url_validate(url: str)

  Validate a url.
  
  Args:
      url (string): Checks whether url is a valid URL.
  
  Returns:
      bool: True if url is a valid URL else False.
