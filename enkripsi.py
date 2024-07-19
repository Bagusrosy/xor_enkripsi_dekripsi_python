import os


def process_file(mode):
    default_in = 'plain.txt' if mode == 'encrypt' else 'cipher.txt'
    default_out = 'cipher.txt' if mode == 'encrypt' else 'plain2.txt'
    input_file = input(f"file input (default: {default_in}): ") or default_in
    output_file = input(f"file out (default: {default_out}): ") or default_out
    
    # Menggunakan path absolut
    input_file = os.path.abspath(input_file)
    output_file = os.path.abspath(output_file)

    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' tidak ditemukan.")
        print(f"Lokasi file yang dicari: {input_file}")
        return

    try:
        with open(input_file, "r") as fin, open(output_file, "w") as fout:
            key = input("Kata kunci: ")
            n, i = len(key), 0
            while char := fin.read(1):
                fout.write(chr(ord(char) ^ ord(key[i])))
                i = (i + 1) % n
        print(f"{mode.capitalize()} selesai. Hasil tersimpan di {output_file}")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' tidak ditemukan.")
    except PermissionError:
        print(f"Error: Tidak bisa akses '{input_file}' atau '{output_file}'.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


def encrypt():
    process_file('encrypt')


def decrypt():

    process_file('decrypt')


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    print(f"Direktori script: {script_dir}")
    print(f"Direktori kerja diubah ke: {os.getcwd()}")
    print("Daftar file dalam direktori kerja:")
    for file in os.listdir():
        print(f"- {file}")

    print("Pastikan file input ada di direktori yang sama dengan script ini.")
    
    while True:
        choice = input("Pilih operasi (1: Enkripsi, 2: Dekripsi, 3: Keluar): ")
        if choice == "1":
            encrypt()
        elif choice == "2":
            decrypt()
        elif choice == "3":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()