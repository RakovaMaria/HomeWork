def find_all_overlapping(query, text):
    indexes = []
    current = text
    shift = 0

    while True:
        index = current.find(query)
        if index == -1:
            break
        indexes.append(index + shift)
        shift += index + 1
        current = current[index + 1:]

    return indexes

ms = "abcbcbc" * 10
query = "bc"
indexes = find_all_overlapping(query, ms)
print(indexes)
