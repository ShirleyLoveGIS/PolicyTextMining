# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 17:06:06 2021

@author: shirley


read pdf/docx and write all text into txt file

    path: parent directory path for files
    out_path: result txt file

Note that docx2txt cannot deal with .doc file
"""


import pathlib



path = pathlib.Path('D:\paper\相关政策标准调研')
out_path = path.joinpath('policytxt.txt')


############## 1. read pdf file ########
import pdfplumber
f_path=sorted(path.rglob("*.pdf"))

for file in f_path:
    print(file)
    with pdfplumber.open(file) as pdf, open(out_path ,'a',encoding='utf-8') as txt:
        for page in pdf.pages:
            textdata = page.extract_text()
            if textdata is not None:
                txt.write(textdata)


############## 2. read word file ##########
import docx2txt
f_path=sorted(path.rglob("*.docx"))

for file in f_path:
    print(file)
    with open(out_path ,'a', encoding='utf-8') as txt:
        doc = docx2txt.process(file)
        txt.write(doc)
