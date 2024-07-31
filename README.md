# Huffman Compression

## Project Overview

This project provides a tool for Huffman compression and decompression of files using a command-line interface (CLI). The tool compresses text files into binary format and decompresses them back to the original text format. The algorithm used is called Huffman tree encoding.

Note that it likely won't be as performant as the built-in file zipper on your machine, but serves more as a proof-of-concept.

## Features

- **Compression**: Convert text files to a compressed binary format using Huffman coding.
- **Decompression**: Restore compressed binary files to their original text format.
- **CLI Tool**: Easily interact with the compression and decompression functionalities from the command line.

## Installation

   ```sh
   pip install -e .
   ```

## Development

### Prerequisites

- Python 3.6 or higher
- `venv` (for creating a virtual environment)
- `pip` (Python package installer)

### Steps to the Development Environment

1. **Clone the Repository**

   ```sh
   git clone https://github.com/your-username/huffman-zip.git
   cd huffman-zip
   ```
2. **Create a Virtual Environment**

   ```sh
   python3 -m venv venv
   ```
3. **Activate the Virtual Environment**

   ```sh
   source venv/bin/activate
   ```

You can run the tests from here.
