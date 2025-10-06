# 🚀 Jornada Engenheiro de Software: 62 Sessões de Código

![Python](https://img.shields.io/badge/Python-3.13-blue.svg?style=for-the-badge&logo=python)
![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Em%20Progresso-green.svg?style=for-the-badge)

Este repositório documenta minha jornada de 62 sessões de estudo focado, com o intuito de avaliar a capacidade de aprendizagem junto a IA. O intuito é reforçar as práticas que são voltadas para a Engenharia de Software. 

Para este projeto, foi desenvolvido um GEM (Gemini), o qual chamei de DevPartner AI, e com ele estou cobrindo desde os fundamentos de Python, Estruturas de Dados, até o desenvolvimento de uma API completa com deploy na nuvem.

Este projeto é a prova viva e o registro periódico do meu comprometimento, evolução e da aplicação prática de cada conceito aprendido.

---

## 🎯 Objetivo

O objetivo final é, ao longo de 62 **sprints** (sessões de estudo focado), avaliar a capacidade da IA em ensinar e construir um portfólio robusto, no qual ela vai auxiliando na capacidade de adquirir as competências técnicas e com isso vou estruturando a mentalidade de um Engenheiro de Software Pleno, cobrindo os pilares de Backend, DevOps e Cloud.

---

## 🛠️ Stack de Tecnologias em Desenvolvimento

* **IA Generativa:** DevPartner AI (Gem criado com a função voltada a programação, ensino e desenvolvimento de projetos)
* **Linguagem:** Python
* **Fundamentos:** Programação Orientada a Objetos (POO), Princípios SOLID, Estruturas de Dados e Algoritmos (EDA)
* **Backend:** FastAPI, Pydantic
* **Banco de Dados:** PostgreSQL, SQL, SQLAlchemy
* **Testes:** Pytest
* **Infraestrutura & DevOps:** Git, GitHub, Docker, Terraform, CI/CD com GitHub Actions
* **Cloud:** Google Cloud Platform (GCP) ou AWS *(Aguardando decisão futura com base no estudo para certificação em nuvem)*
* **Frontend:** Vue.js (previsto)


---

## 📖 Diário de Bordo (Progresso das Sessões)

Esta tabela registra o progresso em cada sessão de estudo.

| Sessão | Tópico Principal | Status | Link para o Código |
| :--- | :--- | :---: | :---: |
| **Fase 1: Fundamentos de Engenharia** |
| 01 | Fundamentos de Python: Variáveis, Tipos e Operadores | ✅ | [Ver Código](./learning-journal/sessao_01/) |
| 02 | Estruturas de Controle: `if`, `for`, `while` | ✅ | [Ver Código](./learning-journal/sessao_02/) |
| 03 | Funções (`def`), DRY e Escopo | ✅ | [Ver Código](./learning-journal/sessao_03/) |
| 04 | Interação com Arquivos: Lendo CSV e Escrevendo TXT | ✅ | [Ver Código](./learning-journal/sessao_04/) |
| 05 | Módulos e Estrutura de Projetos (Teoria) | ✅ | [Ver Nota](./learning-journal/sessao_05/) |
| 06 | POO: Classes, Objetos, `__init__`, `self` | ✅ | [Ver Código](./learning-journal/sessao_06/) |
| 07 | POO: Princípios SOLID (Teoria) | ✅ | [Ver Nota](./learning-journal/sessao_07/) |
| 08 | EDA: Big O Notation e Listas/Arrays | ✅ | [Ver Código](./learning-journal/sessao_08/) |
| 09 | EDA: Pilhas (Stacks) e Filas (Queues) | ✅ | [Ver Código](./learning-journal/sessao_09/) |
| 10 | EDA: Listas Ligadas (Linked Lists) | ✅ | [Ver Código](./learning-journal/sessao_10/) |
| 11 | EDA: Hash Maps (Dicionários) | ✅ | [Ver Código](./learning-journal/sessao_11/) |
| 12 | EDA: Árvores (Trees) e Noções de Busca | ✅ | [Ver Código](./learning-journal/sessao_12/) |
| 13/14 | Git Workflow: Branches e Pull Requests | ✅ | *(Workflow do Repositório)* |
| 15 | Testes Unitários com `Pytest` | ✅ | *[Ver Testes](./tests/)* |
| **Fase 2: Construção do Backend de Alta Performance** |
| 16 | Fundamentos Web (HTTP, JSON) e introdução a APIs REST. | ✅ | [Ver Nota](./learning-journal/sessao_16/) |
| 17 | FastAPI - Primeiros Passos (Rotas, Parâmetros de Path/Query). | ✅ | [Ver Código](./learning-journal/sessao_17/) |
| 18 | FastAPI & Pydantic - Validação de Dados e Modelos. | ✅ | [Ver Código](./app/) |
| 19 | Projeto do Banco de Dados - Modelagem relacional para a "Central de Ativos". | ✅ | [Ver Código](./app/) |
| 20 | SQL Avançado - JOINs, Índices e Transações. | ✅ | [Ver Código](./app/database/) |
| 21 | Introdução ao ORM com SQLModel e SQLAlchemy. | ⏳ | *(A ser iniciado)* |
| 22 | Conectando o FastAPI ao PostgreSQL. | ⏳ | *(A ser iniciado)* |
| 23 | Implementando a rota POST (Criar Ativo). | ⏳ | *(A ser iniciado)* |
| 24 | Implementando as rotas GET (Listar e Detalhar Ativos). | ⏳ | *(A ser iniciado)* |
| 25 | Implementando as rotas PUT e DELETE (Atualizar e Remover). | ⏳ | *(A ser iniciado)* |
| 26 | Lógica de Negócio e Relações (ex: associar ativo a um usuário), incluindo list comprehension. | ⏳ | *(A ser iniciado)* |
| 27 | Testando a API com Pytest e HTTPX. | ⏳ | *(A ser iniciado)* |
| 28 | Tratamento de Erros e Respostas HTTP. | ⏳ | *(A ser iniciado)* |
| 29 | Autenticação com OAuth2 e JWT (Teoria). | ⏳ | *(A ser iniciado)* |
| 30 | Implementação de Login e Rotas Protegidas. | ⏳ | *(A ser iniciado)* |
| 31 | Introdução ao Caching com Redis. | ⏳ | *(A ser iniciado)* |
| 32 | Implementando Cache na API para otimizar consultas. | ⏳ | *(A ser iniciado)* |
| **Fase 3: Criando a Interface do Usuário** |
| 33 | Fundamentos Web - HTML5 Semântico e CSS com Flexbox. | ⏳ | *(A ser iniciado)* |
| 34 | Fundamentos Web - CSS com Grid e Design Responsivo. | ⏳ | *(A ser iniciado)* |
| 35 | JavaScript Moderno (ES6+) - Variáveis, Funções, async/await. | ⏳ | *(A ser iniciado)* |
| 36 | JavaScript - Manipulação do DOM e Eventos. | ⏳ | *(A ser iniciado)* |
| 37 | Introdução ao Vue.js (Setup, Componentes, Reatividade). | ⏳ | *(A ser iniciado)* |
| 38 | Vue.js - Diretivas, Eventos e Propriedades Computadas. | ⏳ | *(A ser iniciado)* |
| 39 | Estruturando o projeto do Painel de Controle. | ⏳ | *(A ser iniciado)* |
| 40 | Consumindo a API FastAPI com axios. | ⏳ | *(A ser iniciado)* |
| 41 | Construindo a tela de Listagem de Ativos. | ⏳ | *(A ser iniciado)* |
| 42 | Construindo o Formulário de Criação/Edição de Ativos. | ⏳ | *(A ser iniciado)* |
| 43 | Gerenciamento de Estado (ex: Pinia). | ⏳ | *(A ser iniciado)* |
| 44 | Implementando um Sistema de Notificações no Frontend. | ⏳ | *(A ser iniciado)* |
| 45 | Polimento da UI/UX e build para produção. | ⏳ | *(A ser iniciado)* |
| **Fase 4: Engenharia de Produção (DevOps & Cloud)** |
| 46 | Docker - Containerizando a API Python (Dockerfile). | ⏳ | *(A ser iniciado)* |
| 47 | Docker - Containerizando o Frontend Vue/Nginx. | ⏳ | *(A ser iniciado)* |
| 48 | Docker Compose - Orquestrando o ambiente local (API + DB + Frontend). | ⏳ | *(A ser iniciado)* |
| 49 | Introdução à Cloud (GCP) e configuração da conta. | ⏳ | *(A ser iniciado)* |
| 50 | Terraform - Fundamentos e provisionamento de uma VPC. | ⏳ | *(A ser iniciado)* |
| 51 | Terraform - Provisionando o Banco de Dados (Cloud SQL). | ⏳ | *(A ser iniciado)* |
| 52 | Terraform - Provisionando o Serviço de Aplicação (Cloud Run). | ⏳ | *(A ser iniciado)* |
| 53 | Introdução ao CI/CD com GitHub Actions. | ⏳ | *(A ser iniciado)* |
| 54 | CI/CD - Pipeline para rodar testes a cada commit. | ⏳ | *(A ser iniciado)* |
| 55 | CI/CD - Pipeline para construir e publicar imagens Docker. | ⏳ | *(A ser iniciado)* |
| 56 | CI/CD - Pipeline para fazer o deploy com Terraform. | ⏳ | *(A ser iniciado)* |
| 57 | Gestão de Segredos na Nuvem (Google Secret Manager). | ⏳ | *(A ser iniciado)* |
| 58 | Configurando Domínio e HTTPS. | ⏳ | *(A ser iniciado)* |
| 59 | Fundamentos de Logging e Monitoramento (Cloud Logging). | ⏳ | *(A ser iniciado)* |
| 60 | Otimização de Custos e Alertas de Orçamento. | ⏳ | *(A ser iniciado)* |
| **Fase 5: Polimento e Finalização do Projeto** |
| 61 | Refatoração Final do Código (Backend e Frontend). | ⏳ | *(A ser iniciado)* |
| 62 | Elaboração de um README.md profissional para o projeto no GitHub. | ⏳ | *(A ser iniciado)* |
---

## 🚀 Como Executar (Setup do Projeto)

Atualmente, o projeto está estruturado com ambientes virtuais padrão do Python.

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/Ricardo-Andrade938/Jornada_Engenheiro_de_Software.git](https://github.com/Ricardo-Andrade938/Jornada_Engenheiro_de_Software.git)
    cd Jornada_Engenheiro_de_Software
    ```
2.  **Crie e ative o ambiente virtual:**
    ```bash
    # Cria o ambiente virtual na pasta 'venv'
    python -m venv venv

    # Ativa o ambiente no PowerShell (Windows)
    .\venv\Scripts\Activate
    ```
3.  **Execute um script de sessão:**
    Navegue até a pasta da sessão desejada e execute o arquivo.
    ```bash
    cd sessao_12
    python session_12.py
    ```

*Nota: Este projeto será migrado para o **Poetry** em breve para um gerenciamento de dependências mais robusto, alinhado com as práticas modernas de desenvolvimento de aplicações.*