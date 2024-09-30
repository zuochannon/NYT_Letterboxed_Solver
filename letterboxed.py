# Scrabble dictionary from https://github.com/redbo/scrabble/blob/master/dictionary.txt
if __name__ == "__main__":
    LETTERS = input("Enter the letters for the daily puzzle: ")
    LETTERS = LETTERS.upper()

    try:
        LETTERS = ''.join(set(filter(str.isalpha, LETTERS)))
        assert len(LETTERS) == 12
    except AssertionError:
        print("Expected letter count: 12")
        print("Received: " + str(len(LETTERS)))

    invalid_pairs = []
    for i, char in enumerate(LETTERS):
        for j, other_char in enumerate(LETTERS):
            if i // 3 == j // 3:
                invalid_pairs.append(char + other_char)

    valid_words = []

    with open('words.txt') as f:
        for word in f:
            word = word.strip()
            for x in invalid_pairs:
                if x not in word:
                    valid_words.append(word)
                else:
                    break
    unique_words = set(valid_words)
    # print(len(unique_words))

    # ['ZYMURGIES', 'ZYMURGY', 'ZYZZYVA', 'ZYZZYVAS', 'ZZZ']
    print(sorted(list(unique_words))[-5:])
