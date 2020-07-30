import datetime

N = int(input())
name_list = []
for i in range(N):
     name = input()
     name_list.append(name)
for name in name_list:
     n_dic = {}
     for n in name:
         n_dic.update({n: name.count(n)})
     n_dic = sorted(n_dic.items(), key=lambda x: x[1], reverse=True)
     piaoliangdu = 26
     all_piaoliangdu = 0
     for key in n_dic:
         all_piaoliangdu += key[1] * piaoliangdu
         piaoliangdu -= 1
     print(all_piaoliangdu)

print(type(datetime.datetime(2020, 7, 1, 17, 20, 20)))
print(str(datetime.datetime(2020, 7, 1, 17, 20, 20)))



