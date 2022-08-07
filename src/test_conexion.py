
import pymysql
  
def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='sql10.freesqldatabase.com',
        user='sql10511207',
        password = "kYFTyGWvH3",
        db='sql10511207',
        )
      
    cur = conn.cursor()
    cur.execute("select @@version")
    output = cur.fetchall()
    print(output)
      
    # To close the connection
    conn.close()
  
# Driver Code
if __name__ == "__main__" :
    mysqlconnect()