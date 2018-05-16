# Clone workspace and environment

```bash
git clone https://github.com/vladbel/chisla.git 

## create environment
python3.6 -m venv chisla_env

## activate
source chisla_env/bin/activate

pip install -r requirements.txt
```

On Ubuntu

to setup venv:

```bash
sudo apt-get install python-virtualenv
virtualenv --python=python3.6 chisla_env
```

install missing dependency for matplotlib:

```bash
sudo apt-get install python3.6-tk
```
