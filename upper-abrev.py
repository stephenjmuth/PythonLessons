

sandwich_orders=['italian','pastrami','ham and cheese','turkey club','blt','pastrami','ham','pb&j','pastrami',]
vowels=['a','e','i','o','u']

for sw in sandwich_orders:
    test=any(letter in list(sw) for letter in vowels)
    if test:
        print(sw.title())
    else:
        print(sw.upper())
