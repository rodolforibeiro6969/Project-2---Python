# Relatório Técnico do Sistema de Quiz Interativo

## Índice
1. [Introdução](#introdução)  
2. [Arquitetura e Componentes do Sistema](#arquitetura-e-componentes-do-sistema)  
    2.1. [Base de Dados (SQLite)](#base-de-dados-sqlite)  
    2.2. [Interface Gráfica (Tkinter)](#interface-gráfica-tkinter)  
    2.3. [Gestão de Utilizadores](#gestão-de-utilizadores)  
    2.4. [Gestão de Perguntas e Respostas](#gestão-de-perguntas-e-respostas)  
    2.5. [Temporizador e Fluxo de Perguntas](#temporizador-e-fluxo-de-perguntas)  
    2.6. [Armazenamento de Resultados](#armazenamento-de-resultados)  
3. [Fluxo de Execução](#fluxo-de-execução)  
4. [Importação e Correção de Perguntas](#importação-e-correção-de-perguntas)  
5. [Segurança e Boas Práticas](#segurança-e-boas-práticas)  
6. [Melhorias Futuras](#melhorias-futuras)  
7. [Conclusão](#conclusão)

---

## Introdução
Este relatório, realizado no âmbito da UFCD 5417 do formador Nelson Santos, descreve em detalhe o funcionamento de um sistema de quiz interativo escrito em Python, que combina a biblioteca Tkinter para a criação de uma interface gráfica com a gestão de dados através de SQLite. O objetivo principal do sistema é permitir que um utilizador se registe ou inicie sessão, responda a um conjunto de perguntas aleatórias, receba feedback imediato sobre cada resposta e, no final, tenha a sua pontuação registada na base de dados.

---

## Arquitetura e Componentes do Sistema

### Base de Dados (SQLite)
A base de dados local `quiz.db` é gerida através do **SQLite**, o que simplifica o processo de configuração e distribuição do sistema, dispensando a necessidade de um servidor de base de dados dedicado. A base de dados contém três tabelas principais:

- **users:** Armazena informações sobre cada utilizador, incluindo nome de utilizador (único), palavra-passe e, opcionalmente, pontuações ou estatísticas adicionais.
- **questions:** Contém o enunciado da pergunta, quatro opções de resposta e um índice que identifica qual a opção correta.
- **results:** Regista as pontuações obtidas pelos utilizadores após a conclusão do quiz, juntamente com a data em que o resultado foi armazenado.

Esta divisão permite um fácil acesso a dados, garantindo simultaneamente a organização e a manutenção das informações num formato simples, mas eficaz.

### Interface Gráfica (Tkinter)
A interface com o utilizador é inteiramente desenvolvida com **Tkinter**, um toolkit padrão do Python para GUI. Existem duas janelas principais:

1. **Janela de Login/Registo:** Apresenta campos para introduzir nome de utilizador e palavra-passe, juntamente com botões para efetuar login ou criar um novo registo.  
2. **Janela do Quiz:** Exibe as perguntas, as opções de resposta e o temporizador. É também responsável por mostrar mensagens de feedback (correto ou incorreto) e, no final, informa o utilizador sobre a sua pontuação global.

A interface prioriza a simplicidade, garantindo assim que o utilizador navegue facilmente no sistema.

### Gestão de Utilizadores
A funcionalidade de gestão de utilizadores permite que novos utilizadores se registem, sendo as suas credenciais guardadas na tabela `users`. A autenticação é feita comparando o nome de utilizador e a palavra-passe introduzidos pelo utilizador com os armazenados na base de dados. Caso haja correspondência, o utilizador é autenticado e pode iniciar o quiz. Caso contrário, recebe uma mensagem de erro.

### Gestão de Perguntas e Respostas
As perguntas encontram-se na tabela `questions`. Sempre que o quiz é iniciado, são selecionadas 10 perguntas de forma aleatória (através de uma query SQL com `ORDER BY RANDOM() LIMIT 10`). Cada pergunta possui quatro opções de resposta, sendo uma delas a correta.

Para aumentar a imprevisibilidade, as opções são embaralhadas antes de serem apresentadas. Quando o utilizador seleciona uma resposta, o código compara a opção escolhida com a resposta correta. Caso a resposta esteja certa, incrementa-se o `score` do utilizador; caso contrário, é exibida uma mensagem de erro, indicando a resposta correta.

### Temporizador e Fluxo de Perguntas
Cada pergunta é acompanhada por um temporizador (por defeito, 10 segundos). Caso o tempo se esgote antes do utilizador responder, a pergunta é considerada falhada e o sistema avança para a próxima questão. Este mecanismo aumenta o desafio e a dinâmica do quiz, evitando que o utilizador fique indefinidamente a pensar numa única pergunta.

Após o utilizador responder (ou após o temporizador expirar), o sistema carrega a próxima pergunta. Quando não existem mais perguntas, o quiz termina.

### Armazenamento de Resultados
Ao finalizar o quiz, a pontuação do utilizador é registada na tabela `results`. Esta operação utiliza uma subquery para associar o `user_id` ao `username` do utilizador, garantindo a rastreabilidade de resultados. Desta forma, o sistema pode futuramente apresentar estatísticas, histórico de pontuações ou rankings.

---

## Fluxo de Execução
O fluxo normal de execução é o seguinte:

1. **Login/Registo:** O utilizador inicia a aplicação e insere o seu nome de utilizador e palavra-passe. Se ainda não tiver conta, pode registá-la no momento.
2. **Início do Quiz:** Após o login com sucesso, a janela do quiz é aberta e o sistema carrega um conjunto de 10 perguntas aleatórias.
3. **Respostas e Temporizador:** O utilizador seleciona uma resposta para cada pergunta. Caso não responda a tempo, a próxima pergunta é exibida.
4. **Cálculo da Pontuação:** À medida que o utilizador responde, o `score` é incrementado para cada resposta correta.
5. **Finalização:** Ao terminar as perguntas, o sistema mostra a pontuação final, regista o resultado na base de dados e encerra o quiz.

---

## Importação e Correção de Perguntas
Para facilitar a manutenção do conteúdo, as perguntas podem ser importadas a partir de um ficheiro CSV. O código apresentado inclui trechos comentados que permitem carregar um conjunto de perguntas a partir de um ficheiro externo e inseri-las na tabela `questions`. Além disso, existe uma função para corrigir índices de respostas e gerar um ficheiro Excel com as questões corrigidas, garantindo a integridade e consistência do conteúdo.

---

## Segurança e Boas Práticas
Atualmente, o sistema armazena palavras-passe em texto simples, o que não é recomendável. Melhorias futuras deveriam envolver a aplicação de hashing e salt nas passwords para aumentar a segurança. Além disso, poderia ser implementada uma lógica de contagem de tentativas de login falhadas e bloqueio temporário, reduzindo o risco de ataques de força bruta.

Outro aspeto a melhorar é a validação da entrada de utilizador e o tratamento de erros. Exceções em operações com a base de dados ou em tentativas de carregar perguntas devem ser geridas de forma mais robusta, fornecendo feedback adequado ao utilizador e registando erros para análise posterior.

---

## Melhorias Futuras
- **Segurança Avançada:** Implementar hashing de palavras-passe (por exemplo, usando bcrypt) e limitar tentativas de login.  
- **Interface de Utilizador Mais Atraente:** Utilizar estilos e elementos gráficos adicionais para tornar o quiz mais apelativo.  
- **Funcionalidades Estatísticas:** Mostrar histórico de resultados, ranking de utilizadores, médias de pontuação e relatórios de evolução.  
- **Suporte Multilingue e Acessibilidade:** Permitir fácil tradução do conteúdo e garantir a acessibilidade, por exemplo, adicionando suporte a leitores de ecrã.  
- **Testes Automatizados:** Criar testes unitários e de integração para garantir a qualidade do código.  

---

## Conclusão
Este sistema de quiz interativo em Python, com interface em Tkinter e base de dados SQLite, demonstra um fluxo simples e funcional: autenticação de utilizadores, carregamento dinâmico de perguntas, validação de respostas, controlo de tempo e registo de resultados. Embora já apresente uma base sólida, existem diversas oportunidades de melhoria, tanto ao nível da segurança e design, como na introdução de novas funcionalidades e análise de dados. As secções apresentadas neste relatório servem como guia para entender a arquitetura atual, o funcionamento interno e os rumos possíveis para o desenvolvimento futuro.
