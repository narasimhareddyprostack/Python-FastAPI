prices=[199,99,75,65,1999,2001,4000,6000]

new_prices1 = []
for price in prices:
    if price >2000:
        new_prices1.append(price)

print(prices)
print(new_prices1)