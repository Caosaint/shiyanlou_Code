# 判断学生成绩是否达标，要求输入物理，数学，历史三科的成绩，总成绩小于120为不及格。
data = {}   # 用来存放每个学生的成绩数据
n = int(input("Enter the number of students: "))

# 第一部分：输入数据并存储
for i in range(0, n):
    name = input('Enter the name of the student:')
    subject_keys = ['Physics', 'Maths', 'History']  
    grades_values = []
    for x in subject_keys:
        grades_values.append(int(input("Enter the mark of {}:".format(x))))
    dictionary = dict(zip(subject_keys, grades_values)) 
    """把这名学生科目与对应成绩存在字典中，再作为值存到字典data中 """
    data[name] = dictionary

	# 第二部分：进行计算和判断
    print("{}/n".format(name))      #先输出此次记录成绩的同学名字，然后再输出其每门科目成绩和总分，并进行判断
    total = 0
    for x, y in dictionary.items():
    	print("the mark of {} is {}".format(x, y))
    	total += y
    print("{}'s total mark is {}".format(name, total))
    if total < 120:
        print(name,"failed :(")
    else:
        print(name, "passed :)")
print(data)
    
