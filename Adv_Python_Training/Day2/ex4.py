## bill calculation
print('==============================================================')
sgst = 2.5
cgst = 2.5
burgerPrice = 30
pizzaPrice = 100
soupPrice = 40
priceList = [burgerPrice, pizzaPrice, soupPrice]
print('Food Items')
print(' 1. Burger')
print(' 2. Pizza')
print(' 3. Soup')
print('Enter your choice of item:',end='')
userChoiceOfFood = int(input())-1
print ('Enter quantity:',end='')
userChoosenQuantity = int(input())
basicFoodPrice = priceList[userChoiceOfFood]*userChoosenQuantity
calculatedCGST = (basicFoodPrice * 2.5)/100
calculatedSGST = (basicFoodPrice * 2.5)/100
actualFoodPrice = basicFoodPrice + calculatedCGST + calculatedSGST
print(f'Total tax to be paid {calculatedCGST+calculatedSGST} rupees')
print(f'Food price {basicFoodPrice} rupees')
print(f'Total paybel ammount {actualFoodPrice} rupees')
print('Thank you visit again') 
print('==============================================================')