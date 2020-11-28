from decimal import Decimal

tax_rate = Decimal('7.25') / Decimal(100)
print(tax_rate)

purchase_amount = Decimal('2.95')
print(tax_rate*purchase_amount)
