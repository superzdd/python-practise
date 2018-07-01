is_num = False
while is_num == False:
    str = input('''请随便在下面打一行字试试
                   如果输入的是数字，则会结束
                   以会车结束
                    ''')
    print('你打印的内容是：\n{}'.format(str))
    is_num = str.isdigit()

print('输出数字，打印结束')

