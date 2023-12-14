# Функция, которая принимает алфавит в качестве аргумента
def symbol_statistics(alphabet):
    # Вложенная функция, которая принимает последовательность и возвращает словарь статистики встречаемости символов
    def count_symbols(sequence):
        # Словарь stats инициализируется значениями 0 для каждого символа из заданного алфавита
        stats = {symbol: 0 for symbol in alphabet}
        # Общее количество символов в последовательности
        total_symbols = len(sequence)

        for char in sequence:
            # Если символ присутствует в словаре stats, то соответствующий счетчик увеличивается на 1
            if char in stats:
                stats[char] += 1

        # Цикл for, который проходит по элементам словаря stats
        for symbol, count in stats.items():
            # Преобразование счетчика в процентное значение. Форматирование числа с плавающей точкой до двух знаков
            # после запятой
            stats[symbol] = f"{(count / total_symbols) * 100:.2f}%"

        return stats

    return count_symbols


# Пример использования функции symbol_statistics для анализа статистики символов в последовательностях РНК и ДНК
if __name__ == '__main__':
    # Для РНК
    rna_alphabet = 'AGCU'
    # rna_counter создает объект функции для подсчета статистики символов в РНК с использованием функции
    # symbol_statistics, передавая алфавит РНК в качестве аргумента
    rna_counter = symbol_statistics(rna_alphabet)
    rna_sequence = 'GAUCCGAUACG'
    # rna_stats вызывает созданный объект функции rna_counter для анализа статистики символов в rna_sequence
    rna_stats = rna_counter(rna_sequence)
    print(f"RNA Symbol Statistics: {rna_stats}")

    # Для ДНК
    dna_alphabet = 'AGCT'
    # dna_counter создает объект функции для подсчета статистики символов в ДНК с использованием функции
    # symbol_statistics, передавая алфавит ДНК в качестве аргумента
    dna_counter = symbol_statistics(dna_alphabet)
    dna_sequence = 'ATGCTGACCTGA'
    # dna_stats вызывает созданный объект функции dna_counter для анализа статистики символов в dna_sequence
    dna_stats = dna_counter(dna_sequence)
    print(f"DNA Symbol Statistics: {dna_stats}")
