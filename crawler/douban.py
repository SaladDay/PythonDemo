'''
Author: SaladDay
Date: 2022-03-15 19:20:56
LastEditors: SaladDay
LastEditTime: 2022-03-20 20:52:51
FilePath: \PythonDemo\crawler\douban.py
Email: 1203511142@qq.com

'''
aa

from bdb import Bdb
from cgitb import html
from turtle import title
from xml.sax import default_parser_list
from bs4 import BeautifulSoup #网页解析，获取数据
import xlwt #进行excel操作
import urllib.request,urllib.error   #制定URL，获取网页数据
import re #进行文字匹配
import sqlite3 #进行SQLlite数据库操作



def main():
    baseurl="https://movie.douban.com/top250?start="
    #1.爬取网页
    datalist= getData(baseurl)
    #3.保存数据
    savepath ="./douban.xls"
    saveData(datalist,savepath)

    


findlink=re.compile(r'<a href="(.*?)">')       #构建正则表达式来条件化搜索
findImgsrc=re.compile(r'<img.*src="(.*?)".*>',re.S)            
#<img alt="肖申克的救赎" class="" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p480747492.jpg" width="100"/>
findTitle=re.compile(r'<span class="title">(.*?)</span>')
# <span class="title">肖申克的救赎</span>
findRating=re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
#   <span class="rating_num" property="v:average">9.7</span>
findJudge =re.compile(r'<span>(\d*)人评价</span>')
findInq=re.compile(r'<span class="inq">(.*)</span>')
# <span class="inq">希望让人自由。</span>
#爬取网页
findBD=re.compile(r'<p class="">(.*?)</p>',re.S)


def getData(baseurl):
    datalist=[]
    for i in range(0,10):
        url=baseurl +str(i*25)
        html = askURL(url)
        soup=BeautifulSoup(html,"html.parser")#将html内的对象放入beautiful内的树形结构中
        for item in soup.find_all("div",class_="item"):
            data=[]
            item = str(item)

            link = re.findall(findlink,item)[0]
            data.append(link)

            ImgSrc=re.findall(findImgsrc,item)[0]
            data.append(ImgSrc)

            Title=re.findall(findTitle,item)
            if(len(Title)==2):
                cTitle=Title[0]
                data.append(cTitle)
                oTitle=Title[1].replace("/","")
                data.append(oTitle)
            else:
                data.append(Title[0])
                data.append(" ")        #留空

            rating=re.findall(findRating,item)[0]
            data.append(rating)

            judegNum= re.findall(findJudge,item)[0]
            data.append(judegNum)

            inq=re.findall(findInq,item)
            if len(inq) != 0:
                inq=inq[0].replace("。","")
                data.append(inq)
            else:
                data.append(" ")
            
            Bd=re.findall(findBD,item)[0]
            Bd=re.sub("<br(\s+)?/>(\s+)?","",Bd)
            # Bd=Bd.replace("\\n"," ")
            data.append(Bd.strip())

            datalist.append(data)  #将一部电影的处理好的信息加入到datalist中去
    # print(datalist)
    return datalist
            

            

        

#得到指定一个URL的html内容
def askURL(url):
    head={     #用户代理
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39"
    }
    req = urllib.request.Request(url,headers=head)
    html =""
    try:
        response =urllib.request.urlopen(req)
        html= response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e :
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

    





#3.保存数据
def saveData (datalist,savepath):
    workbook=xlwt.Workbook(encoding="utf-8")
    worksheet=workbook.add_sheet("电影排行榜",cell_overwrite_ok=True)
    col=["电影详情链接","电影图片链接","中文名","外文名","评分","评价数","概述","相关内容"]
    for i in range(8):
        worksheet.write(0,i,col[i])
    for i in range(250):
        print("第%d条"%(i+1))
        data=datalist[i]
        for j in range(0,8):
            worksheet.write(i+1,j,data[j])
    workbook.save(savepath)
    print("finish!!")






if __name__ == '__main__':
    main()