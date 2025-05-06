import PySimpleGUI as sg
import os
import pandas as pd

# Fungsi untuk memverifikasi apakah file adalah file Excel yang valid
def is_valid_excel(file_path):
    try:
        pd.ExcelFile(file_path, engine='openpyxl')  # Coba baca file dengan openpyxl
        return True
    except Exception:
        return False

def is_valid_csv(file_path):
    try:
        pd.read_csv(file_path)  # Coba baca file CSV
        return True
    except Exception:
        return False
    
# Fungsi untuk memproses file
def process_files(folder, action):
    output_folder = folder + "_saved"
    
    # Buat folder baru jika belum ada
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in os.listdir(folder):
        
        if file.endswith(".xlsx"):
            file_path = os.path.join(folder, file)
            output_path = os.path.join(output_folder, file)  # Simpan ke folder _saved

            if not is_valid_excel(file_path):  # Cek apakah file valid
                print(f"Skip: {file} bukan file Excel yang valid.")
                continue

            try:
                excel_file = pd.ExcelFile(file_path, engine='openpyxl')
                writer = pd.ExcelWriter(output_path, engine='openpyxl')  # Simpan ke output folder

                for sheet_name in excel_file.sheet_names:
                    df = pd.read_excel(excel_file, sheet_name=sheet_name, engine='openpyxl')

                    if action == "Hapus Baris 1-4":
                        df = df.iloc[3:].reset_index(drop=True)  # Hapus baris 1-4
                        df.columns = df.iloc[0]  # Jadikan baris pertama setelah penghapusan sebagai header
                        df = df[1:].reset_index(drop=True)  # Hapus baris pertama yang sudah menjadi header
                    df.to_excel(writer, sheet_name=sheet_name, index=False, header=True)

                writer.close()
                print(f"Berhasil memproses: {file} -> Disimpan di {output_folder}")
            except Exception as e:
                print(f"Gagal memproses {file}: {str(e)}")


        if file.endswith(".csv"):
            file_path = os.path.join(folder, file)
            output_xlsx_path = os.path.join(output_folder, file.replace(".csv", ".xlsx"))
            
            try:
                # Read CSV without setting a header initially
                df = pd.read_csv(file_path, header=None)
                
                # Set the first row as the column headers
                df.columns = df.iloc[0]
                
                # Drop the first row (since it’s now the header) and reset index
                df = df.drop(0).reset_index(drop=True)
                
                # Transpose the dataframe (optional, depending on your exact need)
                # If you only want the first row as headers and no further transposition, skip this
                # df = df.T
                
                # Simpan sebagai XLSX
                df.to_excel(output_xlsx_path, index=False, header=True, engine='openpyxl')
                print(f"Berhasil memproses: {file} -> Disimpan di {output_folder}")
            except Exception as e:
                print(f"Gagal memproses {file}: {str(e)}")
    sg.popup(f"Proses selesai! File disimpan di: {output_folder}")

# Layout PySimpleGUI
layout = [
    [sg.Text("Pilih Folder yang Berisi File Excel:", size=(30, 1))],
    [sg.InputText(size=(40, 1)), sg.FolderBrowse()],
    [sg.Text("Pilih Aksi:", size=(30, 1))],
    [sg.Combo(["Transpose Baris ke Kolom", "Hapus Baris 1-4"], key='ACTION', size=(30, 1))],
    [sg.Button("Proses", size=(15, 1)), sg.Button("Keluar", size=(15, 1))]
]

window = sg.Window("Excel Processor", layout, element_justification='c', font=("Helvetica", 12))

# Event Loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Keluar":
        break
    if event == "Proses":
        folder_path = values[0]
        action = values['ACTION']
        if folder_path and action:
            process_files(folder_path, action)
        else:
            sg.popup("Harap pilih folder dan aksi yang diinginkan.")

window.close()
