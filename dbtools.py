from config import connect_mysql

def getcon():
    connection=connect_mysql('localhost','root','root','empdept')
    if connection.is_connected():
        return connection


def talk_db():
    """fetch the ename sal and job from emp table.
                
                           
            
              
    """
    con=getcon()
    cur=con.cursor()
    cur.execute('select ename,sal,job from emp')
    result=cur.fetchall()
    for _ in result:
        print(_)


# talk_db('select ename,sal,job from emp')


data=[
    ('amitava','kolkata',1234),
    ('samprit','kochi',3234),
    ('spriha','noida',6234),
    ('soumya','asam',7234)
]

def insert_db():
    """insert 4 records in mydata in mysql
                    
                          
                
                  
        """
        
    con=getcon()
    cur=con.cursor()
    q="insert into mydata(name,address,phone) values(%s,%s,%s)"
    cur.executemany(q,data)
    con.commit()
    print('------------data inserted--------------')


# talk_db('select ename,sal,job from emp')
# 
# insert_db(q)


    