factor = [100/383,222/883,237/928,236/946,186/736,166/660,147/581,121/482,204/807]
av = 0
for i in factor :
	av += i
av /= len(factor)
print(av)
print(1-av)
print(int(807*av))