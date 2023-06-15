from pypdf import PdfReader, PdfWriter, PdfMerger
from pathlib import Path



pdf_path=Path().absolute()/'practice_files'/'Pride_and_Prejudice.pdf'
# print(pdf_path)

pdf_reader=PdfReader(pdf_path)
# print(pdf_reader)
# print(len(pdf_reader.pages))
# print(pdf_reader.metadata)
# print(pdf_reader.metadata.title)




first_page=pdf_reader.pages[0]
# print(first_page)
# print('type',type(first_page))
a=first_page.extract_text()

# for page in pdf_reader.pages[:5]:
#     print(page.extract_text())




with open('info.txt','a') as info:
    print(info.write(a))

info.close()

# ---------------------------------------------------------
pdf_path=Path().absolute()/'practice_files'/'ugly.pdf'
pdf_reader_2=PdfReader(pdf_path)
second_page=pdf_reader_2.pages[0]
text=second_page.extract_text()
print(text)

with open('text_ugly.txt',"a") as info:
    print(info.write(text))
