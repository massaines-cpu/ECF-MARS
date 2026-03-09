//contraintes.md

## Un individu peut avoir :

- Entre 0 et 2 parents biologiques
- Peut avoir entre 0 et 2 parents adoptifs
- Un nombre illimité de parents (incluant les parents adoptifs, beaux-parents, etc.)
- Un nombre illimité d'enfants (biologiques ou adoptés)
- Un ou plusieurs prénoms
- Un ou plusieurs noms de famille
- Une seule date de naissance (unique)
- Une seule date de mort (optionnelle)
- Sa date de naissance est toujours inférieure à sa date de décès
```sql
ADD CONSTRAINT verif_date CHECK (DateNaissance < DateDeces OR DateDeces IS NULL);
```
- Ne peut pas s'unir avec lui-même
```sql
ADD CONSTRAINT verif_union CHECK (id_individu_a <> id_individu_b),
```

## Un enfant :

- Ne peut pas naître avant un parent biologique/adoptif
- Ne peut pas être son propre enfant
```sql
ADD CONSTRAINT verif_enfant_bio CHECK (id_parents <> id_enfant),
ADD CONSTRAINT verif_enfant_ado CHECK (id_parents <> id_enfant),
```
- Peut mourir avant un parent

## Les parents :
- Peuvent apparemment être frère et sœur si l'un des deux a été adopté ?...
- Ne peuvent pas être leurs propres parents/beaux-parents
```sql
ADD CONSTRAINT verif_beaux_parents CHECK (id_parents <> id_enfant),
```
- Peuvent mourir avant ou après son enfant
- Ne peuvent pas être l'ancêtre de lui-même

## Union : 
- Peuvent avoir une seule union à la fois
- Une union peut avoir une date de début et de fin (optionnelle)
```sql
date_fin IS NULL
```
- Une autre union peut commencer uniquement si la précédente est terminée
```sql
ADD CONSTRAINT verif_date_union CHECK (date_debut < date_fin OR date_fin IS NULL),
```
- Une fois une union terminée elle ne peut plus renaitre
```sql 
ADD CONSTRAINT unique_union UNIQUE (id_individu_a, id_individu_b);
```

## Listes des différentes tables :
- individu


