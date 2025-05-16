import requests

def exemplo_cep():
    cep = "16702-510"
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    #nao precisa ser response

    if response.status_code == 200:
        dados_cep = response.json()
        print(f"Logradouro: {dados_cep['logradouro']}",)
        print(f"Bairro: {dados_cep['bairro']}")
        print(f"Localidade: {dados_cep['localidade']}")
        print(f"Estado: {dados_cep['estado']}")
        print(f"Região: {dados_cep['regiao']}")
    else:
        print(f"Erro: {response.status_code}\n")


def exemplo_get(id):
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"
    response = requests.get(url)
    if response.status_code == 200:
        dados_get_postagem = response.json()
        print(f"Titulo: {dados_get_postagem['title']}")
        print(f"Conteúdo: {dados_get_postagem['body']}")
        print(f"id: {dados_get_postagem['id']}")
    else:
        print(f"Erro: {response.status_code}\n")
#exemplo_get(5)


def exemplo_post():
    url = "https://jsonplaceholder.typicode.com/posts"
    nova_postagem = {"title": "Novo titulo",
                     "body": "Novo conteúdo",
                     "userId": 1
                     }
    response = requests.post(url, json=nova_postagem)
    if response.status_code == 201:
        dados_postagem = response.json()
        print(f"Titulo: {dados_postagem['title']}")
        print(f"Conteúdo: {dados_postagem['body']}")
    else:
        print(f"Erro: {response.status_code}\n")
#exemplo_post()


def exemplo_put(id):
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"
    nova_postagem = {
        "id": id,
        "title": "Novo titulo",
        "body": "Novo conteúdo",
        "userId": 1
    }
    antes = requests.get(url)
    response = requests.put(url, json=nova_postagem)
    if response.status_code == 200:
        if antes.status_code == 200:
            dados_antes = antes.json()
            print(f"Titulo: {dados_antes['title']}")
        else:
            print(f"Erro: {response.status_code}\n")
        dados_postagem = response.json()
        print(f"Titulo: {dados_postagem['title']}")
    else:
        print(f"Erro: {response.status_code}\n")
exemplo_put(1)