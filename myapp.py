from  flask import  Flask, render_template
import pymysql
app = Flask (__name__)

class Database :
    def __init__(self):
        host = "127.0.0.1"
        user = "root"
        password = "admin123"
        db = "test"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db,
                                   cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def  list_products(self):
        self.cur.execute("SELECT pid, name, price FROM product")
        result = self.cur.fetchall()
        return result



@app.route('/home')
def home ():
    return render_template("home.html")

@app.route('/product')
def product ():
    def db_query():
        db = Database()
        products = db.list_products()
        return products

    res = db_query()

    return render_template("product.html", result=res)

