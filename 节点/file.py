#文件操作类
import os
import shutil

def mkdir(path): #创建目录
    folder = os.path.exists(path)
    if not folder:                   #判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)            #makedirs 创建文件时如果路径不存在会创建这个路径
    else:
        pass
def delete(path):
    '''Delete删除文件、目录
    参数：
    path:删除文件、目录的路径
    '''
    if(os.path.isfile(path)):os.remove(path)
    elif(os.path.isdir(path)):shutil.rmtree(path)
    else:return False
    return True
def upload(path,FileList:dict):
    '''写入上传的文件
    参数：
    path:上传后创建文件、目录的路径
    FileList:文件列表
    '''
    path = f'{path}/'
    for name,data in FileList.items():
        name = f'{path}{name}'
        try:
            with open(name, 'wb') as f:
                f.write(data)
        except:
            mkdir(path)
            with open(name, 'wb') as f:
                f.write(data)
    return True
def add(path,content='null'):
    '''创建文件
    参数:
        path :文件路径
        content :文件写入内容(默认是null)
    '''
    mkdir(os.path.split(path)[0]) #验证目录是否存在,不存在则创建目录
    if(not os.path.isfile(path)):
        try:
            if(str(type(content)) != "<class 'str'>"):
                content='null'
            with open(path, 'w') as f:
                f.write(content)
            return True
        except:
            return False
    else:
        return False
def copy(old,new):
    '''复制文件
    参数：
        old:复制前的路径
        new:复制后的路径
    '''# shutil.copyfile
    print([old,new])
    if(os.path.exists(old) and not os.path.exists(new)): #需要复制前的文件存在,复制的目标路径不存在
        mkdir(os.path.dirname(new))
        if(os.path.isfile(old)):shutil.copyfile(old,new) #复制文件
        else:shutil.copytree(old,new) #复制目录
        return True
    else:
        return False
def move(old,new):
    '''复制路径
    参数：
        old:移动前的路径
        new:移动后的路径
    '''# shutil.copyfile
    if(os.path.exists(old) and not os.path.exists(new)): #需要移动前的文件存在,移动的目标路径不存在
        shutil.move(old,new) #移动成功
        return True
    else:
        return False
def change(path,content): #更改文件
    '''更改文件内容
    参数：
    path: 需要更改的文件路径
    content: 需要更改的内容
    '''
    try:
        with open(path,'wb') as f:
            f.write(content)
            return True
    except:
        return False
def change_txt(path,content): #更改文本文件
    '''更改文件内容（文本）
    参数：
    path: 需要更改的文本文件路径
    content: 需要更改的文本内容
    '''
    try:
        with open(path,'w') as f:
            f.write(content)
            return True
    except:
        return False
# print(copy('/wwwroot/hello','/wwwroot/hxuynuy/aa'))
# print(os.path.exists('./wwwroot/hello') and not os.path.exists('./wwwroot/hxuynuy/aa'))