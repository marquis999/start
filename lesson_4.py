#"Полиморфизм"

class PaymentMethod:
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        return f"Сумма {amount}, оплачивается по кредитной карте"
    
