prices = [7,1,5,3,6,4]
min_price=prices[0]
max_price=0
for i in range(0,len(prices)):
    min_price = min(min_price,prices[i])
    profit=prices[i]- min_price
    max_price=max(profit,max_price)
print(max_price)
