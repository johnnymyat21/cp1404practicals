"""
Word Occurrences
Estimate: 25 minutes
Actual:   (fill in after you finish)
"""


def main():
    text = input("Text: ").strip()
    words = text.lower().split()
    word_to_count = {}
    for word in words:
        # Use get for EAFP-like behaviour
        word_to_count[word] = word_to_count.get(word, 0) + 1

    # Sort words alphabetically
    sorted_words = sorted(word_to_count.keys())
    width = max((len(word) for word in sorted_words), default=0)
    for word in sorted_words:
        print(f"{word:{width}} : {word_to_count[word]}")


if __name__ == "__main__":
    main()
