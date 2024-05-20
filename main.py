print("Calculate Your GPA.")

sub1 = input("please enter your first subject marks : ")
sub2 = input("please enter your second subject marks : ")
sub3 = input("please enter your third subject marks : ")
sub4 = input("please enter your fourth subject marks : ")
sub5 = input("please enter your fifth subject marks : ")
sub6 = input("please enter your sixth subject marks : ")
sub7 = input("please enter your seventh subject marks : ")

sum = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7

percentage = float(sum) / 1050

gpa = percentage / 0.25

if gpa >= 3.7:
	print("Your garde is 'A' and your gpa is : " + str(gpa))

elif gpa >= 2.7:
	print("Your garde is 'B' and your gpa is : " + str(gpa))

elif gpa >= 1.7:
	print("Your garde is 'C' and your gpa is : " + str(gpa))

elif gpa >= 1:
	print("Your garde is 'D' and your gpa is : " + str(gpa))

else :
	print("Your garde is 'F' and your gpa is : " + str(gpa))