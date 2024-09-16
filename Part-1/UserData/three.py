numbers=[4,42,93,41,15,6,17,81,9,110]
evens=0
odds=0
for number in numbers:
    if number %2==0:
        evens=evens+1
    else:
        odds = odds+1

print("No of Even Numbers:", evens)
print("No of Odd Numbers:",odds)