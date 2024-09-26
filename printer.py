import detectorlib

path="2022_LOU_AZE_field_maturation_final_matrix.xlsx"
path2='2021_All raw data_No_background.xlsx'
path3="2020_TN_Field_alldata_SD_divisi.xlsx"


graph=detectorlib.printer()
graph.load(path, 10)
graph.hitmap()

