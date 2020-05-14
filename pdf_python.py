# simple_demo.py

from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')
#adding a new page
pdf.add_page()
#Function for Bold Heading
def boldHead(str,cize):
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Arial",'B',size=cize)
    pdf.cell(15,10,txt=str, align="L")

def text_bold_head(w, h,str1, str2, ):
    x=pdf.get_string_width(str1)
    y=pdf.get_string_width(str2)
    pdf.set_font("Arial", size=12)
    pdf.cell(w,h,txt=str2,align="C")
    xc=pdf.get_x()
    yc=pdf.get_y()
    pdf.set_font("Arial", 'B', size=12)
    pdf.text(xc-(w/2)-(y/2)-x-2,yc+6.25,txt=str1)
#name
name=input("enter your name :")
pdf.set_font("Arial", 'B',size=16)
pdf.cell(200, 10, txt=name, ln=1, align="C")
#Address
str=input("enter your address : ")
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt=str, ln=1, align="C")
#Mobile No
str=input("enter your Mobile No : ")
text_bold_head(100,10,"Mobile No:", str)
#Email Id
str=input("enter your Email Id : ")
text_bold_head(100,10,"Eamil id:",str)
pdf.ln(10)
#function for header
def header(str):
    pdf.set_font("Arial", 'B',size=12)
    pdf.set_text_color(200,0,0)
    pdf.cell(200, 10, txt=str, ln=1, align="L")
    pdf.set_line_width(1)
    pdf.set_draw_color(255,80,0)
    y=pdf.get_y()
    pdf.line(7.5, y, 210-20, y)
    pdf.ln(2)
    pdf.set_line_width(1)
    pdf.set_draw_color(141, 222, 214)
    y=pdf.get_y()
    pdf.line(5, y, 210-25, y)
#Personal Profile
header("Personal Profile Statement")
str=input("enter your Personal Profile Statement : ")
pdf.set_font("Arial", size=12)
pdf.set_text_color(0,0,0)
pdf.multi_cell(200, 10, txt=str)
#Achievements
header("Achievements")
def Achievements():
  str=input("enter your Achievements : ")
  pdf.set_font("Arial", size=12)
  pdf.set_text_color(0,0,0)
  pdf.cell(10)
  pdf.cell(200, 10, txt="* "+str, ln=1, align="L")
while True:
    Achievements()
    conf=input("Do you want to enter more of your Achievements(Y/N)?")
    if conf=="N" or conf == "n":
       break
#Education
header("Education")
def Education():
    print("Educational Details")
    univ=input("enter your school/university Name : ")
    deeg=input("Enter the Degree you pursued(like B.TECH) :")
    strm=input("Enter your Stream (ex: EE,ECE):")
    srtyr=input("Enter the starting year :")
    endyr=input("enter end year :")
    cmmnt=input("Any Comment on the above education Detail")
    str=srtyr+" - "+endyr+"        "+deeg+"        "+strm+"        "+univ
    pdf.set_font("Arial", 'B',size=12)
    pdf.set_text_color(0,0,0)
    pdf.multi_cell(200, 10, txt=str)
    pdf.cell(10)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="* "+cmmnt, ln=1, align="L")
while True:
    Education()
    conf=input("Do you want to enter more of your Education Details(Y/N)?")
    if conf=="N" or conf == "n":
       break
#Employment
header("Employment")
def Employment():
    print("Employment Details")
    org=input("Enter the organization Name :")
    pos=input("Enter the position in the above organization :")
    srtyr=input("Enter the starting year of the position :")
    endyr=input("Enter the ening year of the position :")
    str=srtyr+" - "+endyr+"        "+pos+"        "+org
    pdf.set_font("Arial", 'B', size=12)
    pdf.set_text_color(0,0,0)
    pdf.cell(200, 10, txt=str, ln=1, align="L")
    def responsibility():
        str=input("Enter the responsisbilites of you at the above organization :")
        pdf.set_font("Arial", size=12)
        pdf.set_text_color(0,0,0)
        pdf.cell(10)
        pdf.cell(200, 10, txt="* "+str, ln=1, align="L")
    def responsibilities():
        while True:
            responsibility()
            conf=input("Do you want to enter more responsibilities?(Y/N)")
            if conf=="N" or conf=="n" :
                break
    responsibilities()
while True:
    Employment()
    conf=input("Do you want to enter more Employment Details?(Y/N)")
    if conf=="N" or conf=="n":
       break
#Qualifications
header("Qualifications")
def Qualification():
  str=input("enter your Qualification : ")
  pdf.set_font("Arial", size=12)
  pdf.set_text_color(0,0,0)
  pdf.cell(10)
  pdf.cell(200, 10, txt="* "+str, ln=1, align="L")
while True:
    Qualification()
    conf=input("Do you want to enter more of your Qualifications(Y/N)?")
    if conf=="N" or conf == "n":
       break
#Skills
header("Skills")
def Skill():
  str=input("enter your Skill : ")
  pdf.set_font("Arial", size=12)
  pdf.set_text_color(0,0,0)
  pdf.cell(10)
  pdf.cell(200, 10, txt="* "+str, ln=1, align="L")
while True:
    Skill()
    conf=input("Do you want to enter more of your Skills(Y/N)?")
    if conf=="N" or conf == "n":
       break
#Hobbies and Interest
header("Hobbies and Interest")
str=input("enter your Hobbies and Interest : ")
pdf.set_font("Arial", size=12)
pdf.set_text_color(0,0,0)
pdf.multi_cell(200, 10, txt=str)
#References
header("References")
num=input("How many References you would want to enter?(Max 2)")
def References():
    refName=input("enter the name of your Reference : ")
    refPos=input("Enter the position of the Refere :")
    refOrg=input("Enter the organization of the Refere :")
    refAddr=input("Enter the Address of the Refere :")
    refTelNo=input("Enter the Tel No of the Refere :")
    refEmail=input("Enter the Email Id of the Refere :")
    ref=[refName,refPos, refOrg, refAddr,refTelNo, refEmail]
    return ref
ref=[None, None]
i=0
while True:
    i+=1
    print(f"Details of {i} Reference")
    str=References()
    ref[i-1]=str
    if i==int(num):
        break
if int(num)<=1:
    ref[1]=[" "," "," "," "," "," "]
print(ref)
def refPrint():
    #name of the Reference
    pdf.set_font("Arial", 'B', size=12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(100,10, txt=ref[0][0], align="L")
    pdf.cell(100,10, txt=ref[1][0], align="L")
    pdf.ln(5)
    #position of the Reference
    pdf.set_font("Arial", size=12)
    pdf.cell(100,10, txt=ref[0][1], align="L")
    pdf.cell(100, 10, txt=ref[1][1], align="L")
    pdf.ln(5)
    #Company of the Reference
    pdf.cell(100,10, txt=ref[0][2], align="L")
    pdf.cell(100, 10, txt=ref[1][2], align="L")
    pdf.ln(5)
    #address of the Reference
    boldHead("Addr :",12)
    pdf.set_font("Arial", size=12)
    pdf.cell(85,10, txt=ref[0][3], align="L")
    if int(num)>1:
        boldHead("Addr :",12)
        pdf.set_font("Arial", size=12)
        pdf.cell(85, 10, txt=ref[1][3],  align="L")
    pdf.ln(5)
    #tel num of the Reference
    boldHead("Tel :",12)
    pdf.set_font("Arial", size=12)
    pdf.cell(85,10, txt=ref[0][4], align="L")
    if int(num)>1:
        boldHead("Tel :",12)
        pdf.set_font("Arial", size=12)
        pdf.cell(85, 10, txt=ref[1][4],  align="L")
    pdf.ln(5)
    #Email id of the Reference
    boldHead("Email :",12)
    pdf.set_font("Arial", size=12)
    pdf.set_text_color(0,0, 255)
    pdf.cell(85,10, txt=ref[0][5], align="L", link="mailto:"+ref[0][5])
    if int(num)>1:
        boldHead("Email :",12)
        pdf.set_font("Arial", size=12)
        pdf.set_text_color(0,0, 255)
        pdf.cell(85, 10, txt=ref[1][5], ln=1, align="L", link="mailto:"+ref[1][5])
refPrint()
str=name+"_cv.pdf"
pdf.output(str)
