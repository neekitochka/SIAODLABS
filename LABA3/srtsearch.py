''' Метод Кнута-Морриса-Пратта'''

print("\nМетод Кнута-Морриса-Пратта")

def prefixCalc(text, find):
    new_text = find + "#" + text
    prefix = []
    for i in range(len(new_text)):
        prefix.append(0)
    for i in range(1, len(new_text)):
        k = prefix[i - 1]
        while k > 0 and new_text[k] != new_text[i]:
            k = prefix[k - 1]
        if new_text[k] == new_text[i]:
            k += 1
        prefix[i] = k
    return prefix

def searchKMP(text, find, ignore):
    result = []
    if ignore:
        text=text.lower()
        find=find.lower()
    prefix = prefixCalc(text, find)
    prefix = prefix[len(find) + 1:]
    for i in range(len(prefix)):
        if prefix[i]==len(find):
            result.append([i - len(find) + 1, i])
    return result

text=input("\nИсходный текст: ")
search_str=input("Подстрока: ")

print("Учитывать регистр:\n1-Выкл\n2-Вкл")
case=int(input())

if(case==1):
    result=searchKMP(text,search_str,True)
else:
    result=searchKMP(text,search_str,False)

print(result)

print("\nМетод Бойера-Мура")
def tableCalc(find):
    length=len(find)
    table = []
    for i in range(256):
        table.append(length)
    for i in range(length - 1):
        table[ord(find[i])] = length - 1 - i
    return table

def searchBM(text, find, ignore):
    result = []
    nxt = 0
    length=len(find)
    if ignore:
        text=text.lower()
        find=find.lower()
    table = tableCalc(find)
    while len(text) - nxt >= length:
        if text[nxt:(nxt + length)] == find:
            result.append((nxt, nxt + length - 1))
        nxt += table[ord(text[nxt + length - 1])]
    return result

text=input("\nИсходный текст: ")
search_str=input("Подстрока: ")

print("Учитывать регистр:\n1-Выкл\n2-Вкл")
case=int(input())

if(case==1):
    result=searchBM(text,search_str,True)
else:
    result=searchBM(text,search_str,False)

print(result)