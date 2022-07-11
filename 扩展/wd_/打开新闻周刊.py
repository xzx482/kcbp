
import json
from urllib import request
import time
from selenium import webdriver
from selenium.webdriver.common.by import By



'''
pip3 install selenium -i https://pypi.tuna.tsinghua.edu.cn/simple
'''

'''
uo=request.urlopen('https://api.cntv.cn/NewVideo/getVideoListByColumn?id=TOPC1451559180488841&serviceId=tvcctv')
jl=json.load(uo)

print(jl)
'''


option=webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches",['enable-automation'])
def main(url):
    driver=webdriver.Chrome(chrome_options=option,desired_capabilities=None)
    driver.implicitly_wait(20)
    driver.get(url)
    vpl=None
    while not vpl:
        time.sleep(1)
        #vpl=driver.find_elements_by_class_name('vjs-big-play-button')
        vpl=driver.find_element(By.CLASS_NAME,'vjs-big-play-button')
    vpl.click()
    #driver.find_elements_by_class_name('vjs-fullscreen-control')[1].click()
    driver.find_elements(By.CLASS_NAME,'vjs-fullscreen-control')[1].click()
    #点击播放按钮和点击全屏按钮不能使用js, 浏览器会阻止自动播放和自动全屏
    time.sleep(3)
    driver.execute_script('''

    function sleep(time){
        return new Promise((resolve)=>setTimeout(resolve,time));
    }

    var e=document.createEvent("MouseEvents");
    e.initEvent("click",true,true);
    document.getElementById('myFlash_player').childNodes[10].childNodes[7].childNodes[2].childNodes[0].childNodes[0].dispatchEvent(e);//超清 画质 按钮
    await sleep(100);
    va=document.getElementById("myFlash_player_html5_api");
    var d=va;

    d.onended=()=>{
        window.close();
    }
    d.style.cursor='none';
    d.addEventListener("mousemove",()=>{
        d.style.cursor='auto';
        clearTimeout(d.curto);
        d.curto=setTimeout(()=>{
            d.style.cursor='none';
        },1000);
    });

    d.addEventListener("ended",()=>{

    });

    va.oncanplaythrough=async()=>{
        va.oncanplaythrough=null;
        va.playbackRate=1.6;
        await sleep(2000);
        va.currentTime=24;
    }
    aex=false;
    window.onbeforeunload=(e)=>{let m='?';e.returnValue=m;aex=true;return m;}

    ''')



    #'''
    et=18*60+58
    #print(s)
    while 1:
        try:
            aex=driver.execute_script('return aex;')
        except:
            aex=False
        x_=time.localtime()
        if(aex or(et-(x_.tm_hour*60+x_.tm_min)<=0)):
            break
        time.sleep(1)
    #time.sleep(s*60)
    #'''
    driver.quit()
    #input(1)

if __name__=='__main__':
    url=json.load(request.urlopen('https://api.cntv.cn/NewVideo/getVideoListByColumn?id=TOPC1451559180488841&n=1&p=1&mode=0&serviceId=tvcctv'))['data']['list'][0]['url']
    main(url)