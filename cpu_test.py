import time 
list1 = []
list2 = []
start = time.time_ns()
for i in range(50000):
    stop = time.time_ns()
    list1.append(i)
    list2.append((stop-start))
file = open('cpu_test_vm.txt', 'w')
file.write(str(list2))
file.close()



