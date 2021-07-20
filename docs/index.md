# ShortLink Documentation

## About

ShortLink is a [Python](https://python.org) [library](https://pypi.org/project/shortlink/) that can be used to create url shorteners. This library stores url with a nickname associated with it.

## How it works?

ShortLink library maps a `name` (nickname) to a `url`. This 'map' is then saved to a file given progamatically.

## Installation

### Requirements

- Python version > 3.6
- validators python library (Automatically installed.)

### Approach 1: From PyPI (Recommended)

On your terminal,

```bash
pip install shortlink
```

### Approach 2: Development build from Github

On your terminal,

```bash
pip install git+https://github.com/aerocyber/ShortLink
```

## Approach 3: From whl file

The Python whl file can be obtained from [Github](https://github.com/aerocyber/ShortLink/releases/latest).
Then on your terminal,

```Bash
pip install path/to/downloaded/whl/file
```

## Test installation

In Python,

```python
import ShortLink.ShortLink as S
```

If no error is thrown, congratulations, the installation is success!

## Functions

See [Functions](Functions.md).

## Exceptions

See [Exceptions](Exceptions.md).
