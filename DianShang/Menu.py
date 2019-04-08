import DianShang.Manager
from DianShang.CutManagemnt import *#导入客户信息方法
from DianShang.Pay import *#导入购物管理界面
class Menu():
    def caidan(self):
        print("欢迎使用我行我素购物管理系统")
        print("*************************")
        print("1.客户信息管理\n2.购物结算\n3.注销")
        print("*************************")
        Menu.select(self)
    def select(self,):
        a=int(input("请选择，输入数字"))
        if a==1:
            q=CutManagement()
            q.jiemian()

        if a==2:
            w=Pay()
            w.jiemian()

        if a==3:
            #注销暂时没做
            s=DianShang.Manager.Manager()
            s.yemian()
# p=Menu()
# p.caidan()


