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
Pay2=float(input('What is your hourly pay for your second job $'))
Hours2=float(input('How many hours a week do you work for this job? '))
Job2= (Pay2 * Hours2) - (Pay2 * Hours2 * .10)
print ('Your second job weekly take-home pay is $' +str(Job2))
print('\v')

#Calculates Total Monthly pay of both jobs
MonthJob1=float(Job1) * 4
MonthJob2=float(Job2) * 4
TotalMonth= MonthJob1 + MonthJob2
print ('Your monthly take-home income including both jobs is $' +str(TotalMonth))
print('\v')

#Adds disability pay
DisabilityPay=float(input('Now please enter your VA disability pay: $'))
TotalPay= DisabilityPay + TotalMonth
print ('Your total pay for the month is: $' +str(TotalPay))
print('\v')

print ('Thank you!')