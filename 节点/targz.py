#压缩包处理
import zipfile
import os
#decompression-zip
def deco_zip(zip_path,new_path=None,pwd=None) -> bool:
    '''解压zip文件
    参数(
        zip_path :zip文件路径
        new_path :解压后路径,默认是压缩包所在路径
        pwd :密码,默认无
    )
    '''
    try:
        zip_file = zipfile.ZipFile('1.zip', 'r')
        try:
            for names in zip_file.namelist():
                zip_file.extract(names, path='aa',pwd=None)
        except Exception as e:
            return False
        return True #解压成功
    except:
        return False