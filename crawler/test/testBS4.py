'''
BeautifulSoup4将复杂HTML文档转换成一个复杂的树形解构,每个节点都是PYthon对象
所有对象可以归纳为一下4种
- Tag   标签及其内容(默认拿到第一个东西)
- NavigableString   标签内的字符串
- BeautifulSoup     表示整个文档(树形结构)
- Comment       注释




#文档的搜索
(1)find_all
#字符串过滤:会查找与字符串完全匹配的内容
t_list=bs.find_all("a",limit = 4)
#正则表达式搜索:使用search()方法来匹配内容
t_list=bs.find_all(re.compile("a"))
#方法:传入一个函数,根据函数的要求来搜索
(2)kwargs keyword参数
t_list= bs.find_all(id=="head")
(3)text参数
t_list=bs.find_all(text =re.compile("\d")) 运用正则表达式来查找包含特定文本的内容
(4)选择器


'''


from bs4 import BeautifulSoup



def getData(baseurl):
    datalist = []
    for i in range(0,1):             #循环调用获取十页的函数askURL
        url = baseurl + str(i*25)
        html = askURL(url)

        #开始逐一解析此网页
        soup = BeautifulSoup(html,"html.parser")
        for item in soup.find_all('div',class_="item"):
            data=[]
            item = str(item)
            link=re.findall(findlink,item)[0]
            

            