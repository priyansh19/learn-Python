from string import Template

student = [('Abhishek',90),('Anuj',85),('Jashan',80),('Anirban',70),('Harshit',75)]

temp = Template("$name got $marks in end term exam.")

for stu in student:
	print(temp.substitute(name = stu[0], marks = stu[1]))