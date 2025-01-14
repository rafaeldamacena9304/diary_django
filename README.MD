# Personal Diary App 📓✨

## Descrição do Projeto 🌟

Este projeto é uma **aplicação web** construída com o framework **Django** que permite aos usuários escrever registros diários de suas experiências, incluir pessoas em seus registros e visualizar suas entradas em datas específicas. A aplicação também possui gráficos interativos que mostram quantas vezes cada pessoa foi mencionada nos registros, proporcionando uma visão interessante sobre quem mais tem aparecido no seu diário. 

A ideia por trás deste projeto é criar uma plataforma simples, funcional e com uma interface amigável, para quem deseja manter um diário pessoal digital. 

## Funcionalidades 🚀

### 📜 Funcionalidades Principais:

- **Criação de Registros Diários**: Escreva um novo registro a qualquer momento, detalhando suas experiências, pensamentos ou acontecimentos do dia.
- **Cadastro de Pessoas**: Cadastre pessoas que aparecem em seus registros, para poder incluí-las em entradas específicas.
- **Exibição de Registros**: Visualize todos os seus registros por data, facilitando a busca e o controle de suas memórias.
- **Gráficos de Inclusão de Pessoas**: Veja quantas vezes cada pessoa foi mencionada em seus registros ao longo do tempo, através de gráficos interativos.
- **Exclusão de Registros**: Apague registros antigos que não são mais relevantes ou desejados.

### 🧑‍🤝‍🧑 Recursos Sociais:
- **Pessoas no Diário**: Adicione várias pessoas em seus registros, ajudando a acompanhar quem tem sido mais mencionada ao longo dos dias.
- **Histórico de Inclusões**: Veja um gráfico para entender melhor quais pessoas foram mais citadas, criando uma visão interessante sobre suas interações.

## Tecnologias Usadas 💻

- **Python 3.x**: A linguagem principal para o desenvolvimento da aplicação.
- **Django**: Framework web usado para o desenvolvimento do backend.
- **Tailwind CSS**: Framework CSS utilizado para estilizar a aplicação com design moderno e responsivo.
- **HTML5/CSS3**: Para a criação das páginas web.
- **JavaScript**: Usado para gerar gráficos dinâmicos interativos com as informações sobre as pessoas nos registros.
- **SQLite**: Banco de dados utilizado para armazenar os registros e informações de pessoas.

## Como o Projeto Funciona ⚙️

### Estrutura do Projeto:
1. **Banco de Dados**: A aplicação utiliza o banco de dados **SQLite** (configurado por padrão no Django) para armazenar os registros dos usuários e as pessoas associadas a cada registro.
2. **Cadastro de Registros e Pessoas**: Usuários podem criar novos registros diários e associar pessoas a eles, podendo visualizar suas entradas de acordo com as datas.
3. **Gráficos de Inclusão**: Usando **JavaScript** e gráficos interativos, a aplicação gera um gráfico que mostra quantas vezes cada pessoa foi mencionada em seus registros.
4. **Interface Responsiva**: O uso do **Tailwind CSS** garante que a interface seja moderna e responsiva, adaptando-se bem a diferentes tamanhos de tela.

### Rotas Importantes:
- **/diario**: Página inicial que exibe todos os registros diários do usuário.
- **/diario/escrever**: Formulário para adicionar um novo registro diário.
- **/diario/cadastrar_pessoa**: Formulário para cadastrar uma nova pessoa para incluir em seus registros.

## O que busquei agregar à comunidade 🌍

Este projeto visa criar uma aplicação simples e útil para quem deseja manter um diário pessoal digital, com uma funcionalidade extra de visualizar quem está sendo mais mencionado ao longo do tempo. Ao utilizar **Django**, este projeto serve como um ótimo exemplo de como integrar um framework robusto de backend com um design moderno e responsivo. 

Se você é iniciante em Django, este projeto pode ser uma excelente oportunidade para aprender como integrar essas tecnologias em uma aplicação prática e funcional.

## Instalação e Execução 🔧

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/seu-usuario/personal-diary-app.git
    ```

2. **Instale as dependências**:

    Crie e ative o ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

    Agora, instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure o banco de dados**:
    - O banco de dados **SQLite** já está configurado por padrão no Django. Apenas execute as migrações para criar as tabelas necessárias:

    ```bash
    python manage.py migrate
    ```

4. **Execute a aplicação**:

    ```bash
    python manage.py runserver
    ```

5. Abra o navegador e acesse `http://127.0.0.1:8000`.

---

✨ **Aproveite o projeto e mantenha seu diário pessoal atualizado!** 📓