# Introduction
print ('Welcome to the Pay Calculator!')
print ('This program was created by Evan')
print('\v')

#Calculates first job
print('This calculates your weekly pay for your first job')
Pay1=float(input('What is your hourly pay for your first job? $'))
Hours1=float(input('How many hours a week do you work this job? '))
Job1= (Pay1 * Hours1) - (Pay1 * Hours1 * .10)
print ('Your first job weekly take-home pay is $' +str(Job1))
print('\v')

#Calculates second job pay
Answer1=str(input('Would you like to calculate pay for a second job?'))
if Answer1 in ('Yes' ,'yes', 'yea'):
    Pay2=float(input('What is your hourly pay for your second job $'))
    Hours2=float(input('How many hours a week do you work for this job? '))
    Job2= (Pay2 * Hours2) - (Pay2 * Hours2 * .10)
    print ('Your second job weekly take-home pay is $' +str(Job2))
    print('\v')

#Calculates Total Monthly pay of both jobs
if Answer1 in ('Yes', 'yes', 'yea'):
    MonthJob1= Job1 * 4
    MonthJob2=float(Job2) * 4
    TotalMonth= MonthJob1 + MonthJob2
    print ('Your monthly take-home income for both jobs is $' +str(TotalMonth))
    print('\v')
else:
    MonthJob1=float(Job1) * 4
    print ('Your monthly take-home income for your job is $' +str(MonthJob1))
    print('\v')

#Adds disability pay
Answer2=str(input('Would you like to add any VA pay?'))
if Answer2 in ('No', 'no', 'nah'):
    print('Thank you for using this program!')
elif Answer2 in('Yes', 'yes', 'yea'):
    DisabilityPay=float(input('Now please enter your VA pay: $'))
    TotalPay= DisabilityPay + MonthJob1
    print ('Your total pay for the month is: $' +str(TotalPay))
    print('Thank you for using this program!')
