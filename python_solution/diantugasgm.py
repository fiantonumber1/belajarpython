import pandas as pd

# Path ke file CSV yang berisi data asli
input_file = 'AC - INSTALASI KABEL.csv'
# Path ke file Excel output yang berisi data yang sudah diproses
output_file = 'AC - INSTALASI KABEL_update.xlsx'

# Membaca data dari file CSV
try:
    data = pd.read_csv(input_file, header=None, encoding='utf-8')
except pd.errors.ParserError:
    print("Terjadi kesalahan saat membaca file. Mungkin ada masalah dengan format atau separator.")
    exit()

# Memproses data
processed_data = []

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
    
    colbulan =  combined_col1.split(' ')[0]
    
    final_row = [input_file,'','',col3,colbulan,combined_col1,  col4, row[0] ,col2]

    processed_data.append(final_row)

# Membuat DataFrame dari data yang sudah diproses
df = pd.DataFrame(processed_data, columns=['namaexcel','Sub Sistem','Sistem Klasifikasi','LRU' ,'Bulan', 'Tanggal Lengkap', 'Permasalahan','dataasli', 'No Kereta'])

# Menyimpan DataFrame ke file Excel
df.to_excel(output_file, index=False)

print(f"\nData telah diproses dan disimpan ke file: {output_file}")
