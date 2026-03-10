-- base de données
CREATE DATABASE etrange_genealogie;
USE etrange_genealogie;
-- table individu

CREATE TABLE IF NOT EXISTS individu (
    id INT PRIMARY KEY,
    date_naissance DATE NULL,
    date_deces DATE NULL
    );

-- contraintes individu

ALTER TABLE individu
ADD CONSTRAINT verif_date CHECK (date_naissance < date_deces OR date_deces IS NULL);

-- table individu_nom

CREATE TABLE IF NOT EXISTS individu_nom (
    id INT PRIMARY KEY,
    id_individu INT NOT NULL REFERENCES individu(id) ON DELETE CASCADE,
    nom varchar(100) NOT NULL,
    ordre INT NOT NULL DEFAULT 1
    );

-- table individu_prenom

CREATE TABLE IF NOT EXISTS individu_prenom (
    id INT PRIMARY KEY,
    id_individu INT NOT NULL REFERENCES individu(id) ON DELETE CASCADE,
    prenom varchar(100) NOT NULL,
    ordre INT NOT NULL DEFAULT 1
    );

-- table relation_biologique

CREATE TABLE IF NOT EXISTS relation_biologique (
    id INT PRIMARY KEY,
    id_parents INT NOT NULL REFERENCES individu(id) ON DELETE RESTRICT,
    id_enfant INT NOT NULL REFERENCES individu(id) ON DELETE RESTRICT
    );
-- contraintes relation_biologique

ALTER TABLE relation_biologique
ADD CONSTRAINT verif_enfant_bio CHECK (id_parents <> id_enfant),
ADD CONSTRAINT unique_parents_bio UNIQUE (id_parents, id_enfant);

-- table relation_adoptive

CREATE TABLE IF NOT EXISTS relation_adoptive (
    id INT PRIMARY KEY,
    id_parents INT NOT NULL REFERENCES individu(id) ON DELETE RESTRICT,
    id_enfant INT NOT NULL REFERENCES individu(id) ON DELETE RESTRICT
    );
-- contraintes relation_adoptive

ALTER TABLE relation_adoptive
ADD CONSTRAINT verif_enfant_ado CHECK (id_parents <> id_enfant),
ADD CONSTRAINT unique_parents_ado UNIQUE (id_parents, id_enfant);

-- table relation_beaux_parents

CREATE TABLE IF NOT EXISTS relation_beaux_parents (
    id INT PRIMARY KEY,
    id_parents INT NOT NULL REFERENCES individu(id) ON DELETE RESTRICT,
    id_enfant INT NOT NULL REFERENCES individu(id) ON DELETE RESTRICT
    );

-- contraintes relation_beaux_parents

ALTER TABLE relation_beaux_parents
ADD CONSTRAINT verif_beaux_parents CHECK (id_parents <> id_enfant),
ADD CONSTRAINT unique_beaux_parents UNIQUE (id_parents, id_enfant);

-- table union_conjugale

CREATE TABLE IF NOT EXISTS union_conjugale (
    id INT PRIMARY KEY,
    id_individu_a INT NOT NULL REFERENCES individu(id) ON DELETE RESTRICT,
    id_individu_b INT NOT NULL REFERENCES individu(id) ON DELETE RESTRICT,
    date_debut DATE NULL,
    date_fin DATE NULL
    );
-- contraintes union_conjugale

ALTER TABLE union_conjugale
ADD CONSTRAINT verif_date_union CHECK (date_debut < date_fin OR date_fin IS NULL),
ADD CONSTRAINT verif_union CHECK (id_individu_a <> id_individu_b),
ADD CONSTRAINT unique_union UNIQUE (id_individu_a, id_individu_b);