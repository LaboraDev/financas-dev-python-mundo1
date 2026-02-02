# 🚀 LaboraDev - Python Mundo 1

**Repositorio colaborativo do projeto LaboraDev - Aulas, Desafios e Projeto Final de Financas**

---

## 📚 Sobre o Projeto

Este repositorio contem todo o material do curso **Python Mundo 1** da plataforma LaboraDev, incluindo:

- ✅ Aulas praticas (Aula 06 a 10)
- ✅ Desafios diarios e semanais
- ✅ Projeto final: Sistema de Financas
- ✅ Documentacao e referencias

---

## 📁 Estrutura do Repositorio

```
financas-dev-python-mundo1/
│
├── 📂 docs/                          # Documentacao do projeto
│   ├── 📂 anotacoes_diarias/        # Notas de estudo de cada dia
│   └── 📂 sprints/                  # Planejamento e retrospectivas
│
├── 📂 src/                           # Codigo-fonte das aulas
│   ├── 📂 aula06/                   # Tipos Primitivos e Saida de Dados
│   ├── 📂 aula07/                   # Entrada de Dados e Variaveis
│   ├── 📂 aula08/                   # Operadores Aritmeticos e Logicos
│   ├── 📂 aula09/                   # Estruturas Condicionais (if/else)
│   └── 📂 aula10/                   # Estruturas de Repeticao (for/while)
│
├── 📂 desafios/                      # Exercicios praticos
│   ├── 📂 diarios/                  # Desafios do dia
│   └── 📂 semanais/                 # Desafios da semana
│
├── 📂 projeto_financas/              # Projeto final integrado
│   ├── 📂 versao_dia01/             # Primeira versao
│   └── 📂 versao_dia02/             # Versoes posteriores
│
├── README.md                         # Este arquivo
└── .gitignore                        # Arquivos a ignorar

```

---

## 📖 Conteudo das Aulas

### 🎯 Aula 06: Tipos Primitivos e Saida de Dados

**Tópicos:**
- Tipos de dados em Python (int, float, str, bool)
- Função print() e formatação
- Conversão entre tipos
- Operador type()

**Desafios:**
- [ ] Ex01: Imprimir dados pessoais
- [ ] Ex02: Operacoes com numeros
- [ ] Ex03: Conversão de tipos

---

### 🎯 Aula 07: Entrada de Dados e Variaveis

**Tópicos:**
- Função input() para entrada
- Variaveis e nomenclatura
- Escopo de variaveis
- Atribuição múltipla

**Desafios:**
- [ ] Ex01: Calculo de IMC
- [ ] Ex02: Conversão de moedas
- [ ] Ex03: Calculos geometricos

---

### 🎯 Aula 08: Operadores

**Tópicos:**
- Operadores aritmeticos (+, -, *, /, //, %, **)
- Operadores de comparacao (==, !=, <, >, <=, >=)
- Operadores logicos (and, or, not)
- Precedencia de operadores

**Desafios:**
- [ ] Ex01: Calculos complexos
- [ ] Ex02: Comparacoes e logica
- [ ] Ex03: Precedencia de operadores

---

### 🎯 Aula 09: Estruturas Condicionais

**Tópicos:**
- if, elif, else
- Aninhamento de condicionais
- Operador ternario
- Tratamento de erros

**Desafios:**
- [ ] Ex01: Validacao de dados
- [ ] Ex02: Jogo de numeros
- [ ] Ex03: Classificacao de notas

---

### 🎯 Aula 10: Estruturas de Repeticao

**Tópicos:**
- Loop for
- Loop while
- break e continue
- Ranges e iteracoes

**Desafios:**
- [ ] Ex01: Tabuada
- [ ] Ex02: Sequencias (Fibonacci)
- [ ] Ex03: Validacao com loop

---

## 🎯 Desafios

### Desafios Diarios

Localizados em `desafios/diarios/`, com um desafio para cada dia de aula.

**Estrutura:**
```
desafios/diarios/
├── desafio_dia01.md    # 02/02
├── desafio_dia02.md    # 03/02
├── desafio_dia03.md    # 04/02
├── desafio_dia04.md    # 05/02
└── desafio_dia05.md    # 06/02
```

### Desafios Semanais

Localizados em `desafios/semanais/`, com desafios integradores.

---

## 🛠️ Como Usar Este Repositorio

### 1. Clonar o Repositorio

```bash
git clone https://github.com/LaboraDev/financas-dev-python-mundo1.git
cd financas-dev-python-mundo1
```

### 2. Estrutura de Trabalho

Cada aula tem sua pasta em `src/`. Dentro de cada pasta:
- `exercicios.py` - Exercicios de classe
- `desafios.py` - Exercicios prativos
- `notas.md` - Anotacoes importantes

### 3. Executar os Arquivos

```bash
# Executar um arquivo Python
python src/aula06/exercicios.py

# Ou use python3 em Linux/Mac
python3 src/aula06/exercicios.py
```

### 4. Padrão de Commits

Ao fazer alteracoes, use este padrão:

```bash
git add .
git commit -m "[TIPO] Descricao clara e objetiva"
git push origin main
```

**Tipos de commit:**
- `[AULA]` - Exercicios e conteudo da aula
- `[DESAFIO]` - Desafio diario ou semanal
- `[PROJETO]` - Atualizacao do projeto Financas
- `[DOCS]` - Documentacao e anotacoes
- `[FIX]` - Correcao de bugs
- `[REFACTOR]` - Melhoria de codigo existente

**Exemplos:**
```
[AULA] Exercicios da aula 06 - tipos primitivos
[DESAFIO] Implementacao do calculo de IMC
[PROJETO] Adiciona funcionalidade de login
[DOCS] Anotacoes sobre operadores aritmeticos
```

---

## 📅 Cronograma - Semana 01

| Dia | Data | Aula | Conteudo |
|-----|------|------|----------|
| 🔵 | 02/02 | 06 | Tipos Primitivos e print() |
| 🔵 | 03/02 | 07 | Entrada de dados (input) |
| 🔵 | 04/02 | 08 | Operadores |
| 🔵 | 05/02 | 09 | Estruturas Condicionais |
| 🔵 | 06/02 | 10 | Loops e Repeticao |

**Carga Horaria:** 2h/dia (10h total)

---

## 💡 Boas Praticas

### Codigo
- ✅ Nomes descritivos para variaveis
- ✅ Comentarios em Python (# antes de linhas)
- ✅ Maximo 80 caracteres por linha
- ✅ Espacos em branco significativos em Python
- ✅ Testar sempre antes de commitar

### Git
- ✅ Commits pequenos e frequentes
- ✅ Um commit por feature/exercicio
- ✅ Sempre fazer pull antes de começar
- ✅ Sempre fazer push ao finalizar
- ✅ Mensagens claras e descritivas

---

## 🚀 Projeto Final: Sistema de Financas

Localizados em `projeto_financas/`, com versoes iterativas:

- **versao_dia01/** - Primeira versao (basico)
- **versao_dia02/** - Versao expandida (melhorias)

**Objetivos:**
- [ ] Entrada de dados de gastos
- [ ] Categorias de despesas
- [ ] Relatorio mensal
- [ ] Graficos simples
- [ ] Persistencia de dados

---

## 📚 Recursos e Referencias

### Documentacao Oficial
- [Python.org](https://www.python.org/)
- [Python Docs](https://docs.python.org/3/)
- [W3Schools Python](https://www.w3schools.com/python/)

### Ferramentas Recomendadas
- **Editor:** VS Code, PyCharm Community, Thonny
- **Versionamento:** Git e GitHub
- **Ambiente:** Python 3.8+

### Bibliotecas Basicas
```python
import math        # Operacoes matematicas
import random      # Numeros aleatorios
import datetime    # Data e hora
```

---

## 🤝 Como Contribuir

1. Faça um Fork do repositorio
2. Crie uma branch para sua feature (`git checkout -b feature/minhafuncionalidade`)
3. Commit suas mudancas (`git commit -m '[TIPO] Descricao'`)
4. Push para a branch (`git push origin feature/minhafuncionalidade`)
5. Abra um Pull Request

---

## 📝 Licenca

Este projeto é de educacao. Sinta-se livre para usar e modificar!

---

## 👥 Equipe LaboraDev

**Projeto Colaborativo do Time LaboraDev**

- 🎓 Mentoria e Orientacao
- 💻 Codificacao Colaborativa
- 🚀 Desenvolvimento de Habilidades

---

## 📞 Suporte

Dúvidas ou sugestões? Abra uma issue no repositorio!

---

**Bom aprendizado! 🎉 Vamos crescer juntos!**
