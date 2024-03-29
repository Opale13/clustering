# Laboratoire de clustering de bases de données

Afin d'explorer le clustering de bases de données, différentes options ont été testées au sein du groupe pendant les laboratoires:
1. MongoDB cloud (NoSQL);
2. Firebase (NoSQL);
3. Solutions maisons.

## Explications
1. La première solution (Atlas et MongoDB dans le cloud) semblait répondre au cahier des charges car un système de distribution des données sur les trois noeuds d'un cluster est déjà codé et la réplication est également disponible dans les options.
Cependant, l'activation du load balancer est payante et ne sera donc pas effectuée dans le cadre de ce laboratoire.


2. La seconde solution explorée (Firebase de Google) semblait également prometteuse car la distribution des données est codée.
Deux obstacles ont été rencontrés. Le premier, il est indispensable que la base de données soit en temps réel pour pouvoir activer l'option de réplication (dépendant de l'application). Le second, avoir plus d'une instance par compte est payant et c'est la raison pour laquelle nous n'avons pas été plus loin non plus.


3. La dernière solution a été mise en place au sein du groupe et est détaillée ci-dessous:
- Trois instances de MongoDB ont été déployée sur un VPS (Virtual Private Server).
- Un programme de load balancer a été codé et en plus de dispatcher les données dans les instances créées, une trace de la "séparation" des données a été créé (fichier de log). Ceci est réalisé grâce à une API qui gère les données.
- Concernant l'affichage, deux options sont disponibles. La première via Python (affichage d'un graphique par instance en lecture et écriture). La seconde option est l'affichage par Grafana. Le fichier de log est envoyé dans une base de données InfluxDB et un graphique y a été associé.
- Il est encore possible d'ajouter un petit programme qui tournerait en arrière-plan afin de faire de la réplication des données (ou un thread).
- Afin d'améliorer le load balancer, il faudrait également pouvoir tenir compte de la charge des serveurs pour balancer les données (load balancer dynamique).


Au vu des différentes options explorées, nous pouvons bien nous rendre compte que réaliser une solution de qualité demande pas mal de temps et présente donc un intérêt professionnel.
De plus, il est également possible de diviser une seule base de données en différents shards mais cela ne peut pas être considéré comme un cluster. En effet, un cluster doit être constitué d'un parc de machines ce qui nécessite plusieurs machines.
Il reste encore donc du travail afin de pouvoir déployer ces machines séparément.
