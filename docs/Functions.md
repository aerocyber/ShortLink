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

Usage:

```python
S.del_entry('~/example.db', '{"name":"https://example.com", "example":"https://example.org"}', 'name') # auto_save the data. If not to be, use auto_save=False
```


