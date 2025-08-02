from analyzer.file_finder import find_py_files,select_file
from analyzer.function_parser import parse_functions
from analyzer.text_drawer import draw_relation_graph

def main():
    print("python函数关系分析器(极简版) 支持路径")
    file_name=input("请输入py文件名(不含.py)或完整路径:").strip()
    

    if not file_name:
        print("错误,文件名不能为空")
        return

    found_files=find_py_files(file_name)
    if not file_name:
        print(f"找不到{file_name}.py文件")
        return

    target_file=select_file(found_files)
    functions=parse_functions(target_file)
    draw_relation_graph(functions)

if __name__=="__main__":
    main()
