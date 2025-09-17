s = input("Введите строку: ").strip()

words = s.split()

if not words:
    print("Строка пустая!")
else:
    words2 = [word for word in words if len(word) % 2 == 0] 

    longest = max(words, key=len)

    print(f"Слов с четной длиной: {len(words2)}")
    print(f"Самое длинное слово: '{longest}' ({len(longest)} символов)")