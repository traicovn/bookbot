def count_words(text):
    words = text.split()
    return len(words)

def char_count(text: str) -> dict[str, int]:

    text = text.lower()
    counts = {}

    for char in text:
        counts[char] = counts.get(char, 0) + 1
    return counts

def sorted_char_list(char_counts: dict[str, int]) -> list[dict[str, int]]:
    char_list = [{"char": ch, "num": count}
             for ch, count in char_counts.items() if ch.isalpha()]
    char_list.sort(key=lambda x: x["num"], reverse=True)

    return char_list
