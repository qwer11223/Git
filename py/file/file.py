print('\n', '='*10, '蚂蚁庄园动态', '='*10)

file = open('./message.txt', 'w', encoding='utf-8')

file.write('你使用了一张加速卡，小鸡撸起袖子开始双手吃饲料，进食速度大大加快.\n')

file.flush()

print('\n 写入了一条动态······\n')

file.write('第二条消息\n')

file.close()

# -- 读取文件内容 ---

with open('message.txt', 'r', encoding='utf-8') as file:
    string = file.read()
    print(string)

    file.seek(6)  # 移动文件指针到新位置
    print(file.read(14))  # 读取14个字符

    # -- readline() 读取一行 --
    print('\n', '-'*10, 'readline()', '-'*10)

    num = 0
    while 1:
        num += 1
        line = file.readline()
        if line == '':
            break
        print(num, line, end='\n')

    print('\n', '='*10, 'over', '='*10)

    # -- readlines() 读取全部行 --
    print('\n', '-'*10, 'readlines()', '-'*10)

    file.seek(0)
    print(file.readlines()) #返回字符串列表
