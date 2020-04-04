#!/usr/bin/env python
# coding: utf-8

# In[48]:


import cv2
import uuid 
import pyqrcode
import face_entry
import numpy as np
import mysql.connector


# In[32]:


import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 


# In[ ]:


#create database connection using myconnector
#connect database created in creat_db
face_db=mysql.connector.connect(
        host="localhost",
        user="root",
        password="xxxxx",
        database="face_db")


# In[45]:


#string representing the unique qr code
string=str(uuid.uuid1())


# In[39]:


#generate qrcode
qr=pyqrcode.create(string)


# In[59]:


#save qrcode as png file
#choose filename as username and dob 
file_name=input("Type in the QR-Code file name")
qr.png(file_name,scale=7)


# In[69]:


#sender and receiver email address
from_add="imnoorsingh@gmail.com"
to_add=input("Type in the user's email address: ")


# In[70]:


#instance of MIMEMultipart 
msg=MIMEMultipart() 
#storing the senders email address   
msg['From']=from_add  
#storing the receivers email address  
msg['To']=to_add   
# storing the subject  
msg['Subject']="Unique QR-Code Ready"
#storing the subject  
body="The QR-Code is attached to the mail. Please save it on your device."
#attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 
#open the file to be sent  
filename=file_name+".png"
attachment=open(file_name, "rb") 
#instance of MIMEBase and named as p
p=MIMEBase('application', 'octet-stream') 
#To change the payload into encoded form 
p.set_payload((attachment).read())  
#encode into base64 
encoders.encode_base64(p)   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
# attach the instance 'p' to instance 'msg' 
msg.attach(p) 
# creates SMTP session 
s=smtplib.SMTP('smtp.gmail.com', 587) 
#identify ourselves to smtp gmail client
s.ehlo()
# start TLS for security 
s.starttls()   
#re-identify ourselves as an encrypted connection
s.ehlo()
# Authentication 
s.login(from_add, "xxxxx") 
# Converts the Multipart msg into a string 
text=msg.as_string() 
# sending the mail 
s.sendmail(from_add, to_add, text) 
# terminating the session 
s.quit() 


# In[ ]:


#extract and store new face embedding
embedding=face_entry.face_embedding()


# In[ ]:


#store uniqueid and face embedding in the database
#create cursor object
mycursor=face_db.cursor()
#insert row into the table
query="INSERT INTO Registered_users (UniqueID,Embedding_Vector) VALUES (%s,%s)"
mycursor.execute(query,(string,embedding))
#commit changes
face_db.commit()


# In[ ]:


#close cursor object and database
mycursor.close()
face_db.close()

