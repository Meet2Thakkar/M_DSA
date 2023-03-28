from datetime import date, timedelta
import random

# initializing dates ranges
test_date1 = date(1895, 1, 1) 
test_date2 =  date(2023, 12, 31)

# printing dates
print("The original range : " + str(test_date1) + " to " + str(test_date2))

# initializing K
K = 30

res_dates = [test_date1]

# loop to get each date till end date
while test_date1 != test_date2:
	test_date1 += timedelta(days=1)
	res_dates.append(test_date1)

# random K dates from pack
res = random.choices(res_dates, k=K)

# printing
#print("K random dates in range : " + str(res))
#print(res)

birthday = []

for i in range(0,30):
	day_of_year = res[i].timetuple().tm_yday
	birthday.append(day_of_year)


birthday.sort()
for i in range(0,30):
	print(birthday[i])

print("---------------------")
for i in range(0,29):
	if (birthday[i] == birthday[i+1]):
		print(birthday[i])
		