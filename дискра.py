# 1) Найти пересечение заданных n множеств

def intersection_of_sets(sets):
    # Находит пересечение всех заданных множеств
    if not sets:
        return set()  # Если списков нет, вернуть пустое множество

    # Пересекаем все множества
    result = set.intersection(*sets)
    return result

# Пример использования
sets = [
    {1, 2, 3, 4},
    {2, 3, 5, 6},
    {2, 3, 7, 8},
]
result = intersection_of_sets(sets)
print("Пересечение множеств:", result)




# 2) Построение кодов Фано

def calculate_probabilities(text):

    from collections import Counter
    total_length = len(text)
    frequencies = Counter(text)
    probabilities = [(char, freq / total_length) for char, freq in frequencies.items()]
    return sorted(probabilities, key=lambda x: x[1], reverse=True)

def fano_encoding(probabilities):
    def divide_probs(probs):
        total = sum(prob for _, prob in probs)
        cumulative = 0
        for i, (_, prob) in enumerate(probs):
            cumulative += prob
            if cumulative >= total / 2:
                return probs[:i + 1], probs[i + 1:]
        return probs, []

    def encode(probs, prefix=""):
        if len(probs) == 1:
            char, _ = probs[0]
            return {char: prefix}
        left, right = divide_probs(probs)
        codes = {}
        codes.update(encode(left, prefix + "0"))
        codes.update(encode(right, prefix + "1"))
        return codes

    return encode(probabilities)

def build_fano_codes(text):
    probabilities = calculate_probabilities(text)
    codes = fano_encoding(probabilities)
    return codes

# Пример использования
text = "example text for fano coding"
fano_codes = build_fano_codes(text)
print("Коды Фано:")
for char, code in fano_codes.items():
    print(f"'{char}': {code}")
