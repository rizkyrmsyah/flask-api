# Projek latihan Python Flask API 

<a href="https://codeclimate.com/github/rizkyrmsyah/flask-api/maintainability"><img src="https://api.codeclimate.com/v1/badges/641ce2a12645c39688ee/maintainability" /></a>

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Prerequisite

Make sure you have installed [Python](https://www.python.org/), [pip](https://pip.pypa.io/en/stable/installing/) and [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

## Installation

1. Include Python to venv

```bash
virtualenv venv
```

2. Activate the venv

```bash
source venv/bin/activate
```

3. Install the dependencies

```bash
pip install -r requirements.txt
```

4. Copy and rename the `.env.example` to `.env`

5. run database migration 
```bash
flask db upgrade
```
```bash
flask db migrate
```

## Usage

Run the script.

```
flask run
```

You can see which port the api server running.
