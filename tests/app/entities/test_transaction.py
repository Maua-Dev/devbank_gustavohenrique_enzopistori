import pytest
from src.app.entities.transaction import Transaction
from src.app.errors.entity_errors import ParamNotValidated
from src.app.enums.transaction_type_enum import TransactionTypeEnum

class Teste_Transac:
    def teste_transacoes(self):
        transacao = Transaction(TransactionTypeEnum.DEPOSIT, 1.0, 24556.0, 500.0)
        assert transacao.timestamp == 500.0
        assert transacao.value == 1.0
        assert transacao.types == TransactionTypeEnum.DEPOSIT
        assert transacao.current_balance == 24556.0
    '''
    def test_user_name_is_none(self):
        with pytest.raises(ParamNotValidated):
            User(agency=1234, account='00000-0', current_balance=1000.0)
    
    def test_user_name_is_not_string(self):
        with pytest.raises(ParamNotValidated):
            User(name=1, agency=1234, account='00000-0', current_balance=1000.0)

    def test_agency_is_none(self):
        with pytest.raises(ParamNotValidated):
            User(name="Enzo", account='00000-0', current_balance=1000.0)

    def test_agency_is_not_int(self):
        with pytest.raises(ParamNotValidated):
            User(name="Enzo", agency="Enzo", account='00000-0', current_balance=1000.0)

    def test_agency_is_negative(self):
        with pytest.raises(ParamNotValidated):
            User(name="Enzo", agency=-1234, account='00000-0', current_balance=1000.0)
    
    def test_account_is_none(self):
        with pytest.raises(ParamNotValidated):
            User(name="Enzo", agency=1234, current_balance=1000.0)
    
    def test_account_is_not_int(self):
         with pytest.raises(ParamNotValidated):
            User(name="Enzo", agency=1234, account='Enzo', current_balance=1000.0)

    def test_current_balance_is_none(self):
        with pytest.raises(ParamNotValidated):
            User(name="Enzo", agency=1234, account='00000-0')

    def test_current_balance_is_negative(self):
        with pytest.raises(ParamNotValidated):
            User(name="Enzo", agency=1234, account='00000-0', current_balance=-1000.0)'''