# Activate virtual environment for development
(See "Clone workspace and environment on mac" for first time setup)

To avoid import/export errors and ensure that all these scenarios working:
- running from terminal
- debugging from VS Code
- Linting

we need to have /source and /unit_tests in PYTHONPATH
add `path.pth` file with 

(obsolete) use 
```bash
source ./scripts/activate-venv.sh

# it will
# 1) activate environment
# 2) add paths to pythonpath
```


# Running unit tests

```bash
./scripts/run-ut.sh
# or
./scripts/run-all-ut.sh
```

# Lint

```bash
pylint ./source
pylint ./unit_tests
```

# Clone workspace and environment on mac

Virtual environment tutorial:
https://docs.python.org/3/tutorial/venv.html#managing-packages-with-pip

On Mac:

```bash
git clone https://github.com/vladbel/chisla.git 

## create environment
python3.6 -m venv chisla_env

## activate
source chisla_env/bin/activate

## if nedded
## install new packages
pip install matplotlib

## save virtual environment
pip freeze > venv_mac.config

## clone virtual environment
pip install -r venv_mac.config
```

# Clone workspace and environment on ubuntu
to setup venv:

```bash

## create environment ( python 3.9)
sudo apt-get install python-virtualenv 
virtualenv --python=python3 chisla_env

## save virtual environment
pip freeze > venv_ubuntu.config

## clone virtual environment
pip install -r venv_ubuntu.config
```

May need install missing dependency for matplotlib:

```bash
sudo apt-get install python3.6-tk
```
