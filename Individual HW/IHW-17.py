from collections import Counter

def read_fasta(fasta_file):
    sequences = {}
    current_sequence = None
    with open(fasta_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                current_sequence = line[1:]
                sequences[current_sequence] = ''
            else:
                sequences[current_sequence] += line
    return sequences


def read_bed(bed_file):
    intervals = []
    with open(bed_file, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 3:
                chrom, start, end = parts
                intervals.append((chrom, int(start), int(end)))
            else:
                print(f"Неправильный формат строки: {line}")
    return intervals



def calculate_substitution_statistics(sequences, intervals):
    substitution_statistics = {}
    for interval in intervals:
        chrom, start, end = interval
        interval_sequence = sequences[chrom][start:end]
        substitution_statistics[interval] = Counter(interval_sequence)
    return substitution_statistics

if __name__ == "__main__":
    fasta_file = "C:/Users/Мария/PycharmProjects/pythonProject/Черновики/example.fasta"
    bed_file = "C:/Users/Мария/PycharmProjects/pythonProject/Черновики/example.bed"


    sequences = read_fasta(fasta_file)
    intervals = read_bed(bed_file)
    substitution_statistics = calculate_substitution_statistics(sequences, intervals)

    for interval, stats in substitution_statistics.items():
        print(f"Interval: {interval}")
        print("Substitution statistics:")
        for base, count in stats.items():
            print(f"{base}: {count}")
