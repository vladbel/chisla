# running unit tests

```bash
./scripts/run-ut.sh
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

## create environment
sudo apt-get install python-virtualenv
virtualenv --python=python3.6 chisla_env

## save virtual environment
pip freeze > venv_ubuntu.config

## clone virtual environment
pip install -r venv_ubuntu.config
```

May need install missing dependency for matplotlib:

```bash
sudo apt-get install python3.6-tk
```
