import pandas as pd

# Menggunakan openpyxl sebagai engine untuk membaca file Excel
file_path = 'arif.xlsx'  # Ganti dengan path ke file Excel Anda
output_file_path = 'mbakmeybaruuu.xlsx'
sheet_name = 'Sheet1'  # Ganti dengan nama sheet yang ingin dibaca, jika berbeda

# Membaca file Excel
df = pd.read_excel(file_path, sheet_name=sheet_name, engine='openpyxl')

# Menampilkan nama-nama kolom dan jumlah total kolom
print("Nama-nama kolom:", df.columns)
print("Jumlah kolom:", len(df.columns))

# Memeriksa apakah kolom 'C' ada dalam DataFrame
if 'C' in df.columns:
    # Inisialisasi penghitung total untuk setiap string
    total_count_pi = 0
    total_count_fc = 0
    total_count_fp = 0
    total_count_td = 0
    total_count_pt = 0
    
    # Iterasi melalui setiap baris
    for index, row in df.iterrows():
        # Ambil nilai di kolom 'C', konversi ke string dan huruf besar
        cell_value = str(row['C']).upper()
        # Hitung jumlah kemunculan setiap string
        count_pi = cell_value.count('PI')
        count_fc = cell_value.count('FC')
        count_fp = cell_value.count('FP')
        count_td = cell_value.count('TD')
        count_pt = cell_value.count('PT')
        
        # Tambahkan ke total masing-masing
        total_count_pi += count_pi
        total_count_fc += count_fc
        total_count_fp += count_fp
        total_count_td += count_td
        total_count_pt += count_pt
    
    # Menampilkan total kemunculan
    print(f'Total kemunculan "PI" pada kolom "C": {total_count_pi}')
    print(f'Total kemunculan "FC" pada kolom "C": {total_count_fc}')
    print(f'Total kemunculan "FP" pada kolom "C": {total_count_fp}')
    print(f'Total kemunculan "TD" pada kolom "C": {total_count_td}')
    print(f'Total kemunculan "PT" pada kolom "C": {total_count_pt}')
else:
    print('Kolom "C" tidak ditemukan dalam DataFrame.')

# Memeriksa apakah kolom 'C' ada dalam DataFrame
if 'C' in df.columns:
    # Filter baris berdasarkan kemunculan string di kolom 'C'
    df_pi = df[df['C'].str.contains('PI', case=False, na=False)]
    df_fc = df[df['C'].str.contains('FC', case=False, na=False)]
    df_fp = df[df['C'].str.contains('FP', case=False, na=False)]
    df_td = df[df['C'].str.contains('TD', case=False, na=False)]
    df_pt = df[df['C'].str.contains('PT', case=False, na=False)]
    df_others = df[~df['C'].str.contains('PI|FC|FP|TD|PT', case=False, na=False)]

    # Menyimpan DataFrame yang telah difilter ke file Excel baru dengan 6 sheet
    with pd.ExcelWriter(output_file_path, engine='openpyxl') as writer:
        df_pi.to_excel(writer, sheet_name='PI', index=False)
        df_fc.to_excel(writer, sheet_name='FC', index=False)
        df_fp.to_excel(writer, sheet_name='FP', index=False)
        df_td.to_excel(writer, sheet_name='TD', index=False)
        df_pt.to_excel(writer, sheet_name='PT', index=False)
        df_others.to_excel(writer, sheet_name='Others', index=False)

    print(f'File Excel baru dengan sheet "PI", "FC", "FP", "TD", "PT", dan "Others" telah disimpan sebagai {output_file_path}.')
else:
    print('Kolom "C" tidak ditemukan dalam DataFrame.')
