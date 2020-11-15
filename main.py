from flask import Flask,render_template,request
from project import NAMESLIST,CONTACT_NO,ADDRESSLIST,PRODUCTLIST,DELAYLIST,SHIPMENTSTATUSDETAILS,ESTIMATEDDELIVERYDATE,DELAYLIST
import random
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


app=Flask(__name__)
english_bot = ChatBot("Chatterbot",storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(english_bot)
trainer.train("intents\intents.yml")



@app.route("/")
def main():

    return render_template("main.html")

@app.route("/aboutus.html")
def aboutus():


    return render_template("aboutus.html")
@app.route("/main.html")
def main_():

    return render_template("main.html")
@app.route("/contactus.html")
def contactus():


    return render_template("contactus.html")
@app.route("/orders.html")
def orders():


    return render_template("orders.html")

@app.route("/bot.html")
def bot1():

    return render_template("bot.html")

@app.route("/get")
def get_bot_response():
     userText = request.args.get("msg") #get data from input,we write js  to index.html
     return str(english_bot.get_response(userText))










@app.route("/orders.html/<id>")
def orderss(id):
    NAME=random.choice(NAMESLIST)
    CONTACT=random.randrange(8054598678,9949898799)
    ADDRESS=random.choice(ADDRESSLIST)
    PRODUCT=random.choice(PRODUCTLIST)
    SHIPMENTSTATUS=random.choice(SHIPMENTSTATUSDETAILS)
    if (SHIPMENTSTATUS=="DELIVERED"):
        DELAY="NO DELAY"
        
    else:
        DELAY=random.choice(DELAYLIST)
    ESTIMATED_DELIVERY=random.choice(ESTIMATEDDELIVERYDATE)
    product_type={

        "ASUS TUF GAMING FX505DT,": 'https://image1.pricedekho.com/p/3/2/52/3401052/36636078-asus-tuf-gaming-fx505dt-156-picture-big.jpg',


        "ASUS ROG STRIX G5T31,": 'https://1.bp.blogspot.com/-gVoxb2AI0ls/XXYWCSmt8UI/AAAAAAABMdA/b_rzO0Bi1swBfml9DTf_sjtZL4HRf4NxACLcBGAs/s1600/Asus%2BROG%2BStrix%2BSCAR%2BIII%2BG531GW%2B%2B%25282%2529.JPG',


        "REAL ME 9 PRO,":  'https://devicenext.com/wp-content/uploads/2020/09/realme-7-Pro-goes-on-sale.png',

        "REDMI 11 PRO,":  'https://i01.appmifile.com/webfile/globalimg/zhouyuxin/J6B-Green-800.png',


        "IPHONE GALAXY DUOS,":  'https://images-na.ssl-images-amazon.com/images/I/611JavcU70L._SL1024_.jpg',


        "SAMSUNG GALAXY S20 EDGE,":  'https://images-na.ssl-images-amazon.com/images/I/51TUrW6GlwL._AC_SX425_.jpg',


        "VIVO X50 PRO,":  'https://urbanrepublic.com.my/wp-content/uploads/2020/07/X50-Pro.jpg',


        "VIVO Z1PRO,": 'https://i.gadgets360cdn.com/products/large/vivo-z1-pro-417x800-1562138891.jpg',


        "HONOR 9 LITE,":  'https://www.gizbot.com/imgf/400x80/img/gadget-finder/original/2018/10/honor-8c_1539255267.jpg',


        "SONY XPERIA L24,":  'https://www.gizmochina.com/wp-content/uploads/2020/02/Sony-Xperia-10-II-1-500x500.jpg',


        "ADIDAS MEN SPORTS,":  'https://shoprapy.com/wp-content/uploads/2020/03/15a3663a-5d56-4273-944d-c6d730e022bb1583125082131-ADIDAS-Men-Sports-Shoes-4441583125080663-1.jpg',

    }
    
    return render_template("orders.html",order_image=product_type[PRODUCT],name=NAME,id=id,contact=CONTACT,address=ADDRESS,product=PRODUCT,shipment_details=SHIPMENTSTATUS,estimated=ESTIMATED_DELIVERY,delay=DELAY)

    
if __name__ == "__main__":
    app.run(debug=True)


