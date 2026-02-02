# 🚀 LaboraDev - Python Mundo 1

**Repositório colaborativo do projeto LaboraDev - Aulas, Desafios e Projeto Final de Finanças**

---

## 👥 Equipe


- **Amélia** - Coordenação do projeto
- **Ana** - Desenvolvimento e testes
- **Isaura** - Documentação e boas práticas

---

## 📚 Sobre o Projeto

Este repositório contém todo o material do curso **Python Mundo 1** da plataforma LaboraDev, incluindo:

- ✅ Aulas práticas (Aula 06 a 18)
- ✅ Desafios diários e semanais
- ✅ Projeto final: Sistema de Finanças
- ✅ Documentação e referências

---

## 📅 Cronograma - Semana 1 (02/02 a 14/02)

| Data | Dia | Aula | Tópico | Status |
|------|-----|------|--------|--------|
| 02/02 | Seg | 06 | Tipos Primitivos | ✅ Programado |
| 03/02 | Ter | 07 | Operadores Aritméticos | 📝 Em Detalhamento |
| 04/02 | Qua | 08 | Módulos | 📝 Em Detalhamento |
| 05/02 | Qui | 09 | Texto (Strings) | 📝 Em Detalhamento |
| 06/02 | Sex | 10 | Condições (If/Elif/Else) | 📝 Em Detalhamento |
| 07/02 | Sáb | 11 | Operadores Lógicos | 📝 Em Detalhamento |
| 14/02 | Sáb | 12-18 | Módulos avançados | 🔄 Planejamento |

**Observação:** O cronograma detalhado com objetivos, conceitos-chave e entregáveis está disponível no [Trello do projeto](https://trello.com/b/OnVhgoTJ/laboradev-python-mundo-1).

---

## 📁 Estrutura do Repositório

```
financas-dev-python-mundo1/
├── 📂 docs/                       # Documentação do projeto
│   ├── 📂 anotacoes_diarias/     # Notas de estudo de cada dia
│   ├── 📂 sprints/               # Planejamento e retrospectivas
│   └── BOAS_PRATICAS.md          # Guia de boas práticas (modelo)
│
├── 📂 src/                        # Código-fonte das aulas
│   ├── 📂 aula06/                # Tipos Primitivos e Saída de Dados
│   ├── 📂 aula07/                # Operadores Aritméticos
│   ├── 📂 aula08/                # Módulos
│   ├── 📂 aula09/                # Texto (Strings)
│   ├── 📂 aula10/                # Condições (If/Elif/Else)
│   ├── 📂 aula11/                # Operadores Lógicos
│   └── ... (aulas 12-18)
│
├── 📂 desafios/                   # Exercícios práticos
│   ├── 📂 diarios/               # Desafios do dia
│   └── 📂 semanais/              # Desafios da semana
│
├── 📂 projeto_financas/           # Projeto final integrado
│   ├── 📂 versao_dia01/          # Primeira versão (básico)
│   └── 📂 versao_dia02/          # Versões posteriores (melhorias)
│
├── README.md                      # Este arquivo
└── .gitignore                     # Arquivos a ignorar
```

---

## 📖 Detalhes das Aulas

### 🎯 Dia 03/02 - Aula 07: Operadores Aritméticos

**Conceitos:**
- Operadores: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Ordem de operações (precedência)
- Cálculos com inteiros e floats

**Desafio:** Criar script com exemplos de cada operador

---

### 🎯 Dia 04/02 - Aula 08: Módulos

**Conceitos:**
- O que são módulos em Python
- Importar módulos built-in (math, random, datetime)
- Formas de import: `import`, `from...import`

**Desafio:** Script com 3 módulos diferentes

---

### 🎯 Dia 05/02 - Aula 09: Texto (Strings)

**Conceitos:**
- Strings como sequências de caracteres
- Indexação e slicing
- Métodos: `.upper()`, `.lower()`, `.replace()`, `.split()`, `.join()`
- F-strings para formatação

**Desafio:** Script com manipulação de strings

---

### 🎯 Dia 06/02 - Aula 10: Condições (If/Elif/Else)

**Conceitos:**
- Estruturas condicionais: `if`, `elif`, `else`
- Operadores de comparação: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Operadores lógicos: `and`, `or`, `not`
- Indentação

**Desafio:** Programa com múltiplas condições

---

### 🎯 Dia 07/02 - Aula 11: Operadores Lógicos

**Conceitos:**
- `and`: ambas as condições verdadeiras
- `or`: pelo menos uma condição verdadeira
- `not`: inverte valor booleano
- Tabelas-verdade
- Precedência: `not` > `and` > `or`

**Desafio:** Demonstrar todos operadores lógicos

---

## 📚 Boas Práticas de Desenvolvimento

Ver arquivo [BOAS_PRATICAS.md](./docs/BOAS_PRATICAS.md) para o guia completo.

### Resumo Rápido:

1. **Nomes de variáveis**: Use `snake_case`
   ```python
   nome_usuario = "Ametélia"
   idade = 25
   ```

2. **Comentários**: Explique o "por quê", não o "o quê"
   ```python
   # Calcula o desconto de 10% por ser cliente antigo
   desconto = preco * 0.10
   ```

3. **Funções**: Uma responsabilidade por função
   ```python
   def calcular_total(quantidade, preco):
       """Calcula total de uma compra."""
       return quantidade * preco
   ```

4. **Documentação**: Use docstrings
   ```python
   def soma(a, b):
       """Soma dois números e retorna o resultado.
       
       Args:
           a: Primeiro número
           b: Segundo número
           
       Returns:
           int: A soma de a e b
       """
       return a + b
   ```

---

## 📋 Projeto Final: Sistema de Finanças

### Objetivos:
- Gerenciar receitas e despesas
- Calcular saldos
- Gerar relatórios

### Versões:

**Versão 1 (Básica - até Aula 10):**
- Entrada de dados
- Tipos primitivos
- Operações básicas

**Versão 2 (Melhorada - após Aula 18):**
- Estruturas de dados
- Funções
- Tratamento de erros

---

## 🔗 Links ÚTeis

- [Trello do Projeto](https://trello.com/b/OnVhgoTJ/laboradev-python-mundo-1)
- [Plataforma LaboraDev](https://laboradev.com)
- [Documentação Python](https://docs.python.org/pt-br/)

---

## 📝 Contribuindo

1. Crie uma branch para sua aula: `git checkout -b aula-07`
2. Faça commit das mudanças: `git commit -m "Aula 07 - Operadores"`
3. Push para a branch: `git push origin aula-07`
4. Abra um Pull Request

---

## 📄 Licença

Este projeto é parte do programa de formação LaboraDev.

**Atualizado em:** 02 de Fevereiro de 2026
