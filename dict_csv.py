'''Question
The chief staff of the finance department has asked you to prepare the payment document for the company staff;
5 of the workers are service engineers, they earn 150k each 
The TSM earns twice as the SE
The GM earns twice as the FSM whose salary is ¾ of the TSM’s salary
The project team’s salary is 150% of engineering department’s salary
The finance team’s salary is 90% of the engineering team
The sales team earns 25% of the engineering team as basic (but there’s commission of 5% on every sales made)
The MD earns ¾ of twice the salary of the TSM and FM combined
If the sales team sold 50 million worth of product in a month,
Determine the salary of each team. Write your result to CSV '''

import csv
workers = {}
dept = ['Project Team', 'Engineering Team', 'Financial Team','Sales Team', 'Managing Director']
service_eng = 150000
tech_serv_manager = 2 * service_eng
field_serv_manager = 0.75 * tech_serv_manager
_0 = 1.5 * service_eng #project team
gen_manager = 2 * field_serv_manager
_1 = service_eng + tech_serv_manager + field_serv_manager #Engineering team
_2 = 0.9 * _1 #financial team
_3 = ((0.25 * service_eng ) + (0.05 * 50000000)) #sales team
_4 = 0.75 * (2 * (field_serv_manager + tech_serv_manager)) #managing director

for i in range(len(dept)):
    k = locals()["_" + str(i)]
    workers.update({dept[i] : k})
print(workers)

file = open('angela.csv', 'w')
my_writer = csv.writer(file)

my_writer.writerow(['DEPARTMENT', 'SALARY'])

for department in workers.keys():
    my_writer.writerow([department, workers[department]])
file.close()


