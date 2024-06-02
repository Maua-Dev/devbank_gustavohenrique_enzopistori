from typing import Dict, Optional, List

from ..enums.item_type_enum import ItemTypeEnum
from ..entities.user import User
from .item_repository_interface import IItemRepository
from .user_repository_interface import IUserRepository

class userRepositoryMock(IUserRepository):
    users: Dict[int, User]
    
    def __init__(self):
        self.users = {
            1: User(name="GustavoHenrique", agency=1588, account='12345-6', current_balance=99.65),
            2: User(name="EnzoPistori", agency=132, account='12345-6', current_balance=654.11),
            3: User(name="Geraldo", agency=2295, account='12345-6', current_balance=1002.90),
        }
        
    def get_all_users(self) -> List[User]:
        return self.users.values()
    
    def get_user(self, user_id: int) -> Optional[User]:
        return self.users.get(user_id, None)
    
    '''
    def create_user(self, item: User, user_id: int) -> User:
        
        self.items[user_id] = item
        return item
    
    def delete_user(self, user_id: int) -> User:
        item = self.items.pop(user_id, None)
        return item
        
        
    def update_user(self, user_id:int, name:str=None, agency:int=None, account:int=None, current_balance:float=None) -> User:
        item = self.items.get(user_id, None)
        if item is None:
            return None
        
        if name is not None:
            item.name = name
        if agency is not None:
            item.agency = agency
        if account is not None:
            item.account = account
        if current_balance is not None:
            item.current_balance = current_balance
        self.items[user_id] = item
        
        return item
    '''
    
    