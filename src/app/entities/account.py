#fiz tudo certo??

from ..errors.entity_errors import ParamNotValidated
import re

class Account:
    name: str
    agency: int
    account: str
    current_balance: float

    def __init__(self, name:str, agency:int, account:str, current_balance:float) -> None:
         if type(name) != str:
              raise ParamNotValidated("Invalid Name")
         self.name = name

         if not self.is_valid_agency_number(agency):  
              # pq se eu tirar o self ele nao reconhece a função? usar o static method nao devia fazer a função nao depender do class?
              raise ParamNotValidated("Invalid Agency Number") 
         self.agency = agency

         if not re.match(r'^\d{5}-\d{1}$', account):
              #re.match é uma função para fazer comparação entre strings,
              #r=raw(ignora caracter de escape), \d=digitos 0-9, {5} indica que o caracter anterior(\d) deve ocorrer 5 vezes
              # - corresponde ao hifen literalmente
              raise ParamNotValidated("Invalid Account Number")
         self.account = account
         #Fazer a validação da agencia em formato XXXXX-X

         if not self.validate_current_balance(current_balance):
              raise ParamNotValidated("Invalid Current_Balance")
         self.current_balance = current_balance
    
    
    @staticmethod
    def is_valid_agency_number(agency: int) -> bool:
        return 1000 <= agency <= 9999
    
    @staticmethod
    def validate_current_balance(current_balance: float) -> bool:
         if current_balance is None:
              return False 
         if type(current_balance) != float:
              return False
         if current_balance < 0:
              return False
         return True
    
