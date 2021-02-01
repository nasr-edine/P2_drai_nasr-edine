# project 2: web scrapping
Use the basics of Python for market analysis
## Installation

clone repository locally
```bash
git clone https://github.com/nasr-edine/P2_drai_nasr-edine.git
```

Create a virtual environment in root folder of project 
```bash
python -m venv env
```

Activate virtual environment
```bash
source ./env/bin/activate
```

Install dependencies
```bash
pip3 install -r requirements.txt
```
## Usage

Go to the directory while content source files:
```python
cd src/
```

execute the python script below for begin to scrape the website:
```python
python3 scrape_all_books.py
```
### Folder Structure with csv et images folders created

    .
    ├── src/                    # Source files
    ├── env/                    # Virtual environment python
    ├── csv/                    # Csv files for each book categories
    ├── images/                 # images downloaded are saved in this directory
    ├── requirements.txt        # for install all dependencies necessary for this project
    └── README.md

## How to check style code ?

```python
flake8 src/*
```

### How to run unittest
    P2_drai_nasr-edine
    └──src
        ├── scrape_all_books.py        # 
        └── test_categories.py

Exemple for check all book categories available in home page
```python
cd src/
python -m unittest test_categories
```