# -*- coding: utf-8 -*-
"""lab3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rkMj69Ke0Ak3c0U67a-EN7NmzPKRq7qV
"""

def list_sets(a, b):
    return [set(a) & set(b), set(a) | set(b), set(a) - set(b), set(b) - set(a)]

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

result = list_sets(a, b)
print(result)

def char_count(s):
    return {char: s.count(char) for char in s}

s = "Ana has apples."
result_count = char_count(s)
print(result_count)

def compare_dic(d1, d2):
    if d1.keys() != d2.keys():
        return False
    for key in d1:
        if type(d1[key]) == dict and type(d2[key]) == dict:
            if not compare_dic(d1[key], d2[key]):
                return False
        elif type(d1[key]) == list and type(d2[key]) == list:
            if len(d1[key]) != len(d2[key]) or any(not compare_dic({i: d1[key][i]}, {i: d2[key][i]}) for i in range(len(d1[key]))):
                return False
        elif type(d1[key]) == set and type(d2[key]) == set:
            if d1[key] != d2[key]:
                return False
        else:
            if d1[key] != d2[key]:
                return False
    return True

dic1 = {"a": 1, "b": {"c": 2, "d": [3, 4]}, "e": {5, 6}}
dic2 = {"a": 1, "b": {"c": 2, "d": [3, 4]}, "e": {5, 6}}

print(compare_dic(dic1, dic2))

def build_xml_element(tag, content, **attrs):
    attr_str = " ".join(f'{key}="{value}"' for key, value in attrs.items())
    return f"<{tag} {attr_str}>{content}</{tag}>"
result = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
print(result)

def validate_dict(rules, d):
    if set(d.keys()) != {rule[0] for rule in rules}:
        return False

    for key, prefix, middle, suffix in rules:
        value = d.get(key, "")

        if (prefix and not value.startswith(prefix)) or (suffix and not value.endswith(suffix)):
            return False

        if middle:
            pos = value.find(middle)
            if pos <= 0 or pos + len(middle) >= len(value):
                return False

    return True


s = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
d = {
    "key1": "come inside, it's too cold out",
    "key3": "this is not valid"
}

print(validate_dict(s, d))

def set_operations(*sets):
    results = {}

    for i, a in enumerate(sets):
        for j, b in enumerate(sets):
            if i < j:
                results[f"{a} | {b}"] = a | b
                results[f"{a} & {b}"] = a & b
                results[f"{a} - {b}"] = a - b
                results[f"{b} - {a}"] = b - a

    return results

lst = [1, 2, 2, 3, 4, 4, 4, 5]
result = count_unique_duplicates(lst)
print(result)

def traverse_mapping(mapping):
    result = []
    current = mapping['start']
    visited = set()

    while current not in visited:
        result.append(current)
        visited.add(current)
        current = mapping[current]

    result.append(current)
    return result[:-1]

print(traverse_mapping({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))

def my_function(*args, **kwargs):
    count = 0
    for arg in args:
        if arg in kwargs.values():
            count += 1
    return count

result = my_function(1, 2, 3, 4, x=1, y=2, z=3, w=5)
print(result)