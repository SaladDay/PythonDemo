'''
                       _oo0oo_
                      o8888888o
                      88" . "88
                      (| -_- |)
                      0\  =  /0
                    ___/`---'\___
                  .' \\|     |// '.
                 / \\|||  :  |||// \
                / _||||| -:- |||||- \
               |   | \\\  - /// |   |
               | \_|  ''\---/''  |_/ |
               \  .-\__  '-'  ___/-. /
             ___'. .'  /--.--\  `. .'___
          ."" '<  `.___\_<|>_/___.' >' "".
         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
         \  \ `_.   \_ __\ /__ _/   .-` /  /
     =====`-.____`.___ \_____/___.-`___.-'=====
                       `=---='


     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

           佛祖保佑     永不宕机     永无BUG

       佛曰:  
               写字楼里写字间，写字间里程序员；  
               程序人员写程序，又拿程序换酒钱。  
               酒醒只在网上坐，酒醉还来网下眠；  
               酒醉酒醒日复日，网上网下年复年。  
               但愿老死电脑间，不愿鞠躬老板前；  
               奔驰宝马贵者趣，公交自行程序员。  
               别人笑我忒疯癫，我笑自己命太贱；  
               不见满街漂亮妹，哪个归得程序员？
'''

from bdb import Bdb
from cgitb import html
from turtle import title
from xml.sax import default_parser_list
from bs4 import BeautifulSoup #网页解析，获取数据
import xlwt #进行excel操作
import urllib.request,urllib.error   #制定URL，获取网页数据
import re #进行文字匹配
import sqlite3



def main():
    baseurl="https://my.cqu.edu.cn/api/sam/score/student/score"
    #1.爬取网页
    datalist= getData(baseurl)
    #3.保存数据
    savepath ="./grade.xls"
    # saveData(datalist,savepath)




def getData(baseurl):
    datalist=[]
    html=askURL(baseurl)
    soup=BeautifulSoup(html,"html.parser")





def askURL(url):
    head={
        "Cookie":"FSSBBIl1UgzbN7N443S=fbNkPhoi0iUjbHIIYWv6SQPycuds2Ihj0rEQyPoL8nTlNtq9BoJt6ANKGewU8cqr; FSSBBIl1UgzbN7N443T=4pNBtEf.j3vBTaFaHzCXly8aDXdQfmme6uzLnJ4vOYsezeebILBkSe_WqYyWd3kJdvkZxeJR8cdeSpY6rbhhrtOriAulC9qHAQmfIabgexoDAZq8l.kCvmZ3H9qHFIQssKmYTSiGPZnn8iRok3uEfHikKTxAZcy8Z8djet5DXbpFrvA7Xnn1ePC0N294nzfM_8_a5zBrAoBar36HlYqwXdbSSRDTy9bIIKXgaEswcY_i3t_DEecWaet8rJyxIU.LhnqVW77MoM0qRsEPyeV_YvD2T3rkb_mEnAmcBsR47DaFvkmetb6ViazivJeW9qu0k4MJiti_Aqi6l5RAfes8VgGHZq9CUJBY9xyaVBYQaoEX_5a; iPlanetDirectoryPro=b6tfnTqsMbEKY6H3T5FrdF; SESSION=MmEwYzMyZGItNGI3NC00Y2QzLTg3ZGMtNGM2OWE1NzJmZjM5",
        "Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NDc3OTA0NTIsInVzZXJfbmFtZSI6IjMwMDEzNDUxIiwiYXV0aG9yaXRpZXMiOlsi5a2m55SfJktSX1NSVFAiXSwianRpIjoiMjUxN2YxOWQtMzIzZS00NmZlLWE3N2EtNGNmOTAwMTA5NjgwIiwiY2xpZW50X2lkIjoidGltZXRhYmxlLXByb2QiLCJzY29wZSI6WyJhbGwiXX0.7QjYs7yp49vVI71pDihybhW2f95o8pzP0Ix-MKJFe0g",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46"
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




if __name__ == '__main__':
   main()