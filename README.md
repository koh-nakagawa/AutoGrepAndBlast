
# Sequence Extraction and BLAST Automation Script -greo_balst_primer_amplicon.py-

## Overview
This script automates the process of extracting sequences using specific primer IDs from transcriptome data, conducting BLAST searches with those sequences, and consolidating the results into a single CSV file. It is designed to streamline workflows in molecular biology and genomics research.

## Requirements
- Python 3.x
- Biopython
- Pandas
- BLAST command line tools installed and accessible from the terminal

## Input Files
1. A CSV file containing the primer details (`primer_num`, `primer_id`, and `sequence`).
2. A transcriptome data file in FASTA format.

## Output
- FASTA files for each primer sequence extracted.
- CSV files containing the sorted BLAST results for each primer.
- A merged CSV file consolidating all BLAST results, including the `evalue`, `sseqid`, and `primer_num_id`.

## Usage
1. Prepare your CSV file with columns for `primer_num`, `primer_id`, and `sequence`.
2. Specify the path to your transcriptome data file in FASTA format.
3. Set the paths for the output directories where the FASTA files and BLAST result CSV files will be saved.
4. Run the script to execute the sequence extraction, BLAST search, and result merging process.

## Steps
1. The script reads the primer details from the input CSV file.
2. It extracts sequences from the transcriptome data based on the primer IDs.
3. Performs BLAST searches for each extracted sequence against a specified database.
4. Sorts the BLAST results by evalue and saves them to CSV files.
5. Merges all individual BLAST result files into a single consolidated CSV file.

## Important Notes
- Ensure that the BLAST command line tools are correctly installed and configured on your system.
- Adjust the BLAST database path and other parameters in the script as needed for your specific research requirements.
- The script assumes a specific structure for the input CSV file and the FASTA format of the transcriptome data. Ensure your files conform to these requirements.

## Support
For issues or questions regarding this script, please reach out to the repository maintainer or open an issue on the GitHub project page.


-------------------------------------------


### Sequence Extraction and BLAST Automation Scriptに関するREADME

#### 概要
このスクリプトは、特定のプライマーIDを用いてトランスクリプトームデータからシーケンスを抽出し、これらのシーケンスでBLAST検索を行い、その結果を一つのCSVファイルにまとめるプロセスを自動化します。特に、トランスクリプトーム研究におけるシーケンスの解析を効率化するために設計されています。

#### 前提条件
- Python 3.x
- Biopython
- 環境からアクセス可能なBLASTコマンドラインツールがインストールされていること

#### 入力要件
1. プライマーの詳細（primer_num、primer_id、sequenceの列）を含むCSVファイル。
2. FASTA形式のトランスクリプトームデータファイル。
3. 検索クエリ用に設定されたBLASTデータベース。

#### 使用方法
1. すべての前提条件がシステムにインストールされ、適切に設定されていることを確認します。
2. 指定された通りにプライマーの詳細を含む入力CSVファイルを準備します。
3. FASTA形式のトランスクリプトームデータファイルへのパスを指定します。
4. 抽出されたシーケンスをFASTAファイルに保存し、BLAST検索結果をCSVファイルに保存するための出力ディレクトリのパスを設定します。
5. スクリプトを実行します。スクリプトは以下を行います：
   - 提供されたプライマーIDに基づいてトランスクリプトームデータからシーケンスを抽出します。
   - 抽出されたシーケンスで指定されたBLASTデータベースに対してBLAST検索を実行します。
   - BLAST結果をe-valueでソートし、CSVファイルに保存します。
   - 分析を容易にするために、全ての個々のBLAST結果を一つの統合されたCSVファイルにマージします。

#### 出力
- 抽出されたシーケンスのFASTAファイルが含まれるディレクトリ。
- 各プライマーのBLAST結果をソートしたCSVファイルが含まれるディレクトリ。
- e-value、sseqid、primer_num_idを含む全BLAST結果を統合した単一のCSVファイル。

#### カスタマイズ
BLASTデータベースへのパスなど、システム構成に応じて他のファイルパスを調整する必要があります。
