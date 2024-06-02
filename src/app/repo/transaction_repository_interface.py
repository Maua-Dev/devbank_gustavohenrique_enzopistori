from abc import ABC, abstractmethod
from ..entities.transaction import Transaction


class TransacRepository(ABC):
    @abstractmethod
    def create_deposit(self, transac:Transaction, transac_id:int) -> Transaction:
        '''
        create new deposit transact in the database
        '''
        pass