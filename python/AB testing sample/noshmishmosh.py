import noshmishmosh
import numpy as np

all_visitors = noshmishmosh.customer_visits
total_visitor_count = len(all_visitors)
paying_visitors = noshmishmosh.purchasing_customers
paying_visitor_count = len(paying_visitors)
baseline_percent = 100 * (paying_visitor_count/total_visitor_count)
print(baseline_percent)
payment_history = noshmishmosh.money_spent
average_payment = np.mean(payment_history)
print(average_payment)
new_customers_needed = np.ceil(1240 / average_payment)
print(new_customers_needed)
percentage_point_increase = new_customers_needed / total_visitor_count * 100
print(percentage_point_increase)
lift = (percentage_point_increase / baseline_percent) * 100
print(lift)
ab_sample_size = 494

print('#' * 100)
print('''when calculating the AB sample size the following are the parameters:
      baseline = 18.6
      confidence level = 10%
      lift = 50.54
      which gives us an ab sample size of 494''')
print('#' * 100)



