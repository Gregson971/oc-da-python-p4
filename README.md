[![oc-project-shield][oc-project-shield]][oc-project-url]

[oc-project-shield]: https://img.shields.io/badge/OPENCLASSROOMS-PROJECT-blueviolet?style=for-the-badge
[oc-project-url]: https://openclassrooms.com/fr/paths/518-developpeur-dapplication-python

# Openclassrooms - Développeur d'application Python - Projet 4

Développez un programme logiciel en Python

![Chess Game](https://user.oc-static.com/upload/2020/09/22/16007793690358_chess%20club-01.png)

## Compétences évaluées

- :bulb: Structurer le code d'un programme Python en utilisant un design pattern
- :bulb: Écrire un code Python robuste en utilisant la PEP 8
- :bulb: Utiliser la programmation orientée objet pour développer un programme Python

## Installation et exécution du projet

### Pré-requis

- Avoir `Python` et `pip` installé sur sa machine.

1. Cloner le repo

```sh
git clone https://github.com/Gregson971/oc-da-python-p4.git
```

2. Se placer dans le dossier oc-da-python-p4

```sh
cd /oc-da-python-p4
```

3. Créer l'environnement virtuel

```sh
python -m venv env
```

4. Activer l'environnement virtuel \
   Si vous utilisez Mac ou Linux

```sh
source env/bin/activate
```

Si vous utilisez Windows

```sh
env\Scripts\activate.bat
```

5. Installer les packages requis

```sh
pip install -r requirements.txt
```

6. Exécuter le script

```sh
python main.py
```

7. Générer un rapport flake8

```sh
flake8 --vv
```

![flake8-report](img-documentation/p4_flake8_report.png)

## Options des menus

### Menu principal

![main-menu](img-documentation/p4_main_menu.png)

### Menu de visualisation des rapports

![report-menu](img-documentation/p4_report_menu.png)

### Exemple de rapport : Liste des joueurs

![report-example](img-documentation/p4_ex_list_player.png)
