# -*- coding: utf-8 -*-
cars = 100  #车100辆
space_in_a_car = 4  # 一辆车4个位置
drivers = 30 # 司机30人
passengers = 90 # 乘客90人
cars_not_driven = cars - drivers # 没有驾驶的车＝车－司机人数
cars_driven = drivers  # 驾驶的车数＝司机人数
carpool_capacity = cars_driven * space_in_a_car # 车辆运载能力＝驾驶的车数＊一辆车上的空座
average_passengers_per_car = passengers /cars_driven # 单位车辆的平均乘客数＝乘客数／驾驶车


print "There are", cars, "cars_available."
print "There are only",drivers,"drivers available."
print "There will be", cars_not_driven,"empty cars today."
print "We can transport", carpool_capacity, "people today"
print "We have",passengers,"to carpool today."
print "We need to put about",average_passengers_per_car,"people in each car."

# 文件“ex4.py”的第8行carpool打成car_capacity,这个错误变量名没有用＝定义过，因此系统显示未定义
#Traceback (most recent call last):
#   File "ex4.py", line 8, in <module>
#   average_passengers_per_car = car_pool_capacity / passenger
#NameError: name 'car_pool_capacity' is not defined
