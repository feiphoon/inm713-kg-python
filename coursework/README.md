# INM713 Semantic Web Technologies and Knowledge Graphs

## Setup

`git clone` this repo so you can run it locally.

This repo was written for Python 3.8.5. On Mac, please check your version:

```
python --version
```

### Virtualenv


#### Create your new virtual environment

```
python3 -m venv venv # in this folder
```

#### Start and set up your new environment

```
source venv/bin/activate
pip install -r requirements.txt # Install the required packages in your new environment
pip list # Optional: check what was installed in `venv`
```
#### Exit your environment

```
deactivate
```

## Code formatting

Just run this:

```
inv lint
```

The packages run by this are as follows (if you want to run them individually).

### `black`

Aggressive PEP 8 code reformatter.

https://pypi.org/project/black/
```
black . # In the folder you're in, or a particular file you want to format
```

### `flake8`

Reports PEP 8 violations.

https://pypi.org/project/flake8/
```
flake8 . # In the folder you're in, or a particular file you want to report on
```

## Running tests

### `doctest`

Run `doctest` on any docstring tests.
```
python -m doctest <any-file>.py -v
```
