import itertools
import time

x_list = list(range(1000))
y_list = list(range(1000))

product = itertools.product(x_list, y_list)
start_time = time.time()
for x, y in product:
    pass
end_time = time.time()
print("%f[sec]" % (end_time-start_time))
# => 0.062474[sec]

start_time = time.time()
for x in x_list:
    for y in y_list:
        pass
end_time = time.time()
print("%f[sec]" % (end_time-start_time))
# => 0.015663[sec]
