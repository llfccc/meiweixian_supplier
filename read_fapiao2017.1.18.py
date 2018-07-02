#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time,datetime
time1 = time.time()
import win32com.client
import os
import requests
import json



def read_excel(file,table):
     xlApp = win32com.client.Dispatch('Excel.Application') #打开EXCEL，这里不需改动
     xlApp.Visible = False
     xlBook = xlApp.Workbooks.Open(file) #将D:\\1.xls改为要处理的excel文件路径
     xlSht = xlBook.Worksheets(table) #要处理的excel页，默认第一页是‘sheet1’
     rowcount =xlSht.UsedRange.Rows.Count
     colcount =28  #读取几列xlSht.UsedRange.Columns.count

     data=xlSht.Range(xlSht.Cells(1, 1), xlSht.Cells(rowcount+1, colcount+1)).Value
     xlBook.Close(SaveChanges=1) #完成 关闭保存文件
     del xlApp
     return data


print u"开始处理excel文件"
char=os.getcwd()
# file_name=char+unicode(r'\入库单--厨邦','gbk')
table_name=u'sheet1'

file_name=char+u'\\入库单--厨邦.xlsx'
if os.path.exists(file_name):
    print 'true'
else:
    file_name = char + u'\\入库单--美味鲜.xlsx'
    if os.path.exists(file_name):
        pass
    else:
        print u'找不到入库单文件，请确认是是以  入库单--厨邦 这种方式命名 '

company_name = file_name.split('--')[1].split('.')[0]

#读取excel文件保存为元祖的列表
try:
    data=read_excel(file_name,table_name)
except:
    print u"error:读取文件失败，工作表名必须为“sheet1”，首行必须为列名"
    input()
###删掉空余行
def delNone(data):
    result=[]
    for k in data:
        if k[3]:
            result.append(k)
    return result
nowTime=str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d'))
data=delNone(data)
#将列表变为带有标题的字典
excelResult={}
for k in range(len(data[0])):
    excelResult[data[0][k]]=map(lambda s:s[k],data[1:])

#转换时间
def convert_time(data):
    for k,v in enumerate(data):
        if v:
            try:
                v=int(v)
                data[k] = str(datetime.datetime.fromtimestamp(int(v)).strftime('%Y-%m-%d'))
            except:
                data[k]=str(v)

convert_time(excelResult[u'入库日期'])
#添加一个时间戳
excelResult[u'timestamp']=[nowTime]*len(excelResult[u'订单号'])
excelResult[u'所属公司']=[company_name]*len(excelResult[u'订单号'])
#转换文本
def convert_float(data):
    for k, v in enumerate(data):
        data[k] = float(str(v).replace(',',''))

convert_float(excelResult[u'本币无税金额'])
# map(lambda x:str(x).replace(',',''),excelResult[u'本币无税金额'])
# map(lambda x:str(x).replace(',',''),excelResult[u'本币无税单价'])
# map(lambda x:str(x).replace(',',''),excelResult[u'原币含税单价'])
#按指定顺序摆放数据并转置矩阵
result=[u'供应商',u'入库日期',u'订单号',u'入库单号',u'存货编码',u'存货名称',u'规格型号',u'主计量单位',u'数量',u'本币无税单价',u'本币无税金额',u'原币含税单价',u'阶段报价',u'所属公司',u'timestamp']
finalData=[]
for t in result:
    try:
        finalData.append(excelResult[t])
    except:
        print u"缺少必须的列，请检查是否有\"%s\"这一列" %t
        raw_input()
Data=map(list,zip(*finalData))


print(data[1:2])
#发送json数据到网站上去
def http_post(data):
   #url = "http://127.0.0.1:8000/order/receiveExcelInvoice/"
   url = "http://meiwei.duapp.com/order/receiveExcelInvoice/"
   data = json.dumps(data)
   r=requests.session().post(url, json=data)
   return r

resp = http_post(Data)
print resp.status_code
if resp.status_code==200:
	print u"成功"
	os.remove(file_name)
	print u"删除成功"
time2 = time.time()
print u"所有任务已完成,总计花费",round(time2 - time1,3),u"秒完成",'\n',u"按任意键退出"
raw_input()
