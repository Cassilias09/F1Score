# 🏎️ F1Score Hub - Formula 1 Website for Data Analysis

![Project Status](https://img.shields.io/badge/status-development-orange)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)
![Flask Version](https://img.shields.io/badge/flask-2.x-lightgrey)

Um projeto de hobby Open Source para analisar e visualizar estatísticas da Fórmula 1. Desenvolvido como um monorepo, com um backend Flask servindo uma API REST e um frontend moderno para exibir os dados.

## 📝 Tabela de Conteúdos

1.  [Sobre o Projeto](#-sobre-o-projeto)
2.  [Funcionalidades](#-funcionalidades)
    * [Backend (Atual)](#backend-atual)
    * [Em Desenvolvimento / Próximos Passos](#em-desenvolvimento--próximos-passos)
3.  [Tecnologias Utilizadas](#-tecnologias-utilizadas)
    * [Backend](#backend)
    * [Frontend (Futuro)](#frontend-futuro)
4.  [Estrutura do Projeto](#-estrutura-do-projeto)
5.  [Como Começar](#-como-começar)
    * [Pré-requisitos](#pré-requisitos)
    * [Instalação](#instalação)
    * [Executando o Backend](#executando-o-backend)
    * [Explorando a API](#explorando-a-api)
6.  [Contribuições](#-contribuições)
7.  [Licença](#-licença)
8.  [Agradecimentos](#-agradecimentos)

---

## 🏁 Sobre o Projeto

O **F1Score Hub** é um projeto de hobby criado com o objetivo de servir como um ambiente de aprendizado e aprimoramento em desenvolvimento web. Ele busca oferecer uma plataforma para explorar e visualizar uma vasta gama de estatísticas da Fórmula 1, utilizando dados da biblioteca `FastF1`.

A ideia é construir um projeto Open Source, permitindo que entusiastas e desenvolvedores possam contribuir, aprender e expandir suas habilidades em um contexto real.

---

## ✨ Funcionalidades

### Backend (Atual)

Atualmente, o backend oferece os seguintes endpoints para dados de campeonato:

* **Classificação do Campeonato (Pilotos e Construtores):**
    * Obtenha a classificação final de pilotos e construtores para uma temporada específica.
    * **Endpoint:** `GET /api/championship/standings`
    * **Parâmetros de Query:**
        * `season` (inteiro, obrigatório): O ano da temporada (ex: `2023`).

### Em Desenvolvimento / Próximos Passos

* **Dados de Corridas:**
    * Listar todas as corridas de uma temporada.
    * Obter resultados detalhados de uma corrida específica.
* **Estatísticas de Pilotos:** Desempenho ao longo da carreira, comparação com outros pilotos, etc.
* **Estatísticas de Equipes:** Histórico de desempenho, análise de construtores.
* **Visualizações de Dados:** Implementação do frontend para exibir os dados de forma interativa (tabelas, gráficos).
* **Voltas Mais Rápidas:** Análise das voltas mais rápidas por corrida e temporada.
* **Análise de Pit Stops:** Tempos médios e estratégias.

---

## 🛠️ Tecnologias Utilizadas

Este projeto utiliza uma arquitetura de monorepo para organizar o backend e o frontend.

### Backend

* **Python:** Linguagem de programação principal.
* **Flask:** Micro-framework web para o desenvolvimento da API REST.
* **`fastf1`:** Biblioteca para extrair dados históricos da Fórmula 1.
* **`flask-smorest`:** Extensão para Flask que simplifica a criação de APIs RESTful e gera documentação OpenAPI (Swagger UI).
* **`Marshmallow`:** Biblioteca para serialização/desserialização e validação de objetos Python.
* **`Flask-CORS`:** Para lidar com políticas de Cross-Origin Resource Sharing.
* **`python-dotenv`:** Para gerenciar variáveis de ambiente.

### Frontend (Futuro)

* **Framework (a ser definido):** React, Vue.js ou Svelte (provavelmente Vue.js para iniciantes ou React para robustez).
* **TypeScript:** Para adicionar tipagem estática ao JavaScript.
* **Vite:** Ferramenta de build rápida para desenvolvimento frontend.

---

## 📂 Estrutura do Projeto

A arquitetura do projeto é um monorepo com separação clara entre backend e frontend.

/F1Score
├── /backend                    # Código do backend (API REST)
│   ├── app.py                  # Ponto de entrada da aplicação Flask
│   ├── config.py               # Configurações da aplicação
│   └── /src
│       ├── /controllers        # Controladores da API (Flask-Smorest, MethodView)
│       │   └── /championship   # Controladores relacionados a campeonatos
│       │       └── championship_controller.py
│       ├── /schemas            # Schemas de dados e filtros (Marshmallow)
│       │   └── /championship   # Schemas relacionados a campeonatos
│       │       ├── championship_filter_schema.py
│       │       └── championship_schema.py
│       ├── /services           # Lógica de negócio e integração com FastF1
│       │   └── championship_service.py # Serviço de campeonato
│       └── /utils              # Utilitários gerais
│           └── http.py         # Ex: Utilitários HTTP
├── /eda                        # Análise Exploratória de Dados
│   └── championship_eda.ipynb  # Notebooks Jupyter para análise de dados
├── /frontend                   # (Será adicionado) Código do frontend
│   └── ...
├── .gitignore                  # Arquivos e pastas a serem ignorados pelo Git
└── README.md                   # Este arquivo

---

## 🚀 Como Começar

Siga estas instruções para configurar e executar o backend do projeto em sua máquina local.

### Pré-requisitos

Certifique-se de ter o seguinte instalado:

* **Python 3.12+**
* **pip** (gerenciador de pacotes do Python)

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Cassilias09/F1Score.git](https://github.com/Cassilias09/F1Score.git)
    cd F1Score/backend
    ```

2.  **Crie e ative um ambiente virtual:**
    É altamente recomendável usar um ambiente virtual para isolar as dependências do projeto.
    ```bash
    python -m venv .venv
    ```
    * No Windows:
        ```bash
        .venv\Scripts\activate
        ```
    * No macOS/Linux:
        ```bash
        source .venv/bin/activate
        ```

3.  **Instale as dependências do backend:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configuração de Variáveis de Ambiente (`.env`):**
    Crie um arquivo `.env` na raiz da pasta `backend` (ao lado de `app.py` e `requirements.txt`).
    Por enquanto, nenhuma variável de ambiente crítica é necessária para o funcionamento básico, mas é uma boa prática já ter o arquivo.
    ```ini
    # .env
    # Adicione variáveis de ambiente aqui se necessário no futuro
    FLASK_APP=app.py
    FLASK_ENV=development # Altere para 'production' em ambiente de produção
    ```

5.  **Criação da pasta de cache do FastF1:**
    O FastF1 utiliza cache para evitar downloads repetidos de dados. Certifique-se de que a pasta `src/cache/fastf1` exista na raiz do seu diretório `backend`. Você pode criá-la manualmente:
    ```bash
    cd src
    mkdir cache
    cd cache
    mkdir fastf1
    ```

### Executando o Backend

1.  Certifique-se de que seu ambiente virtual esteja ativado (`.venv` ativado).
2.  Na raiz da pasta `backend`, execute a aplicação Flask:
    ```bash
    flask run
    ```
    O servidor estará rodando em `http://127.0.0.1:5000`.

### Explorando a API

Após iniciar o backend, você pode acessar a documentação interativa da API (Swagger UI) em:

* `http://127.0.0.1:5000/swagger`

Você pode testar o endpoint de classificação diretamente no Swagger UI ou usando ferramentas como cURL/Postman/Insomnia:

* **Exemplo:** Obter a classificação do campeonato de 2023:
    ```bash
    curl "[http://127.0.0.1:5000/api/championship/standings?season=2023](http://127.0.0.1:5000/api/championship/standings?season=2023)"
    ```

---

## 🤝 Contribuições

Contribuições são **muito bem-vindas**! Seja corrigindo bugs, adicionando novas funcionalidades, melhorando a documentação ou otimizando o código. Para contribuir:

1.  Faça um fork do repositório.
2.  Crie uma nova branch (`git checkout -b feature/sua-funcionalidade`).
3.  Faça suas alterações e commit (`git commit -m 'feat: adiciona nova funcionalidade X'`).
4.  Envie suas alterações para o seu fork (`git push origin feature/sua-funcionalidade`).
5.  Abra um Pull Request descrevendo suas mudanças.

Por favor, siga as melhores práticas de código e teste suas alterações.

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) (será criado) para mais detalhes.

---

## 🙌 Agradecimentos

* À comunidade da Fórmula 1 e aos desenvolvedores do `FastF1` por fornecerem dados e ferramentas incríveis.
* Ao Flask e às extensões de código aberto que tornam este projeto possível.
* A todos os futuros colaboradores e entusiastas!

---
