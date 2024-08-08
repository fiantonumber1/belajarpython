import pandas as pd

# Baca file PI PT.xlsx dan sumberdata.xlsx
df_pi_pt = pd.read_excel("PI PT.xlsx")
df_sumberdata = pd.read_excel("sumberdata.xlsx")

# Ambil data dari kolom ketiga (indeks 2) di PI PT.xlsx
data_pi_pt = df_pi_pt.iloc[:, 2]

# Iterasi setiap nilai di data_pi_pt
for index, value in data_pi_pt.iteritems():
    # Cari nilai di sumberdata.xlsx pada kolom A hingga I (indeks 0 hingga 8)
    matching_row = df_sumberdata[df_sumberdata.iloc[:, 0:9].isin([value]).any(axis=1)]
    
    # Jika ditemukan, copy nilai dari kolom W (indeks 22) ke file PT PI.xlsx pada kolom F (indeks 5)
    if not matching_row.empty:
        value_to_copy = matching_row.iloc[0, 22]
        df_pi_pt.at[index, 'F'] = value_to_copy  # Update nilai di DataFrame df_pi_pt

# Simpan file dengan nama baru PT PI_update.xlsx
df_pi_pt.to_excel("PT PI_update.xlsx", index=False)
print("File PT PI_update.xlsx berhasil disimpan.")
