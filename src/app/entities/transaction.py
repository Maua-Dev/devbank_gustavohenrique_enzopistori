from ..enums.transaction_type_enum import TransactionTypeEnum
from ..errors.entity_errors import ParamNotValidated
from datetime import datetime

class Transaction:
    type: TransactionTypeEnum
    value: float
    current_balance: float
    timestamp: int

    def __init__(self, type:TransactionTypeEnum, value:float, current_balance:float) -> None:
         if type(type) != TransactionTypeEnum: 
              raise ParamNotValidated("Invalid Type")
         self.type = type
         
         if not self.validate_value(value):
            raise ParamNotValidated("Invalid Value")
         self.value = value
         
         if not self.validate_current_balance(current_balance):
              raise ParamNotValidated("Invalid Current_Balance")
         self.current_balance = current_balance

         self.timestamp = datetime.now()

    @staticmethod
    def validate_value(value: float) -> bool:
         if value is None:
              return False 
         if type(value) != float:
              return False
         if value < 0:
              return False
         return True
    
    @staticmethod
    def validate_current_balance(current_balance: float) -> bool:
         if current_balance is None:
              return False 
         if type(current_balance) != float:
              return False
         if current_balance < 0:
              return False
         return True
    
    

         
    
