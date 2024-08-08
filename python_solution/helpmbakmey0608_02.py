import pandas as pd

# Fungsi untuk menemukan satu pasangan nilai duplikat di kolom tertentu dari DataFrame
def find_unique_duplicates(file_path, column_index):
    # Membaca file Excel
    df = pd.read_excel(file_path)
    
    # Mendapatkan nama kolom berdasarkan indeks yang diberikan
    column_name = df.columns[column_index]
    
    # Mencari semua nilai duplikat di kolom yang ditentukan
    duplicated_values = df[df.duplicated([column_name], keep=False)][column_name]
    
    # Mengambil baris pertama dari setiap nilai duplikat
    unique_duplicates = df[df[column_name].isin(duplicated_values)].drop_duplicates(subset=[column_name])
    
    # Menghitung jumlah pasangan dokumen yang memiliki duplikasi
    num_unique_duplicates = unique_duplicates[column_name].nunique()
    
    # Menyimpan satu pasangan duplikat ke file baru
    output_file = 'unique_duplikat.xlsx'
    unique_duplicates.to_excel(output_file, index=False)
    
    return num_unique_duplicates, output_file

# Path ke file Excel yang ingin diperiksa
file_path = 'cekarif2.xlsx'

# Kolom yang ingin diperiksa untuk duplikasi (misalnya kolom kedua)
column_to_check = 1  # 0 untuk kolom pertama, 1 untuk kolom kedua, dst.

# Menjalankan fungsi dan mencetak hasil
num_unique_duplicates, output_file = find_unique_duplicates(file_path, column_to_check)
print(f"Jumlah pasangan yang memiliki duplikasi: {num_unique_duplicates}")
print(f"File Excel dengan daftar satu pasangan duplikat disimpan sebagai: {output_file}")
