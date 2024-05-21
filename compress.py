import zstandard as zstd
import os

def compress_file(input_file, output_file):
    with open(input_file, 'rb') as f:
        data = f.read()

    compressor = zstd.ZstdCompressor()
    compressed_data = compressor.compress(data)

    with open(output_file, 'wb') as f:
        f.write(compressed_data)

    print(f"Compressed {input_file} to {output_file}")
