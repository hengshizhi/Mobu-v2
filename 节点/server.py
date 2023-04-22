# 一人我编程累
# 碎过了节操心沉醉
# 两眼是Code相随
# 不求他日能早归
# 鼠标我轻点屏
# 键盘我手速行
# 痴情代码
# 心甘情愿
# 千里把那个bug寻
# 说项目呵呵笑
# PM主意太奇妙
# 我轻狂那太高傲
# 我懵懂的无知太年少
# 赶进度，没班下
# 上线了产品还牵挂
# 千古的留名传佳话
# 我三年架构已白发
# 天天加班何人陪
# 谁是谁非谁相随
# 全栈通吃为了谁
# 我能写几回，测几回
# 败硬件，斗时间
# 提高了并发已成仙
# 豪情万丈天地间
# 我续写了另类码农篇
# 红尘事我已斩断
# 久居帝都人心乱
# 当年房价没上万
# 我 为这了没买留遗憾
# 创业我愁断肠
# 眼中我泪两行
# 多年为君早日上市
# 一朝敲钟把名扬
# 白：感谢我这么漂亮~
# 白：年轻的快乐时刻，享受一首"一人编程累"
# 白：快乐的动感旋律，一起来吧~~
# 爱情是什么鬼
# 谁信谁就脑进水
# 谁错谁对谁是谁非
# 深夜我把代码怼
# 性能我心头事
# 此生我怀大志
# 为了老板回眸一笑
# 我立下这毒誓
# VR我常相伴
# AI我深度上
# 回眸沧海
# 一曲忧伤
# 感触盒饭香
# 项目实施人在外
# 我归来之日谁还在
# 兄弟写码论豪迈
# 我驰骋职场求一败
# 程序员我们都是傻逼
# 编程语言改变了哥的口味
# C++，JAVA，PHP
# 许多年前还要学VB
# 找不到对象毫不诡异
# 茶不思饭不想视死如归
# 别说我平时像条死鱼
# 内存泄漏让哥没了性欲
# 寂寞的时候干什么？
# 写程序写程序
# 失恋的时候干什么？
# 写程序写程序写程序
# 发骚的时候干什么？
# 写程序写程序
# 剩下的时候干什么？
# 调程序调程序调程序
try:
    from sanic import Sanic #导入sanic web的本体
    from sanic.response import text,html,json,file,raw,file_stream,redirect,empty #导入sanic web的工具类
    import md5 #导入md5
    import sys #导入系统模块
    from urllib.parse import unquote #导入URL解码
    import file as File_operation #导入文件操作
    import route as routeLabor #导入目录操作
    import PathInfo as PathInfo # 路径信息获取
    import json as json # json操作类
    import config as config # config
    from NodeStatistics import statistics # 导入统计
    # import os
    import time
except:
    import autoinstall #自动下载库
    from sanic import Sanic #导入sanic web的本体
    from sanic.response import text,html,json,file,raw,file_stream,redirect,empty #导入sanic web的工具类
    import md5 #导入md5
    import sys #导入系统模块
    from urllib.parse import unquote #导入URL解码
    import file as File_operation #导入文件操作
    import route as routeLabor#导入目录操作
    import PathInfo as PathInfo # 路径信息获取
    import json as json # json操作类
    import config as config # config
    from NodeStatistics import statistics # 导入统计
    # import os
    import time

try:
    config_data = config.config()
    host = config_data['host'] # 。。。
    wwwroot = config_data['wwwroot']#sys.path[0]+'/mnt/' #网站服务器根路径
    api_id = config_data['api_id'] #API_ID
    api_key = config_data['api_key'] #API_KEY
    user = config_data['user'] #xinghengshizhiaaa
    pwd = config_data['pwd'] #aaaaiumuy3298s872m98zauz
    Apikey_verification = config_data['Apikey_verification'] #是否开启APIkey的验证
    File_read_APIkey_verification = config_data['File_read_APIkey_verification'] #访问读取APIkey验证（私有读）
    port = config_data['port'] #启动端口
    debug = config_data['debug'] #debug模式
    dev = config_data['dev'] #开发环境
    admin_path = config_data['admin_path'] #管理路径
    from PIL import Image
    from io import BytesIO
except:
    host = "0.0.0.0" # 。。。
    wwwroot = './wwwroot/'#sys.path[0]+'/mnt/' #网站服务器根路径
    api_id = 'yWq7XGpQMZqHZOY3zZJCXc11TEHQwA' #API_ID
    api_key = '6kwKzwu9VLPc4j8UDKIh3f58wm9VXR' #API_KEY
    user = 'f2aeadaa9424b3b72a2b2734533596b9' #xinghengshizhiaaa
    pwd = '738eb259b35e85bde8549bcecf221457' #aaaaiumuy3298s872m98zauz
    Apikey_verification = False #是否开启APIkey的验证
    File_read_APIkey_verification = False #访问读取APIkey验证（私有读）
    port = 8840 #启动端口
    debug = True #debug模式
    dev = True #开发环境
    admin_path = 'admin' #管理路径
    Moebu_node_api_verification_failed = True #萌部节点API验证
    from PIL import Image
    from io import BytesIO

app = Sanic("Luxis_file_management") #实例化Sanic

def get_or_post(request,key): #如果没有GET参数就用post
    if(request.args.get(key) != None):
        return request.args.get(key)
    elif(request.form.get(key) != None):
        return request.form.get(key)
    return None
def Get_file_dict(request) -> dict:
    '''获取包含文件内容的字典,参数request是Sanic的request对象'''
    FileDict = {}
    for i in request.files['file']:
        i = tuple(i)
        FileDict[i[2]] = i[1]
    return FileDict
def Web_path_to_absolute_path(path):
    '''web路径转绝对路径
    参数：
        path:web路径
    '''
    return '{}{}'.format(wwwroot,unquote(path))

def Path_Execution(request,path_arg):
    '''
    文件流:GET :filestream=true
    '''
    filestream = request.args.get('filestream')
    if(not filestream == 'true'):
        try:
            return [file,(Web_path_to_absolute_path(path_arg))]
        except:
            return text('404',404)
    else:
        try:
            return [file_stream,(Web_path_to_absolute_path(path_arg))]
        except:
            return text('404',404)

def API_Execution(request,name):
    '''API运行函数
    参数:
        (路径参数)name:请求的API名字
    公共参数:
        path :操作的路径
    '''
    if(get_or_post(request,'route') != None):route = True #判断是否是路径操作
    else:route = False
    try:
        path_arg = wwwroot+get_or_post(request,'path') #转换web路径为系统绝对路径
    except:
        path_arg = wwwroot #转换web路径为系统绝对路径
    
    if(name == 'path'):
        return [text,(path_arg)]
    elif(name == 'delete'): #删除目录或者文件
        if(File_operation.delete(path_arg)):
            return [text,('OK!')]
        else:
            return [text,('non-existent')]
    elif(name == 'upload'): #上传
        if(File_operation.upload(path_arg,Get_file_dict(request))):
            return [text,('OK!')]
        else:
            return [text,('non-existent')]
    elif(name == 'add'): #创建
        '''add文件API '''
        if(route): #判断是否是创建路径
            if(routeLabor.mkdir(path_arg)): #创建目录
                return [text,('OK!')]
            else:
                return [text,('The directory you want to create already exists')] #希望创建的目录已存在
        else: #创建文件
            if(File_operation.add(path_arg)):
                return [text,('OK!')]
            else:
                return [text,('The file or path to be created already exists')] #要创建的文件或路径已存在
    elif(name == 'rename'): #重命名目录或者文件
        '''重命名目录或者文件
        GET参数:
            old:重命名前的目录或文件
            new:重命名后的目录或文件
        '''
        try: #接收GET参数
            old = get_or_post(request,'old')
            old = unquote(f'{path_arg}{old}')
            new = get_or_post(request,'new')
            new = unquote(f'{path_arg}{new}')
        except:
            return [text,('Incomplete parameters')] #参数不完整
        if(routeLabor.rename(old,new)):
            return [text,('OK!')]
        else:
            return [text,('The source file or directory cannot be found')] #源文件或者目录找不到
    elif(name == 'copy'): #复制文件或目录
        '''复制目录或者文件
        GET参数:
            old:复制前的目录或文件
            new:复制后的目录或文件
        '''
        try: #接收GET参数
            old = get_or_post(request,'old')
            new = get_or_post(request,'new')
            old = unquote(f'{path_arg}{old}')
            new = unquote(f'{path_arg}{new}')
        except:
            return [text,('Incomplete parameters')] #参数不完整
        if(route): #判断是否是路径模式
            if(routeLabor.copy(old,new)): 
                return [text,('OK!')]
            else:
                return [text,('The source folder (file) to be copied does not exist or the destination folder (file) already exists')] 
                #要复制的源文件夹（文件）不存在或者目标文件夹（文件）已存在
        else:
            if(File_operation.copy(old,new)):
                return [text,('OK!')]
            else:
                return [text,('The source folder (file) to be copied does not exist or the destination folder (file) already exists')]
                #要复制的源文件夹（文件）不存在或者目标文件夹（文件）已存在
    elif(name == 'move'):
        '''move目录或者文件
        参数:
            old:move前的目录或文件
            new:move后的目录或文件
        '''
        try: #接收GET参数
            old = get_or_post(request,'old')
            new = get_or_post(request,'new')
            old = unquote(f'{path_arg}{old}')
            new = unquote(f'{path_arg}{new}')
        except:
            return [text,('Incomplete parameters')] #参数不完整
        if(route): #判断是否是路径模式
            if(routeLabor.move(old,new)): 
                return [text,('OK!')]
            else:
                return [text,('The source folder (file) to be moved does not exist or the destination folder (file) already exists')] 
                #要移动的源文件夹（文件）不存在或者目标文件夹（文件）已存在
        else:
            if(File_operation.move(old,new)):
                return [text,('OK!')]
            else:
                return [text,('The source folder (file) to be moved does not exist or the destination folder (file) already exists')]
                #要移动的源文件夹（文件）不存在或者目标文件夹（文件）已存在
    elif(name == 'changeTxt'):
        '''更改文本内容（文本啊）
        参数 :
            content:文本内容
        '''
        content = str(request.form.get('content'))
        if(File_operation.change_txt(path_arg,content)):
            return [text,('OK!')]
        else:
            return [text,('The file to be changed does not exist')] #要更改的文件不存在
    elif(name == 'PathInfo'):
        '''获取路径信息
        参数 :
            type :信息类型,支持(
                All :所有路径信息
                appoint :指定路径信息
            )
        --> json data(
            {文件或者目录名: [路径,绝对路径,是否是文件:bool,大小,最近访问时间,文件创建时间,最近修改时间]}
        )
        '''
        Type = get_or_post(request,'type')
        if(Type == 'All'):
            return [text,json.dumps(PathInfo.All_Dict(path=path_arg,wwwroot=wwwroot))]
        elif(Type == 'appoint'):
            print(path_arg)
            return [text,json.dumps(PathInfo.Dict(path=path_arg,wwwroot=wwwroot))]
        return [text,'The requested data is not specified']
    else:  
        return [text,('Path - {}{}'.format(wwwroot,path_arg))]

async def admin(request,admin_path=None):
    import os
    if(admin_path == None):
        if(os.path.isfile(f'./admin/index.html')):return await file(f'./admin/index.html')
        else:return text('无效的页面',404)
    else:
        if(os.path.isfile(f'./admin/{admin_path}')):return await file_stream(f'./admin/{admin_path}')
        elif(os.path.isfile(f'./admin/404.html')):return await file(f'./admin/404.html')
        else:return text('无效的页面',404)

async def api(request,name):
    '''API请求执行函数
    参数:
        name:请求的API名字
    '''
    get_api_id  = get_or_post(request,'api_id')
    get_api_key = get_or_post(request,'api_key')
    if(Apikey_verification):
        if(get_api_id == api_id and get_api_key == api_key):
            API_Execution_data = API_Execution(request,name)
            return API_Execution_data[0](API_Execution_data[1])
    else:
        API_Execution_data = API_Execution(request,name)
        return API_Execution_data[0](API_Execution_data[1])
    return text('APIkey验证不通过')

async def upload(request): #生成上传页面（只是页面而已）
    return html(f'''
            <html>
            <body>
                <form action = "/api/upload?path={get_or_post(request,'path')}&api_key={get_or_post(request,'api_key')}&api_id={get_or_post(request,'api_id')}" method = "POST" 
                    enctype = "multipart/form-data">
                    <input type = "file" name = "file" multiple/>
                    <input type = "submit"/>
                </form>
            </body>
            </html>
    ''')
async def path(request,path_arg):
    '''path请求执行函数
    参数:
        path_arg:请求的web路径
    --> 二进制流
    '''
    get_api_id  = get_or_post(request,'api_id')
    get_api_key = get_or_post(request,'api_key')
    try:
        if(File_read_APIkey_verification):
            if(get_api_id == api_id and get_api_key == api_key):
                Path_Execution_data = Path_Execution(request,path_arg)
                return await Path_Execution_data[0](Path_Execution_data[1])
        else:
            Path_Execution_data = Path_Execution(request,path_arg)
            return await Path_Execution_data[0](Path_Execution_data[1])
    except:
        return text('404',404)
    return text('APIkey验证不通过')

async def favicon(request):
    '''favicon.ico图标'''
    return text('OK!')

import Mobuv2
async def MobuV2Odj(request):
    def get_or_post(key):
        if(request.args.get(key) != None):
            return request.args.get(key)
        elif(request.form.get(key) != None):
            return request.form.get(key)
        return None
    if(get_or_post('Moebu_node_api_key') == Moebu_config['api_key'] or not Moebu_config['api_MobuV2Odj_verification_failed']):
        ret = Mobuv2.MobuV2Main(get_or_post,statistics,request)
        return raw(ret['content'],headers=[['content-type',ret['MIME']],['Content-Disposition','inline; name="{filename}"; filename="{filename}"'.format(filename='Mobuv2.jpg')]]) # 返回图片
    else:
        return text('api verification failed')

async def MobuV2NodeAPI(request):
    def get_or_post(key): #如果没有GET参数就用post
        if(request.args.get(key) != None):
            return request.args.get(key)
        elif(request.form.get(key) != None):
            return request.form.get(key)
        return None
    ApiName = get_or_post('ApiName') # 接收API名
    def AddImg(): # 新增图片
        imgdata = list(request.files.get("img"))
        img = Image.open(BytesIO(imgdata[1]))
        name = str(time.time())+'.webp'
        # houzui = os.path.splitext(imgdata[2])[-1] # 文件后缀名
        img.save('{wwwroot}/img/{name}'.format(wwwroot=wwwroot, name=name))
        urllist = Mobuv2.GAFNUTD2() # 图片url列表
        return json.dumps({'OK': True,'id':len(urllist)-1,'url':urllist[-1]})
    def DelImg(): # 减少图片
        pass
    def API(): # API 执行函数
        if(ApiName == 'Node_data'):
            ret = {'NodeName':Moebu_config['NodeName'],
               'obey':Moebu_config['obey'],
               'statistics':Moebu_config['statistics'],
            }
            return text(body=json.dumps(ret))
        elif(Moebu_config['obey']): # 如果服从主节点的控制就会检索控制API
            if(ApiName  == 'ImgList'):
                list = Mobuv2.ImgList()
                return text(json.dumps(list))
            elif(ApiName == 'AddImg'):
                return text(str(AddImg()))
            elif(ApiName == 'DelImg'):
                pass
            elif(ApiName == 'StatisticsData'):
                statisticsData = statistics.get()
                TotalFlow = 0 # 总流量
                for i in statisticsData:TotalFlow += i['Volume'] # 计算总流量
                return text({'total flow':TotalFlow,  # 总流量
                             'total visits':len(statisticsData), # 总访问量
                             'Detail':json.dumps(statisticsData), # 细节数据
                             })
            elif(ApiName == 'StatisticsAddW'):
                return text(statistics.AddW())
    if(get_or_post('Moebu_node_api_key') == Moebu_config['api_key'] 
       or not Moebu_config['api_verification_failed']): # API key验证通过或者不需要验证
        return API()
    else:
        return text('api verification failed')
app.add_route(upload,f'/upload',methods=['GET','POST']) #绑定上传页面
app.add_route(admin,f'/{admin_path}',methods=['GET']) #管理页面
app.add_route(admin,f'/{admin_path}/<admin_path:path>',methods=['GET'])
app.add_route(favicon, "/favicon.ico",methods=["GET"]) # favicon.ico
app.add_route(path, "/<path_arg:path>",methods=["POST", "GET"]) # 定义根目录访问
app.add_route(api, "/api/<name:alpha>",methods=["POST", "GET"]) #定义API访问
app.add_route(MobuV2Odj ,'/Mobuv2',methods=["POST", "GET"])
app.add_route(MobuV2NodeAPI ,'/Mobuv2NodeAPI',methods=["POST", "GET"])
# app.add_route(MobuV2Odj ,'/Mobuv2/',methods=["POST", "GET"])
statistics = statistics()
Moebu_config = {
    'NodeName' : 'Mobu node',
    'statistics' : True,
    'api_key' : 'iueyxiuwjyuh392ysj8y8kas',
    'api_verification_failed' : True,
    'obey' : True, # Whether to obey the management of the main node
    'api_MobuV2Odj_verification_failed' : False, # 随机图片是否需要验证API
}
if __name__ == "__main__":
    app.run(host=host,port=port,debug=debug,dev=dev)