Welcome to ShortLink's documentation!
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

.. raw:: html

   <!--
    Copyright 2021 Aditya Ajay
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at
    
        http://www.apache.org/licenses/LICENSE-2.0
    
    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
   -->

About
=====

ShortLink is a url shortening tool maker. This does means ShortLink is a
url shortener. However, ShortLink can be used for making url shorteners.

Usage
-----

First, import ShortLink:

.. code:: python

   import ShortLink

Exceptions raised BY ``ShortLink``:

-  NotUrlError: Raised when input url is not a valid URL. Raised by:
   open_in_browser()
-  EntryExistsError: Raised when ``url`` and ``name`` exist in the given
   database. Raised by: new_entry()
-  FIleNotFoundError: When specified file cannot be found on system.
   Raised by: read_()
-  KeyError: When specified name (key) is already present. Raised by:
   new-entry()
-  ValueError: When specified url (value) is already present. Raised by:
   new_entry()
-  KeyError: When specified name (key) is not present. Raised by:
   del_entry()

Importing
---------

.. code:: python

   # To import, use this method:
   import ShortLink.ShortLink as S

Functions which can be used
---------------------------

url_validate(url: str)
~~~~~~~~~~~~~~~~~~~~~~

Validate a url.

Args: url (string): Checks whether url is a valid URL.

Returns: bool: True if url is a valid URL else False.

open_in_browser(url : str)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Open the link in (default) browser.

Args: url (string): URL to be opened.

Raises: NorURLError: If the url is NOT a url.

save_(db_path,data: dict)
~~~~~~~~~~~~~~~~~~~~~~~~~

Save data to db_path.

Args: db_path (PATH): An existing file. File will be overwritten and the
data will be in JSON format. data (dict): Data to be written.

read_(db_path)
~~~~~~~~~~~~~~

Read data from db_path.

Args: db_path (PATH): Path to file.

Raises: FileNotFoundError: If file is not found.

Returns: dict: Associated data.

return_url(db, name, open_in_browsers=True)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Return URL of the nickname name.

Args: db (dict): The database where data is stored. name (string): The
nickname of url. open_in_browsers (bool, optional): Open in browser?.
Defaults to True.

Returns: url: URL associated with nickname name.

new_entry(db, name, url, db_path, auto_save = True)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add a new entry to database.

Args: db (dict): The database. name (string): Nickname to be assigned.
url (URL): URL which is to be called name. db_path (PATH): PATH to file
where database is to be saved. auto_save (bool, optional): Save on
adding the entry?. Defaults to True.

Raises: EntryExistsError: If both name and url exist in the database.
KeyError: If name exist in database. ValueError: If url exist in
database.

Returns: dict: Updated database.

del_entry(db_path, db, name, auto_save=True)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Delete an entry.

Args: db_path (PATH): Path to file to which data is to be saved. db
(dict): Database. name (string): Nickname. auto_save (bool, optional):
Save data upon deletion of data. Defaults to True.

Raises: KeyError: Raised when name do not exist.

Returns: dict: Updated database.

mod_url(name, url, db, db_path, auto_save=True)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Modify the url of the entry.

Args: name (string): Nickname in which url is to be modified. url (URL):
New URL. db (dict): Database. db_path (PATH): PATH to the file to which
data is to be saved. auto_save (bool, optional): Autosave on
modification?. Defaults to True.

Returns: dict: Updated database.

mod_name(name, url, db, db_path, name_old, auto_save=True):
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Modify the name of the entry.

Args: name (string): New nickname. url (URL): URL which name is to be
assigned. db (dict): Database. db_path (PATH): PATH to the file to which
data is to be saved. name_old(string): The old nickname. auto_save
(bool, optional): Autosave on modification?. Defaults to True.

Returns: dict: Updated database.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
