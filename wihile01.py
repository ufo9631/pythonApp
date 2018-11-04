benqian=10000
year=0
while benqian<200000:
    benqian=benqian*(1+0.067)
    year+=1
    print("第{0}年拿了{1}块钱".format(year,benqian))
else:
    print("循环结束")