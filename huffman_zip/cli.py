import argparse
from huffman_zip.huffman_compressor import Compressor

def main():
    parser = argparse.ArgumentParser(description='Compress files using Huffman coding.')
    parser.add_argument('action', choices=['compress', 'decompress'], help='Action to perform: compress or decompress')
    parser.add_argument('input_file', type=str, help='Input file to process')
    parser.add_argument('output_file', type=str, help='Output file after processing')
    
    args = parser.parse_args()
    compressor = Compressor()

    if args.action == 'compress':
        compressor.compress_file(args.input_file, args.output_file)
    elif args.action == 'decompress':
        try:
            compressor.decompress_file(args.input_file, args.output_file)
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Invalid action. Valid actions are 'compress' or 'decompress'.")

if __name__ == '__main__':
    main()
