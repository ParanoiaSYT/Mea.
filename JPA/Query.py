# 登陆
import lab
lab.login('zw','12345678')



# 查询仪器开关以及设置
rc = lab.open_resource('SGS733')
a = rc.getValue('Power')
print(a)

# 查询已有app
lab.listApps()
# 查询单个app
lab.getAppClass('NA.JPA_Spec_vs_ppower_pfreq_SYT').show()
lab.listOneApp('NA.JPA_Spec_vs_ppower_pfreq_SYT')



# 查询数据库
res=lab.query("NA.JPA_Spev_vs_ppower_pfreq_SYT")
# cou=res.count()
# print(res[cou-1].id)
print(res[-1].id)
# 打印出最近的数据

# 取出数据库数据
res=lab.query()
res.display()
x,y=res[0].data
# 绘图
import matplotlib.pyplot as plt
plt.plot(x,y)
plt.show() 