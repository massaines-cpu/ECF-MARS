#api
from fastapi import FastAPI
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
def creer_individu(individu: individu):
    connexion = connexion_mysql()
    cursor = connexion.cursor()
    cursor.execute('INSERT INTO individu (id, date_naissance, date_deces VALUES (%s, %s, %s)',
                   (individu.id, individu.date_naissance, individu.date_deces))
    connexion.commit()

@app.get('/individu/{id}')
def recup_individu(id: int):
    connexion = connexion_mysql()
    cursor = connexion.cursor()
    cursor.execute('SELECT * FROM individu WHERE id = %s', (id,))
    recuperation_ligne = cursor.fetchone()
    connexion.commit()

@app.put('individu/{id}')
def modif_individu(id: int, ind: individu):
    connexion = connexion_mysql()
    cursor = connexion.cursor()
    cursor.execute('UPDATE individu SET date_naissance = %s, date_deces = %s WHERE id = %s ',
                   (individu.date_naissance, individu.date_deces, id,))
    connexion.commit()

@app.delete('/individu/{id}')
def supp_individu(id: int):
    connexion = connexion_mysql()
    cursor = connexion.cursor()
    cursor.execute('DELETE FROM individu WHERE id = %s', (id,))
    connexion.commit()



