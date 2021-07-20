# Build instructions

First, clone the repository and cd into. 

```bash
git clone https://github.com/aerocyber/ShortLink
cd ShortLink
```

Now, install build requirement. **Using virtual environment is highly recommended as poetry is being installed as build requirement.**

```bash
python3 -m pip install pip setuptools wheel --upgrade
python3 -m pip install -r build-requirements.txt
```

Now, use `poetry build` to build whl file.

```bash
poetry build
```

The `dist` dir contains the built whl file.
