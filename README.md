# wsBackend-Fabrica25.2
Este projeto é uma aplicação web feita em Django, desenvolvida para ser um gerenciador de biblioteca pessoal. A principal característica é a automação: em vez de digitar todas as informações de um livro manualmente, o sistema busca e preenche os dados usando uma API pública.

A espinha dorsal do projeto são dois modelos de dados: Livro e Autor. Quando você insere o título de um livro, a aplicação consulta a Open Library API. Se o autor ainda não estiver cadastrado, a aplicação o cria automaticamente. Depois, ela cadastra o livro com todos os detalhes obtidos da API e os vincula ao autor correto.

A aplicação inclui todas as operações básicas de CRUD (criar, ler, atualizar e deletar) para livros e autores. A interface é construída com HTML e CSS. 
