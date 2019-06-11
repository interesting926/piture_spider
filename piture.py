import requests
import json
import urllib
from threading import Thread

def getSogouImag(category,length,path):
    n = length
    cate = category
    url = 'http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?category='+cate+'&tag=%E5%85%A8%E9%83%A8&start=0&len='+str(n)
    imgs = requests.get(url) 
    jd = json.loads(imgs.text)
    jd = jd['all_items']
    imgs_url = []
    for j in jd:
        imgs_url.append(j['pic_url'])
    m = 0
    for img_url in imgs_url:
            print('***** '+str(m)+'.jpg *****'+'   Downloading...')
            try:
                urllib.request.urlretrieve(img_url,path+str(m)+'.jpg')
            except:
                print('图片迷路了') 
            else:         
                m = m + 1
    print('Download complete!')

if __name__ == "__main__":
    title = input('请输入关键字: ')
    t1 = Thread(target=getSogouImag, args=(title,2000,'d:/download/',))
    t2 = Thread(target=getSogouImag, args=(title,2000,'d:/download/',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()