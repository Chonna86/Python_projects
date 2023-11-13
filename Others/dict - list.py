def lookup_key(data, value):
    data = {}
    keys = []
    for k, v in data.items() :
        if v != value :
            continue
        else :
            keys.append(list(k))
            
    return keys
a = lookup_key({'key1': 1, 'key2': 2, 'key3': 3, 'key4': 2}, 2)
print(a)
