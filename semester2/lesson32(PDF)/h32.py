from pypdf import PdfWriter,PdfReader
from pathlib import Path

# __________________________________________________________________________
# Task-1
pdf_path_1=Path().absolute()/'practice_files'/'merge1.pdf'

pdf_path_2=Path().absolute()/'practice_files'/'merge2.pdf'

merger=PdfWriter()
for pdf in [pdf_path_1,pdf_path_2]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()

# _____________________________________________________________________
merger=PdfWriter()
for pdf in ['practice_files/merge1.pdf','practice_files/merge2.pdf']:
    merger.append(pdf)

merger.write("merged-pdf-2.pdf")
merger.close()
# _____________________________________________________________________

merger=PdfWriter()
input1=open("practice_files/ugly.pdf","rb")
input2=open("practice_files/zen.pdf","rb")
input3=open("practice_files/top_secret.pdf","rb")
merger.append(fileobj=input1,pages=(0,3))
merger.merge(position=2,fileobj=input2,pages=(0,1))
merger.append(input3)
output=open("document-output.pdf",'wb')
merger.write(output)

merger.close()
output.close()


# ____________________________________________________________________
# Task-2

pdf_path=Path().absolute()/'practice_files'/'ugly.pdf'
pdf_reader=PdfReader(pdf_path)
page=pdf_reader.pages[-1]
text=page.extract_text()
print(text)
# _____________________________________________________________________

# Task-3
pdf_path=Path().absolute()/'practice_files'/'ugly.pdf'
pdf_reader=PdfReader(pdf_path)
page=pdf_reader.pages[0]
text=page.extract_text()
# print(text)

with open('info-ugly.txt','a') as info:
    print(info.write(text))

info.close()
with open('info-ugly.txt','r') as inf:
    s=inf.read().replace('\n',' ').lower().split()

words={}
words[s[0]]=1

k=0
for i in range(0,len(s)-1):
        if s[i] in words:
              k+=1
              words[s[i]]=k

        else:
              words[s[i]]=1

word=list(words.keys())

word_count=list(words.values())

max_word_count=0
min_word=''


for i in range(len(word_count)-1):
    if word_count[i]>max_word_count:
        max_word_count=word_count[i]
        min_word=word[i]
    elif word_count[i] ==max_word_count:
         if word[i]<min_word:
              min_word=word[i]
print("min_word=",f"'{min_word}'",'max_word_count=',max_word_count)