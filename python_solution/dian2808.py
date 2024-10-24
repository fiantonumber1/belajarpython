from openpyxl import load_workbook

# Mengatur file Excel yang akan digunakan
file_path = '28082024.xlsx'
sheet_name = 'dian'

# Membuka workbook
wb = load_workbook(file_path)
sheet = wb[sheet_name]

# Membaca nilai kolom P dan menyimpan nilai beserta indeksnya, dimulai dari baris ke-4, hanya jika ada angka
col_p_values = [(cell.value, i) for i, cell in enumerate(sheet['P'][3:], start=4) if isinstance(cell.value, (int, float))]

# Mengurutkan nilai berdasarkan nilai di kolom P
sorted_values_with_indices = sorted(col_p_values)

# Menulis urutan angka ke kolom AD sesuai urutan yang baru
for new_index, (value, original_index) in enumerate(sorted_values_with_indices, start=1):
    sheet[f'AD{original_index}'] = new_index

# Menyimpan perubahan kembali ke file Excel
wb.save(file_path)
