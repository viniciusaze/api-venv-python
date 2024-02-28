#Começo e criação da rota

from fastapi import FastAPI, Query
import requests

app = FastAPI()

# Vamos definir um endpoint simples que retorna uma saudação quando acessado?

@app.get('/api/hello')
def hello_world():
    '''
    
    Endpoint que exibe uma mensagem no mundo da programação

    '''
    return {'Hello':'Word'}

# Aqui, definimos um endpoint simples que retorna uma saudação quando acessado.

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
    '''
    
    Endpoint para exibir o cardápio dos restaurantes

    '''
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)

# No próximo endpoint, realizamos uma requisição à API de restaurantes. Caso a resposta seja bem-sucedida (código 200), o código percorre cada item nesse objeto, representando um restaurante, e extrai dados específicos, como o nome do restaurante (Company), o item oferecido (Item), o preço (price), e a descrição (description).

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                }) 
        return {'Restaurante': restaurante, 'Cardápio': dados_restaurante}
    
# Se a resposta for 200, indicando o sucesso da requisição, o código percorre cada item do objeto dados_json e extrai os dados desejados para o restaurante específico fornecido como parâmetro. O resultado é então retornado no formato de um dicionário contendo o nome do restaurante (Restaurante) e seu cardápio (Cardapio). Caso a requisição não seja bem-sucedida, o código retorna um dicionário indicando o erro ocorrido, incluindo o código de status e o texto da resposta.

    else: 
        return {'Erro':f'{response.status_code} - {response.text}'}
    
# Lembre-se: é importante verificar o status code, processar os dados, e retornar informações específicas com base nos parâmetros fornecidos com a versatilidade do FastAPI o torna uma escolha sólida para uma variedade de casos de uso, proporcionando alta performance e uma experiência de desenvolvimento agradável com Python.