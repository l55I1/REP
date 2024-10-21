# REP

## TP1
Ces codes permettent de tester l’associativité de l’addition en Java, javascript, et python.

Les codes génèrent 1 000 000 de tests avec des nombres aléatoires x, y, et z entre 0 et 1.
Ils effectuent ensuite une comparaison entre (x + y) + z et x + (y + z). Les résultats (pourcentage positif) sont affichés sous forme :

`xx.xx% accuracy for language`

### Lancement en local
Pour lancer chaque langage dans le terminal : 

#### Java
```aiignore
javac Java.java
java Java
```

#### JavaScript
```aiignore
node javascript.js
```

#### python
```aiignore
python python.py
```

### Lancement avec Docker

```aiignore
docker build -t asso
docker run --rm asso
```

## TP2
### Structure du Projet

Ce projet est structuré en 4 branches, chacune ayant des objectifs spécifiques :

#### 2 Branches de Test des Tolerances et Plages Aléatoires :
Dans ces branches, nous avons expérimenté avec différentes tolerances et plages aléatoires pour tester divers facteurs.

#### Branche all_factors :
Cette branche utilise Jinja2 pour explorer tous les facteurs impliqués dans notre projet.
Nous avons comparé différents facteurs comme suit : plage aléatoire générée, tolérance, et différentes bibliothèques de nombres aléatoires.
Les résultats de l'exploration des facteurs sont stockés dans le fichier results.csv, situé dans la branche all_factors.
