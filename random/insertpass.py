import MySQLdb


def main():
    conn = MySQLdb.connect(host="10.41.118.31",
                           user="imsuser",
                           passwd="Password@123",
                           db="ims")
    x = conn.cursor()
    try:
        x.execute("select user_id from user where mobile_number like '66661%'")
        results = x.fetchall()
        print len(results)
        for row in results:
            query = "insert into user_passwords(user_id, password, created_time, updated_time) values("+row[0]+\
                    ",'4eb462fa94aa598d5ddaf84088560f90aa12cda56f387139c77be4a81b52b6ae',now(),now());"
            # x.execute()
            # conn.commit()
            print query
        print results
    except MySQLdb.Error:
        conn.rollback()
    conn.close()

if __name__ == '__main__':
    main()
