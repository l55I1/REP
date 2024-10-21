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
