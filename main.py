from flask import Flask, render_template
import datetime
from os import listdir
from os.path import isfile, join
import twitter as tw
import image_overlay as ilay
import band_name as bn

app = Flask(__name__)
app.debug = True
names_made=0

page_info = {}
page_info['business_name'] = u"Band Name Generator"
page_info['desciption'] = u"Get your band name generated here."
page_info['about'] = u"We make the band name for real."
page_info['phone'] = u"(900) 985-2781"
page_info['phone_link'] = u"+1"
page_info['address'] = u"Saint Joseph, MO"
page_info['email'] = u"jaredhaer@gmail.com"
page_info['facebook'] = u"https://www.facebook.com/jared.haer"
page_info['twitter'] = u"https://twitter.com/jared216"
page_info['slides'] = [f for f in listdir('./static/images/band_names/') if isfile(join('./static/images/band_names/', f))]
page_info["moment"]=str(datetime.datetime.now())

@app.route("/")
def index():
    page_info["moment"]=str(datetime.datetime.now())
    return render_template("index.html",page_info=page_info)

@app.route("/band_name")
def bandName():
    global names_made
    page_info['band_name']=bn.getName()
    bname=page_info['band_name']
    p="./static/"
    fn_out='images/band_names/'+str(names_made%12+1)+'.png'
    print(ilay.makeImage(bname,fn_in='./bg.png',fn_out=p+fn_out))
    page_info['band_image']=fn_out
    names_made+=1
    datetime.datetime.now()
    # page_info['tweet_status']=tw.tweetImage(bn.getTweet(bname),ilay.makeImage(bname))
    page_info['slides'] = [f for f in listdir('./static/images/band_names/') if isfile(join('./static/images/band_names/', f))]
    return render_template("band_name.html", page_info=page_info)




if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5004)
