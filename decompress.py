import zstandard as zstd
import os

def decompress_file(input_file, output_file):
    with open(input_file, 'rb') as f:
        compressed_data = f.read()

    decompressor = zstd.ZstdDecompressor()
    data = decompressor.decompress(compressed_data)

    with open(output_file, 'wb') as f:
        f.write(data)

    print(f"Decompressed {input_file} to {output_file}")
