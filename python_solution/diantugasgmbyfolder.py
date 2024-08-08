import pandas as pd
import os
import chardet

# Folder yang berisi file CSV input
input_folder = 'inputexcel'
# Path ke file Excel output yang berisi data yang sudah diproses
output_file = 'hasilnya.xlsx'

# Membaca semua file CSV dari folder input
all_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]
processed_data = []

for file in all_files:
    input_file_path = os.path.join(input_folder, file)
    
    # Mendeteksi encoding menggunakan chardet
    with open(input_file_path, 'rb') as f:
        result = chardet.detect(f.read())
    enc = result['encoding']

    # Membaca data dari file CSV dengan encoding yang terdeteksi
    try:
        data = pd.read_csv(input_file_path, header=None, encoding=enc)
    except UnicodeDecodeError:
        print(f"Encoding {enc} gagal untuk file {file}.")
        continue
    except pd.errors.ParserError:
        print(f"Terjadi kesalahan saat membaca file {file}. Mungkin ada masalah dengan format atau separator.")
        continue

    # Memproses data dari setiap file
    for index, row in data.iterrows():
        # Memecah data di kolom pertama (kolom A) berdasarkan koma
        row_data = row[0].split(',')

        # Gabungkan elemen pertama dan kedua dari row_data menjadi kolom pertama
        if len(row_data) > 1:
            combined_col1 = f"{row_data[0]},{row_data[1]}"
        else:
            combined_col1 = row_data[0]

        # Kolom kedua berisi elemen ketiga
        col2 = row_data[2] if len(row_data) > 2 else ''

        # Kolom ketiga berisi elemen keempat
        col3 = row_data[3] if len(row_data) > 3 else ''

        # Kolom keempat berisi gabungan dari sisa pecahan setelah elemen keempat
        col4 = ','.join(row_data[4:]) if len(row_data) > 4 else ''

        # Ambil bagian tanggal untuk kolom Bulan
        colbulan = combined_col1.split(' ')[0]

        # Menambahkan nama file sebagai kolom 'namaexcel'
        final_row = [file, '', '', col3, colbulan, combined_col1, col4, row[0], col2]

        processed_data.append(final_row)

# Membuat DataFrame dari data yang sudah diproses
df = pd.DataFrame(processed_data, columns=['namaexcel', 'Sub Sistem', 'Sistem Klasifikasi', 'LRU', 'Bulan', 'Tanggal Lengkap', 'Permasalahan', 'dataasli', 'No Kereta'])

# Menyimpan DataFrame ke file Excel
df.to_excel(output_file, index=False)

print(f"\nData telah diproses dan disimpan ke file: {output_file}")
