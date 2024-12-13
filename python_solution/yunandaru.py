import pandas as pd
import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO
from openpyxl.drawing.image import Image
import re







# Fungsi untuk memproses file Excel
def process_excel(file_path, columns, divider):
    try:
        # Membaca sheet pertama dari file Excel
        data = pd.read_excel(file_path, sheet_name=0)

        # Mengambil kolom sesuai pilihan pengguna (dikurangi 1 untuk indeks berbasis 0)
        selected_columns = data.iloc[:, [int(col) - 1 for col in columns]]

        # Menghapus baris pertama dari data untuk isi sheet
        data_to_save = selected_columns.iloc[1:]

        # Menyimpan hasil ke file Excel baru
        output_file = "allparameter.xlsx"
        stdev_summary = {}  # Untuk menyimpan nilai standar deviasi setiap sheet

        with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
            # Menyimpan semua kolom ke satu sheet bernama "AllParameter"
            data_to_save.to_excel(writer, index=False, header=True, sheet_name="AllParameter")

            # Menyimpan setiap kolom ke sheet terpisah dengan nama "Sheet1", "Sheet2", dst.
            for idx, col in enumerate(columns):
                # Ambil nilai untuk nama sheet menggunakan slicing
                sheet_name_raw = f"{data.iloc[0:1, [int(col) - 1]]}"

                # Bersihkan angka, titik, tanda minus, dan trim spasi
                sheet_name_cleaned = re.sub(r'[\d.\-]', '', sheet_name_raw).strip()

                 # Pastikan sheet_name tidak kosong, gunakan nama default jika kosong
                sheet_name = sheet_name_cleaned if sheet_name_cleaned else f"Sheet{idx + 1}"


                selected_column_data = data.iloc[1:, [int(col) - 1]]  # Data dari baris ke-2 dan seterusnya
                

                # Membagi data menjadi blok divider baris
                total_rows = len(selected_column_data)
                blocks = [selected_column_data.iloc[i:i + divider] for i in range(0, total_rows, divider)]

                # Membuat DataFrame untuk setiap blok
                max_length = max(len(block) for block in blocks)
                split_data = pd.DataFrame()

                for i, block in enumerate(blocks):
                    # Setiap blok menjadi kolom baru
                    column_data = block.values.flatten()
                    if len(column_data) < max_length:
                        # Isi kekurangan baris dengan NaN
                        column_data = list(column_data) + [None] * (max_length - len(column_data))
                    split_data[f"Part{i + 1}"] = column_data

                # Menghitung standar deviasi untuk setiap kolom
                stdev_row = split_data.apply(lambda x: np.nanstd(x.dropna()), axis=0)

                # Menyimpan standar deviasi dalam dictionary
                stdev_summary[sheet_name] = stdev_row.values

                # Menambahkan baris standar deviasi ke DataFrame
                split_data.loc[max_length] = stdev_row

                # Menyimpan data yang telah dipecah ke sheet Excel
                split_data.to_excel(writer, index=False, header=True, sheet_name=sheet_name)


            # Membuat DataFrame untuk StDevSummary
            summary_df = pd.DataFrame(stdev_summary)

            # Membulatkan nilai di dalam DataFrame (misalnya 2 angka desimal)
            summary_df = summary_df.round(2)

            # Menambahkan kolom total sesuai aturan yang diberikan
            total_column = []

            # Iterasi untuk menghitung total sesuai dengan aturan khusus
            for idx in range(len(summary_df)):
                total = 0

                # Menghitung total berdasarkan aturan yang diberikan
                if len(summary_df.columns) >= 2:
                    total += (summary_df.iloc[idx, 0] + summary_df.iloc[idx, 1]) / 2  # Parameter 1 dan 2
                if len(summary_df.columns) >= 4:
                    total += (summary_df.iloc[idx, 2] + summary_df.iloc[idx, 3]) / 2  # Parameter 3 dan 4

                # Untuk sisanya, dijumlahkan
                if len(summary_df.columns) > 4:
                    total += summary_df.iloc[idx, 4:].sum()

                total_column.append(round(total, 2))

            # Menambahkan kolom total ke DataFrame summary_df
            summary_df['TQI Total KAI'] = total_column





            


            # Menambahkan kolom total sesuai aturan yang diberikan
            total_column_2 = []

            # Iterasi untuk menghitung total sesuai dengan aturan khusus
            for idx in range(len(summary_df)):
                total = 0

                # Menghitung total berdasarkan aturan yang diberikan
                if len(summary_df.columns) >= 2:
                    total += ((summary_df.iloc[idx, 0] + summary_df.iloc[idx, 1]) / 2)**2       # Parameter 1 dan 2
                if len(summary_df.columns) >= 4:
                    total += ((summary_df.iloc[idx, 2] + summary_df.iloc[idx, 3]) / 2)**2  # Parameter 3 dan 4

                # Untuk sisanya, dijumlahkan
                if len(summary_df.columns) > 4:
                    total += (summary_df.iloc[idx, 4])**2
                    total += (summary_df.iloc[idx, 5])**2
                    total += (summary_df.iloc[idx, 6])**2

                sqrtotal=   round(total**(0.5), 2)

                total_column_2.append(sqrtotal)

            # Menambahkan kolom total ke DataFrame summary_df
            summary_df['TQI Total EN'] = total_column_2












            

            # Modifikasi index dengan mengalikan index dengan divider
            summary_df.index = divider / 4* (summary_df.index+1) 

            # Menyimpan DataFrame StDevSummary ke sheet
            summary_df.to_excel(writer, index=True, header=True, sheet_name="StDevSummary")

            # Menambahkan grafik ke dalam sheet StDevSummary
            for idx, column in enumerate(summary_df.columns):
                fig, ax = plt.subplots()
                ax.plot(summary_df.index, summary_df[column], label=column)
                ax.set_title(f"Grafik {column}")
                ax.set_xlabel('Km')
                ax.set_ylabel('TQI')
                ax.legend()

                # Simpan grafik ke dalam buffer
                img_stream = BytesIO()
                fig.savefig(img_stream, format='png')
                img_stream.seek(0)

                # Masukkan gambar ke dalam worksheet
                image = Image(img_stream)
                sheet = writer.sheets["StDevSummary"]
                image.anchor = f"A{len(summary_df) + idx + 2}"  # Mengatur posisi gambar di bawah tabel
                sheet.add_image(image)

        return f"Data berhasil disimpan ke {output_file}"

    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}"

# Layout GUI
layout = [
    [sg.Text("Pilih file Excel:")],
    [sg.Input(key="-FILE-"), sg.FileBrowse(file_types=(("Excel Files", "*.xlsx"),))],
    [sg.Text("Masukkan kolom / paremeter yang ingin diambil (pisahkan dengan koma, misal: 2,4,5,6):")],
    [sg.Input(key="-COLUMNS-")],
    [sg.Text("Pilih Meter:")],
    [sg.Combo(["10","20", "40", "100", "1000"], default_value="40", key="-DIVIDER-")],
    [sg.Button("Proses"), sg.Button("Keluar")],
    [sg.Text("", size=(50, 2), key="-OUTPUT-")]
]

# Membuat jendela GUI
window = sg.Window("Filter Kolom Excel", layout)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Keluar":
        break

    if event == "Proses":
        file_path = values["-FILE-"]
        columns = values["-COLUMNS-"].split(",")
        divider = int(values["-DIVIDER-"]) * 4

        if not file_path or not columns:
            window["-OUTPUT-"].update("Harap masukkan file dan kolom yang valid.")
        else:
            result = process_excel(file_path, columns, divider)
            window["-OUTPUT-"].update(result)

window.close()
