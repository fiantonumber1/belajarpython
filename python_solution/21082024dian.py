import pandas as pd

# Baca file formatsumberdian21082024.xlsx, sheet 'sumber'
file_sumber = 'formatsumberdian21082024.xlsx'
df_sumber = pd.read_excel(file_sumber, sheet_name='sumber')

# Baca file formatrencanadian21082024.xlsx
file_rencana = 'ra.xlsx'
xl_rencana = pd.ExcelFile(file_rencana)

# Loop melalui setiap sheet di file rencana
with pd.ExcelWriter(file_rencana, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    for sheet_name in xl_rencana.sheet_names:
        df_rencana = xl_rencana.parse(sheet_name)
        
        # Update kolom C (kolom ke-3, nama dokumen) berdasarkan no dokumen di kolom B (kolom ke-2)
        for index, row in df_rencana.iterrows():
            no_dokumen = row.iloc[1]  # Kolom ke-2 (B) untuk no dokumen
            
            # Cari no_dokumen di file sumber dan ambil nama dokumen dari kolom E (kolom ke-5)
            sumber_row = df_sumber[df_sumber.iloc[:, 3] == no_dokumen]  # Kolom ke-4 (D) untuk no dokumen
            if not sumber_row.empty:
                nama_dokumen = sumber_row.iloc[0, 4]  # Kolom ke-5 (E) untuk nama dokumen
                df_rencana.at[index, df_rencana.columns[2]] = nama_dokumen  # Kolom ke-3 (C) untuk nama dokumen
        
        # Simpan perubahan kembali ke file excel rencana
        df_rencana.to_excel(writer, sheet_name=sheet_name, index=False)

print("Proses update selesai.")
