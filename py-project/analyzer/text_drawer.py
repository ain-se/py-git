def draw_relation_graph(functions):
    """纯文本关系图"""
    print("\n函数调用关系:")
    print("="*40)

    for func,data in functions.items():
        if not data['calls']:
            continue

        print(f"\n■ {func}({','.join(data['params'])})")
        for i,call in enumerate(data["calls"],1):
            arrow="⇔ "if call==func else "→"
            prefix=" ├─" if i<len(data['calls']) else " └─"
            print(f" {prefix}{arrow}{call}")

            if call in functions and functions[call]['params']:
                print(f"    │   ← {','.join(functions[call]['params'])}")

    print("\n图例: →普通调用 ⇔递归调用")
