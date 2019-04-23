'''
定义一个学生类，用来形容学生
'''
# 定义一个空的类
class Student():
    #一个空类，pass代表直接路过
    #此处pass必须有
    pass

# 定义一个对象
fanfan = Student()

# 再定义一个类，用来描述听Python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    '''
    注意：
    1、这里缩进的层级；
    2、系统默认有一个self参数
    '''
    def doHomework(self):
        print("fanfan 正在写爬虫")
        return None  #return 结尾

# 实例化一个叫huanhuan的学生，是一个具体的人
huanhuan = PythonStudent()
print(huanhuan.name)
print(huanhuan.age)
# 注意成员函数的调用没有传递进入参数
huanhuan.doHomework()