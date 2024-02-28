import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url) # Para solicitar (pegar) os dados.
print(response)

if response.status_code == 200:
    dados_json = response.json() # Usamos .json() para puxar este tipo específico de informação

    # Separando os itens do json:
    dados_restaurante = {}
    for item in dados_json:
        nome_do_restaurante = item['Company']
        # Se o restaurante não estiver dentro do dicionario criado...
        if nome_do_restaurante not in dados_restaurante:
            # Se o nome do restaurante não estiver em dados_restaurante, vamos criar uma nova lista vazia, que podemos começar a popular. Ou seja, tudo que é desse restaurante vamos colocar nesse item.
            # Por isso, podemos colocar um dados_restaurante[nome_do_restaurante].append() para colocar o item de fato.
            dados_restaurante[nome_do_restaurante] = []

        dados_restaurante[nome_do_restaurante].append({
            "item": item['Item'],
            "price": item['price'],
            "description": item['description']
        })

else:
    print(f'O erro foi {response.status_code}')

# Agora queremos pegar o nome do restaurante e os dados que estão dentro dos itens desses dados.

# Criando um arquivo json para cada restaurante:
    
for nome_do_restaurante, dados in dados_restaurante.items():
    nome_do_arquivo = f'{nome_do_restaurante}.json'
    with open(nome_do_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados,arquivo_restaurante,indent=4)

#O método .items() retorna uma lista de tuplas, onde cada tupla é composta por um par (chave, valor). Assim, quando fazemos for nome_do_restaurante, dados in dados_restaurante.items(), estamos basicamente dizendo "para cada par (chave, valor) no dicionário dados_restaurante, atribua a chave à variável nome_do_restaurante e o valor à variável dados

#Por exemplo, se tivermos um dicionário dados_restaurante = {'Burguer King': {'item': 'Whopper', 'price': 46.35}}, na primeira (e única, neste caso) iteração do loop, nome_do_restaurante será 'Burguer King' e dados será {'item': 'Whopper', 'price': 46.35}.