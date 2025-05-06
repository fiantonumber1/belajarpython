import pandas as pd
import os

try:
    import spss
    print(f"Berhasil mengimpor modul spss")
    try:
        import SpssClient
        print(f"Berhasil mengimpor modul spss client")
    except ImportError as e:
        print(f"Gagal mengimpor modul spss client: {e}")
        exit()
except ImportError as e:
    print(f"Gagal mengimpor modul spss: {e}")
    exit()

def run_spss_correlation(x_data, y_data, var1="X", var2="Y", output_pdf_name="correlation_report.pdf", output_excel_name="correlation_report.xlsx"):
    try:
        # Pastikan panjang data sama
        if len(x_data) != len(y_data):
            raise ValueError("Panjang data X dan Y harus sama.")
        
        # Buat DataFrame dari input
        df = pd.DataFrame({var1: x_data, var2: y_data})
        
        # Dapatkan direktori tempat file .py berada
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Simpan CSV sementara
        temp_csv = os.path.join(current_dir, "temp_data.csv").replace("\\", "/")
        df.to_csv(temp_csv, index=False)
        print(f"File CSV sementara telah dibuat: {temp_csv}")
        
        # Tentukan path untuk file lain
        output_pdf = os.path.join(current_dir, output_pdf_name).replace("\\", "/")
        temp_sav = os.path.join(current_dir, "temp_data.sav").replace("\\", "/")
        output_excel = os.path.join(current_dir, output_excel_name).replace("\\", "/")
        
        # Langkah 1: Baca data dan beri nama dataset
        print("Mencoba membaca data...")
        spss.Submit(f"""
            GET DATA /TYPE=TXT 
                /FILE='{temp_csv}' 
                /DELIMITERS=',' 
                /ARRANGEMENT=DELIMITED 
                /FIRSTCASE=2 
                /VARIABLES={var1} F8.2 {var2} F8.2.
            DATASET NAME MyData.
            SAVE OUTFILE='{temp_sav}'.
        """)
        print("Data berhasil dibaca dan disimpan sebagai .sav")
        
        # Langkah 2: Verifikasi variabel dan jalankan korelasi
        print("Menjalankan analisis korelasi...")
        spss.Submit(f"""
            DATASET ACTIVATE MyData.
            DISPLAY VARIABLES.
            CORRELATIONS 
                /VARIABLES={var1} {var2} 
                /PRINT=TWOTAIL NOSIG 
                /MISSING=PAIRWISE.
        """)
        print("Korelasi selesai")

        # Menampilkan versi SPSS
        print("Menampilkan versi SPSS...")
        spss.Submit("SHOW VERSION.")
        
        
    except spss.SpssError as e:
        print(f"Kesalahan SPSS: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan lain: {e}")

# Contoh pemanggilan fungsi
if __name__ == "__main__":
    x_values = [1, 2, 3, 4, 5]
    y_values = [5, 4, 3, 2, 1]
    run_spss_correlation(x_values, y_values)

