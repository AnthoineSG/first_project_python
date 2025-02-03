# Premier projet python

## Vesion de Python sur la machine

```bash
python -V
```

## Environement virtuel

crée un environement virtuel

```bash
python -m venv nom_de_lenvironement
```

pour activer l'environement

```bash
# Dans powershell
.\nom_de_lenvironement\Scripts\Activate.ps1
# Ou https://docs.python.org/3/library/venv.html#how-venvs-work
```

Pour desactiver l'environement

```bash
deactivate
```

run un fichier en ligne de commande

```bash
python start.py
```

## Installer des dependences

Installer une dependence

```bash
pip install python_dotenv
# Ou avec poetry
poetry install python_dotenv
```

## Start le projet

- Ouvrir un terminal powershell
  - Activer la Environement virtuel
  - `.\venv-first-project\Scripts\Activate.ps1`
    - Installer les dependences
    - `poetry install`
      - Lancer le projet
      - `poetry run start`
        - Stopper le projet
        - `deactivate`

## Build

Crée un fichier .whl et .tar.gz

```bash
python -m build
```

## Linter

Utiliser [Ruff](https://docs.astral.sh/ruff/installation/)

Pour check le linter

```bash
ruff check
ruff check --watch
```

Pour formatter

```bash
ruff format
```

check le tree en powershell
tree /F
