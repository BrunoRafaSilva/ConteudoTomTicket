let abrirChamado = new FormData();

abrirChamado.append('titulo', 'Nome do Chamado');
abrirChamado.append('id_departamento', '9e4667bd129b50aecbab4ec31f1792a9');
abrirChamado.append('id_tipoassunto', 'fac0bf1de89a884cae6bad4b50ed51ed');
abrirChamado.append('mensagem','Chamado criado \n Via API, utilizando JavaScript.')

fetch('https://api.tomticket.com/criar_chamado/09d1992e784d427251007c5c54d830be/9994',{
    method: 'POST',
    body: abrirChamado
})
    .then(response => response.json())
    .then(data => {
        console.log(data);
    })

    