# File Manipulator

## Description

File manipulator is a simple command-line tool that provides various file manipulation operations, including reversing file contents, copying files, duplicating file contents, and replacing strings within files.

## Requirements

- Python 3.x

## Installation

```bash
git clone https://github.com/z6wdc/python-file-manipulator.git
cd python-file-manipulator
```

## Usage

Run the script using Python and specify one of the following commands:

### Reverse File Contents

Reverses the content of the input file and saves it to the output file.

```bash
python3 file_manipulator.py reverse <inputpath> <outputpath>
```

### Copy File

Copies a file from the input path to the output path.

```bash
python3 file_manipulator.py copy <inputpath> <outputpath>
```

### Duplicate File Contents

Duplicates the contents of a file n times.

```bash
python3 file_manipulator.py duplicate-contents <inputpath> <n>
```

### Replace String

Replaces all occurrences of a given string with a new string in the specified file.

```bash
python3 file_manipulator.py replace-string <inputpath> <needle> <newstring>
```
