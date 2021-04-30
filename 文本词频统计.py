import jieba
excludes = {'将军','却说','荆州','二人','不可','不能','如此'}
# with open('C:\\Users\\ASUS\\Downloads\\三国演义.txt','r', encoding='utf-8') as txt:
#     txt.read()
txt = open('C:\\Users\\ASUS\\Downloads\\三国演义.txt','r', encoding='utf-8').read()
##使用结巴的函数对文本进行分词
words = jieba.lcut(txt) #jieba.lcut 直接生成的就是一个list
print(type(words))
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        reword = "孔明"
    elif word == "关公" or word == "云长曰":
        reword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        reword = "刘备"
    elif word == "孟德" or word == "丞相":
        reword = "曹操"
    else:
        reword = word
    #   dict.get(key, default=None)    key -- 字典中要查找的键   default -- 如果指定键的值不存在时，返回该默认值
    counts[reword] = counts.get(reword,0) + 1
    #    counts[reword] 表示将列表中被分割好的词语作为该字典的键，通过键来访问值，同样也可以将值赋给对应的键  如   count['曹操'] = 1,这里的值默认给0，然后通过每次迭代相加1
    #   字典有两种访问值的方式     1.counts[键]     2.counts.get(键，默认为None)
print(type(counts[reword]))
for word in excludes:
    del (counts[word])
items = list(counts.items())    #将字典转为列表
#   Python 字典 items() 方法以列表返回可遍历的(键, 值) 元组数组
print(type(items))
#根据iems的第二个值进行从大到小的排序
items.sort(key= lambda x:x[1], reverse=True)  #这里的x[1]就是列表中的第二项，也就是词频    降序排列
#   python列表排序 sort   python字典排序 sorted     key 是带一个参数的函数, 用来为每个元素提取比较值. 默认为 None, 即直接比较每个元素
for i in range(5):
    word,count = items[i]
    #左对齐，占位10位，填充字符为空格
    print("{0:<10} {1:>5}".format(word,count))

#输入列表——将值作为键给字典，并且字典将相同的键的值迭代相加，键要唯一    最终将字典——列表输出

