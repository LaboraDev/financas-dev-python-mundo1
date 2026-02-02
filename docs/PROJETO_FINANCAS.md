# 💼 Projeto Final: Finanças Dev v1.0

## 📋 Visão Geral

Este documento apresenta a especificação completa do **Projeto Final: Finanças Dev v1.0**, um projeto de aprendizado prático do curso **Python Mundo 1** de Gustavo Guanabara. O objetivo é criar uma aplicação de gestão financeira para freelancers, consolidando todos os conceitos aprendidos durante o curso.

---

## 🎯 Objetivo do Projeto

Desenvolver uma aplicação de **gestão financeira para freelancers** usando Python, aplicando todos os conceitos aprendidos no Mundo 1 do curso do Gustavo Guanabara. A aplicação deve ser funcional, bem documentada e apta para ser adicionada ao portfólio profissional.

---

## 💻 Funcionalidades Principais

### 1. Cadastro de Jobs/Projetos
Permite que o freelancer registre seus trabalhos com as seguintes informações:
- **Nome do projeto**: Identificação do trabalho realizado
- **Valor bruto em reais**: O valor inicial da proposta sem descontos
- **Tipo de pagamento**: PIX, transferência bancária ou boleto
- **Data de recebimento**: Quando o pagamento foi ou será recebido

### 2. Cálculos Automáticos
Realiza cálculos financeiros automaticamente:
- **Desconto de impostos** (opcional): Percentual a ser descontado
- **Taxa de plataforma** (se aplicável): Desconto de plataformas terceirizadas (ex: Upwork, Freelancer)
- **Valor líquido recebido**: Resultado final após todos os descontos (Valor Bruto - Impostos - Taxa Plataforma)

### 3. Relatórios
Gera relatórios com resumo dos dados cadastrados:
- **Total de jobs cadastrados**: Quantidade de projetos
- **Valor total bruto**: Soma de todos os valores antes dos descontos
- **Valor total líquido**: Soma de todos os valores após os descontos
- **Média de valor por job**: Cálculo do valor médio por projeto

---

## 🛠️ Tecnologias e Conceitos Utilizados

O projeto utiliza os seguintes conceitos e módulos Python:

- ✅ **Tipos primitivos**: `int`, `float`, `str`, `bool`
- ✅ **Operadores aritméticos**: Para cálculos de valores, impostos e taxas
- ✅ **Módulos**: Importação de `math` para operações matemáticas e `datetime` para gerenciar datas
- ✅ **Manipulação de strings**: Formatação de saída e entrada de dados
- ✅ **Estruturas condicionais**: `if/elif/else` para validações e decisões
- ✅ **Laços de repetição**: `for/while` para iterar sobre os dados cadastrados
- ✅ **Funções personalizadas**: Modularizar o código em funções reutilizáveis
- ✅ **Listas e dicionários**: Armazenar e organizar dados dos projects/jobs

---

## 📅 Cronograma de Desenvolvimento

### Semana 1 (02 a 06/02): Desafios Diários Incrementais

#### Dia 1 (02/02) - Aula 06: Tipos Primitivos
**Objetivo**: Criar módulo básico de cadastro
- Declarar variáveis com tipos primitivos
- Criar estrutura básica para receber dados do usuário
- Armazenar informações do primeiro job (nome, valor, tipo de pagamento, data)

#### Dia 2 (03/02) - Aula 07: Operadores Aritméticos
**Objetivo**: Adicionar cálculos
- Implementar cálculo do valor líquido
- Usar operadores aritméticos para descontos
- Exibir resultado dos cálculos

#### Dia 3 (04/02) - Aula 08: Módulos
**Objetivo**: Importar módulos
- Importar módulo `datetime` para trabalhar com datas
- Importar módulo `math` para operações matemáticas
- Adicionar funcionalidades relacionadas a data

#### Dia 4 (05/02) - Aula 09: Manipulação de Strings
**Objetivo**: Formatação elegante
- Formatar valores em moeda (reais)
- Criar saída visual atraente
- Melhorar legibilidade dos dados exibidos

#### Dia 5 (06/02) - Aula 10: Condições
**Objetivo**: Adicionar validações
- Validar entrada de dados
- Verificar se valores são positivos
- Aplicar regras condicionais para descontos

### Semana 2 (09 a 13/02): Integração e Finalização

#### Dia 6 (09/02) - Aula 11: Operadores Lógicos
**Objetivo**: Combinar condições
- Usar operadores `and`, `or`, `not` para validações complexas
- Criar fluxos de lógica mais sofisticados

#### Dia 7 (10/02) - Aula 12: Estruturas Condicionais
**Objetivo**: Expandir estruturas condicionais
- Implementar menus de opções
- Criar navegação na aplicação

#### Dia 8 (11/02) - Aula 13: Loops
**Objetivo**: Permitir múltiplos cadastros
- Usar loops para cadastrar vários jobs
- Permitir adicionar novos registros em iteração

#### Dia 9 (12/02) - Aula 14: Funções
**Objetivo**: Modularizar o código
- Criar funções para cada operação principal
- Melhorar organização e reusabilidade
- Implementar funções para cálculos e exibição

#### Dia 10 (13/02) - Aula 15: Listas e Tuplas
**Objetivo**: Armazenar múltiplos jobs
- Usar listas para armazenar todos os jobs cadastrados
- Usar tuplas para dados imutáveis
- Iterar sobre os dados para gerar relatórios

#### Semana 3 - Refinamento e Documentação
- **Aula 16: Dicionários** - Estruturar dados com chaves-valor
- **Aula 17: Manipulação de Strings** - Melhorar formatação
- **Aula 18: Exceções** - Tratamento de erros robusto

---

## 📊 Estrutura de Dados

### Modelo de um Job/Projeto
```python
job = {
    'nome': 'Desenvolvimento de Site',
    'valor_bruto': 5000.00,
    'tipo_pagamento': 'PIX',
    'data_recebimento': '2026-02-15',
    'desconto_imposto': 15.0,  # percentual
    'taxa_plataforma': 0.0,     # percentual
    'valor_liquido': 4250.00
}
```

---

## 🎯 Meta Final

Criar um projeto **funcional e bem documentado** que demonstre domínio dos fundamentos de Python e que possa ser adicionado ao portfólio profissional no GitHub.

### Critérios de Sucesso:
- ✅ Código limpo e bem estruturado
- ✅ Documentação completa
- ✅ Todas as funcionalidades implementadas
- ✅ Tratamento de erros e validações
- ✅ Testes funcionais realizados
- ✅ Subido e organizado no GitHub
- ✅ Pronto para apresentação

---

## 📂 Estrutura de Arquivos do Projeto

```
projeto_financas/
├── versao_dia01/          # Primeira versão (conceito)
├── versao_dia02/          # Segunda versão (com melhorias)
├── main.py                # Arquivo principal da aplicação
├── modulos/
│   ├── cadastro.py        # Módulo de cadastro de jobs
│   ├── calculos.py        # Módulo de cálculos financeiros
│   └── relatorios.py      # Módulo de geração de relatórios
├── dados/
│   └── jobs.json          # Arquivo de armazenamento de dados (futuro)
└── README.md              # Documentação do projeto
```

---

## 🚀 Como Executar

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/LaboraDev/financas-dev-python-mundo1.git
   cd financas-dev-python-mundo1/projeto_financas
   ```

2. **Execute a aplicação**:
   ```bash
   python main.py
   ```

3. **Siga as instruções na tela** para cadastrar jobs e visualizar relatórios

---

## 📝 Notas Importantes

- Este projeto é parte do aprendizado do **Python Mundo 1** do Gustavo Guanabara
- Desenvolvido incrementalmente ao longo de 2 semanas
- Cada dia adiciona novos conceitos e funcionalidades
- O código deve ser mantido limpo e bem documentado
- Recomenda-se seguir as **Boas Práticas de Desenvolvimento** definidas no repositório

---

## 👥 Equipe LaboraDev

- **Amélia**: Coordenação do projeto
- **Ana**: Desenvolvimento e testes
- **Isaura**: Documentação e boas práticas

---

## 📚 Referências

- [Curso Python Mundo 1 - Gustavo Guanabara](https://www.cursoemvideo.com/course/python-3-mundo-1/)
- [Documentação Python](https://docs.python.org/3/)
- [Guia de Boas Práticas](../BOAS_PRATICAS.md)
- [Guia de Documentação de Código](../GUIA_DOCUMENTACAO_CODIGO.md)

---

**Última atualização**: Fevereiro de 2026
**Status**: Em desenvolvimento
**Versão**: 1.0
