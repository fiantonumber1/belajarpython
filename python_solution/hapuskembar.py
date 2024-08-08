
import pandas as pd

# Path file input dan output
input_file_path = 'ujicoba123.xlsx'  # Ganti dengan path file input Anda
output_file_path = 'file_output.xlsx'  # Path untuk menyimpan file output

# Membaca file Excel
df = pd.read_excel(input_file_path)

# Menghapus duplikat pada kolom ke-6 (kolom F)
df_unique = df.drop_duplicates(subset=df.columns[5], keep='first')

# Menyimpan hasil ke file Excel baru
df_unique.to_excel(output_file_path, index=False)

print(f"File baru telah disimpan sebagai {output_file_path}")

