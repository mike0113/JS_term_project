from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy


# 配置資料庫 URI
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lands.sqlite3'
app.config['SECRET_KEY'] = "random string"


# 初始化 SQLAlchemy
db = SQLAlchemy(app)


class Land(db.Model):
    id                  = db.Column(db.Integer, primary_key=True)
    name                = db.Column(db.String(13), nullable=False)
    #地址
    city_id             = db.Column(db.Integer, nullable=False) # 縣市
    dist                = db.Column(db.String(10),  nullable=False) # 鄉鎮區
    land_ping           = db.Column(db.Float)   # 地坪 (小數3位)
    total_price             = db.Column(db.Float)   # 總價 (小數1位)
    unit_price          = db.Column(db.Float)   # 單價/坪 (小數2位) 由系統計算

# 建立資料表
with app.app_context():
    db.create_all()


@app.route('/search', methods= ['POST'])
def search():
    query = Land.query
    if 'city' in request.form: 
        cityID = int(request.form["city"])
        query = query.filter(Land.city_id == cityID)
    if 'keyword' in request.form:
        keyword = request.form["keyword"]
        query = query.filter(Land.name.like(f"%{keyword}%"))

    print("****************************************")
    lands = query.all()
    print("lands", lands)


    if not lands:
        lands = "No lands"

    return render_template('result.html', result=lands)






    print (city, keyword)


if __name__ == '__main__':
    app.run(debug = True)


#測試資料: 
#1:
#name: Land C
#city: 新北市

#2:
#name: Land house
#city: 新北市