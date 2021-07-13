#写一个函数， 可以实现帮一所大学录取考生，要求如下
#1. 函数的参数包括如下变量： 大学名称、 专业、 招生分数线、招生老师名单、 报考考生及其高考成绩
#2. 需要用到本讲所有的参数形式
#3. 给函数传参， 运行后， 需要输出如下信息：大学名称、专业、招生分数线、
#报考人数、达线人数、录取名单（分数由高到低排序）、录取人数
#知识点：list可以做切片，dictionary不好做切片，是能用键值对提取

pass_score_dic = {} #过分数线名单
pass_list = [] #最终录取名单

def enroll_list(university,major,pass_score = 550,pass_count=10,*args,**kwargs):
#args招生老师名单， ***可变参数--不确定数量
#kwargs招生考生及其高考成绩， ***可变关键字--不确定考生名字和成绩
    global pass_score_dic, pass_list  #全局变量的引用  
    if len(kwargs)>0:#首先要判断是否有报考的考生这个是第一判断，没人报考，那么一下任何逻辑没有意义
        for stu,score in kwargs.items():#包考生和分数先分开，dict的items, key和values
            if int(score)>pass_score: #判断是否高于录取分数
                pass_score_dic[stu] = int(score)  #操作列表的添加，特别注意对全局的操作，可变类型添加无需global

        #对已经过分数线的同学按照分数进行高到低排序
        dic_desc = sorted(pass_score_dic.items(), key = lambda k:k[1], reverse = True)
        print("**演示输出排序输出**：", dic_desc, "\n") #注意这里返回的结构 {a:1, C:2}  --> [(a,1), (c,2)]

        #设定取值的量 切片
        for stu_pass in dic_desc[:pass_count]: #特别注意这里告诉系统， 我要提取多少个出来pass_count是我们的录取总量
            pass_list.append(stu_pass) #符合录取条件的前XX名同学进入  最终录取名单

        print(f"学校：{university}; \n专业:{major}; \n录取分数线:{pass_score}; \n招生人数：{pass_count} \n招生老师:{args} \n考生名单及分数：{kwargs}\n报考人数:{len(kwargs)};\n达线人数:{len(pass_score_dic)}\n录取名单（分数由高到低):{pass_list};\n录取人数：{len(pass_list)}")

    else:
        print("无人报考")

enroll_list("Yale University", "Computer Science",550,3,"Mr. James","Mr.Holland","Ms.Johnson", Lucy_Reay="540",Sam_White="575",Keith_Jordan="583",Lily_van_Dam="569",Rita_Peeters="557")

