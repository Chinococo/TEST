# total_amt(成交頭數_總數)、average_weight(成交頭數_平均重量)
# average_price(成交頭數_平均價格)
import numpy as np

# 讀入資料，檔案以","分隔，跳過第一行標題
dt = np.dtype([('total_amt',  float),('average_weight',  float),('average_price',  float)])
nf1 = np.genfromtxt('pig.csv', delimiter=',', skip_header=1,dtype=dt)
#print(nf1)
test = np.sort(nf1,order='average_weight')
print('全年成交平均重量的成交頭數，最低前 5 筆資料')
for i in range(5):
    print(test[i])
test = np.sort(nf1,order='total_amt')
test = test[::-1]
print('輸出全年成交平均價格的成交頭數，最高前 5 筆資料')
for i in range(5):
    print(test[i])
'''
test = np.sort(nf1,order='average_weight')
print('全年成交平均重量的成交頭數，最低前 5 筆資料')
for i in range(5):
    print(test[i])
'''