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


def filter_vcf_by_bed(vcf_file, bed_intervals):
    filtered_variants = []
    with open(vcf_file, 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue
            parts = line.strip().split('\t')
            if len(parts) < 2:
                print(f"Неверный формат строки в файле VCF: {line}")
                continue
            chrom = parts[0]
            try:
                pos = int(parts[1])
            except ValueError:
                print(f"Неверный формат позиции в строке файла VCF: {line}")
                continue
            for interval in bed_intervals:
                if chrom == interval[0] and interval[1] <= pos <= interval[2]:
                    filtered_variants.append(line)
                    break
    return filtered_variants

if __name__ == "__main__":
    bed_file = "C:/Users/Мария/PycharmProjects/pythonProject/Черновики/example.bed"
    vcf_file = "C:/Users/Мария/PycharmProjects/pythonProject/Черновики/example2.vcf"

    bed_intervals = read_bed(bed_file)
    filtered_variants = filter_vcf_by_bed(vcf_file, bed_intervals)

    with open("filtered_variants.vcf", 'w') as output_file:
        output_file.writelines(filtered_variants)
