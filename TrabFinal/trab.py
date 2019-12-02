from peewee import *
import os
from playhouse.shortcuts import model_to_dict

arq = 'estudio.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db

class Filme(BaseModel):
    titulo = CharField()
    dat_lancamento = CharField()
    genero = CharField()

class Ator(BaseModel):
    nome = CharField()
    idade = IntegerField()
    cache = CharField()
    filme = ForeignKeyField(Filme)

class Elenco(BaseModel):
    filme = ForeignKeyField(Filme)
    ator = ForeignKeyField(Ator)

class Diretor(BaseModel):
    nome = CharField()
    idade = IntegerField()
    filme = ForeignKeyField(Filme)

class Estudio(BaseModel):
    local = CharField()
    qnt_salas = IntegerField()
    tempo_uso = CharField()

class Funcionario(BaseModel):
    nome = CharField()
    cpf = CharField()
    estudio = ForeignKeyField(Estudio)

class FilmesLançados(BaseModel):
    filmes_prontos = []
    estudio = ForeignKeyField(Estudio)

class CompraDeFilme(BaseModel):
    valor = CharField()
    filme = ForeignKeyField(Filme)

class EquipeDublagem(BaseModel):
    nome_dublador = CharField()
    cache = CharField()
    papel = CharField()
    filme = ForeignKeyField(Filme)

class Comprador(BaseModel):
    filme = ForeignKeyField(Filme)
    empresa = CharField()
    valor = CharField()


db.connect()
db.create_tables([Filme,Ator,Elenco,Diretor,Estudio,Funcionario,FilmesLançados,CompraDeFilme,EquipeDublagem,Comprador])          
    
february = Filme.create(titulo = "February", dat_lancamento = "7/9/2018", genero = "Terror")
filmelist = list(map(model_to_dict, Filme.select()))
kiernan = Ator.create(nome = "Kiernan Shipka", idade = 20, cache = "$60000", filme = february)
atorlist = list(map(model_to_dict, Ator.select()))
elencoFebruary = Elenco.create(filme = february, ator = kiernan)
elencolist = list(map(model_to_dict, Elenco.select()))
julian = Diretor.create(nome = "Julian Grey", idade = 46, filme = february)
diretorlist = list(map(model_to_dict, Diretor.select()))
abc = Estudio.create(local = "Los Angeles", qnt_salas = 13, tempo_uso = "4 meses")
estudiolist = list(map(model_to_dict, Estudio.select()))
jairo = Funcionario.create(nome = "Jairo da Silva", cpf = "12332112342", estudio = abc)
funcionariolist = list(map(model_to_dict, Funcionario.select()))
season2019 = FilmesLançados.create(filmes_prontos = ["Deixe a neve cair", "Silence"], estudio = abc)
filmeslançadoslist = list(map(model_to_dict, FilmesLançados.select()))
compraFilmes = CompraDeFilme.create(filme = february, valor = "$1000000000")
compradefilmelist = list(map(model_to_dict, CompraDeFilme.select()))
dublagem_february = EquipeDublagem.create(nome_dublador = "Luiza Porto", cache = "$5000", papel = "Angie", filme = february)
equipedublagemlist = list(map(model_to_dict, EquipeDublagem.select()))
comprador = Comprador.create(filme = february, empresa = "Sony", valor = "$500000000")
compradorlist = list(map(model_to_dict, Comprador.select()))  

def lista():
    programacao = [filmelist, atorlist, elencolist, diretorlist, estudiolist, funcionariolist, filmeslançadoslist, compradefilmelist, equipedublagemlist, compradorlist]
    return programacao