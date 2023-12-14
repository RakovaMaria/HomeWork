from abc import ABC, abstractmethod


# Абстрактный базовый класс для представления биологических последовательностей
class NucleotideSequence(ABC):

    # Инициализация объекта.
    def __init__(self, name, sequence):
        self.name = name
        self.sequence = sequence

    # Метод возвращает длину последовательности
    def __len__(self):
        return len(self.sequence)

    # Абстрактное свойство, возвращает строку с алфавитом нуклеотидов для данного типа последовательности
    @property
    @abstractmethod
    def _alphabet_str(self) -> str:
        pass

    # Свойство, возвращает последовательность нуклеотидов
    @property
    def sequence(self) -> str:
        return self._sequence

    # Свойство с сеттером, проверяющим соответствие последовательности алфавиту. Сеттер вызывается, когда
    # устанавливается значение свойства
    @sequence.setter
    # Новая последовательность seq в виде строки
    def sequence(self, seq: str):
        if set(self._alphabet_str) != set(seq):
            raise ValueError(f'Inputted sequence is not {self.__class__.__name__}')
        # Все символы приводятся к верхнему регистру
        self._sequence = seq.upper()

    # Метод возвращает комплементарную последовательность
    def compliment_seq(self):
        trans_dict = str.maketrans(self._alphabet_str, self._alphabet_str[::-1])
        return self._sequence.translate(trans_dict)

    # Свойство, возвращает долю каждого нуклеотида в последовательности
    @property
    # Метод использует словарь frac_dict, инициализированный нулями для каждого нуклеотида из алфавита. Затем
    # проходится по каждому нуклеотиду в последовательности и увеличивает соответствующий счетчик в словаре на величину
    # 1 / len(self).
    def nucleotides_fraction(self) -> dict:
        frac_dict = dict(zip(self._alphabet_str, [0, 0, 0, 0]))
        for nucl in self.sequence:
            frac_dict[nucl] += 1 / len(self)
        return frac_dict

    # Метод выводит молекулярный вес одноцепочечной молекулы
    def get_one_stranded_molecular_weight(self):
        nucleotide_molecular_weight = 330
        print(f'Molecular weight of the {self.name} is {nucleotide_molecular_weight * len(self)} g/mol')


class RNA(NucleotideSequence):
    # Алфавит РНК
    _alphabet_str = 'AGCU'

    # Таблица кодонов для трансляции РНК в белок
    _codon_table = {
        'AUA': 'I', 'AUC': 'I', 'AUU': 'I', 'AUG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',
        'AAC': 'N', 'AAU': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGU': 'S', 'AGA': 'R', 'AGG': 'R',
        'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',
        'CAC': 'H', 'CAU': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
        'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
        'GAC': 'D', 'GAU': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G',
        'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
        'UUC': 'F', 'UUU': 'F', 'UUA': '', 'UAG': '', 'UGA': '',
        'UGC': 'C', 'UGU': 'C', 'UGG': 'W',
    }

    # Метод трансляции РНК в белок
    def translate(self):
        # Трансляция происходит по три нуклеотида (кодона) за раз, и поэтому длина должна быть кратной 3
        if not len(self) % 3 == 0:
            raise ValueError(f'Sequence length is not a multiple of 3')

        protein = []
        for nucl_num in range(0, len(self.sequence), 3):
            protein.append(self._codon_table[self.sequence[nucl_num:nucl_num + 3]])
            # Метод возвращает строку, полученную объединением всех аминокислот
        return ''.join(protein)


class DNA(NucleotideSequence):
    # Алфавит ДНК
    _alphabet_str = 'AGCT'

    # Метод транскрипции ДНК в РНК
    def transcript(self, name_of_rna: str = 'New RNA') -> RNA:
        # Создается словарь trans_dict с использованием метода str.maketrans, который представляет собой таблицу
        # символов
        trans_dict = str.maketrans(self._alphabet_str, 'AGCU')
        return RNA(name_of_rna, self.sequence.translate(trans_dict))


# Основной блок кода
if __name__ == '__main__':
    # Создание объекта класса DNA "Sample DNA" с заданной последовательностью
    dna_sequence = DNA(name="Sample DNA", sequence="ATGCTGACCTGA")

    # Вывод информации о ДНК
    print(f"Name: {dna_sequence.name}")
    print(f"Sequence: {dna_sequence.sequence}")
    print(f"Length: {len(dna_sequence)}")
    print(f"Alphabet: {dna_sequence._alphabet_str}")
    print(f"Nucleotides Fraction: {dna_sequence.nucleotides_fraction}")
    dna_sequence.get_one_stranded_molecular_weight()
    print(f"Complementary Sequence: {dna_sequence.compliment_seq()}")

    # Транскрипция ДНК в РНК.
    rna_sequence = dna_sequence.transcript(name_of_rna="Generated RNA")

    # Вывод информации о РНК.
    print(f"\nRNA Name: {rna_sequence.name}")
    print(f"RNA Sequence: {rna_sequence.sequence}")
    print(f"RNA Length: {len(rna_sequence)}")
    print(f"RNA Alphabet: {rna_sequence._alphabet_str}")
    print(f"RNA Nucleotides Fraction: {rna_sequence.nucleotides_fraction}")
    rna_sequence.get_one_stranded_molecular_weight()
    print(f"RNA Complementary Sequence: {rna_sequence.compliment_seq()}\n")

    # Трансляция РНК в белок.
    protein_sequence = rna_sequence.translate()

    # Вывод информации о белке.
    print(f"Protein Name: {rna_sequence.name}")
    print(f"Protein Sequence: {protein_sequence}")
    print(f"Protein Length: {len(protein_sequence)}")
    print(f"Protein Alphabet: {''.join(set(protein_sequence))}")
