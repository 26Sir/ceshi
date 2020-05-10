#conding=utf-8

def expectional(x,y):
    '''
    :param x:
    :param y:
    :return:
    '''
    try:
        result = x / y
    except Exception as e:
        print(e)
    else:
        print("结果是",int(result))
    finally:
        print("嘿，我在这")
#expectional(10,1)
def student(name,age,sex):
