# 📖 Boas Práticas de Desenvolvimento - Python Mundo 1

Este guia estabelece as boas práticas que toda a equipe LaboraDev deve seguir ao desenvolver código Python.

---

## 📝 1. Nomenclatura e Variáveis

### ✅ Use `snake_case` para variáveis e funções

```python
# Correto
nome_usuario = "Amélia"
idade_cadastro = 25

# Errado
nomeUsuario = "Amélia"
IdadeCadastro = 25
nomeusuario = "Amélia"
```

### ✅ Use `PascalCase` para classes

```python
# Correto
class CalculadoraFinanceira:
    pass

# Errado
class calculadora_financeira:
    pass
```

### ✅ Use `UPPER_CASE` para constantes

```python
# Correto
TAXA_DESCONTO = 0.10
VERSAO_SISTEMA = "1.0.0"

# Errado
taxa_desconto = 0.10
versao = "1.0.0"
```

---

## 📝 2. Comentários e Docstrings

### ✅ Comente o "por quê", não o "o quê"

```python
# Correto - Explica o motivo
# Aplicamos desconto de 10% apenas para clientes de 5+ anos
desconto = preco * 0.10

# Errado - Só repete o código
# Multiplica preco por 0.10
desconto = preco * 0.10
```

### ✅ Use docstrings em funções

```python
def calcular_total_compra(quantidade, preco, desconto=0):
    """Calcula o total de uma compra com desconto opcional.
    
    Args:
        quantidade (int): Número de itens
        preco (float): Preço unitário
        desconto (float): Percentual de desconto (0-1). Default: 0
        
    Returns:
        float: Valor total a pagar
        
    Exemplo:
        >>> calcular_total_compra(2, 50.0, 0.1)
        90.0
    """
    subtotal = quantidade * preco
    return subtotal * (1 - desconto)
```

---

## 📝 3. Funções

### ✅ Uma responsabilidade por função

```python
# Correto - Funções simples e focadas
def validar_email(email):
    """Valida se o email está no formato correto."""
    return "@" in email and "." in email

def validar_idade(idade):
    """Valida se a idade é válida (18+)."""
    return idade >= 18

# Errado - Função faz muitas coisas
def validar_usuario(email, idade, nome):
    if "@" not in email or "." not in email:
        print("Email inválido")
        return False
    if idade < 18:
        print("Menor de idade")
        return False
    if len(nome) < 3:
        print("Nome inválido")
        return False
    return True
```

### ✅ Mantenha funções pequenas (max 15-20 linhas)

```python
# Correto - Fácil de entender
def aplicar_desconto(preco, percentual):
    """Aplica desconto ao preço."""
    desconto = preco * percentual
    return preco - desconto

# Errado - Função muito longa
def processar_venda(lista_itens, cliente, cupom=None):
    # 30+ linhas de lógica complexa aqui...
    pass
```

---

## 📝 4. Estrutura de Código

### ✅ Organize o código logicamente

```python
# No início do arquivo
"""Módulo de cálculos financeiros."""

# Imports
import math
from datetime import datetime

# Constantes
TAXA_IMPOSTO = 0.15
VERSAO = "1.0"

# Classe
class GerenciadorFinanceiro:
    def __init__(self):
        pass
    
    def calcular(self):
        pass

# Funções
def processar_dados():
    pass

# Execução principal
if __name__ == "__main__":
    pass
```

### ✅ Use espaçamento adequado

```python
# Correto - Espaço legvel
def somar_numeros(a, b):
    resultado = a + b
    return resultado

# Errado - Muito compactado
def somar_numeros(a,b):
    resultado=a+b
    return resultado
```

---

## 📝 5. Tratamento de Erros

### ✅ Use try/except apropriadamente

```python
# Correto - Trata erros específicos
try:
    numero = int(input("Digite um número: "))
    resultado = 100 / numero
except ValueError:
    print("Erro: Digite um número válido")
except ZeroDivisionError:
    print("Erro: Não pode dividir por zero")

# Errado - Captura todos os erros
try:
    numero = int(input("Digite um número: "))
    resultado = 100 / numero
except:
    print("Algo deu errado")
```

---

## 📝 6. Tipos de Dados

### ✅ Use type hints quando possível

```python
# Correto - Deixa claro os tipos
def calcular_idade(ano_nascimento: int) -> int:
    """Calcula a idade com base no ano de nascimento."""
    ano_atual = 2026
    return ano_atual - ano_nascimento

# Ainda funciona, mas menos claro
def calcular_idade(ano_nascimento):
    return 2026 - ano_nascimento
```

---

## 📝 7. Exemplo Completo

```python
"""Sistema de gerenciamento de contas."""

from typing import Optional
from datetime import datetime

# Constantes
TAXA_JUROS = 0.05
LIMITE_MINIMO = -1000

class ContaBancaria:
    """Representa uma conta bancária.
    
    Atributos:
        titular (str): Nome do titular
        saldo (float): Saldo atual
    """
    
    def __init__(self, titular: str, saldo_inicial: float = 0):
        """Inicializa uma nova conta.
        
        Args:
            titular: Nome do titular
            saldo_inicial: Saldo inicial (default: 0)
        """
        self.titular = titular
        self.saldo = saldo_inicial
        self.historico = []
    
    def depositar(self, valor: float) -> bool:
        """Realiza um depósito na conta.
        
        Args:
            valor: Valor a depositar
            
        Returns:
            bool: True se bem-sucedido
        """
        if valor <= 0:
            print("Erro: Valor deve ser positivo")
            return False
        
        self.saldo += valor
        self._registrar_transacao(f"Depósito: +{valor}")
        return True
    
    def sacar(self, valor: float) -> bool:
        """Realiza um saque da conta.
        
        Args:
            valor: Valor a sacar
            
        Returns:
            bool: True se bem-sucedido
        """
        if valor <= 0:
            print("Erro: Valor deve ser positivo")
            return False
        
        if self.saldo - valor < LIMITE_MINIMO:
            print(f"Erro: Saldo insuficiente. Limite: {LIMITE_MINIMO}")
            return False
        
        self.saldo -= valor
        self._registrar_transacao(f"Saque: -{valor}")
        return True
    
    def _registrar_transacao(self, descricao: str) -> None:
        """Registra uma transação no histórico (privado).
        
        Args:
            descricao: Descrição da transação
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.historico.append(f"[{timestamp}] {descricao}")
    
    def exibir_saldo(self) -> None:
        """Exibe o saldo atual da conta."""
        print(f"Conta de {self.titular}: R$ {self.saldo:.2f}")


if __name__ == "__main__":
    # Teste
    conta = ContaBancaria("Amélia", 1000)
    conta.depositar(500)
    conta.sacar(200)
    conta.exibir_saldo()
```

---

## 📝 8. Checklist antes de fazer commit

- [ ] O código segue `snake_case` para variáveis
- [ ] Todas as funções tãm docstrings
- [ ] Os comentários explicam o "por quê"
- [ ] Não há variáveis não utilizadas
- [ ] Erros são tratados especificamente
- [ ] O código é fácil de ler e entender
- [ ] Não há funções muito longas (max 20 linhas)
- [ ] Constantes estão em `UPPER_CASE`
- [ ] O repositório tem estrutura correta

---

## 📋 9. Boas Práticas de Código

### Uma Função = Uma Tarefa

Cada função deve ter uma única responsabilidade (Single Responsibility Principle):

```python
# ❌ Ruim - Função faz várias coisas
def processar_venda(cliente, produto, quantidade):
    # Validar
    if not cliente:
        raise ValueError("Cliente inválido")
    # Calcular
    total = produto.preco * quantidade
    # Salvar
    salvar_banco_dados(cliente, produto, total)
    # Enviar email
    enviar_email(cliente)
    return total

# ✅ Bom - Funções bem separadas
def calcular_total(preco_unitario: float, quantidade: int) -> float:
    """Calcula o total da venda."""
    return preco_unitario * quantidade

def processar_venda(cliente, produto, quantidade):
    """Orquestra todo o processo de venda."""
    validar_cliente(cliente)
    total = calcular_total(produto.preco, quantidade)
    salvar_banco_dados(cliente, produto, total)
    enviar_email(cliente)
    return total
```

### Tamanho Máximo de Função

- **Ideal**: 10-20 linhas
- **Máximo**: 30 linhas
- **Por quê**: Fácil de ler, entender e testar

### Comprimento de Linha

- **Máximo**: 80 caracteres por linha
- **Objetivo**: Melhor legibilidade e compatibilidade

### Comentários Explicam o POR QUÉ

- **Bom comentário**: Explica a intengão, motivo ou decisão
- **Ruim comentário**: Apenas descreve o código (redundante)

```python
# ✅ Bom
# Usamos DRY (Don't Repeat Yourself) para evitar bugs de sincronização
valores = [item for item in dados if item.valido]

# ❌ Ruim - Apenas repete o código
# Filtra itens válidos
valores = [item for item in dados if item.valido]
```

### Type Hints

Use type hints para melhorar clareza e permitir verificação de tipos:

```python
# ✅ Com type hints
def calcular_idade(ano_nascimento: int) -> int:
    """Calcula a idade com base no ano de nascimento."""
    return 2026 - ano_nascimento

# ❌ Sem type hints
def calcular_idade(ano_nascimento):
    return 2026 - ano_nascimento
```

### Evite Variáveis Globais

- Variáveis globais deixam o código implícito
- Dificultam testes unitários
- Facilitam bugs

```python
# ❌ Ruim
TAXA_GLOBAL = 0.1

def calcular_valor_com_taxa(valor):
    return valor * (1 + TAXA_GLOBAL)  # Depende de variável global

# ✅ Bom
def calcular_valor_com_taxa(valor: float, taxa: float) -> float:
    """Calcula valor com taxa, recebendo ambos como parâmetros."""
    return valor * (1 + taxa)
```

### DRY - Don't Repeat Yourself

Reutilize código em vez de repetir:

```python
# ❌ Ruim - Código repetido
def validar_email(email):
    if "@" not in email:
        raise ValueError("Email inválido")

def validar_telefone(telefone):
    if len(telefone) < 10:
        raise ValueError("Telefone inválido")

def enviar_email(email):
    validar_email(email)
    # ...

def salvar_contato(email, telefone):
    validar_email(email)
    validar_telefone(telefone)
    # ...

# ✅ Bom - Código reutilizável
def validar_campo(valor: str, min_tamanho: int = 1, requerido: bool = True):
    """Valida um campo genérico."""
    if requerido and not valor:
        raise ValueError("Campo obrigatório")
    if len(valor) < min_tamanho:
        raise ValueError(f"Mínimo de {min_tamanho} caracteres")
    return True

def enviar_email(email):
    validar_campo(email, min_tamanho=5)  # Validar como email
    # ...
```

---

## 🔍 10. Validação de Entradas

### Sempre Valide Dados do Usuário

Nunca confie cegamente em dados de entrada:

```python
def calcular_idade(ano_nascimento: int) -> int:
    """Calcula idade com validação completa."""
    
    # Valida tipo
    if not isinstance(ano_nascimento, int):
        raise TypeError(f"Esperado int, recebido {type(ano_nascimento).__name__}")
    
    # Valida alcance
    if ano_nascimento < 1900 or ano_nascimento > 2026:
        raise ValueError(f"Ano inválido: {ano_nascimento}. Deve estar entre 1900 e 2026")
    
    # Calcula
    idade = 2026 - ano_nascimento
    
    return idade
```

### Checklist de Validação

- [ ] **Tipo de Dado**: O dado é do tipo esperado?
- [ ] **Alcance**: O valor está dentro dos limites aceitos (mínimo, máximo)?
- [ ] **Obrigatório**: Campos obrigatórios não são nulos?
- [ ] **Formato**: O dado possui o formato esperado (email, telefone, etc)?
- [ ] **Mensagens de Erro**: Os erros são claros e informativos?

### Tratamento de Erros com Try/Except

```python
def processar_valor(valor_str: str) -> float:
    """Processa valor com tratamento de erro."""
    try:
        # Tentar converter
        valor = float(valor_str)
        
        # Validar alcance
        if valor < 0:
            raise ValueError("Valor não pode ser negativo")
        
        return valor
    
    except ValueError as e:
        print(f"Erro ao processar valor: {e}")
        raise
    except Exception as e:
        print(f"Erro inesperado: {e}")
        raise
```

### Mensagens de Erro Significativas

```python
# ❌ Ruim - Mensagem genérica
if not valor:
    raise ValueError("Erro")

# ✅ Bom - Mensagem clara e específica
if not valor:
    raise ValueError("Campo 'valor' obrigatório. Recebido valor vazio")

if valor < 0:
    raise ValueError(f"Campo 'valor' deve ser positivo. Recebido: {valor}")

if not isinstance(valor, (int, float)):
    raise TypeError(f"Campo 'valor' deve ser número. Recebido: {type(valor).__name__}")
```

---

## 📖 Referências

- [Clean Code - Robert C. Martin](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882)
- [SOLID Principles](https://en.wikipedia.org/wiki/SOLID)
- [PEP 8 - Style Guide for Python Code](https://pep8.org/)
- [Python Exception Handling Best Practices](https://docs.python.org/3/tutorial/errors.html)

**Atualizado em:** 02 de Fevereiro de 2026

**Responsável:** Isaura (Documentação e Boas Práticas)
