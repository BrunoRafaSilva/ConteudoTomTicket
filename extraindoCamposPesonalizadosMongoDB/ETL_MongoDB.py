# %% [markdown]
# # Importação do PyMongo e Requests

# %%
import requests,pymongo

# %% [markdown]
# # Parâmetros

# %%
client = pymongo.MongoClient("localhost",27017)
db = client["tomticket"]["chamados"]

ul = 'https://api.tomticket.com/chamados/dd9a5939c23a8c4e8075dd3a5645b6d3/1'

# %% [markdown]
# # Requisição e Tratamento Do Retorno

# %%
get = requests.get(ul)
response = get.json()
chamados = response["data"]

# %% [markdown]
# # Inserindo Dados no Banco e Fechando Conexão

# %%
db.insert_many(chamados)
client.close()


