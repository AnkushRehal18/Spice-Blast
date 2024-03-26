import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


from datetime import datetime, date

# Open the file in read mode
with open('credentials.txt', 'r') as file:
    content = file.readlines()

# Initialize variables
number = None
date_obj = None
current_date = date.today()

# Iterate through each line
for line in content:
    # Split each line into key and value
    parts = line.split('=')

    # Check if there are at least two parts (key and value)
    if len(parts) >= 2:
        # Extract key and value, and strip whitespaces
        key = parts[0].strip()
        value = parts[1].strip()

        # Check if the key is "number"
        if key == 'number':
            number = int(value)
        elif key == 'date':
            try:
                # Attempt to convert string to datetime.date
                date_obj = datetime.strptime(value, "%Y-%m-%d").date()
            except ValueError:
                print(f"Error parsing date: {value}. Check the date format.")

# Check if both 'number' and 'date' were successfully obtained
if number is not None and date_obj is not None:
    pass
    # def new_calculations():
    #     if date_obj >= current_date and number >= 7:
    #         table_not_booked = "your table cannot be booked"
    #         print(table_not_booked)
    #     else:
    #         table_booked = "your table is booked"
    #         print(table_booked)

    # new_calculations()
else:
    print("Error: 'number' or 'date' not found in the file.")


def email(subject , body , to_email):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "ankush234323@gmail.com"
    smtp_password = "nuzb bqox szta mddc"

    msg = MIMEMultipart()
    msg['From'] = "smtp_username"
    msg['to'] = "to_email"
    msg['subject'] = "subject"

    msg.attach(MIMEText(body,'plain'))

    with smtplib.SMTP("smtp.gmail.com" , 587) as server:
        server.starttls()
        server.login(smtp_username,smtp_password)
        server.sendmail(smtp_username,to_email,msg.as_string())

try:
    if date_obj >= current_date and number >= 7:
            table_not_booked = "your table cannot be booked"
            print(table_not_booked)
            with open("table data.txt",'w') as tablefile:
                tablefile.write( table_not_booked)

    else:
        table_booked = "your table is booked"
        print(table_booked)
        with open("table data.txt",'w') as tablefile:
            tablefile.write(table_booked)

except Exception as e:
    print(e)

with open("credentials.txt",'r') as file:
   content =  file.readline()

with open('table data.txt','r') as data_to_be_send:
    info = data_to_be_send.readline()


new = content.split(" = ")
print(new[1])
subject = "market email"
body = info
to_email = new[1]

try:
    email(subject,body , to_email)
    print("Emaill sent succesfully")

except Exception as e:
    print(e)
    