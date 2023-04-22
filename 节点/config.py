import json
def BuildConfiguration(config={'host':'0.0.0.0',
                 'wwwroot':'/mnt/',
                 'api_key':'sxaewezaeqx',
                 'api_id':'xwezqwxa',
                 'user':'XZWDX',
                 'pwd':'QWA',
                 'Apikey_verification':False,
                 'File_read_APIkey_verification':False,
                 'port':9000,
                 'debug':True,
                 'dev':True,
                 'admin_path':'admin'
                 }): #写入配置
    with open('config.json','w',encoding='utf-8') as f:
        f.write(json.dumps(config))
        return True

def config() -> dict: #查看配置
    with open('config.json','r') as f:
        return json.loads(f.read())
#BuildConfiguration()