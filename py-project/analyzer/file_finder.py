from ntpath import isfile
import os

def find_py_files(file_name):
    """智能查找文件(按需递归)"""
    #处理用户可能输入的.py后缀名
    if file_name.endswith(".py"):
        target=file_name
    else:
        target=f"{file_name}.py"

    #检查是否是绝对路径
    if os.path.isfile(target):
        return [os.path.abspath(target)]

    #检查当前目录
    if os.path.isfile(target):
        return [os.path.abspath(target)]

    #检查是否需要递归
    if not any(os.path.isdir(d) for d in os.listdir(".")):
        return []

    #递归查找子目录(跳过当前目录)
    found=[]
    for root,dirs,files in os.walk('.'):
        if root!='.' and target in files:
            found.append(os.path.abspath(os.path.join(root,target)))
    return found

def select_file(files):
    """处理多文件选择"""
    if len(files)==1:
        return files[0]

    print("找到多个匹配文件")
    for i,f in enumerate(files,1):
        print(f"{i}:{f}")
        
    while True:
        try:
            choice=int(input("请选择序号:"))
            if 1<=choice<=len(files):
                return files[choice-1]
            print(f"请输入1~{len(files)}之间的数字:")
        except ValueError:
            print("请输入有效数字:")
