import sqlite3
conn = sqlite3.connect("test.db")
c=conn.cursor()
# sql='''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real);
# '''
sql1='''
    insert into company (id,name,age,address,salary)
        values(1,'张三',30,"重庆",4000);
'''
sql2='''
    insert into company (id,name,age,address,salary)
        values(2,'罗帆靖',28,"重庆",11000);
'''

# c.execute(sql1)
c.execute(sql2)
conn.commit()
conn.close()

