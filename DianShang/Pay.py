import DianShang.Menu
xinxi=[[1623,"06/22",10000],[1545,"04/8",5000]]
product=[["addidas运动鞋","￥880.0"],["addidasT恤","￥420.78"],["耐克运动鞋","￥900.0."]]
bool=True
bianhao=[]#用于输出多次购买的商品编号
class Pay():
    def jiemian(self):
        print("我行我素购物管理系统》》购物结算\n************************************")
        print("请选择购买的商品编号:\n1: addidas运动鞋\n2:addidasT恤\n3:耐克运动鞋")
        Pay.shuru(self)
    def shuru(self):
        sum=0
        a=int(input("请输入会员号："))
        b = len(xinxi)
        for i in range(0, b):
            try:
                xinxi[i].index(a)
            except:
                # bool=False
                pass
            else:
                jifen=xinxi[i][2]#该会员的积分
                print("你卡内有积分",jifen)
            break
        # if bool==False :
        #     print("输入有误,请重新输入")
        #     p.shuru()
        while bool==True:
            b=int(input("请输入商品编号"))
            c=int(input("请输入购买数量"))
            d=input("是否继续y/n")
            bianhao.append(b)
            if d=="n":
                print("**********************消费清单******************")
                print("物品\t\t\t\t单价\t\t个数\t\t金额\t\t\t")
                for m in bianhao :
                    if m==1:
                        product[0].append(c)
                        e=c*880.0
                        product[0].append(e)
                        print("\t\t".join("%s" % id for id in product[0]))
                    if m == 2:
                        product[1].append(c)
                        e = c * 420.78
                        product[1].append(e)
                        print("\t\t".join("%s" % id for id in product[1]))
                    if m==3:
                        product[2].append(c)
                        e = c * 900
                        product[2].append(e)
                        print("\t\t".join("%s" % id for id in product[2]))
                    sum+=e
                code=int(sum/10)#获得的积分
                if jifen+code>=15000:
                    o=0.7
                elif jifen+code>=8000:
                    o=0.8
                elif jifen+code>=5000:
                    o=0.9
                else:
                    o=0
                print("折扣：",o)
                print("金额总计￥",sum*o)
                zhifu=int(input("实际缴费:￥"))
                print("找钱:￥",zhifu-sum)
                print("此次获得的积分为：",code)
                g=int(input("输入0返回主菜单"))
                if g==0:
                    s=DianShang.Menu.Menu()
                    s.caidan()

# p=Pay()
# p.shuru()