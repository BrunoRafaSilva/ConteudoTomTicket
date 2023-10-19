import requests

ruby={
    'id_departamento':'e7db68ceda0c625573535cf04917f1d3',
    'titulo':'Extração será feita com Ruby!!',
    'mensagem':'mensagem meramente ilustrativa',
    'id_tipoassunto':'9a3121d66db5e9783ed400c05095f434'
}

def abrirChamados(id):
    apilink = f'https://api.tomticket.com/criar_chamado/{token}/{id}'
    r = requests.post(apilink, data=ruby)

abrirChamados(12345)