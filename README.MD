# Documentação do Projeto - Tasklist (Django + Vuejs) - Urbe

## Backend

### Decisões de Projeto

- **Framework Django:** O Django apresenta uma sintaxe bem intuitiva e ferramentas bem simples de utilizar no desenvolvimento web. Apesar de ter sido desafiador (por ser uma tecnologia nova para mim), foi muito interessante explorar algumas funcionalidades no desenvolvimento desse projeto.

- **Autenticação e Autorização:** Para autenticação de usuários, foi utilizado o pacote djoser que fornece endpoints para autenticação via Token e para operações de criação e gerenciamento de usuários. Além disso, foram configuradas permissões para garantir que apenas usuários autenticados possam acessar determinados endpoints da API.

- **Modelagem de Dados:** A estrutura de dados foi projetada para armazenar as tarefas dos usuários. Utilizou-se um modelo Tasklist com campos como título, status de conclusão e datas de criação e atualização. Foi implementada uma relação de Foreign key com o modelo de usuário padrão do Django para associar as tarefas a usuários específicos.

- **API RESTful:** A API foi desenvolvida seguindo os princípios RESTful para operações CRUD (Create, Read, Update, Delete) das tarefas. Foram definidos endpoints para login e registro de usuários, operações de criação, listagem, atualização e exclusão de tarefas.

- **Testes Automatizados:** Foram criados testes automatizados utilizando o módulo unittest do Django para garantir o funcionamento correto dos endpoints da API. Os testes cobrem cenários como criação, listagem, atualização e exclusão de tarefas.

### Instruções de Execução

1. **Pré-requisitos:** Certifique-se de ter o Python instalado em sua máquina. Recomenda-se o uso de um ambiente virtual para isolar as dependências do projeto.

2. **Instalação de Dependências:** Navegue até o diretório raiz do projeto e execute o seguinte comando para instalar as dependências listadas no arquivo requirements.txt:

   ```
   pip install django
   ```

3. **Configuração do Banco de Dados:** O projeto está configurado para usar o SQLite como banco de dados padrão. Certifique-se de que o arquivo db.sqlite3 seja criado automaticamente após a execução das migrações.
4. **Migrações do Banco de Dados:** Execute o seguinte comando para aplicar as migrações e criar as tabelas necessárias no banco de dados:

   ```
   python manage.py migrate
   ```

5. **Execução do Servidor:** Após instalar as dependências e configurar o banco de dados, execute o seguinte comando para iniciar o servidor de desenvolvimento:

   ```
   python manage.py runserver
   ```

6. **Testes Automatizados:** Para executar os testes automatizados, utilize o seguinte comando:
   ```
   python manage.py test
   ```

## Frontend

### Decisões de Projeto

- **Framework Vue.js:** Optou-se pelo Vue.js por ser mais intuitivo e com funcionalidades que atendem bem ao que foi pensado para o projeto, além da flexibilidade e eficiência no desenvolvimento de interfaces de usuário interativas.

- **Gerenciamento de Estado:** Para gerenciar o estado da aplicação, foi utilizado o Vuex, o gerenciador de estado oficial do Vue.js. Isso permitiu centralizar o estado compartilhado entre os componentes e facilitou a comunicação com a API backend.

- **Integração com API Backend:** Utilizou-se a biblioteca Axios para realizar requisições HTTP para a API backend. Foram implementadas funções para lidar com operações CRUD de tarefas, bem como para lidar com a autenticação de usuários.

- **Estilização com Tailwind CSS e SCSS:** Para estilizar a aplicação, foi utilizado o Tailwind CSS e SCSS devido à abordagem baseada em utilitários e sua capacidade de personalização. Isso permitiu a criação de uma interface limpa e responsiva com pouco esforço.

### Instruções de Execução

1. **Pré-requisitos:** Certifique-se de ter o Node.js e o npm (ou yarn) instalados em sua máquina.

2. **Instalação de Dependências:** Navegue até o diretório raiz do projeto frontend (comando no terminal: cd ./frontend, partindo do diretorio raiz) e execute o seguinte comando para instalar as dependências listadas no arquivo package.json:

   ```
   npm install
   ```

3. **Configuração da API Backend:** No arquivo de configuração do frontend (geralmente em src/config.js), verifique a URL da API backend para que as requisições possam ser direcionadas corretamente.

4. **Compilação e Execução:** Após instalar as dependências e configurar e executar a API backend em outro terminal simultaneamente, execute o seguinte comando para compilar e iniciar o servidor de desenvolvimento:

   ```
   npm run serve
   ```

5. **Acesso à Aplicação:** Abra o navegador e acesse a URL fornecida pelo servidor de desenvolvimento (geralmente http://localhost:8080) para visualizar a aplicação frontend.

## Rotas da API Backend

### POST /login/

#### Exemplo de Requisição:

```json
{
  "username": "testuser",
  "password": "12345"
}
```

Exemplo de Resposta (Sucesso):

```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJh...",
  "user_id": 5
}
```

### GET /list-create-tasklist/

#### Exemplo de Requisição:

Cabeçalho da Requisição:

```js

Authorization: Token eyJ0eXAiOiJKV1Qi...

```

#### Exemplo de Resposta (Sucesso - Listagem de Tarefas):

```json
[
  {
    "id": 1,
    "title": "Task 1",
    "completed": false,
    "create_date": "2024-03-23T12:00:00Z",
    "update_date": "2024-03-23T12:00:00Z"
  },
  {
    "id": 2,
    "title": "Task 2",
    "completed": true,
    "create_date": "2024-03-23T13:00:00Z",
    "update_date": "2024-03-23T13:00:00Z"
  }
]
```

### POST /list-create-tasklist/

#### Exemplo de Requisição:

Cabeçalho da Requisição:

```js

Authorization: Token eyJ0eXAiOiJKV1Qi...

```

Corpo da Requisição:

```json
{
  "title": "Nova Tarefa",
  "completed": false
}
```

#### Exemplo de Resposta (Sucesso - Criação de Tarefa):

```json
{
  "id": 3,
  "title": "Nova Tarefa",
  "completed": false,
  "create_date": "2024-03-24T10:00:00Z",
  "update_date": "2024-03-24T10:00:00Z"
}
```

## Rotas do Frontend

### Rota: '/'

Componente: Login

#### Exemplo de Entrada:

```json
{
  "username": "testuser",
  "password": "12345"
}
```

### Rota: '/signup'

Componente: Signup

#### Exemplo de Entrada:

```json
{
  "username": "novousuario",
  "password": "senhadonovousuario",
  "password2": "senhadonovousuario"
}
```

### Rota: '/about'

Componente: About - Página informativa.

### Rota: '/tasklist'

Componente: Tasklist

#### Exemplo de Entrada (Adicionar Nova Tarefa):

```json
{
  "title": "Nova Tarefa",
  "completed": false
}
```

#### Exemplo de Entrada (Editar Tarefa):

```json
{
  "title": "Tarefa Editada",
  "completed": true
}
```

#### Exemplo de Entrada (Alterar status da Tarefa):

```json
{
  "completed": true
}
```

## Conclusão

Este documento fornece uma visão geral dos processos de decisão e desenvolvimento do projeto Tasklist, incluindo detalhes sobre o backend, frontend e instruções para execução do projeto em suas máquinas. Se houver dúvidas ou sugestões de melhoria, sinta-se à vontade para entrar em contato com o autor.

## Autor

<a href="https://github.com/rafael-isidro">
    <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/118776145?v=4" width="100px;" alt="Foto de perfil - Rafael Isidro"/>
    <br />
    <sub><b>Rafael Santos Isidro</b></sub>
</a> 
<br />

<a href="https://github.com/rafael-isidro" title="Github">⚫ Github</a>
<br />
<a href="https://www.linkedin.com/in/rafael-isidro/" title="Linkedin">🔵 Linkedin</a>