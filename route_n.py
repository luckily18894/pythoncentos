
import os

route_n_result = os.popen("route -n").read()  # 执行并返回命令的结果
print(route_n_result)

l1 = route_n_result.split('\n')
print(l1)

for a in l1:
    if a == '':
        pass
    elif a.split()[3] == 'UG':
        print('网关为：', a.split()[1])



if __name__ == '__main__':
