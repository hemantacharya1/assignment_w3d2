def count_vowels(word: str) -> int:
    return sum(1 for c in word.lower() if c in "aeiou")

def string_length(word: str) -> int:
    return len(word)
