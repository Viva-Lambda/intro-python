"""
Solution to Exercice 03
"""
# License: see, LICENSE

import os


if __name__ == "__main__":
    asset_path = os.path.join("assets", "ex03.txt")
    ligne = "ikinci satirim"
    with open(asset_path, "a", encoding="utf-8", newline="\n") as fd:
        fd.write(ligne)
