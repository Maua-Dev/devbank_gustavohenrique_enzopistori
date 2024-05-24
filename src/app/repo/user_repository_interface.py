from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from ..enums.item_type_enum import ItemTypeEnum

from ..entities.user import User


class IUserRepository(ABC):
    
    
    @abstractmethod
    def get_all_users(self) -> List[User]:
        '''
        Returns all the itens in the database 
        '''
        pass
    
    @abstractmethod
    def get_user(self, item_id: int) -> Optional[User]:
        '''
        Returns the item with the given id.
        If the item does not exist, returns None
        '''
        pass
    
    @abstractmethod
    def create_user(self, item: User, item_id: int) -> User:
        '''
        Creates a new item in the database
        '''
        pass
    
    @abstractmethod
    def delete_user(self, item_id: int) -> User:
        '''
        Deletes the item with the given id.
        If the item does not exist, returns None
        '''
        
    @abstractmethod
    def update_user(self, user_id:int, name:str=None, agency:int=None, account:int=None, current_balance:float=None) -> User:
        '''
        Updates the item with the given id.
        If the item does not exist, returns None
        '''
        pass
    
    