def search_word_in_text(text, word):
    lines = text.split('\n')
    results = []

    for i, line in enumerate(lines, start=1):
        index = line.find(word)
        while index != -1:
            start = max(0, index - 15)
            end = min(len(line), index + len(word) + 15)
            context = line[start:end]
            results.append((i, index, context))
            index = line.find(word, index + 1)

    return results

def print_search_results(results):
    print("Номер строки\tПозиция в строке\tКонтекст")
    print("-" * 40)
    for result in results:
        print(f"{result[0]}\t{result[1]}\t\t{result[2]}")

def main():
    input_text = """ACGTGTCAGTACGTAGCTAGCTAGCTAGCTGACGATCGATCGATCGATCGTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTA
    GCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTA
    GCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAG"""

    search_word = input("слово: ")
    results = search_word_in_text(input_text, search_word)
    print_search_results(results)

if __name__ == "__main__":
    main()
