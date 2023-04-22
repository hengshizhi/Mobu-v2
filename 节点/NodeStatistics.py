from config import config as config
import json as json
config = config()
class statistics():
    path = '{wwwroot}/statistics/statistics.json'.format(wwwroot=config['wwwroot'])
    data = []
    def get(self):
        with open(self.path,'r') as fr:
            return json.loads(fr.read())
    def create(self):
        '''创建(初始化)统计数据'''
        with open(self.path,'w') as f:
            f.write(json.dumps([]))
    def add(self,id,Volume,url,ip):
        '''增量:
        id : 访问的id
        Volume : 访问的流量
        url : 访问的url
        ip : 访问者的ip地址
        '''
        data = self.get()
        with open(self.path,'w') as f:
            data.append({'id':id,
                            'Volume':Volume,
                            'url':url,
                            'ip':ip,
                            })
            f.write(json.dumps(data))
    def AddNotW(self,id,Volume,url,ip):
        self.data.append({'id':id,'Volume':Volume,'url':url,'ip':ip,})
    def AddW(self):
        data = self.get()
        for i in self.data:data.append(i) # 循环增加待写入内容
        lens = len(self.data)
        self.data = []
        print(str(data)+'3333333333333333333333333')

        with open(self.path,'w') as f:
            f.write(json.dumps(data))
        return 'OK,Add {len} pieces of data'.format(len=lens)

# statistics = statistics()
# statistics.create()
# statistics.AddNotW(21321,12321,'http://localhost','127.07.0.1')
# statistics.AddNotW(1345,123242321,'http://localhost','127.07.0.1')
# statistics.AddW()
# print(statistics.get())