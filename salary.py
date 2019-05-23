#write a python program to find and display the new salary of an employee.
def find_new_salary(current_salary,job_level):
  if(job_level==3):
    new_salary=((15/100)*current_salary)+current_salary
    return new_salary    
  elif(job_level==4):
    new_salary=((7/100)*current_salary)+current_salary
    return new_salary    
  elif(job_level==5):
    new_salary=((5/100)*current_salary)+current_salary
    return new_salary    
 
    


new_salary=find_new_salary(10000,3)
print(int(new_salary))
