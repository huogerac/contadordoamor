# 🏆 loveyou

## Entendendo o projeto

## BACKEND Django API

### Organização das camadas

### Estrutura de pastas

Visao geral

```shell
loveyou                   👉 Pasta raiz do projeto
 ├── README.md
 ├── manage.py                     👉 Django CLI (Ponto de entrada)
 ├── docker-compose.yml            👉 Descritor docker para rodar local
 ├── Dockerfile                    👉 Receita para rodar projeto
 ├── tox.ini
 ├── uwsgi.ini
 └── loveyou              👉 base do projeto
    ├── accounts                   👉 app relacionado a usuarios e autenticacao
    │   └── ...
    ├── core                       👉 app principal com o "core business" 
    │   └── ...
    └── loveyou           👉 centraliza configuracoes do projeto
        ├── api.py
        ├── settings.py            👉 Configuracoes principal do Django
        ├── urls.py                👉 Configuracao principal/inicial das rotas no Django
        └── wsgi.py
```


## Rodando o projeto

## Requisitos

- Git
- 🐍 Python 3.9.x ou 3.11.x (para utilizar Poetry)
- Um terminal (de preferência um terminal Linux, é para funcionar em um terminal WSL no Windows)

Temos três formas para **Rodar** 🍨:
- Sem Docker 📦: Apenas **Python** (usando sqlite)
- Apenas Banco de dados usando 🐋 Docker (melhor para debug)
- Tudo usando Docker 🐋: **Docker** and **Docker compose** (tudo rodando com um comando)

Links:
- Para entender [rodar com ou sem docker](https://www.djavue.org/README_EN.html#%F0%9F%90%8B-run-locally-using-docker-vs-not-using-docker-containers)
- [Para rodar tudo com docker](https://www.djavue.org/README_EN.html#%F0%9F%90%8B-running-all-with-docker)
- [Para rodar sem docker](https://www.djavue.org/README_EN.html#%F0%9F%93%A6-running-the-%F0%9F%A6%84-backend-without-docker)
- [Rodando com Poetry](https://www.djavue.org/README_EN.html#%F0%9F%93%A6-package-management-with-poetry)
