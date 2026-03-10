from pydantic import BaseModel
from datetime import date
from typing import Optional

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

class relation_beaux_parents(BaseModel):
    id: int
    id_parents: int
    id_enfant: int

class union_conjugale(BaseModel):
    id: int
    id_individu_a: int
    id_individu_b: int
    date_debut: Optional[date] = None
    date_fin: Optional[date] = None
