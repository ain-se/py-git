import re
from typing import Dict,Any
from chardet import detect

def parse_functions(file_path:str)->Dict[str,Dict[str,Any]]:
    """解析py函数调用关系"""
    code=""
    with open(file_path,'rb') as f:
        raw_data=f.read()
        encoding=detect(raw_data)['encoding'] or 'utf-8'
    try:
        with open(file_path,'r',encoding=encoding) as f:
            code=f.read()
    except Exception as e:
        print(f"无法读取文件:{e}")

    functions={}
    for match in re.finditer(r'def\s+(\w+)\s *\((.*?)\)\s*:',code):
        name,params=match.group(1),[p.strip() for p in match.group(2) if p.strip()]

        #查找函数体结束位置
        start=match.end()
        indent=0
        body_end=len(code)

        #简单查找函数体结束
        for m in re.finditer(r'^\s+',code[start:],re.MULTILINE):
            if not indent:
                indent=len(m.group(0))
            elif len(m.group(0))<indent:
                body_end=start+m.start()
                break

        body=code[start:body_end]
        calls=set()

        #查找函数调用
        for call in re.finditer(r'(\w+)\s*\(',body):
            called=call.group(1)
            if called!=name and called not in params:
                calls.add(called)

        functions[name]={'params':params,'calls':list(calls)}
    return functions
