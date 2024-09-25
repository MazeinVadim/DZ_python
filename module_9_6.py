def all_variants(text):
    length = len(text)
    for size in range(1, length + 1):
        for start in range(length - size + 1):
            yield text[start:start + size]

a = all_variants("abc")
for i in a:
    print(i)