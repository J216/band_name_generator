from TwitterAPI import TwitterAPI
from random import shuffle
import api_auth as aa

hashtags ="#BandNames"

def hashtagString(length=140,mode=0):
    #return string of hashtags filling given character space
    hs=''
    ll=[]
    for item in hashtags:
        if len(item)+2<=length:
            ll.append(item)
    ll.sort(key=len)
    while length > len(ll[0]) and len(ll) > 0:
        il=[]
        for item in ll:
            if len(item)+2<=length:
                il.append(item)
        shuffle(il)
        if not len(il)==0:
            nh=il.pop()
            if len(nh)+2<=length:
                length=length-len(nh)-2
                hs=hs+'#'+nh.strip()+' '
                if nh in ll:
                    ll.remove(nh)
            if len(ll)<1:
                return str(hs).strip()
    return str(hs).strip()

def tweetImage(message="The black dog runs at midnight", image_file="bg.png"):
    try:
        api = TwitterAPI(aa.CK, aa.CS, aa.ATK, aa.ATS)
        file = open(image_file, 'rb')
        data = file.read()
        print(image_file)
        r = api.request('statuses/update_with_media', {'status':message}, {'media[]':data})
        return str(str(r.status_code))
    except:
        return "Tweet not sent"
