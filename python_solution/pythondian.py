import pandas as pd

# Fungsi untuk memodifikasi string sesuai dengan aturan yang diberikan
def modify_string(s):
    # Menambahkan "." antara anggota string ke-2 dan ke-3
    modified = s[:2] + "." + s[2:3] + "-" + s[3:-2]
    return modified

# Membaca file Excel
file_path = 'dianhariini.xlsx'
df = pd.read_excel(file_path)

# Memodifikasi kolom A
df['A'] = df['A'].apply(modify_string)

# Menyimpan hasil modifikasi ke file Excel baru
output_path = 'dianhariini_modified_file.xlsx'
df.to_excel(output_path, index=False)
