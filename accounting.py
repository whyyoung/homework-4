salesperson_index = 0
internet_index = 1

print "*" * 80

type_order_file = open("orders-by-type.txt")
melon_tallies = {"Musk": 0, "Hybrid": 0, "Watermelon": 0, "Winter": 0}
melon_prices = {"Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00}
total_revenue = 0

for line in type_order_file:
    data = line.split("|")
    melon_type = data[1]
    melon_count = int(data[2])
    melon_tallies[melon_type] += melon_count

for melon_type in melon_tallies:
    price = melon_prices[melon_type]
    revenue = price * melon_tallies[melon_type]
    total_revenue += revenue
    # print "We sold %d %s melons at %0.2f each for a total of %0.2f" % (melon_tallies[melon_type], melon_type, price, revenue)
    print "We sold {} {} melons at {:.2f} each for a total of {:.2f}".format(melon_tallies[melon_type], melon_type, price, revenue)

type_order_file.close()

print "*" * 80

sales_order_file = open("orders-with-sales.txt")
sales = [0, 0]
for line in sales_order_file:
    data = line.split("|")
    if data[1] == "0":
        sales[0] += float(data[3])
    else:
        sales[1] += float(data[3])
print "Salespeople generated ${:.2f} in revenue.".format(sales[1])
print "Internet sales generated ${:.2f} in revenue.".format(sales[0])
if sales[1] > sales[0]:
    print "Guess there's some value to those salespeople after all."
else:
    print "Time to fire the sales team! Online sales rule all!"
sales_order_file.close()

print "*" * 80
