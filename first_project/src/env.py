import os

common_text = "Les variables d'environements fonctionne ? =>"


def check_env() -> None:
    init = os.getenv("INIT_ENV")
    if init:
        return print(f"{common_text} {init}")
    else:
        return print(f"{common_text} Il y a un probleme :(")
