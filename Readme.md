# Premier projet python

Premier projet pour decouvrir l'univers de Python

- [x] Crée un environement pour dev
- [x] Faire une methode simple
  - `./first_project/src/car.py`
- [x] Ajouter un gestionnaire de package
  - [`poetry`](https://python-poetry.org/)
- [x] Ajouter un linter
  - [`isort`](https://pycqa.github.io/isort/)
- [x] Ajouter du typage
  - [`mypy`](https://mypy-lang.org/)
- [x] Ajouter des variables d'environements
  - [`python-dotenv`](https://pypi.org/project/python-dotenv/)
- [x] Ajouter des libs
  - `mypy` / `isort` / `python-dotenv`
- [x] Ajouter des tests
  - [`pytest`](https://docs.pytest.org/en/stable/)
- [ ] Ajouter de la doc
- [ ] Ajouter des github actions
- [ ] Ajouter un equivalent a semantic-release pour python
- [ ] Publier le projet

## Start le projet

- Ouvrir un terminal powershell
  - Activer la Environement virtuel
  - `./activate.ps1`
    - Installer les dependences
    - `poetry install`
      - Lancer le projet
      - `poetry run start`
        - Stopper le projet
        - `deactivate`

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

## Build

Crée un fichier .whl et .tar.gz

```bash
python -m build
# Ou avec poetry
poetry build
```

## Check le tree en powershell

```bash
tree /F
```

## Trier les imports

```bash
isort ./nom_du_fichier.py
# Ou avec poetry
poetry run sort-imports
```

## Verifier le typage

```bash
mypy ./nom_du_fichier.py # Verifie le typage actuel
mypy --strict ./nom_du_fichier.py # Verifie si le typage est partout
# Ou avec poetry
poetry run type_check
```

## Lancer les tests

```bash
pytest
pytest -v
# Ou avec poetry
poetry run test
```

## Linter

Utiliser [Ruff](https://docs.astral.sh/ruff/installation/)

Pour check le linter

```bash
ruff check
ruff check --watch
# Ou avec poetry
poetry run check
```

Pour formatter

```bash
ruff format
# Ou avec poetry
poetry run format
```
