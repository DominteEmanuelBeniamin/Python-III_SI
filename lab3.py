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
