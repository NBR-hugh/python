# -*- coding:utf-8 -*-

# BE 00
print "  BE 00"

cars = 100  #车100辆
space_in_a_car = 4.0  # 一辆车4个位置
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


#SK

#00 解释错误信息
print "  SK00:变量名未定义,即参与运算的变量还未被定义赋值"

#01 'space_in_a_car' = 4.0 是否有必要,定义为4会有什么问题?
print "  SK01:有必要,因为求单位车辆平均乘客数 'average_passengers_per_car' 有可能除不尽,会涉及小数."

#02 浮点数的意思:小数

#03 每行变量定义添加注释
