# PolicyTextMining

构建评价指标体系时，在完成政策收集和行业标准收集后，通过关键字词频构建指标重要度的特征信息。

- extract_policy.py：将所有pdf、word文件中的文字提取并写入policytxt.txt
- index_cal.py: 计算index.txt中所有指标在政策文字中出现的频率

数据文件
- policytxt.txt 
- policy_fre.csv(注意编码为GBK，适宜excel打开)