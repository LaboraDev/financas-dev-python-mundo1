# 📄 Guia de Documentação e Estudo - Python Mundo 1

Este guia define o padrão para as anotações diárias, documentação de código e commits da equipe LaboraDev.

---

## 📝 1. Anotações Diárias de Estudo

As anotações devem ser salvas em `docs/anotacoes_diarias/YYYY-MM-DD_estudo.md`.

### O que incluir:
- **Tópico do dia**: Ex: Aula 07 - Operadores Aritméticos.
- **Principais conceitos**: O que você aprendeu de mais importante? (Ex: Divisão inteira `//` vs real `/`).
- **Dificuldades encontradas**: Onde você travou? Como resolveu?
- **Exemplos práticos rápidos**: Pequenos trechos de código que testou.
- **Links úteis**: Artigos ou vídeos extras consultados.

### Modelo Sugerido:
```markdown
# Estudo Diário - [DATA]
**Aula:** [Número e Título]

## 🎯 Conceitos Chave
- [Conceito 1]
- [Conceito 2]

## 💡 Aprendizados
- Resumo do que foi fixado hoje.

## 🚧 Desafios/Dúvidas
- O que foi difícil e como superei.
```

---

## 🛠️ 2. Documentação do Código (Final da Semana)

Toda sexta-feira/sábado, devemos consolidar a documentação técnica em `docs/CONSOLDIDADO_SEMANA_X.md`.

### Estrutura Padrão:
1. **Visão Geral**: O que foi construído na semana.
2. **Componentes/Módulos**: Descrição das funções criadas em `src/`.
3. **Instruções de Uso**: Como rodar os scripts da semana.
4. **Dependências**: Se algum módulo extra foi necessário.

---

## 🚀 3. Padrão de Commits (Git)

Para manter o histórico limpo, usaremos o padrão **Conventional Commits**.

### Formato do Título:
`<tipo>(escopo): <descrição curta em português>`

### Tipos permitidos:
- `feat`: Novo recurso (ex: nova aula, novo exercício).
- `fix`: Correção de bug no código.
- `docs`: Mudanças na documentação.
- `style`: Formatação, pontos e vírgulas (sem mudança de lógica).
- `refactor`: Refatoração de código.
- `test`: Adição ou correção de testes.

### Exemplos:
- `feat(aula07): adicionar exercícios de operadores`
- `docs(readme): atualizar cronograma da equipe`
- `fix(aula06): corrigir erro de conversão de tipo`

Descrição dos Commits obrigatória: incluir contexto da mudança

---

## ✅ 4. Padrão de Entrega
Todo Daily deve ter:
- Código com exemplos práticos e comentários
- Arquivo de anotações
- Commit com título e descrição.

### ⚠️ Pontos Importantes
- Manter sincronização GitHub ↔ Trello ↔ Anotações
- Descrever sempre o que foi feito (commit messages claras)
- Praticar todos os conceitos antes de passar para próxima aula
- Documentar dúvidas para discussão em grupo
- Fazer backup local diariamente
  
---

## 📅 5. Alinhamento com Trello

- **Cartão no Trello**: O link do arquivo de anotação diária deve ser anexado ao cartão correspondente da Daily.
- **Checklist**: Marque o item "Documentação" no Trello apenas após o commit no GitHub.
- **Status**: Mova para "✅ Concluído" apenas quando o código e a documentação estiverem no repositório.

---

## 📋 6. Estrutura Padrão de Documentação de Arquivo

### Cabeçalho de Arquivo

Todo arquivo Python deve começar com um cabeçalho descritivo:

```python
"""
Nome do Projeto: Finanças Dev
Módulo: [Nome do Módulo]
Autor: [Nome]
Data: AAAA/MM/DD
Descrição: [O que faz e para que serve]
"""
```

### Estrutura de Docstring de Função

Toda função deve ter uma docstring clara e bem formatada:

```python
def minha_funcao(param1: int, param2: str) -> bool:
    """
    Descrição breve da função.

    Args:
        param1 (int): Descrição do parâmetro 1
        param2 (str): Descrição do parâmetro 2

    Returns:
        bool: Descrição do retorno

    Exemplo:
        >>> resultado = minha_funcao(10, "teste")
        >>> print(resultado)
        True
    """
    # Código da função
    pass
```

---

## 📖 7. Nomenclatura (PEP 8)

Mantenha os padrões de nomenclatura Python:

- **Variáveis**: `snake_case` → `idade_usuario`, `nome_projeto`
- **Funções**: `snake_case` → `calcular_idade()`, `validar_entrada()`
- **Constantes**: `UPPER_CASE` → `MAX_TENTATIVAS`, `PI`
- **Classes**: `PascalCase` → `CalculadoraFinanceira`, `Usuario`
- **Privadas**: `_com_underscore` → `_metodo_interno()`, `_variavel_privada`

---

## 📚 8. Comentários e Docstrings

### Diferenças

- **Docstring** (`"""..."""`): Documentação formal, processada por ferramentas como Sphinx
- **Comentário** (`#`): Notas informais no código

### Boas Práticas

- Docstrings: Use para módulos, classes e funções
- Comentários: Explique o POR QUÉ, não o O QUÉ
- Comece comentários com letra maiúscula
- Atualize comentários quando alterar o código

```python
# Bom: Explica o motivo
# Usamos lista em vez de conjunto porque preserva ordem
ids = [1, 2, 3]

# Ruim: Apenas repete o código
# Cria uma lista com os números 1, 2, 3
ids = [1, 2, 3]
```

---

## 📈 9. Changelog

Mantenha um registro de mudanças significativas no projeto:

### Formato

```
DD/MM/AAAA - [TIPO] Descrição da mudança
```

### Exemplos

```
02/02/2026 - [FEAT] Adicionada função de cálculo de valor líquido
03/02/2026 - [FIX] Corrigido bug no cálculo de impostos
04/02/2026 - [DOCS] Atualizada documentação de docstrings
05/02/2026 - [REFACTOR] Refatorado módulo de validação
```

---

## 🔍 10. Testes

### Estrutura de Testes

- **Nome do arquivo**: `test_nome_modulo.py`
- **Nome da função**: `test_o_que_testamos()`
- **Padrão**: Arrange (preparar), Act (agir), Assert (verificar)

### Exemplo

```python
def test_calcular_idade_valida():
    """Testa cálculo de idade com entrada válida."""
    # Arrange (preparar)
    ano_nascimento = 2000
    
    # Act (agir)
    idade = calcular_idade(ano_nascimento)
    
    # Assert (verificar)
    assert idade == 26

def test_calcular_idade_invalida():
    """Testa cálculo de idade com entrada inválida."""
    # Arrange
    ano_invalido = "abc"
    
    # Act & Assert
    with pytest.raises(TypeError):
        calcular_idade(ano_invalido)
```

### Cobertura

- Teste casos **normais** (funçionamento esperado)
- Teste casos **extremos** (valores máximos, mínimos)
- Teste **erros** (entradas inválidas)

---

## 📝 Referéncias

- [PEP 8 - Style Guide for Python](https://pep8.org/)
- [PEP 257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Documentação Oficial de Python](https://docs.python.org/3/)

**Atualizado em:** 04 de Fevereiro de 2026 | Hora: 14:14
**Equipe:** Amélia, Ana, Isaura
