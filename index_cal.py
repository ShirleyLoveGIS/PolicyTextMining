# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 17:06:06 2021

@author: shirley

frequency calculate for each index
    index: index file path
    txtfile: extracted text from policy files

Note that result shall be encoding in GBK and open with excel
"""
import pandas as pd


index = pd.read_csv('index.txt',sep='\t')
txtfile = 'policytxt.txt'
fre_index = []
fre_keyword=[]

with open(txtfile, encoding='utf-8') as f:
    policy = f.readlines()
    policy_txt = "".join(policy)
    
    policy_txt = policy_txt.replace('\t','').replace('\n','')
    
    ### start calculate ###
    for i in range(0, 51):
        index_name = index.loc[i]['name']
        index_keyword = index.loc[i]['keyword']
        
        fre_index.append(policy_txt.count(index_name))
        fre_keyword.append(policy_txt.count(index_keyword))
        
index['fre_index'] = fre_index
index['fre_keyword'] = fre_keyword
print(index)
index.to_csv('policy_fre.csv', encoding='GBK')     