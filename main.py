#api
from fastapi import FastAPI, HTTPException
import mysql.connector as mysql
from dotenv import load_dotenv
import os
from models import *
load_dotenv()

app = FastAPI(title="API REST pour mon étrange généalogie")

def connexion_mysql():
    return mysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
    )

@app.post('/individu')
def creer_individu(ind: individu):
    try:
        connexion = connexion_mysql()
        cursor = connexion.cursor()
        cursor.execute('INSERT INTO individu (id, date_naissance, date_deces) VALUES (%s, %s, %s)',
                       (ind.id, ind.date_naissance, ind.date_deces))
        connexion.commit()
    except mysql.Error as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get('/individu/{id}')
def recup_individu(id: int):
    try:
        connexion = connexion_mysql()
        cursor = connexion.cursor()
        cursor.execute('SELECT * FROM individu WHERE id = %s', (id,))
        recuperation_ligne = cursor.fetchone()
        if recuperation_ligne is None:
            raise HTTPException(status_code=404, detail='individu introuvable')
        return recuperation_ligne

    except mysql.Error as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.put('/individu/{id}')
def modif_individu(id: int, ind: individu):
    try:
        connexion = connexion_mysql()
        cursor = connexion.cursor()
        cursor.execute('UPDATE individu SET date_naissance = %s, date_deces = %s WHERE id = %s ',
                       (ind.date_naissance, ind.date_deces, id,))
        connexion.commit()
    except mysql.Error as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete('/individu/{id}')
def supp_individu(id: int):
    try:
        connexion = connexion_mysql()
        cursor = connexion.cursor()
        cursor.execute('DELETE FROM individu WHERE id = %s', (id,))
        connexion.commit()
    except mysql.Error as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post('/individu/{id}/prenom')
def ajout_prenom(id: int, ind: individu_prenom):
    try:
        connexion = connexion_mysql()
        cursor = connexion.cursor()
        cursor.execute('INSERT INTO individu_prenom (id, id_individu, prenom, ordre) VALUES (%s, %s, %s, %s)',
                       (ind.id, id, ind.prenom, ind.ordre))
        connexion.commit()
    except mysql.Error as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put('/individu/{id}/prenom/{id_prenom}')
def modif_prenom(id: int, id_prenom: int, ind: individu_prenom):
    try:
        connexion = connexion_mysql()
        cursor = connexion.cursor()
        cursor.execute('UPDATE individu_prenom SET prenom = %s, ordre = %s WHERE id = %s',
                       (ind.prenom, ind.ordre, id_prenom))
        connexion.commit()
    except mysql.Error as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete('/individu/{id}/prenom/{id_prenom}')
def supp_prenom(id:int, id_prenom: int):
    try:
        connexion = connexion_mysql()
        cursor = connexion.cursor()
        cursor.execute('DELETE FROM individu_prenom WHERE id = %s', (id_prenom,))
        connexion.commit()
    except mysql.Error as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post('/individu/{id}/nom')
def ajout_nom(id: int, ind: individu_nom):
    try:
        connexion = connexion_mysql()
        cursor = connexion.cursor()
        cursor.execute('INSERT INTO individu_nom (id, id_individu, nom, ordre) VALUES (%s, %s, %s, %s)',
                       (ind.id, id, ind.nom, ind.ordre))
        connexion.commit()
    except mysql.Error as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put('/individu/{id}/nom/{id_nom}')
def modif_nom(id: int, id_nom: int, ind: individu_nom):
    try:
        connexion = connexion_mysql()
        cursor = connexion.cursor()
        cursor.execute('UPDATE individu_nom SET nom = %s, ordre = %s WHERE id = %s',
                       (ind.nom, ind.ordre, id_nom))
        connexion.commit()
    except mysql.Error as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete('/individu/{id}/nom/{id_nom}')
def supp_nom(id:int, id_nom: int):
    try:
        connexion = connexion_mysql()
        cursor = connexion.cursor()
        cursor.execute('DELETE FROM individu_nom WHERE id = %s', (id_nom,))
        connexion.commit()
    except mysql.Error as e:
        raise HTTPException(status_code=400, detail='c\'est interdit de faire ça !')

@app.post('/relation/biologique')
def creer_relation_biologique(rel: relation_biologique):
    try:
        connexion = connexion_mysql()
        cursor = connexion.cursor()
        cursor.execute('INSERT INTO relation_biologique (id, id_parents, id_enfant) VALUES (%s, %s, %s)',
                       (rel.id, rel.id_parents, rel.id_enfant))
        connexion.commit()
    except mysql.Error as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete('/relation/biologique/{id}')
def supp_relation_bio(id: int):
    try:
        connexion = connexion_mysql()
        cursor = connexion.cursor()
        cursor.execute('DELETE FROM relation_biologique WHERE id = %s', (id,))
        connexion.commit()
    except mysql.Error as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post('/relation/adoptive')
def creer_relation_adoptive(rel: relation_adoptive):
    try:
        connexion = connexion_mysql()
        cursor = connexion.cursor()
        cursor.execute('INSERT INTO relation_adoptive (id, id_parents, id_enfant) VALUES (%s, %s, %s)',
                       (rel.id, rel.id_parents, rel.id_enfant))
        connexion.commit()
    except mysql.Error as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete('/relation/adoptive/{id}')
def supp_relation_adoptive(id: int):
    try:
        connexion = connexion_mysql()
        cursor = connexion.cursor()
        cursor.execute('DELETE FROM relation_adoptive WHERE id = %s', (id,))
        connexion.commit()
    except mysql.Error as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post('/relation/beaux_parents')
def creer_relation_beaux_parents(rel: relation_beaux_parents):
    try:
        connexion = connexion_mysql()
        cursor = connexion.cursor()
        cursor.execute('INSERT INTO relation_beaux_parents (id, id_parents, id_enfant) VALUES (%s, %s, %s)',
                       (rel.id, rel.id_parents, rel.id_enfant))
        connexion.commit()
    except mysql.Error as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete('/relation/beaux_parents/{id}')
def supp_relation_beaux_parents(id: int):
    try:
        connexion = connexion_mysql()
        cursor = connexion.cursor()
        cursor.execute('DELETE FROM relation_beaux_parents WHERE id = %s', (id,))
        connexion.commit()
    except mysql.Error as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post('/union/')
def creer_union_conjugale(union: union_conjugale):
    try:
        connexion = connexion_mysql()
        cursor = connexion.cursor()
        cursor.execute('INSERT INTO union_conjugale (id, id_individu_a, id_individu_b, date_debut, date_fin) VALUES (%s, %s, %s, %s, %s)',
                       (union.id, union.id_individu_a, union.id_individu_b, union.date_debut, union.date_fin,))
        connexion.commit()
    except mysql.Error as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put('/union/{id}')
def modif_union(id: int, union: union_conjugale):
    try:
        connexion = connexion_mysql()
        cursor = connexion.cursor()
        cursor.execute('UPDATE union_conjugale SET id_individu_a = %s, id_individu_b = %s, date_debut = %s, date_fin = %s WHERE id = %s',
                        (union.id_individu_a, union.id_individu_b, union.date_debut, union.date_fin, id))
        connexion.commit()
    except mysql.Error as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete('/union/{id}')
def supp_union(id: int):
    try:
        connexion = connexion_mysql()
        cursor = connexion.cursor()
        cursor.execute('DELETE FROM union_conjugale WHERE id = %s', (id,))
        connexion.commit()
    except mysql.Error as e:
        raise HTTPException(status_code=400, detail=str(e))


