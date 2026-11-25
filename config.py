import mysql.connector as ms

def connect_mysql(h:str,u:str,p:str,db:str):
    return ms.connect(   
    host=h,
    user=u,
    password=p,
    database=db
    )


# if connect_mysql('localhost','root','root','empdept').is_connected():
#     print('------------we are connected---------------')
# else:
#     print('sorry............')



