a= {'jack','rose','mike','lucy'}
b = {'adam','brian','nikki','sam','jack','lucy'}
print(a | b)  #total name in both sets a and b
print(a & b)  #common name
print(a-b)  #unique data of a in the combined set of a and b
print(b-a)  #unique data of b in the combined set of a and b


price= [100,120,80,70]
earning_per_share = [9,15,0,6]
price_earned_dict = {price[i]:earning_per_share[i] for i in range(len(price))}

#here in the code below, we are returning the actual ration only if the value of e is not 0 otherwise we are returning the value of ratio as -1
pe_ratio = [round(p/e,2) if e!=0 else -1 for p,e in zip(price,earning_per_share)] #here we are rounding off the ratio into .2 decimals
print(pe_ratio)


prices = [120,99,150,80,200]
prices_after_discount = [(price-0.15*price) if price > 100 else price for price in prices]  #here we are giving 15% discount on prices if the price is greater than 100 else the price will remain original

print(prices_after_discount)
print(price_earned_dict)  #creating a dictionary based on comprehension method


transactions = [
    {'customer_name':'Asok','amount':250,'date':'2002-03-24'},
    {'customer_name':'Asok','amount':750,'date':'2002-03-24'},
    {'customer_name':'Sita','amount':400,'date':'2001-03-24'},
    {'customer_name':'Gita','amount':650,'date':'2000-03-24'}
]

unique_names = {transaction['customer_name'] for transaction in transactions}
print(set(unique_names))

products = [
    {"product_name": "Laptop", "category": "Electronics", "price": 1200},
    {"product_name": "Jeans", "category": "Apparel", "price": 40},
    {"product_name": "Coffee Maker", "category": "Home Appliances", "price": 80},
    {"product_name": "Smartphone", "category": "Electronics", "price": 999},
    {"product_name": "Jacket", "category": "Apparel", "price": 60},
    {"product_name": "Blender", "category": "Home Appliances", "price": 150},
    {"product_name": "Book", "category": "Literature", "price": 15}
]

# extracting the data based on the categories

electronics = [product['product_name'] for product in products if product['category']=='Electronics']
Apparel = [product['product_name'] for product in products if product['category']=='Apparel']
Home_Appliances = [product['product_name'] for product in products if product['category']=='Home Appliances']
Literature = [product['product_name'] for product in products if product['category']=='Literature']


#data extraction
concert_a_attendees = {"Alice", "Bob", "Charlie", "Diana"}
concert_b_attendees = {"Bob", "Diana", "Eve", "Frank"}
concert_c_attendees = {"Alice", "George", "Elle", "Frank","Bob"}
#unique in concert A
concert_A = [person for person in concert_a_attendees if
             person not in concert_b_attendees and person not in concert_c_attendees]
#unique in concert B
concert_B = [person for person in concert_b_attendees if
             person not in concert_a_attendees and person not in concert_c_attendees]
#unique in concert C
concert_C = [person for person in concert_c_attendees if
             person not in concert_a_attendees and person not in concert_b_attendees]
#common among all the concerts
common = concert_a_attendees & concert_b_attendees & concert_c_attendees  # common among every concerts


#identifying the maximum temperatures
daily_temperatures = [68, 71, 74, 69, 70, 71, 68, 73, 72, 71, 70, 74, 72, 68]
filtered_temperature = [temp for temp in daily_temperatures if temp>70]

#identifyin unique temperatures
uniques={temp for temp in filtered_temperature}
print(uniques)
