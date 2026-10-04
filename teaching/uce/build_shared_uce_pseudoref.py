#!/usr/bin/env python3

from pathlib import Path
import argparse


def read_fasta(path):
    name = None
    seq = []

    with open(path) as handle:
        for line in handle:
            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):
                if name is not None:
                    yield name, "".join(seq)

                name = line[1:].split()[0]
                seq = []
            else:
                seq.append(line)

        if name is not None:
            yield name, "".join(seq)


def clean_sequence(sequence):
    sequence = sequence.upper()
    sequence = sequence.replace("-", "").replace(".", "")

    return "".join(
        base if base in "ACGT" else "N"
        for base in sequence
    )


def write_fasta_record(handle, name, sequence, width=80):
    handle.write(f">{name}\n")

    for i in range(0, len(sequence), width):
        handle.write(sequence[i:i + width] + "\n")


def main():

    parser = argparse.ArgumentParser(
        description=(
            "Build a shared UCE pseudoreference from "
            "locus-by-locus FASTA alignments."
        )
    )

    parser.add_argument(
        "--alignments",
        required=True,
        help="Directory containing uce-*.fasta alignments."
    )

    parser.add_argument(
        "--output",
        required=True,
        help="Output shared UCE pseudoreference FASTA."
    )

    parser.add_argument(
        "--report",
        required=True,
        help="Output TSV provenance/QC report."
    )

    parser.add_argument(
        "--max-ambiguous",
        type=float,
        default=0.10,
        help=(
            "Maximum allowed fraction of ambiguous bases "
            "(default: 0.10)."
        )
    )

    args = parser.parse_args()

    alignment_dir = Path(args.alignments)
    fasta_files = sorted(alignment_dir.glob("uce-*.fasta"))

    if not fasta_files:
        raise SystemExit(
            f"ERROR: no uce-*.fasta files found in {alignment_dir}"
        )

    loci_retained = 0
    loci_skipped = 0

    with open(args.output, "w") as fasta_out,          open(args.report, "w") as report_out:

        report_out.write(
            "locus\t"
            "status\t"
            "selected_sample\t"
            "aligned_length\t"
            "ungapped_length\t"
            "ambiguous_bases\t"
            "ambiguous_fraction\t"
            "total_sequences\t"
            "eligible_sequences\n"
        )

        for fasta_file in fasta_files:

            locus = fasta_file.stem
            candidates = []
            total_sequences = 0

            for sample, aligned_seq in read_fasta(fasta_file):

                total_sequences += 1

                aligned_length = len(aligned_seq)
                clean_seq = clean_sequence(aligned_seq)
                ungapped_length = len(clean_seq)

                if ungapped_length == 0:
                    continue

                ambiguous_bases = clean_seq.count("N")
                ambiguous_fraction = (
                    ambiguous_bases / ungapped_length
                )

                if ambiguous_fraction > args.max_ambiguous:
                    continue

                candidates.append({
                    "sample": sample,
                    "sequence": clean_seq,
                    "aligned_length": aligned_length,
                    "ungapped_length": ungapped_length,
                    "ambiguous_bases": ambiguous_bases,
                    "ambiguous_fraction": ambiguous_fraction
                })

            if not candidates:

                report_out.write(
                    f"{locus}\t"
                    f"SKIPPED\t"
                    f"NA\tNA\tNA\tNA\tNA\t"
                    f"{total_sequences}\t0\n"
                )

                loci_skipped += 1
                continue

            candidates.sort(
                key=lambda x: (
                    -x["ungapped_length"],
                    x["ambiguous_fraction"],
                    x["sample"]
                )
            )

            best = candidates[0]

            write_fasta_record(
                fasta_out,
                locus,
                best["sequence"]
            )

            report_out.write(
                f"{locus}\t"
                f"SELECTED\t"
                f"{best['sample']}\t"
                f"{best['aligned_length']}\t"
                f"{best['ungapped_length']}\t"
                f"{best['ambiguous_bases']}\t"
                f"{best['ambiguous_fraction']:.6f}\t"
                f"{total_sequences}\t"
                f"{len(candidates)}\n"
            )

            loci_retained += 1

    print()
    print("Shared UCE pseudoreference completed")
    print("------------------------------------")
    print(f"Input loci:       {len(fasta_files)}")
    print(f"Loci retained:    {loci_retained}")
    print(f"Loci skipped:     {loci_skipped}")
    print()
    print(f"Pseudoreference:  {args.output}")
    print(f"Provenance table: {args.report}")
    print()


if __name__ == "__main__":
    main()
