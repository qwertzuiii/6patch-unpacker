def crypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file_in:
        with open(output_file, 'wb') as file_out:
            while True:
                chunk = file_in.read(1024)  # Lese eine Dateicharge (1024 Bytes) ein
                if not chunk:
                    break  # Dateiende erreicht, Abbruch

                encrypted_chunk = bytearray([byte ^ (key % 256) for byte in chunk])  # XOR-Verschlüsselung mit dem Schlüssel
                file_out.write(encrypted_chunk)  # Verschlüsselte Daten in die Ausgabedatei schreiben