import DianShang.Menu
xinxi=[[1623,"06/22",5000],[1545,"04/8",2200]]
add=[]
class CutManagement():
    def jiemian(self):
        print("我行我素购物管理系统》》客户管理系统")
        print("***********************************")
        print("1.显示所有客户信息\n2.添加客户信息\n3.查询客户信息")
        print("***********************************")
        CutManagement.select(self)

    def show(self):
        print("我行我素购物管理系统》》客户信息管理》》显示客户信息")
        print("\n")
        print("会员号\t\t生日\t\t积分\t\t")
        print("------||-----------||---------")
        for i in xinxi:
            print("\t\t".join("%s" % id for id in i))
        CutManagement.select(self)
    def add(self):
        print("我行我素购物管理系统》》客户信息管理》》添加客户信息")
        print("\n")
        a=int(input("请输入会员号（<=4位整数）："))
        add.append(a)
        b=input("请输入会员生日（请用“/”格式输入）：")
        add.append(b)
        c=input("请输入积分：")
        add.append(c)
        xinxi.append(add)
        print(xinxi)
        print("新会员添加成功")
        CutManagement.show(self)
        CutManagement.select(self)
    def find(self):
        print("我行我素购物管理系统》》客户信息管理》》查询客户信息")
        print("\n")
        # print(xinxi)
        a = int(input("请输入要查询的客户编号"))
        b=len(xinxi)
        for i in range(0,b):
            try:
             xinxi[i].index(a)
            except:
                bool=True
            else:
                print("会员号\t\t生日\t\t积分\t\t")
                print("------||-----------||---------")
                print("\t\t".join("%s" % id for id in xinxi[i]))
                CutManagement.select(self)
                break
        if bool==True:
            print("没有该顾客,请重新输入")
            CutManagement.find(self)
    def select(self):
        a = int(input("请选择,输入数字或输入0返回上一级菜单或输入4返回主菜单"))
        if a==0:
            CutManagement.jiemian(self)
        elif a==1:
            CutManagement.show(self)
        elif a==2:
            CutManagement.add(self)
        elif a==3:
            CutManagement.find(self)
        elif a==4:
            s=DianShang.Menu.Menu()
            s.caidan()

        else:
            print("输入有误，请重新选择")
            CutManagement.jiemian(self)


# c=CutManagement()
# c.jiemian()


