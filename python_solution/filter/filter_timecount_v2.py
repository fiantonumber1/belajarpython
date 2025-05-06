import PySimpleGUI as sg
import os
import pandas as pd
import time

# Fungsi untuk memverifikasi apakah file adalah file Excel yang valid
def is_valid_excel(file_path):
    try:
        pd.ExcelFile(file_path, engine='openpyxl')
        return True
    except Exception:
        return False

def is_valid_csv(file_path):
    try:
        pd.read_csv(file_path)
        return True
    except Exception:
        return False
    
# Fungsi untuk memproses file
def process_files(folder, action):
    start_time = time.time()
    output_folder = folder + "_saved"
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in os.listdir(folder):
        if file.endswith(".xlsx"):
            file_path = os.path.join(folder, file)

            if not is_valid_excel(file_path):
                print(f"Skip: {file} bukan file Excel yang valid.")
                continue

            try:
                excel_file = pd.ExcelFile(file_path, engine='openpyxl')

                for sheet_name in excel_file.sheet_names:
                    df = pd.read_excel(excel_file, sheet_name=sheet_name, engine='openpyxl')

                    if action == "Hapus Baris 1-4":
                        df = df.iloc[3:].reset_index(drop=True)
                        df.columns = df.iloc[0]
                        df = df[1:].reset_index(drop=True)
                        
                        # Debugging: Cek kolom dan data
                        print(f"Kolom DataFrame untuk {sheet_name}: {df.columns.tolist()}")
                        print(df.head())
                        
                        base_filename = os.path.splitext(file)[0]
                        output_path = os.path.join(output_folder, f"{base_filename}_{sheet_name}.csv")
                        
                        # Simpan CSV dengan pemisah koma dan encoding untuk Excel
                        df.to_csv(output_path, index=False, header=True, sep=';', encoding='utf-8-sig')
                        print(f"Berhasil memproses sheet {sheet_name} dari {file} -> Disimpan sebagai {output_path}")
                    

            except Exception as e:
                print(f"Gagal memproses {file}: {str(e)}")

        if file.endswith(".csv"):
            file_path = os.path.join(folder, file)
            output_xlsx_path = os.path.join(output_folder, file.replace(".csv", ".xlsx"))
            
            try:
                df = pd.read_csv(file_path, header=None)
                df.columns = df.iloc[0]
                df = df.drop(0).reset_index(drop=True)
                
                df.to_excel(output_xlsx_path, index=False, header=True, engine='openpyxl')
                print(f"Berhasil memproses: {file} -> Disimpan di {output_folder}")
            except Exception as e:
                print(f"Gagal memproses {file}: {str(e)}")

    end_time = time.time()
    processing_time = end_time - start_time
    sg.popup(f"Proses selesai! File disimpan di: {output_folder}\nWaktu pemrosesan: {processing_time:.2f} detik")

# Layout PySimpleGUI
layout = [
    [sg.Text("Pilih Folder yang Berisi File Excel:", size=(30, 1))],
    [sg.InputText(size=(40, 1)), sg.FolderBrowse()],
    [sg.Text("Pilih Aksi:", size=(30, 1))],
    [sg.Combo(["Hapus Baris 1-4"], key='ACTION', size=(30, 1))],
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