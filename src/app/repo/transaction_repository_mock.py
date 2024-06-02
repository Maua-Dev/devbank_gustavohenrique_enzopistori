from typing import Dict, Optional, List

from src.app.repo.transaction_repository_interface import TransacRepository
from ..entities.transaction import Transaction


class TransacRepositoriMock(TransacRepository):
    transacoes: Dict[int, Transaction]

    def __init__(self):
        self.transactions = {}

    def create_deposit(self, transac: Transaction, transac_id: int) -> Transaction:
        self.transactions[transac_id] = transac
        return transac

    def get_transac(self, transac_id: int) -> Optional[Transaction]:
        return self.transactions.get(transac_id, None)

    def cria_transacao(self, transac: Transaction, transac_id: int):
        while self.transactions.get(transac_id, None):
            transac_id += 1
        self.transactions[transac_id] = transac
        return transac

    def get_all_transactions(self) -> List[Transaction]:
        return self.transactions.values()