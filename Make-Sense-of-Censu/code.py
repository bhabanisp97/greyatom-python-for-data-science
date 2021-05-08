# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here
census=np.concatenate((data,new_record),axis=0)
age=np.array(census[:,0])
max_age=age.max()
print(max_age)
min_age=age.min()
print(min_age)
age_mean=age.mean()
print(age_mean)
age_std=age.std()
print(age_std)

race=np.array(census[:,2])

m_0=(race==0)
race_0=race[m_0]

m_1=(race==1)
race_1=race[m_1]

m_2=(race==2)
race_2=race[m_2]

m_3=(race==3)
race_3=race[m_3]

m_4=(race==4)
race_4=race[m_4]

len_0=len(race_0)

len_1=len(race_1)

len_2=len(race_2)

len_3=len(race_3)

len_4=len(race_4)

if len_0<len_1 and len_0<len_2 and len_0<len_3 and len_0<len_4:
    minority_race=0
elif len_1<len_0 and len_1<len_2 and len_1<len_3 and len_1<len_4:
    minority_race=1
elif len_2<len_0 and len_2<len_1 and len_2<len_3 and len_2<len_4:
    minority_race=2
elif len_3<len_0 and len_3<len_1 and len_3<len_2 and len_3<len_4:
    minority_race=3
elif len_4<len_0 and len_4<len_1 and len_4<len_2 and len_4<len_3:
    minority_race=4

print(minority_race)


senior_citizens = census[census[:,0]>60]

working_hours_sum=sum(senior_citizens[:,6])
print(working_hours_sum)

senior_citizens_len=len(senior_citizens)
print(senior_citizens_len)

avg_working_hours=(working_hours_sum/senior_citizens_len)
print(avg_working_hours)

high=census[census[:,1]>10]
low=census[census[:,1]<=10]

m=np.array(high[:,7])
avg_pay_high=m.mean()
print(avg_pay_high)

n=np.array(low[:,7])
avg_pay_low=n.mean()
print(avg_pay_low)

np.array_equal(avg_pay_high,avg_pay_low)











