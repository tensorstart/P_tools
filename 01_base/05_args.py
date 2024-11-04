# 新需求

# 计算 1+2+3+4

def add(a, b, args=None):
    result = a + b
    if args:
        for arg in args:
            result += arg
    print(result)
    return result


add(1, 2, (3, 4))


# 这种写法很啰嗦，需要把后面的内容要到元组或者数组里面解包

# 优化

def new_add(a, b, *args):
    print(args)
    result = a + b
    for arg in args:
        result += arg
    print(result)
    return result


new_add(1, 2)
new_add(1, 2, 3, 4)




# 2. **函数参数**：
#    - `*args` 用于将任意数量的位置参数传递给函数。
#    - `**kwargs` 用于将任意数量的关键字参数传递给函数。
#    ```python
#    def example(*args, **kwargs):
#        print(args)    # 输出为元组
#        print(kwargs)  # 输出为字典
#
#    example(1, 2, 3, a=4, b=5)
#    # 输出:
#    # (1, 2, 3)
#    # {'a': 4, 'b': 5}
#    ```
#
# 3. **解包（Unpacking）**：
#    - `*` 可以用于解包可迭代对象，如列表、元组等。
#    - `**` 可以用于解包字典。
#    ```python
#    # 列表解包
#    list1 = [1, 2, 3]
#    list2 = [*list1, 4, 5]  # 解包 list1 并合并
#    print(list2)  # 输出: [1, 2, 3, 4, 5]
#
#    # 字典解包
#    dict1 = {"a": 1, "b": 2}
#    dict2 = {**dict1, "c": 3}
#    print(dict2)  # 输出: {'a': 1, 'b': 2, 'c': 3}
#    ```
#
# 4. **函数调用中的解包**：
#    - `*` 用于将列表或元组中的元素作为单独的参数传递给函数。
#    - `**` 用于将字典中的键值对作为关键字参数传递给函数。
#    ```python
#    def add(a, b, c):
#        return a + b + c
#
#    values = [1, 2, 3]
#    result = add(*values)  # 等同于 add(1, 2, 3)
#    print(result)  # 输出: 6
#    ```
#
# 5. **列表解析中的使用**：
#    - `*` 可以用于在赋值时将剩余元素分配给一个变量。
#    ```python
#    a, *b, c = [1, 2, 3, 4, 5]
#    print(a)  # 输出: 1
#    print(b)  # 输出: [2, 3, 4]
#    print(c)  # 输出: 5
#    ```

