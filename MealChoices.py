import itertools

main_courses = ['beef stew', 'fried fish']
price_main_courses = [28, 23]

desserts = ['ice-cream', 'cake']
price_desserts = [2, 4]

drinks = ['cola', 'wine']
price_drinks = [3, 10]

# Finding out all possible combinations (main, dessert, drink) and printing an affordable option under 30$

for pm, pd, pdr in itertools.product(price_main_courses, price_desserts, price_drinks):
    total_price = pm + pd + pdr
    if total_price <= 30:
        print(f'{main_courses[price_main_courses.index(pm)]} '
              f'{desserts[price_desserts.index(pd)]} '
              f'{drinks[price_drinks.index(pdr)]} {pm + pd + pdr}')