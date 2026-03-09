#api
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date
from typing import Optional
import mysql.connector as mysql
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="API REST pour mon étrange généalogie")
class individu(BaseModel):
    id: int
    date_naissance: date
    date_deces: Optional[date] = None

class individu_nom(BaseModel):
    id: int
    id_individu: int
    nom: str

class individu_prenom(BaseModel):
    id: int
    id_individu: int
    prenom: str

class relation_biologique(BaseModel):
    id: int
    id_parents: int
    id_enfant: int
class relation_adoptive(BaseModel):
    id: int
    id_parents: int
    id_enfant: int

class relation_beau_parents(BaseModel):
    id: int
    id_parents: int
    id_enfant: int

class union_conjugale(BaseModel):
    id: int
    id_individu_a: int
    id_individu_b: int
    date_debut: Optional[date] = None
    date_fin: Optional[date] = None

def connexion_mysql():
    return mysql.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
    )



@app.post('/individu')
def creer_individu(ind: individu):
    connexion = connexion_mysql()
    cursor = connexion.cursor()

@app.get('/individu/{id}')
def recup_individu(id: int):
    connexion = connexion_mysql()
    cursor = connexion.cursor()

@app.put('individu/{id}')
def modif_individu(id: int, ind: individu):
    connexion = connexion_mysql()
    cursor = connexion.cursor()

@app.delete('/individu/{id}')
def supp_individu(id: int):
    connexion = connexion_mysql()
    cursor = connexion.cursor()



