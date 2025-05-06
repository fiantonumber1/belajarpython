import pandas as pd
import spss

def run_spss_correlation(x_data, y_data, var1="X", var2="Y"):
    try:
        # Pastikan data yang diterima adalah list atau array
        if len(x_data) != len(y_data):
            raise ValueError("Panjang data X dan Y harus sama.")
        
        # Membuat DataFrame dari data input langsung
        df = pd.DataFrame({var1: x_data, var2: y_data})
        
        # Simpan ke CSV sementara agar bisa diakses oleh SPSS
        temp_csv = "temp_data.csv"
        df.to_csv(temp_csv, index=False)
        
        # Cek apakah file CSV berhasil dibuat
        print(f"File CSV sementara telah dibuat: {temp_csv}")
        
        # Jalankan SPSS dengan format yang lebih fleksibel untuk tipe data
        spss.Submit(f"""
            GET DATA /TYPE=TXT /FILE='{temp_csv}' /DELIMITERS=',' /ARRANGEMENT=DELIMITED /FIRSTCASE=2 /VARIABLES={var1} F8.1 {var2} F8.1.
            CORRELATIONS /VARIABLES={var1} {var2} /PRINT=TWOTAIL NOSIG /MISSING=PAIRWISE.
        """)
        
        print(f"Analisis korelasi untuk {var1} dan {var2} selesai.")
    
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Contoh pemanggilan fungsi dengan input array
x_values = [1, 2, 3, 4, 5]
y_values = [5, 4, 3, 2, 1]

run_spss_correlation(x_values, y_values)
