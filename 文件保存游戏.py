from random import randint

name = input('请输入你的名字:\n')    #输入玩家名字

with open('game2.txt',encoding='gbk') as f:
    lines = f.readlines()

scores = {}  #初始化一个空字典
for line in lines:
    s = line.split()
    scores[s[0]] = s[1:]    #第一项作为key，剩下的作为value    参考 字典常见语句
score = scores.get(name)    #找到当前玩家数据   这里的name是键   name    <=> s[0]
if score is None:   #None用来判断字符串是否存在    input你懂的
    score = [0,0,0]

game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])
if game_times > 0:
    avg_times = total_times / game_times
else:
    avg_times = 0
print('%s,你已经完了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案' %(name,game_times,min_times,avg_times))

num = randint(1,100)
times = 0
print('Guess what I think?\n')
bingo = False
while bingo == False:
    times += 1
    answer = int(input())
    if answer<num:
        print('too small')
    if answer>num:
        print('too big')
    if answer==num:
        print('BINGO!')
        bingo =True
if game_times ==0 or times<min_times:
    min_times = times
total_times += times
game_times += 1

scores[name] = [str(game_times),str(min_times),str(total_times)]
result = ''
for n in scores:
    linepath = n+' '+' '.join(scores[n]) + '\n'
    result += linepath

with open('game2.txt','w',encoding='gbk') as f:
    f.write(result)
