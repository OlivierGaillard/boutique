# Ajouter les images

On peut les ajouter une à une mais comme la date de création des images
suit la séquence des clés primaires il est possible d'automatiser
le processus:

- copier toutes les images dans le répertoire `/media/articles`.
- créer une requête chargeant tous les articles, en partant du plus
  ancien.
- pour chaque article créer une instance du modèle `Photo` et 
  renseigner la clé étrangère sur l'ID de l'article, et le chemin sur la
  *bonne* image.
  
Il faut créer une liste des couples `(article_id, image_name)`.
Une fois cette liste en place on crée les instances de `Photo` avec le 
chemin et l'ID de l'article.

# Analyse des ventes

Une vente peut concerner plusieurs articles. Momentanément nous
avons besoin d'une solution permettant d'indiquer qu'un article
a été vendu pour tel montant, et quelle taille.

Il est possible de créer un champ *ventes* qui contiendra la liste
des montants séparés par des virgules. On ajoute aussi le champ
*tailles_vendues* qui contiendra les tailles vendues et la quantité, comme
par exemple`[('XL', 1), ('M', 2)]`.

# boutique
