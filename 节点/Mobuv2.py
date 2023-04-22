#Mobu v2 main function

import os
import config
from PIL import Image
from io import BytesIO
from random import choice,randint
import os
import json
import output

url = 'https://service-djbqi6pz-1306777571.sh.apigw.tencentcs.com/release/?'

def GetAllFileNamesUnderTheDirectory(): #获取目录下所有文件名
    root = '{wwwroot}/img'.format(wwwroot=config.config()['wwwroot'])
    path = os.path.join(root)
    filenames = os.listdir(path)
    pathnames = [os.path.join(path, filename) for filename in filenames]
    return pathnames
def ImageZoom(width,p_img): #图像缩放
    '''Parameters:
    Width: width of the target image
    p_ Img: PIL object'''
    widths, height = p_img.size   # 获取宽高
    fdl = width/widths #缩放率
    p_img = p_img.resize((int(widths*fdl), int(height*fdl)), Image.ANTIALIAS)
    return p_img

def MobuV2Main(get_or_post):
    def Picture_stream():
        def load(id = None):
            pathnames = GetAllFileNamesUnderTheDirectory()
            if(id != None):
                id = int(id)
                #choice(pathnames) 随机
                try: #id正确的情况
                    with open(pathnames[id], 'rb') as f:
                        im = f.read()
                except: #id错误的情况
                    output.echo('id错误', 'text/html')
            else:
                with open(choice(pathnames), 'rb' ) as f:
                    im = f.read()
            return Image.open(BytesIO(im))   # BytesIO实现了在内存中读写Bytes
            #->return p_img
        def PilTob(p_img,mode,widths=1920): # PIL 转二进制
            b_img = BytesIO()   # 创建一个空的Bytes对象
            ImageZoom(widths,p_img).save(b_img, format=mode) # 保存为jpg格式
            return b_img.getvalue()
        if(get_or_post('id') != None):
            p_img = load(get_or_post('id'))
        else:
            p_img = load()
        if(get_or_post('form') != None):
            try:
                # 格式输入正确
                output.echo(PilTob(p_img,get_or_post('form')),f'''image/{get_or_post('form')}''')
            except:
                output.echo('格式输入错误', 'text/html')
        else:
            output.echo(PilTob(p_img,'webp'),'image/webp')
    def json_output():
        pathnames = GetAllFileNamesUnderTheDirectory()
        outputdict = {'url':f'{url}'} #需要输出的字典
        changedict = {}
        if(get_or_post('id') != None):
            changedict['id'] = get_or_post('id')
        else:
            changedict['id'] = randint(0,len(pathnames)-1)
        if(get_or_post('form') != None):
            changedict['form'] = get_or_post('form')
        else:
            changedict['form'] = 'webp'
        for k,v in changedict.items():
            outputdict[k] = v
            outputdict['url'] += f'{k}={v}&'
        output.echo(json.dumps(outputdict),'text/json')
    if(get_or_post('output')=='json'):
        json_output()
    elif(get_or_post('output')=='TotalNumberOfImages'): #图像总数
        output.echo(len(GetAllFileNamesUnderTheDirectory()),'text/html')
    else:
        Picture_stream()
    return output.Web_output() # web output