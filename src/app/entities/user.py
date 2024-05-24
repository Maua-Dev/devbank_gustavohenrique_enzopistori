
from ..errors.entity_errors import ParamNotValidated
import re
from typing import Tuple

class User:
    name: str
    agency: int
    account: str
    current_balance: float

    def __init__(self, name:str = None, agency:int = None, account:str = None, current_balance:float = None) -> None:
          validation_name = self.validate_name(name)
          if validation_name[0] is False:
               raise ParamNotValidated("name", validation_name[1])
          self.name = name

          validation_agency = self.is_valid_agency_number(agency)
          if validation_agency[0] is False:  
              raise ParamNotValidated("Invalid Agency Number", validation_agency[1]) 
          self.agency = agency

          validation_account = self.validate_account(account)
          if validation_account[0] is False:
              raise ParamNotValidated("Invalid Account Number", validation_account[1])
          self.account = account
         #Fazer a validação da agencia em formato XXXXX-X

          validation_current_balance = self.validate_current_balance(current_balance)
          if validation_current_balance[0] is False:
              raise ParamNotValidated("Invalid Current_Balance", validation_current_balance[1])
          self.current_balance = current_balance
    
    
    @staticmethod
    def is_valid_agency_number(agency: int) -> bool:
        if agency is None:
             return(False, "Agency is reequired")
        if type(agency) != int:
             return(False, "Agency must be int")
        if agency < 0:
             return(False, "Agency must be a positive number")
        if 1 <= agency <= 9999:
             return (True, "")
    
    @staticmethod
    def validate_current_balance(current_balance: float) -> bool:
         if current_balance is None:
              return (False, "Current Balance is required") 
         if type(current_balance) != float:
              return (False, "Current Balance must be a float")
         if current_balance < 0:
              return (False, "Current Balance must be positive")
         return (True, "")
    
    @staticmethod
    def validate_name(name: str) -> Tuple[bool, str]:
         if name is None:
              return(False,"Name is required")
         if type(name) != str:
              return(False, "Name must be a string")
         if len(name) < 3:
              return(False, "Name must be at least 3 characters long")
         return (True, "")
    
    @staticmethod
    def validate_account(account: str) -> Tuple[bool, str]:
         if account is None:
              return(False,"Account is required")
         if type(account) != str:
              return(False,"Account must be a string")
         if re.match(r'^\d{5}-\d{1}$', account):
              return(True, "")
         return(False,"Account format must be XXXXX-X")
           #re.match é uma função para fazer comparação entre strings,
              #r=raw(ignora caracter de escape), \d=digitos 0-9, {5} indica que o caracter anterior(\d) deve ocorrer 5 vezes
              # - corresponde ao hifen literalmente

    @staticmethod
    def validate_user_id(user_id: int) -> Tuple[bool, str]:
        if user_id is None:
            return (False, "Missing 'user_id' parameter")

        if type(user_id) != int:
            return (False, "Parameter 'user_id' must be an integer")
        
        if user_id < 0:
            return (False, "Parameter 'user_id' must be a positive integer")

        return (True, "")

    def to_dict(self):
        return {
            "name": self.name,
            "agency": self.agency,
            "account": self.account,
            "current_balance": self.current_balance
        }
