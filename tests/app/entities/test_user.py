import pytest
from src.app.entities.user import User
from src.app.errors.entity_errors import ParamNotValidated

class Test_User:
    def test_user(self):
        user= User("Enzo",1234,'00000-0',1000.0)
        assert user.name == "Enzo"
        assert user.agency == 1234
        assert user.account == '00000-0'
        assert user.current_balance == 1000.0
    
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
            User(name="Enzo", agency=1234, account='00000-0', current_balance=-1000.0)