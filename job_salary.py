import matplotlib.pyplot as pt
import csv

with open("job_salary.csv",'r') as file:
  csv_reader = csv.reader(file)
  #for i in csv_reader:
  x = []
  y = []
  next(csv_reader)
         
  for i in csv_reader:
      x.append(i[0])
      y.append(int(i[4]))
           
         
pt.bar(x,y)
pt.title("work year vs salary")   

pt.xlabel("work year")
pt.ylabel("salary") 
pt.legend()        
pt.show()