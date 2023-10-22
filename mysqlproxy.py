import pymysql

class MySQLProxy:
    def __init__(self, dbname = 'davdbcoffeerebrewer'):
        """ Init the class with the dbname, all other information are now still hard-coded.
        The DB will be created automatically if it doesn't exist
        """
        self.dbname = dbname
        conn1 = pymysql.connect(host="davdbcoffeerebrewer.c3ruoumhmoer.us-west-1.rds.amazonaws.com", port=3306,
                                    user="admin", password="davdbcoffeerebrewer", db="")
        stdb1 = conn1.cursor()
        stdb1.execute("CREATE DATABASE IF NOT EXISTS " + self.dbname)
        self.conn = pymysql.connect(host="davdbcoffeerebrewer.c3ruoumhmoer.us-west-1.rds.amazonaws.com", port=3306,
                                    user="admin", password="davdbcoffeerebrewer", db=dbname)
        self.stdb = self.conn.cursor()

    def create_database(self):
        """
        Create the database table if it's not exists.
        """
        str1 = """CREATE TABLE IF NOT EXISTS coffeeshops ( 
        shopid varchar(32),
        opendate DATE,
        rate DOUBLE
        )
        """
        self.stdb.execute(str1)

    def show_database(self):
        """
        show all the tables in the DB
        """
        print("SHOW TABLES IN DB")
        self.stdb.execute("SHOW TABLES")
        tables = self.stdb.fetchall()
        print(tables)

    def clean_database(self):
        """
        clean all the tables
        """
        self.stdb.execute("DELETE FROM coffeeshops")

    def add_shop_records(self, shoplist):
        """
        add stock information, the input is a list of dict, the dict is column:value pair
        """
        str1 = "INSERT INTO coffeeshops(shopid, opendate, rate) VALUES "
        start = True
        for item in shoplist:
            if not start:
                str1 = str1 + ","
            str1 = str1 + "("
            str1 = str1 + "\'" + item["shopid"] + "\',"
            str1 = str1 + "\'" + item["opendate"] + "\',"
            str1 = str1 + str(item["rate"])
            str1 = str1 + ")"
            start = False
        
        print(str1)
        self.stdb.execute(str1)
    
    def print_all_shops(self):
        """
        Testing only, print all the records
        """
        str1 = "SELECT * FROM coffeeshops"
        self.stdb.execute(str1)
        all_shops = self.stdb.fetchall()
        print("SHOW all Shops")
        print(all_shops)


if __name__ == "__main__":
    proxy = MySQLProxy()
    proxy.show_database()
    proxy.create_database()
    proxy.show_database()
    stock_prices = [{"shopid":"test1", "opendate":"1999-08-20", "rate":3}, {"shopid":"test2", "opendate":"1999-09-20", "rate":4}]
    proxy.add_shop_records(stock_prices)
    proxy.print_all_shops()
