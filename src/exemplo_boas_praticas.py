"""Exemplo de código seguindo boas práticas Python.

Este arquivo demonstra como aplicar as boas práticas de desenvolvimentos
do projeto LaboraDev em código Python.
"""

from typing import List, Optional
from datetime import datetime

# Constantes (UPPER_CASE)
TAXA_IMPOSTO = 0.15
VERSAO_SISTEMA = "1.0.0"
SALDO_MINIMO = -100


class GerenciadorContas:
    """Gerencia contas de usuários.
    
    Esta classe é responsável por gerenciar as contas de usuários,
    permitindo depósitos, saques e consultas de saldo.
    
    Atributos:
        contas (dict): Dicionário com as contas registradas
    """
    
    def __init__(self):
        """Inicializa o gerenciador de contas."""
        self.contas = {}
    
    def criar_conta(self, cpf: str, nome: str, saldo_inicial: float = 0) -> bool:
        """Cria uma nova conta no sistema.
        
        Args:
            cpf (str): CPF do usuário (sem máscara)
            nome (str): Nome completo do usuário
            saldo_inicial (float): Saldo inicial da conta. Default: 0
            
        Returns:
            bool: True se conta foi criada com sucesso
            
        Raises:
            ValueError: Se CPF já existe
        """
        if cpf in self.contas:
            raise ValueError(f"Erro: CPF {cpf} já possui conta")
        
        self.contas[cpf] = {
            "nome": nome,
            "saldo": saldo_inicial,
            "criada_em": datetime.now(),
            "historico": [f"Conta criada com saldo inicial: R$ {saldo_inicial:.2f}"]
        }
        return True
    
    def depositar(self, cpf: str, valor: float) -> bool:
        """Realiza um depósito em uma conta.
        
        Args:
            cpf (str): CPF do usuário
            valor (float): Valor a depositar
            
        Returns:
            bool: True se depósito foi realizado
            
        Raises:
            ValueError: Se valor é inválido ou CPF não existe
        """
        # Validar entrada
        if valor <= 0:
            raise ValueError("Erro: Valor deve ser positivo")
        
        if cpf not in self.contas:
            raise ValueError(f"Erro: CPF {cpf} não encontrado")
        
        # Realizar depósito
        self.contas[cpf]["saldo"] += valor
        self._registrar_transacao(cpf, f"Depósito: +R$ {valor:.2f}")
        return True
    
    def sacar(self, cpf: str, valor: float) -> bool:
        """Realiza um saque em uma conta.
        
        Args:
            cpf (str): CPF do usuário
            valor (float): Valor a sacar
            
        Returns:
            bool: True se saque foi realizado
            
        Raises:
            ValueError: Se saldo insuficiente ou valor inválido
        """
        # Validar entrada
        if valor <= 0:
            raise ValueError("Erro: Valor deve ser positivo")
        
        if cpf not in self.contas:
            raise ValueError(f"Erro: CPF {cpf} não encontrado")
        
        # Validar saldo
        saldo_atual = self.contas[cpf]["saldo"]
        if saldo_atual - valor < SALDO_MINIMO:
            mensagem = f"Erro: Saldo insuficiente (saldo: R$ {saldo_atual:.2f})"
            raise ValueError(mensagem)
        
        # Realizar saque
        self.contas[cpf]["saldo"] -= valor
        self._registrar_transacao(cpf, f"Saque: -R$ {valor:.2f}")
        return True
    
    def obter_saldo(self, cpf: str) -> float:
        """Retorna o saldo de uma conta.
        
        Args:
            cpf (str): CPF do usuário
            
        Returns:
            float: Saldo da conta
            
        Raises:
            ValueError: Se CPF não existe
        """
        if cpf not in self.contas:
            raise ValueError(f"Erro: CPF {cpf} não encontrado")
        
        return self.contas[cpf]["saldo"]
    
    def _registrar_transacao(self, cpf: str, descricao: str) -> None:
        """Registra uma transação no histórico (método privado).
        
        Args:
            cpf (str): CPF do usuário
            descricao (str): Descrição da transação
        """
        # Use underscore para indicar método privado
        timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        mensagem = f"[{timestamp}] {descricao}"
        self.contas[cpf]["historico"].append(mensagem)
    
    def obter_historico(self, cpf: str) -> List[str]:
        """Retorna o histórico de transações de uma conta.
        
        Args:
            cpf (str): CPF do usuário
            
        Returns:
            List[str]: Lista com histórico de transações
        """
        if cpf not in self.contas:
            raise ValueError(f"Erro: CPF {cpf} não encontrado")
        
        return self.contas[cpf]["historico"]


def demonstrar_uso() -> None:
    """Demonstra o uso do GerenciadorContas com exemplo prático."""
    print(f"\n=== Sistema de Gestão de Contas v{VERSAO_SISTEMA} ===")
    print(f"Taxa de Imposto: {TAXA_IMPOSTO * 100}%\n")
    
    # Criar gerenciador
    gerenciador = GerenciadorContas()
    
    try:
        # Criar contas
        gerenciador.criar_conta("123456789", "Amélia Silva", 1000)
        gerenciador.criar_conta("987654321", "Ana Santos", 500)
        
        # Realizar transações
        gerenciador.depositar("123456789", 200)
        gerenciador.sacar("123456789", 150)
        
        # Exibir saldos
        print("Saldos das contas:")
        print(f"  Amélia: R$ {gerenciador.obter_saldo('123456789'):.2f}")
        print(f"  Ana: R$ {gerenciador.obter_saldo('987654321'):.2f}")
        
        # Exibir histórico
        print("\nHistórico de Amélia:")
        for transacao in gerenciador.obter_historico("123456789"):
            print(f"  {transacao}")
        
    except ValueError as erro:
        print(f"\nErro: {erro}")


if __name__ == "__main__":
    # Executa o programa principal
    demonstrar_uso()
