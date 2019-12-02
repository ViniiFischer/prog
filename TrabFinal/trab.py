from peewee import *
import os

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

if __name__ == '__main__':

    db.connect()
    db.create_tables([Filme,Ator,Elenco,Diretor,Estudio,Funcionario,FilmesLançados,CompraDeFilme,EquipeDublagem,Comprador])          
    
    february = Filme.create(titulo = "February", dat_lancamento = 7/9/2018, genero = "Terror")
    kiernan = Ator.create(nome = "Kiernan Shipka", idade = 20, cache = "$60000", filme = february)
    elencoFebruary = Elenco.create(filme = february, ator = kiernan)
    julian = Diretor.create(nome = "Julian Grey", idade = 46, filme = february)
    abc = Estudio.create(local = "Los Angeles", qnt_salas = 13, tempo_uso = "4 meses")
    jairo = Funcionario.create(nome = "Jairo da Silva", cpf = "12332112342", estudio = abc)
    season2019 = FilmesLançados.create(filmes_prontos = ["Deixe a neve cair", "Silence"], estudio = abc)
    compraFilmes = CompraDeFilme.create(filme = february, valor = "$1000000000")
    dublagem_february = EquipeDublagem.create(nome_dublador = "Luiza Porto", cache = "$5000", papel = "Angie", filme = february)
    comprador = Comprador.create(filme = february, empresa = "Sony", valor = "$500000000")  
    print (season2019.filmes_prontos)

"""
{
  "Filme":
  {
  "titulo":"February",
  "dar_lancamento":7/9/2018,
  "genero":"Terror",
  }
}

{
  "Ator":
  {
  "nome":"Kiernan Shipka",
  "idade":20,
  "cache":"$60000",
  "filme" : {
     "nome:":"February"
     "dat_lancamento":7/9/2018
     "genero":"Terror
    },
  }
}
{
  "Elenco":
   {
    "filme" : {
     "nome:":"February"
     "dat_lancamento":7/9/2018
     "genero":"Terror
     },
    "ator" : {
     "nome":"Kiernan Shipka"
     "idade":20
     "cache":"$60000"
    },
   }
}
{
  "Diretor":
  {
  "nome":"Julian Grey",
  "idade":46,
  "filme" : {
    "nome:":"February"
    "dat_lancamento":7/9/2018
    "genero":"Terror
    },
  }
}

{
  "Estudio":
  {
  "local":"Los Angeles"
  "qnt_salas":13
  "tempo_uso":"4 meses"
  }
}
 
{
  "Funcionario":
  {
  "nome":"Jairo da Silva",
  "cpf":"12332112342",
  "estudio": {
    "local":"Los Angeles"
    "qnt_salas":13
    "tempo_uso":"4 meses"
  }
  }
}

{
  "FilmesLançados":
  {
    "filmes_prontos": [
      {
        "nome":"Deixe a neve cair" 
      },
      {
        "nome":"Silence"
      }
    ]      
    "estudio": {
      "local":"Los Angeles"
      "qnt_salas":13
      "tempo_uso":"4 meses"
  }
}

{
  "CompraDeFilme":[
    {
    "filme" : {
      "nome:":"February"
      "dat_lancamento":7/9/2018
      "genero":"Terror
      },
    "valor":"$1000000000",
    }
  ] 
}

{
  "EquipeDublagem":[
  {
  "nome_dublador":"Luiza Porto",
  "cache":"$5000",
  "papel":"Angie",
  "filme" : {
    "nome:":"February"
    "dat_lancamento":7/9/2018
    "genero":"Terror
    },
  }
  ] 
}

{
  "Comprador":[
  {
  "filme" : {
    "nome:":"February"
    "dat_lancamento":7/9/2018
    "genero":"Terror
    },
  "empresa":"Sony",
  "valor":"$500000000",
  }
  ] 
}
"""