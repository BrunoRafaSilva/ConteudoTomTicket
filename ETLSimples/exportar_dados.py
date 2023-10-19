import requests
import mysql.connector

response = requests.get('https://api.tomticket.com/chamados/{SEU_TOKEN}/1')
retorno = response.json()
chamados = retorno['data']

db_config = {
    "host": "127.0.0.1",
    "port": "3306",
    "user": "root",
    "password": "root",
    "database": "etl"
}
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

for chamado in chamados:
    idchamado = chamado.get("idchamado")
    protocolo = chamado.get("protocolo")
    titulo = chamado.get("titulo")
    mensagem = chamado.get("mensagem")
    nomecliente = chamado.get("nomecliente")
    ultimasituacao = chamado.get("ultimasituacao")
    dataultimasituacao = chamado.get("dataultimasituacao")
    descsituacao = chamado.get("descsituacao")
    categoria = chamado.get("categoria")
    departamento = chamado.get("departamento")
    atendente = chamado.get("atendente")
    id_cliente = chamado.get("id_cliente")
    nomeorganizacao = chamado.get("nomeorganizacao")
    
    insert_query = "INSERT INTO CHAMADOS (idchamado, protocolo, titulo, mensagem, nomecliente, ultimasituacao, dataultimasituacao, descsituacao, categoria, departamento, atendente, id_cliente, nomeorganizacao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    data = (idchamado, protocolo, titulo, mensagem, nomecliente, ultimasituacao, dataultimasituacao, descsituacao, categoria, departamento, atendente, id_cliente, nomeorganizacao)
    cursor.execute(insert_query, data)
    
connection.commit()
cursor.close()
connection.close()

