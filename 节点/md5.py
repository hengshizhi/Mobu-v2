#MD5算法
import hashlib
def get_md5(data):   #传参为需要加密的字符串
    obj = hashlib.md5("sidrsicxwersdfsaersdfsdfresdy54436jgfdsjdxff123ad".encode('utf-8'))
    obj.update(data.encode('utf-8'))
    result = obj.hexdigest()
    return result