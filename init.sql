CREATE DATABASE individus_louches;
-- table individu

CREATE TABLE IF NOT EXISTS individu (
    id PRIMARY KEY,
    DateNaissance DATE NOT NULL,
    DateDeces DATE DEFAULT NULL
    );

ALTER TABLE individu
ADD CONSTRAINT verif_date CHECK (DateNaissance < DateDeces);

CREATE TABLE IF NOT EXISTS individu_nom (
    id PRIMARY KEY,
    id_individu
    nom varchar(30) NOT NULL DEFAULT,
    );

CREATE TABLE IF NOT EXISTS individu_prenom (
    id PRIMARY KEY,
    id_individu
    prenom varchar(30) NOT NULL DEFAULT,
    );

CREATE TABLE IF NOT EXISTS relation_biologique (
    id PRIMARY KEY,
    id_parents
    id_enfant,
    );

CREATE TABLE IF NOT EXISTS relation_adoptive (
    id PRIMARY KEY,
    id_parents,
    id_enfant,
    );

CREATE TABLE IF NOT EXISTS relation_beaux_parents (
    id PRIMARY KEY,
    id_parents
    id_enfant,
    );

CREATE TABLE IF NOT EXISTS union_conjugale (
    id PRIMARY KEY,
    id_individu_a,
    id_individu_b
    date_debut DATE DEFAULT NULL
    date_fin DATE DEFAULT NULL
    );
