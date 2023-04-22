#路径信息
import os

def getFileFolderSize(fileOrFolderPath):
  """get size for file or folder
  计算文件夹的大小(包含子文件夹的大小)
  """
  totalSize = 0
 
  if not os.path.exists(fileOrFolderPath):
    return totalSize
  
  if os.path.isfile(fileOrFolderPath):
    totalSize = os.path.getsize(fileOrFolderPath) # 5041481
    return totalSize
 
  if os.path.isdir(fileOrFolderPath):
    with os.scandir(fileOrFolderPath) as dirEntryList:
      for curSubEntry in dirEntryList:
        curSubEntryFullPath = os.path.join(fileOrFolderPath, curSubEntry.name)
        if curSubEntry.is_dir():
          curSubFolderSize = getFileFolderSize(curSubEntryFullPath) # 5800007
          totalSize += curSubFolderSize
        elif curSubEntry.is_file():
          curSubFileSize = os.path.getsize(curSubEntryFullPath) # 1891
          totalSize += curSubFileSize
 
      return totalSize
def PathSize(path:str,File_or_folders:bool = None) -> int:
    '''
    计算一个目录的大小，参数:
    path :目标路径
    File_or_folders :是否自动检测路径类型,如果不传,就是自动检测,如果传,则需要传一个路径是否是文件
    '''
    try:
        if(File_or_folders == None):
            File_or_folders = File_or_folder(path)
        if(File_or_folders):
            return os.path.getsize(path)
        else:
            return getFileFolderSize(path)
    except:
        return False
def File_or_folder(path):
    '''
    一个路径是否是文件？
    返回:
    True :目标是文件
    False :目标是目录
    None :目标不存在
    '''
    try:
        if(os.path.isfile(path)):
            return True
        else:
            return False
    except:
        return None
def List(path):
    return [os.path.join(path,i) for i in os.listdir(path)]
def NameList(path):
    return os.listdir(path)

def FileData(path,wwwroot='/mnt/'):
    '''获取文件信息
    传入: path :需要获取的
    返回：
    (
        路径,
        绝对路径,
        是否是文件:bool,
        大小,
        最近访问时间,
        文件创建时间,
        最近修改时间,
        文件所在路径【如果是目录就和目录路径一致】,
        文件名
    )
    '''
    '''
    path :文件路径
    file_path :文件所在目录路径
    file_name :文件名
    '''
    file_path, file_name = os.path.split(path) #文件所在目录路径，文件名
    File_or_folder_data = File_or_folder(path) #检测是否是文件
    return ((os.path.normpath(path.replace(wwwroot, '')),  #相对路径
    os.path.abspath(path), #绝对路径
    File_or_folder_data, #是否是文件:bool
    PathSize(path,File_or_folder_data) , #文件（目录）大小
    os.path.getatime(path), #最近访问时间
    os.path.getctime(path) , #文件创建时间
    os.path.getmtime(path) , #最近修改时间
    file_path, #文件所在目录路径【如果是目录就和目录路径一致】
    file_name #文件名
    ))
def Dict(path,wwwroot='/mnt/'):
    '''
    传入 : path :需要遍历的目录
    返回 :{file_name:FileData(ListData[i])}
    '''
    returnDict = {}
    ListData = List(path)
    NameListData = NameList(path)
    for i in range(len(NameListData)):
        '''
        ListData[i] :文件路径
        '''
        returnDict[NameListData[i]] = FileData(ListData[i],wwwroot) #获取文件信息
    return returnDict
def All_Dict(path,wwwroot='/mnt/'):
    '''
    传入: path :需要遍历的目录(注意，包括子目录的遍历)
    返回 :{file_name:FileData(ListData[i])}
    '''
    ListData = []
    NameListData = []
    for root, dirs, files in os.walk(path, topdown=False): #遍历所有子目录
        for name in files:
            ListData.append(os.path.join(root, name))
            NameListData.append(name) #加入文件名
        for name in dirs:
            ListData.append(os.path.join(root, name))
            NameListData.append(name)
    returnDict = {}
    for i in range(len(NameListData)):
        '''
        ListData[i] :文件路径
        '''
        returnDict[NameListData[i]] = FileData(ListData[i],wwwroot) #获取文件信息
    return returnDict
#print(Dict('d:\Downloads\Luxis file management\wwwroot\\'))