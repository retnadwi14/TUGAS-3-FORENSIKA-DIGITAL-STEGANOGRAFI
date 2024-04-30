from PyPDF2 import PdfReader

# Buka file PDF yang ingin Anda periksa metadata-nya
file_pdf = "jurnal.pdf"

# Baca metadata dari file PDF
pdf = PdfReader(file_pdf)

# Periksa apakah metadata ada dan apakah informasi yang diinginkan tersedia
if "/Info" in pdf.trailer:
    metadata = pdf.trailer["/Info"]
    for key in ["/Author", "/Creator", "/Producer", "/CreationDate"]:
        if key in metadata:
            print(f"{key[1:]}: {metadata[key]}")
        else:
            print(f"{key[1:]}: Tidak tersedia")
else:
    print("Informasi metadata tidak tersedia dalam PDF.")

