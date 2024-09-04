product_Prices=[1000,50,20,30,500,600,2000]
#display all product prices below 1000
def filterdata(price):
    return price<1000
    
new_prices=list(filter(filterdata, product_Prices))
print(product_Prices)
print(new_prices)
