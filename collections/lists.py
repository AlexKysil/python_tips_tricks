
# Unpack List / Tuple

# 1
p = (4,5)
x, y = p

print(x)
print(y)

# 2
data = ["ACME", 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print('\n ------------------------------')
print(name)
print(date)

# 3 Unpack with not stickt length
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print('\n ------------------------------')
print(name)
print(email)
print(phone_numbers)

# 4 How to get first / last elements using * sign
record = ("ACME", 50, 91.1, (12, 18, 2012))
name, *_, (*_, year) = record
print('\n ------------------------------')
print(name)
print(year)

# 5
*before, last_el = [10, 8, 7, 1, 9, 5, 10, 3]
print('\n ------------------------------')
print(before)
print(last_el)

# 6
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3,4)
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

print('\n ------------------------------')
for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


# 7 Example with string
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print('\n ------------------------------')
print(uname)
print(homedir)
print(sh)