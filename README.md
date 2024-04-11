# API de Gerenciamento de Desenvolvedores

Este é um exemplo de uma API simples construída com Flask para gerenciar informações de desenvolvedores. A API permite adicionar, listar, atualizar e excluir informações de desenvolvedores.

## Funcionalidades

- **Listar todos os desenvolvedores:** `GET /dev/`
  - Retorna uma lista de todos os desenvolvedores cadastrados.

- **Adicionar um novo desenvolvedor:** `POST /dev/`
  - Permite adicionar um novo desenvolvedor. Os dados devem ser enviados no formato JSON no corpo da requisição.

- **Obter, Atualizar ou Excluir um desenvolvedor pelo ID:**
  - **Obter:** `GET /dev/<int:id>/`
  - **Atualizar:** `PUT /dev/<int:id>/`
  - **Excluir:** `DELETE /dev/<int:id>/`
  - Permite obter, atualizar ou excluir um desenvolvedor específico com base em seu ID. O ID do desenvolvedor deve ser fornecido na URL da requisição.

## Como Executar

1. Certifique-se de ter o Python instalado em seu sistema.
2. Testando com Postman

Você também pode testar a API usando o Postman, uma ferramenta útil para testar APIs web. Siga estas etapas para começar:

1. Baixe e instale o [Postman](https://www.postman.com/downloads/) em seu sistema.
3. Use a coleção para enviar solicitações à sua API e visualizar as respostas.

Certifique-se de ajustar as configurações de ambiente no Postman, como a URL base da sua API.

## Contribuição
Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões para melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Autor
Este exemplo foi desenvolvido por [Eduardo (~Dux)].
