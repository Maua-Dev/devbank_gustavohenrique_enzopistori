from ..enums.transaction_type_enum import TransactionTypeEnum
from ..errors.entity_errors import ParamNotValidated
from datetime import datetime
from typing import Tuple

class Transaction:
    types: TransactionTypeEnum
    value: float
    current_balance: float
    timestamp: float

    def __init__(self, types:TransactionTypeEnum, value:float, current_balance:float, timestamp:float) -> None:
         #raise ParamNotValidated( f"Invalid Type: {type(type)}")
         if type(types) != TransactionTypeEnum: 
              raise ParamNotValidated( f"Invalid Type: {type(types)}")
         self.types = types
         
         validate = self.validate_value(value)
         if not validate[0]:
            raise ParamNotValidated('value', validate[1])
         self.value = value

         validate = self.validate_current_balance(current_balance)
         if not validate[0]:
              raise ParamNotValidated('current_balance', validate[1])
         self.current_balance = current_balance

         validate = self.validate_timestamp(timestamp)
         if not validate[0]:
              raise ParamNotValidated('timestamp', validate[1])
         self.timestamp = timestamp

         #self.timestamp = datetime.now()

    @staticmethod
    def validate_value(value: float) -> Tuple[bool, str]:
         if value is None:
              return (False, "the value must not be None") 
         if type(value) != float:
              return (False, "the value must be float")
         if value < 0:
              return (False, "Low value")
         return (True, '')
    
    @staticmethod
    def validate_current_balance(current_balance: float) -> Tuple[bool, str]:
         if current_balance is None:
              return (False, "the value must not be None") 
         if type(current_balance) != float:
              return (False, "the value must be float") 
         if current_balance < 0:
              return (False, "Low value")
         return (True, "")
    
    @staticmethod
    def validate_timestamp(timestamp:float) -> Tuple[bool, str]:
        if type(timestamp) != float:
            return (False, "the timestamp must be float")
        if timestamp < 0:
            return (False, "the timestamp must be a vaid number" )
        if timestamp is None:
            return(False, "the timestamp must not be None")
        return (True,"")
    

    def to_dict(self):
        return {
            "type": self.tipo,
            "current_balance": self.saldoNaHora,
            "timestamp": self.hora,
            "value": self.quantia
        }
    
    

         
    
