import csv
with open('text.txt','w') as file:
    txt = [
        ["Это первая строка."],
        ["Здесь могла быть ваша реклама."],
        ["I feel so sigma."],
        ["Здесь определенно что-то есть."],
        ["Последняя строка."]
    ]
    writer = csv.writer(file)
    writer.writerows(txt)


with open('text.txt','r') as file:
    content = file.readlines()
    num_lines = len(content)
    words = sum(len(line.split()) for line in content)
    longest_words = max(content,key = len).strip() if content else None

print(f'Количество сторк:{num_lines}')
print(f'Количество слов:{words}')
print(f'Самая длинная строка:{longest_words}')

