ice = {'메로나' : 1000, '폴로포': 1200, '빵빠레' : 1800, '조스바' : 200}

print(ice['빵빠레'])
ice['메로나'] = 1500
print(ice)
del ice['폴로포']
print(ice)
inventory = {'메로나' : [1000, 20], '폴로포': [1200,5], '빵빠레' : [1800,80], '조스바' : [200,50]}
print(inventory)
print(inventory['메로나'][0])
print(inventory['메로나'][1])

print(inventory['돼지바'])
inventory['돼지바'] = [900, 30]

print(inventory.keys())
print(inventory.values())
print(inventory.items())

for k, v in inventory.items():
    print("키:",k)
    print("밸류:",v)