'''FASTA summarizer - Week 2 exercise.

Reads a FASTA file, prints each sequence id, its length, and GC% percentage.
'''

from pathlib import Path

def parse_fasta(file_path: str) -> dict:
    """Parse a FASTA file and return a dict of {header: sequence}."""
    records = {}
    header = None
    seq_parts = []

    for line in Path(file_path).read_text().splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            if header is not None:
                records[header] = "".join(seq_parts)
            header = line[1:]
            seq_parts = []
        else:
            seq_parts.append(line)

    if header is not None:
        records[header] = "".join(seq_parts)
    return records

def gc_percentage(seq: str) -> float:
    """Return GC percentage of a nucleotide sequence."""
    if len(seq) == 0:
        return 0.0
    gc = seq.count("G") + seq.count("C")
    return (gc / len(seq)) * 100

def main() -> None:
    fasta_path = "example.fa"
    records = parse_fasta(fasta_path)
    for name, seq in records.items():
        print(f"{name}\t{len(seq)}\t{gc_percentage(seq):.2f}%")

if __name__ == "__main__":
    main()
