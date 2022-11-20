
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