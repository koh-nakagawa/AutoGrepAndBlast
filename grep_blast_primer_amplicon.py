'''
This script automates the extraction of sequences from transcriptome data using specific primer IDs,
performs BLAST searches with those sequences, and consolidates the results into a single CSV file.
It requires an input CSV file with primer details (number, ID, and sequence), a transcriptome data file in FASTA format,
and specifies output directories for saving the extracted sequences and BLAST results.

Usage:
1. Prepare a CSV file with columns for primer_num, primer_id, and sequence.
2. Specify the path to your transcriptome data file in FASTA format.
3. Set the output directory paths for saving FASTA files and BLAST result CSV files.
4. Run the script to execute the sequence extraction, BLAST search, and results merge-process.

このスクリプトは、特定のプライマーIDを使用してトランスクリプトームデータからシーケンスを抽出し、
それらのシーケンスでBLAST検索を実行し、結果を単一のCSVファイルにまとめることを自動化します。
プライマーの詳細（番号、ID、およびシーケンス）を含む入力CSVファイル、FASTA形式のトランスクリプトームデータファイル、
および抽出されたシーケンスとBLAST結果のCSVファイルを保存するための出力ディレクトリのパスが必要です。

使用方法：
1. primer_num、primer_id、sequenceの列を持つCSVファイルを準備します。
2. FASTA形式のトランスクリプトームデータファイルへのパスを指定します。
3. FASTAファイルとBLAST結果のCSVファイルを保存する出力ディレクトリのパスを設定します。
4. スクリプトを実行して、シーケンスの抽出、BLAST検索、および結果の統合プロセスを実行します。
'''



import pandas as pd
from Bio import SeqIO
import os
import subprocess

# Adjusting paths to the new CSV file and other necessary paths
csv_file_path = '/home/t16623kn/new_chr_primer240215/past_primers_seq.csv'
transcriptome_path = "/home/t16623kn/o.sybotides_sex_chr/o.sybotides_trsc/Octonoba_sybotides_741-W1_S3_merged_bridger.fasta"
base_output_dir = "/home/t16623kn/new_chr_primer240215/240226_past_primer_blast_sortedcsv"

# Output directories for FASTA and BLAST results
fasta_output_dir = os.path.join(base_output_dir, "fasta_files")
blast_output_dir = os.path.join(base_output_dir, "blast_csv_sorted_results")

# Creating output directories if they do not exist
os.makedirs(fasta_output_dir, exist_ok=True)
os.makedirs(blast_output_dir, exist_ok=True)

# Reading primer information from the new CSV file
primer_df = pd.read_csv(csv_file_path)
primer_info = primer_df.to_dict('records')

# Loading the transcriptome data
records = SeqIO.index(transcriptome_path, "fasta")

# Path for the merged CSV file
merged_csv_path = os.path.join(base_output_dir, "blast_csv_sorted_results_merge.csv")

# Initializing an empty DataFrame for merged results
merged_df = pd.DataFrame(columns=['evalue', 'sseqid', 'primer_num_id'])

for primer in primer_info:
    # Remove _fw or _rv from the end of primer_id before searching in the records
    primer_id_original = primer['primer_id']
    primer_num = primer['primer_num']
    primer_id = primer_id_original.rsplit('_', 1)[0]  # Remove the suffix after the last underscore

    if primer_id in records:
        # File name format: "primer_num_primer_id.fasta/csv"
        file_identifier = f"{primer_num}_{primer_id_original}"
        fasta_file_path = os.path.join(fasta_output_dir, f"{file_identifier}.fasta")
        SeqIO.write(records[primer_id], fasta_file_path, "fasta")
        
        blast_csv_file_path = os.path.join(blast_output_dir, f"{file_identifier}_sorted_blast.csv")
        blast_command = f"blastn -db /home/t16623kn/o.sybotides_sex_chr/o.sybotides_trsc/o.sybotidesDB -query {fasta_file_path} -outfmt '10 evalue sseqid' -out {blast_csv_file_path}"
        subprocess.run(blast_command, shell=True)
        
        blast_df = pd.read_csv(blast_csv_file_path, header=None, names=['evalue', 'sseqid'])
        sorted_blast_df = blast_df.sort_values(by='evalue', ascending=True)
        sorted_blast_df.to_csv(blast_csv_file_path, index=False)
        
        # Adding a new column to denote "primer_num_primer_id"
        sorted_blast_df['primer_num_id'] = file_identifier
        merged_df = pd.concat([merged_df, sorted_blast_df], ignore_index=True)

# Saving the merged results to a CSV file with file names
with open(merged_csv_path, 'w') as merged_file:
    merged_file.write('evalue,sseqid,primer_num_id\n')  # Write the header
    for primer in primer_info:
        primer_id_original = primer['primer_id']
        primer_num = primer['primer_num']
        primer_id = primer_id_original.rsplit('_', 1)[0]  # Remove the suffix after the last underscore

        if primer_id in records:
            file_identifier = f"{primer_num}_{primer_id_original}"
            fasta_file_path = os.path.join(fasta_output_dir, f"{file_identifier}.fasta")
            blast_csv_file_path = os.path.join(blast_output_dir, f"{file_identifier}_sorted_blast.csv")

            # Check if BLAST results exist and write the file name followed by the results
            if os.path.exists(blast_csv_file_path):
                merged_file.write(f'>{file_identifier}.csv\n')  # Write the file name
                with open(blast_csv_file_path, 'r') as blast_results:
                    for line in blast_results:
                        merged_file.write(line)  # Write the BLAST results
                merged_file.write('\n')  # Add a newline between files for readability

