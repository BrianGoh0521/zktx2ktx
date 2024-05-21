import os
import sys
from compress import compress_file
from decompress import decompress_file

def main():
    if not os.path.exists('input'):
        os.makedirs('input')
    if not os.path.exists('output'):
        os.makedirs('output')

    action = input("Select your choise：Compress (c) or decompress (d)：").strip().lower()
    input_filename = input("Enter your file name（In Input Dir）：").strip()
    input_filepath = os.path.join('input', input_filename)

    if not os.path.isfile(input_filepath):
        print(f"File {input_filepath} doesn't exists.")
        return

    output_filename = input("Enter your file export name（In Output Dir）：").strip()
    output_filepath = os.path.join('output', output_filename)

    if action == 'c':
        compress_file(input_filepath, output_filepath)
    elif action == 'd':
        decompress_file(input_filepath, output_filepath)
    else:
        print("Invalid operation. Please select 'c' for compression or 'd' for decompression.")

if __name__ == "__main__":
    main()
