def crypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file_in:
        with open(output_file, 'wb') as file_out:
            while True:
                chunk = file_in.read(1024)
                if not chunk:
                    break

                encrypted_chunk = bytearray([byte ^ (key % 256) for byte in chunk])
                file_out.write(encrypted_chunk)