from DianShang.Menu import *
class Manager():
    def yemian(self):
        print("**********欢迎登录京东电子商城购物系统***********")
        print("1.登录系统")
        print("2.退出")
        a=int(input("请选择，输入数字"))
        if a==1:
            Manager.puanduan(self)
        elif a==2:
            exit()
        else:
            print("输入有误,请重新登录")
            Manager.yemian(self)
    def puanduan(self):
        str=input("请输入用户名：")
        str1=input("请输入密码：")
        if str=="admin" and str1=="0000":
            s=Menu
            s.caidan(self)#调用主菜单页面
        else:
            print("请输入正确账号和密码")
            Manager.puanduan(self)

# p=Manager()
# p.yemian()



