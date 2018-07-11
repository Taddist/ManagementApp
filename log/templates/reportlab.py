from  reportlab.pdfgen import canvas 
from reportlab.lib.pagesizes import letter 
from reportlab.lib.pagesizes import landscape 
from reportlab.platypus import Image 
import csv 

data_file='data.csv'

def import_data(data_file):
	attendee_data=csv.reader(open(data_file,"rb"))
	for row in attendee_data:
			last_name=row[0]
			first_name=row[1]
			course_name=row[2]
			pfd_file_name=course_name+'_'+last_name+first_name+'.pdf'
	generate_certificate(first_name,last_name,course_name,pfd_file_name)

def generate_certificate(first_name,last_name,course_name,pfd_file_name):
	attendee_name= first_name +' '+ last_name
	c= canvas.canvas(pfd_file_name,pagesize=landscape(letter))

	#header text 
    c.setFont('Helvetica',48,leading=None)
    c.drawCentredString(415,500,"Certificate of Completion")
    c.setFront('Helvetica',24,leading=None)
    c.drawCenterString(415,450,"This certificate is presented to :")
    #attendee name
    c.setFront('Helvetica-Bold',34,leading=None)
    c.drawCentredString(415,395,attendee_name)
    # for completing the .....
    c.setFront('Helvetica',24,leading=None)
    c.drawCentredString(415,350,"for completing the following course:")
    #course name 
    c.setFront('Helvetica',20,leading=None)
    c.drawCentredString(415,310,course_name)
    #image of seal 
    seal='seal.png'
    c.drawImage(350,50,width=None,height=None)

    c.showPage() #start a new page after saving what is above 
    c.save()
	import_data(date_file)


