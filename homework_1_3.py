# HW_1
print("hello girl")
# Variables
a = "hello"
b = 16
c = 2.5
d = ['apple', 'banana', 'cherry']
e = ('green', 'yellow', 'red')
f = {'comedy', 'drama', 'biopic'}
g = frozenset(d)
i = {
    "name": "Anna",
    "age": 35,
    "weight": 57
}
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(i)

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(i))

x = 'golden'
y = 'bridge'
z = (x + y)
print(z)
w = (x + " " + y)
print(w)
n = 33
s = 'cows'
result = str(n), s
print(result)
result_2 = str(n) + " " + s
print(result_2)
#
#
#
#
#
#


#HW_3
int_item = 10
comp_item = 18
mult_int = int_item * 2
item_2 = True
item_3 = False
item_4 = 0
item_5 = 1

usd_item = 'usd'
usd_usd_rate = 1

eur_item = 'eur'
usd_eur_rate = 0.86

uah_item = 'uah'
usd_uah_rate = 26.23

chf_item = 'chf'
usd_chf_rate = 0.91

rub_item = 'rub'
usd_rub_rate = 71.88

byn_item = 'byn'
usd_byn_rate = 2.46

# 20
if mult_int > comp_item:
    print("Переменная mult_int больше", comp_item)

# 21 22
div_int = int_item / 2
if div_int < comp_item:
    print("Переменная div_int меньше", comp_item)

# 23 24
item_1 = int_item + 10
if item_1 < comp_item:
    print("Переменная item_1 меньше", comp_item)
else:
    print("Переменная item_1 больше или равна", comp_item)

# 25
if item_2:
    print("Переменная item_2 =", item_2)
else:
    print("Переменная item_2 =", item_3)

# 26
if item_3:
    print("Переменная item_3 =", item_2)
else:
     print("Переменная item_3 =", item_3)

# 27
if item_5:
    print("Переменная item_5 =", item_5)
else:
    print("Переменная item_5 =", item_4)

# 28
if item_4:
    print("Переменная item_4 =", item_5)
else:
    print("Переменная item_4 =", item_4)

# 29
currency_convertor = item_2

# 30 31
if currency_convertor:
    currency_usd = usd_item       # 31.1
    target_currency = eur_item    # 31.2
    target_currency_amount = 50   # 31.3
    currency_result = 0           # 31.4
    if target_currency =='eur':   # 31.4
        currency_result = target_currency_amount * usd_eur_rate
        print(target_currency_amount, eur_item, "=", currency_result, usd_item)

    elif target_currency == 'uah':  # 31.5
        currency_result = target_currency_amount * usd_uah_rate
        print(target_currency_amount, uah_item, "=", currency_result, usd_item)

    elif target_currency == 'chf':  # 31.6
        currency_result = target_currency_amount * usd_chf_rate
        print(target_currency_amount, chf_item, "=", currency_result, usd_item)

    elif target_currency == 'rub':  # 31.6
        currency_result = target_currency_amount * usd_rub_rate
        print(target_currency_amount, rub_item, "=", currency_result, usd_item)

    elif target_currency == 'byn':  # 31.6
        currency_result = target_currency_amount * usd_byn_rate
        print(target_currency_amount, byn_item, "=", currency_result, usd_item)

    else:
        ptint("Unknow currency")































