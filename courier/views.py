from django.shortcuts import render
from fuauth import User
import math
from random import shuffle

# Create your views here.
all_users = User.objects.all()

group_a = []
group_b = []
group_c = []

def divide_users(group_a, group_b, group_c):
    num_of_users = len(all_users)
    remainder_users = num_of_users%3
    users_divided_by_three = math.floor(num_of_users/3)
    group_a_total = users_divided_by_three
    group_b_total = users_divided_by_three
    group_c_total = users_divided_by_three + remainder_users
    group_b_range = group_a_total + group_b_total
    group_c_range = group_b_range + group_c_total
    # print('all_users:' + str(all_users))
    users_list = list(all_users)
    # print('users_list:' + str(users_list))
    users_list = list(all_users)
    shuffle(users_list)
    group_a = users_list[0:group_a_total]
    # print(group_a)
    group_b = users_list[group_a_total:group_b_range]
    # print(group_b)
    group_c = users_list[group_b_range:group_c_range]
    # print(group_c)
    return(group_a, group_b, group_c)


group_a, group_b, group_c = divide_users(group_a, group_b, group_c)

print(group_a, group_b, group_c)

def set_times():

