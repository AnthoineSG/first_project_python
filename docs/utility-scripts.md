# Linter

Utiliser [Ruff](https://docs.astral.sh/ruff/installation/)

Pour check le linter

```bash
ruff check
ruff check --watch
# Ou avec poetry
poetry run check
```

# Pour formatter

```bash
ruff format
# Ou avec poetry
poetry run format
```

# Trier les imports

```bash
isort ./nom_du_fichier.py
# Ou avec poetry
poetry run sort-imports
```

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

# Lancer les tests

```bash
pytest
pytest -v
# Ou avec poetry
poetry run test
```

# Verifier le typage

```bash
mypy ./nom_du_fichier.py # Verifie le typage actuel
mypy --strict ./nom_du_fichier.py # Verifie si le typage est partout
# Ou avec poetry
poetry run type_check
```
