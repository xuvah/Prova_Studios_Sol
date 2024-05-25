Prova de Programação - Backend - 05/2024  
Candidato Filipe Augusto Marques de Paula

Este é um projeto desenvolvido como parte do processo seletivo para os Studios Sol.

Descrição:
O projeto consiste em uma API GraphQL para calcular o número de combinações possíveis de placares em uma partida de futebol americano, considerando os pontos marcados por cada equipe.

A lógica implementada tem complexidade O(n) pois para cada entrada é calculado a quantidade de combinações das somas para todos inteiros de 0 até n.

Execução:

-Certifique-se de ter o Docker instalado. 

-Dentro do projeto execute o comando 'make build' para construir a imagem do Docker

-Execute 'make up' para iniciar o container

- A api estará disponível para testes manuais em 'http://localhost:8080/graphql'

-Para executar os testes automatizados execute 'make test'

Testes automatizados:

Os testes automatizados consistem em 4 testes com placares factíveis e 10 testes aleatórios, que podem resultar em resultados infactíveis, o resultado de combinações esperado para placares infactíveis é 0.