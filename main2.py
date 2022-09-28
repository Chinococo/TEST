import pandas as pd

df1 = pd.read_json('bike.json',encoding='utf-8')
df1.columns = ['sno','sna','tot','sbi','sarea','mday','lat','lng','ar','sareaen','snaen','aren','bemp','act']
print(df1[(df1.bemp>10)])
test = df1[(df1.bemp>10)]
print(test.bemp.sum())

