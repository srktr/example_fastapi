import pytest
from app.calculations import add, sub, div, mul, BankAccount, InsufficientFunds


@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1, num2, exp",[(3,2,5),(7,1,8),(12,4,16)])

def test_add(num1,num2,exp):
    assert add(num1,num2) == exp

@pytest.mark.parametrize("num1, num2, exp",[(3,2,1),(7,1,6),(12,4,8)])

def test_sub(num1,num2,exp):
    assert sub(num1,num2) == exp

@pytest.mark.parametrize("num1, num2, exp",[(4,2,2),(6,2,3),(12,4,3)])

def test_div(num1,num2,exp):
    assert div(num1,num2) == exp

@pytest.mark.parametrize("num1, num2, exp",[(3,2,6),(7,1,7),(12,4,48)])

def test_mul(num1,num2,exp):
    assert mul(num1,num2) == exp


def test_bank_test_initial_amount(bank_account):
    assert bank_account.balance == 50

def test_bank_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0

def test_withdraw(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance == 30

def test_deposit(bank_account):
    bank_account.deposit(20)
    assert bank_account.balance == 70

def test_collect_interest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance,6) == 55

@pytest.mark.parametrize("dep, wit, exp",[(200,100,100),(71500,5000,66500),(12,4,8)])

def test_bank_transaction(zero_bank_account, dep, wit, exp):
    zero_bank_account.deposit(dep)
    zero_bank_account.withdraw(wit)
    assert zero_bank_account.balance == exp

def test_insufficient_funds(bank_account):
    with pytest.raises(InsufficientFunds):
        bank_account.withdraw(200)

