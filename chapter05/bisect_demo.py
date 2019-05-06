import bisect


inter_list = []
bisect.insort(inter_list, 3)
bisect.insort(inter_list, 3)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 5)
bisect.insort(inter_list, 1)
bisect.insort(inter_list, 6)
print(inter_list)

print(bisect.bisect_right(inter_list, 3))
