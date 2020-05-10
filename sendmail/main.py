import smtplib as s 

#SMTP is an application layer protocol. 

object1=s.SMTP("smtp.gmail.com",587) 

#port adress

object1.starttls()

#Transport Layer Security

object1.login("*****@gmail.com",'***Your**password***')

#I recomond you to keep your password in another file

#do not directly embedd the password inside the script

subject='Sending email using python'

body='This is vishal'

message="subject:{}\n\n{}".format(subject,body) #formating 

listofadresses=['*list of adresses in a file*']

object1.sendmail('*user name*',listofadresses,message)

object1.quit()

print("Done....Mail sent.")
