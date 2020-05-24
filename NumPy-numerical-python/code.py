# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
data=np.genfromtxt(path,delimiter=",",skip_header=1)
census=np.concatenate((list(data),new_record))


#Code starts here



# --------------
#Code starts here
import numpy as np
age=census[:,0]

max_age=age.max()
min_age=age.min()
n=census.shape[0]

age_mean=round((age.sum()/n),2)

y=age-age_mean

age_std=round(np.sqrt(((y*y).sum()/n)),2)



# --------------
#Code starts here
race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]


len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
lis=[len_0,len_1,len_2,len_3,len_4]

minority_race=lis.index(min(lis))
# print(minority_race)

# print(race_0)
# print(race_1)
# print(race_2)
# print(race_3)
# print(race_4)

# print(len_0)
# print(len_1)
# print(len_2)
# print(len_3)
# print(len_4)





# --------------
#Code starts here
senior_citizens=census[census[:,0]>60]
# print(senior_citizens)
working_hours_sum=sum(senior_citizens[:,6])
# print(working_hours_sum)
senior_citizens_len=len(senior_citizens)
# print(senior_citizens_len)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
import numpy
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
avg_pay_high=numpy.mean(high[:,7])
avg_pay_low=numpy.mean(low[:,7])



