import codecademylib3

import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

visits_cart = pd.merge(visits, cart, how = 'left')
print(visits_cart)
print(len(visits_cart[visits_cart.cart_time.isnull()]))

percent_in_cart = (len(visits_cart[visits_cart.cart_time.notnull()]) / len(visits_cart.cart_time))
print('#' *100)
print('the conversion rate from site to cart is')
print(percent_in_cart)
print('#' *100)
cart_checkout = pd.merge(cart, checkout, how = 'left')
print(cart_checkout)
print(len(cart_checkout[cart_checkout.checkout_time.notnull()]))

percent_in_checkout =  (len(cart_checkout[cart_checkout.checkout_time.notnull()]) / len(cart_checkout.checkout_time))
print('#' *100)
print('The conversion rate from cart to checkout is')
print(percent_in_checkout)
print('#' *100)
all_data = visits.merge(cart, how='left')\
                  .merge(checkout, how='left')\
                  .merge(purchase, how='left')
# print(all_data.head(100))

total_checkout = len(all_data[all_data.checkout_time.notnull()])
total_purchase = len(all_data[all_data.purchase_time.notnull()])

checkout_to_purchase = total_purchase / total_checkout
print('#' *100)
print('The conversion rate from checkout to purchase is')
print(checkout_to_purchase)
print('#' *100)

all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time
print(all_data)
print('#' *100)
print('the average time from visit to purchase (on successful conversions) is')
print(all_data.time_to_purchase.mean())
print('#' *100)
