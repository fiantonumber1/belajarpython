from flask import Flask, request, jsonify
import os
import sys
import pandas as pd
import spss

app = Flask(__name__)

def run_spss_correlation(x_data, y_data, var1="X", var2="Y", output_txt_name="correlation_output.txt"):
    try:
        # Validasi panjang data
        if len(x_data) != len(y_data):
            raise ValueError("Panjang data X dan Y harus sama.")
        
        # Membuat DataFrame dari data yang diterima
        df = pd.DataFrame({var1: x_data, var2: y_data})
        
        # Menentukan direktori saat ini
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Menyimpan DataFrame ke file CSV sementara
        temp_csv = os.path.join(current_dir, "temp_data.csv").replace("\\", "/")
        df.to_csv(temp_csv, index=False)
        print(f"File CSV sementara telah dibuat: {temp_csv}")
        
        # Menentukan file .sav dan output teks
        temp_sav = os.path.join(current_dir, "temp_data.sav").replace("\\", "/")
        output_txt = os.path.join(current_dir, output_txt_name).replace("\\", "/")
        
        # Menjalankan SPSS untuk analisis
        print("Menampilkan versi SPSS...")
        spss.Submit("SHOW VERSION.")
        
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
        
        print("Menjalankan analisis korelasi...")
        # Redirect output ke file
        with open(output_txt, "w", encoding="utf-8") as f:
            sys.stdout = f  # Redirect stdout ke file
            spss.Submit(f"""
                DATASET ACTIVATE MyData.
                CORRELATIONS
                    /VARIABLES={var1} {var2}
                    /PRINT=TWOTAIL NOSIG
                    /MISSING=PAIRWISE.
            """)
        
        # Kembalikan stdout ke default
        sys.stdout = sys.__stdout__
        print("Korelasi selesai.")
        print(f"Hasil korelasi telah disimpan di {output_txt}")
        
        return output_txt  # Kembalikan nama file output

    except spss.SpssError as e:
        print(f"Kesalahan SPSS: {e}")
        return None
    except Exception as e:
        print(f"Terjadi kesalahan lain: {e}")
        return None

@app.route('/run_correlation', methods=['POST'])
def run_correlation():
    try:
        # Mendapatkan data JSON dari POST request
        data = request.get_json()

        # Ekstrak data yang diterima
        x_data = data['x_data']
        y_data = data['y_data']
        var1 = data.get('var1', 'X')
        var2 = data.get('var2', 'Y')
        
        # Memanggil fungsi dengan data yang sudah disiapkan
        output_txt = run_spss_correlation(x_data, y_data, var1, var2)
        
        # Jika output.txt berhasil dibuat, kirimkan isi file ke klien
        if output_txt:
            # Baca isi file output_txt
            with open(output_txt, 'r', encoding='utf-8') as file:
                file_content = file.read()
            return jsonify({"correlation_result": file_content}), 200
        else:
            return jsonify({"error": "Terjadi kesalahan dalam proses korelasi."}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
