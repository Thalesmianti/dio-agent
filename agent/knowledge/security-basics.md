# Fundamentos de Segurança da Informação

## Vulnerabilidade

Uma vulnerabilidade é uma falha em um sistema, aplicação ou processo que pode permitir comportamentos indesejados.


## Ameaça

Uma ameaça representa algo que pode explorar uma vulnerabilidade.


## Risco

Risco é a combinação entre:

- probabilidade;
- impacto.


## Tríade CIA

Os três pilares fundamentais da segurança da informação são:

- **Confidencialidade:** garantia de que a informação só é acessível por pessoas, entidades ou processos devidamente autorizados.
- **Integridade:** garantia de que a informação e os sistemas são mantidos exatos, completos e protegidos contra modificações não autorizadas ou acidentais.
- **Disponibilidade:** garantia de que os usuários autorizados tenham acesso à informação e aos recursos sempre que necessário.


## Boas Práticas

- **Validar e sanitizar entradas:** nunca confiar cegamente nos dados enviados pelo usuário; tratar qualquer entrada externa como potencialmente hostil.
- **Usar consultas parametrizadas:** separar estritamente dados de comandos SQL (*Prepared Statements*) para evitar injeções de código.
- **Princípio do Menor Privilégio:** conceder apenas as permissões estritamente necessárias para cada usuário, serviço ou conexão com banco de dados.
- **Defesa em Profundidade:** aplicar múltiplas camadas de segurança para que a falha de um controle não comprometa o sistema inteiro.
- **Manter sistemas e dependências atualizados:** aplicar correções e patches de segurança regularmente.
