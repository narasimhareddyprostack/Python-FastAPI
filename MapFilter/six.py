product_Prices=[1000,50,20,30,500,600,2000]
#display all product prices below 1000
new_prices=[]

for price in product_Prices:
    if price <1000:
        new_prices.append(price)
    
print(product_Prices)    
print(new_prices)