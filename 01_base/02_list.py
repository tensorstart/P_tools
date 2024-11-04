empty_list = list()
print(empty_list)
print(type(empty_list))

a = [10, 11, 12, 13, 14]
print(a[1:3])

a = [100, 'a', 'b', 200]
del a[0]

print(a)

##列表方法

# 列表中某个元素个数
a = [1, 1, 2, 3, 4, 5]
print(len(a))  # 总个数：6
# 元素1出现的个数
print(a.count(1))  # 2
# l.index(ob) 返回列表中元素 ob 第一次出现的索引位置，如果 ob 不在 l 中会报错。
print(a.index(1))  # 0

# 列表添加元素

# 向列表添加单个元素
# a.append(ob) 将元素 ob 添加到列表 a 的最后。
a = [1, 1, 2, 3, 4, 5]
a.append(10)
print(a)  # [1, 1, 2, 3, 4, 5, 10]

# append每次只添加一个元素，并不会因为这个元素是序列而将其展开：
a.append([11, 12])
print(a)  # [1, 1, 2, 3, 4, 5, 10, [11, 12]]

# 向列表添加序列
# l.extend(lst) 将序列 lst 的元素依次添加到列表 l 的最后，作用相当于 l += lst。
a = [1, 2, 3, 4]
a.extend([6, 7, 1])
print(a)  # [1, 2, 3, 4, 6, 7, 1]

# 插入元素
# l.insert(idx, ob) 在索引 idx 处插入 ob ，之后的元素依次后移，包括当前的。
a = [1, 2, 3, 4]
# 在索引 3 插入 'a'
a.insert(3, 'a')
print(a)  # [1, 2, 3, u'a', 4]
a

# 移除元素
# l.remove(ob) 会将列表中第一个出现的 ob 删除，如果 ob 不在 l 中会报错。
a = [1, 1, 2, 3, 4]
# 移除第一个1
a.remove(1)
print(a)  # [1, 2, 3, 4]

# 弹出元素
# l.pop(idx) 会将索引 idx 处的元素删除，并返回这个元素。
a = [1, 2, 3, 4]
b = a.pop(0)  # 1
print('pop:', b, ' ;result:', a)

# 排序
# l.sort() 会将列表中的元素按照一定的规则排序：
a = [10, 1, 11, 13, 11, 2]
a.sort()
print(a)  # [1, 2, 10, 11, 11, 13]

# 如果不想改变原来列表中的值，可以使用 sorted 函数：
a = [10, 1, 11, 13, 11, 2]
b = sorted(a)
print(a)  # [10, 1, 11, 13, 11, 2]
print(b)  # [1, 2, 10, 11, 11, 13]

# 列表反向
# list.reverse() 会将列表中的元素从后向前排列。
a = [1, 2, 3, 4, 5, 6]
a.reverse()
print(a)  # [6, 5, 4, 3, 2, 1]

# 如果不想改变原来列表中的值，可以使用这样的方法：
a = [1, 2, 3, 4, 5, 6]
b = a[::-1]
print(a)
print(b)
a

