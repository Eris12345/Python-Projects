from tkinter import *
import random
import time
import datetime

payroll = Tk()
payroll.geometry("1350x650+0+0")
payroll.title("Payroll Management System")

def Exit():
    payroll.destroy()

def PayRef():
    PayDate.set(time.strftime("%d/%m/%Y"))
    #PayDate.set(time.strftime("%x"))
    Refpay =  random.randint(20000,709467)
    Refpaid = str(Refpay)
    Reference.set("PR"+Refpaid)
    NIpay = random.randint(2487, 9467)
    NIpaid = str(NIpay)
    NINumber.set("NI" + NIpaid)

def PayPeriod():
    i = datetime.datetime.now()
    TaxPeriod.set(i.month)

    NIcod = random.randint(2487, 9467)
    NIc = str("NICode"+ str(NIcod))
    NICode.set(NIc)

def MonthlySalary():
     BS = float(BasicSalary.get())
     CW = float(cityWeighting.get())
     OT = float(OverTime.get())

     MTax = "$" + "{:.2f}".format((BS+CW+OT)*0.02)
     Tax.set(MTax)


     M_Pension = "$" + "{:.2f}".format((BS + CW + OT) * 0.029)
     Pension.set(M_Pension)

     M_StuLoan = "$" + "{:.2f}".format((BS + CW + OT) * 0.012)
     StudentLoan.set(M_StuLoan)

     M_NIpay = "$" + "{:.2f}".format((BS + CW + OT) * 0.011)
     NIPayment.set(M_NIpay)

     Ded = (BS+CW+OT)*0.02 + (BS + CW + OT) * 0.029 + (BS+CW+OT)*0.012 + (BS + CW + OT) * 0.011
     Deduc = "$" + "{:.2f}".format((BS+CW+OT)*0.02 + (BS + CW + OT) * 0.029 + (BS+CW+OT)*0.012 + (BS + CW + OT) * 0.011)
     Deductions.set(Deduc)

     Gross_Pay = "$" + "{:.2f}".format(BS+CW+OT)
     GrossPay.set(Gross_Pay)

     Net = "$" + "{:.2f}".format((BS+CW+OT)-Ded)
     NetPay.set(Net)

     TaxablePay.set("0.00")
     PensionablePay.set("0.00")
     OtheePaymentDue.set("0.00")


def Reset():
    EmployeeName.set("")
    Adress.set("")
    Reference.set("")
    EmployerName.set("")
    cityWeighting.set("")
    BasicSalary.set("")
    OverTime.set("")
    GrossPay.set("")
    NetPay.set("")
    Tax.set("")
    Pension.set("")
    StudentLoan.set("")
    NIPayment.set("")
    Deductions.set("")
    PostCode.set("")
    Gender.set("")
    PayDate.set("")
    TaxPeriod.set("")
    NINumber.set("")
    NICode.set("")
    TaxablePay.set("")
    PensionablePay.set("")
    OtheePaymentDue.set("")



EmployeeName = StringVar()
Adress = StringVar()
Reference =StringVar()
EmployerName=StringVar()
cityWeighting=StringVar()
BasicSalary =StringVar()
OverTime =StringVar()
GrossPay =StringVar()
NetPay = StringVar()
Tax =StringVar()
Pension =StringVar()
StudentLoan =StringVar()
NIPayment =StringVar()
Deductions =StringVar()
PostCode =StringVar()
Gender =StringVar()
PayDate =StringVar()
TaxPeriod =StringVar()
NINumber =StringVar()
NICode =StringVar()
TaxablePay =StringVar()
PensionablePay =StringVar()
OtheePaymentDue = StringVar()


Tops = Frame(payroll, width = 1350,height = 50,bd = 16, relief = "raise" )
Tops.pack(side=TOP)

LF = Frame(payroll, width = 700,height = 650,bd = 16, relief = "raise" )
LF.pack(side=LEFT)

RF = Frame(payroll, width = 600,height = 650,bd = 16, relief = "raise" )
RF.pack(side=RIGHT)

lblInfo=Label(Tops,font=('arial',50,'bold'),text="Payroll Management System",fg="Steel Blue", bd=10,anchor='w')
lblInfo.grid(row=0,column=0)


LEFTinsideLF = Frame(LF, width = 700,height = 100,bd = 8, relief = "raise")
LEFTinsideLF.pack(side=TOP)
LEFTinsideLFLF = Frame(LF, width = 325,height = 400,bd = 8, relief = "raise")
LEFTinsideLFLF.pack(side=LEFT)
LEFTinsideRFRF = Frame(LF, width = 325,height = 400,bd = 8, relief = "raise")
LEFTinsideRFRF.pack(side=RIGHT)


RIGHTinsideLF = Frame(RF, width = 600,height = 200,bd = 8, relief = "raise")
RIGHTinsideLF.pack(side=TOP)
RIGHTinsideLFLF = Frame(RF, width = 300,height = 400,bd = 8, relief = "raise")
RIGHTinsideLFLF.pack(side=LEFT)
RIGHTinsideRFRF = Frame(RF, width = 300,height = 400,bd = 8, relief = "raise")
RIGHTinsideRFRF.pack(side=RIGHT)

#======================================================= Sol Kısım ==============================================

lblEmployeeName=Label(LEFTinsideLF,font=('arial',12,'bold'),text="Employee Name",fg="Steel Blue", bd=10,anchor='w')
lblEmployeeName.grid(row=0,column=0)
txtEmployeeName = Entry(LEFTinsideLF,font=('arial',12,'bold'),bd=20,width=54,bg="powder blue", justify = "right"
                        ,textvariable = EmployeeName)
txtEmployeeName.grid(row=0,column=1)


lblAddress=Label(LEFTinsideLF,font=('arial',12,'bold'),text="Adress",fg="Steel Blue", bd=10,anchor='w')
lblAddress.grid(row=1,column=0)
txtAddress = Entry(LEFTinsideLF,font=('arial',12,'bold'),bd=20,width=54,bg="powder blue",
                   justify = "right",textvariable = Adress)
txtAddress.grid(row=1,column=1)

lblReference=Label(LEFTinsideLF,font=('arial',12,'bold'),text="Reference",fg="Steel Blue", bd=10,anchor='w')
lblReference.grid(row=2,column=0)
txtReference = Entry(LEFTinsideLF,font=('arial',12,'bold'),bd=20,width=54,bg="powder blue",
                     justify = "right",textvariable = Reference)
txtReference.grid(row=2,column=1)


lblEmployerName=Label(LEFTinsideLF,font=('arial',12,'bold'),text="Employer Name",fg="Steel Blue", bd=10,anchor='w')
lblEmployerName.grid(row=3,column=0)
txtEmployerName = Entry(LEFTinsideLF,font=('arial',12,'bold'),bd=20,width=54,bg="powder blue",
                        justify = "right",textvariable = EmployerName)
txtEmployerName.grid(row=3,column=1)

#============================================ Sol Sol Kısım ====================================================

lblCity=Label(LEFTinsideLFLF,font=('arial',12,'bold'),text="City Weighting",fg="Steel Blue", bd=10,anchor='w')
lblCity.grid(row=0,column=0)
txtCity = Entry(LEFTinsideLFLF,font=('arial',12,'bold'),bd=10,width=18,bg="powder blue",
                justify = "right",textvariable = cityWeighting)
txtCity.grid(row=0,column=1)

lblBasicSalary=Label(LEFTinsideLFLF,font=('arial',12,'bold'),text="Basic Salary",fg="Steel Blue", bd=10,anchor='w')
lblBasicSalary.grid(row=1,column=0)
txtBasicSalary = Entry(LEFTinsideLFLF,font=('arial',12,'bold'),bd=10,width=18,bg="powder blue",
                       justify = "right",textvariable = BasicSalary)
txtBasicSalary.grid(row=1,column=1)

lblOverTime=Label(LEFTinsideLFLF,font=('arial',12,'bold'),text="Over Time",fg="Steel Blue", bd=10,anchor='w')
lblOverTime.grid(row=2,column=0)
txtOverTime = Entry(LEFTinsideLFLF,font=('arial',12,'bold'),bd=10,width=18,bg="powder blue",
                    justify = "right",textvariable = OverTime)
txtOverTime.grid(row=2,column=1)

lblGrossPay=Label(LEFTinsideLFLF,font=('arial',12,'bold'),text="Gross Pay",fg="Steel Blue", bd=10,anchor='w')
lblGrossPay.grid(row=3,column=0)
txtGrossPay = Entry(LEFTinsideLFLF,font=('arial',12,'bold'),bd=10,width=18,bg="powder blue",
                    justify = "right",textvariable = GrossPay)
txtGrossPay.grid(row=3,column=1)

lblNetPayment=Label(LEFTinsideLFLF,font=('arial',12,'bold'),text="NetPay ment",fg="Steel Blue", bd=10,anchor='w')
lblNetPayment.grid(row=4,column=0)
txtNetPayment = Entry(LEFTinsideLFLF,font=('arial',12,'bold'),bd=10,width=18,bg="powder blue",
                      justify = "right",textvariable = NetPay)
txtNetPayment.grid(row=4,column=1)

#============================================ Sol Sağ Kısım ====================================================

lblTax=Label(LEFTinsideRFRF,font=('arial',12,'bold'),text="Tax",fg="Steel Blue", bd=10,anchor='w')
lblTax.grid(row=0,column=0)
txtTax = Entry(LEFTinsideRFRF,font=('arial',12,'bold'),bd=10,width=18,bg="powder blue",
               justify = "right" ,textvariable = Tax)
txtTax.grid(row=0,column=1)

lblPension=Label(LEFTinsideRFRF,font=('arial',12,'bold'),text="Pension",fg="Steel Blue", bd=10,anchor='w')
lblPension.grid(row=1,column=0)
txtPension = Entry(LEFTinsideRFRF,font=('arial',12,'bold'),bd=10,width=18,bg="powder blue",
                   justify = "right" ,textvariable = Pension)
txtPension.grid(row=1,column=1)

lblStudentLoan=Label(LEFTinsideRFRF,font=('arial',12,'bold'),text="Student Loan",fg="Steel Blue", bd=10,anchor='w')
lblStudentLoan.grid(row=2,column=0)
txtStudentLoan = Entry(LEFTinsideRFRF,font=('arial',12,'bold'),bd=10,width=18,bg="powder blue",
                       justify = "right" ,textvariable = StudentLoan)
txtStudentLoan.grid(row=2,column=1)

lblNIPayment=Label(LEFTinsideRFRF,font=('arial',12,'bold'),text="NI Payment",fg="Steel Blue", bd=10,anchor='w')
lblNIPayment.grid(row=3,column=0)
txtNIPayment = Entry(LEFTinsideRFRF,font=('arial',12,'bold'),bd=10,width=18,bg="powder blue",
                     justify = "right" ,textvariable = NIPayment)
txtNIPayment.grid(row=3,column=1)

lblDeductions=Label(LEFTinsideRFRF,font=('arial',12,'bold'),text="Deductions",fg="Steel Blue", bd=10,anchor='w')
lblDeductions.grid(row=4,column=0)
txtDeductions = Entry(LEFTinsideRFRF,font=('arial',12,'bold'),bd=10,width=18,bg="powder blue",
                      justify = "right" ,textvariable = Deductions)
txtDeductions.grid(row=4,column=1)




#======================================================= Sağ Kısım ==============================================

lblPostCode=Label(RIGHTinsideLF,font=('arial',12,'bold'),text="Post Code",fg="Steel Blue", bd=10,anchor='w')
lblPostCode.grid(row=0,column=0)
txtPostCode = Entry(RIGHTinsideLF,font=('arial',12,'bold'),bd=20,width=48,bg="powder blue",
                    justify = "right" ,textvariable = PostCode)
txtPostCode.grid(row=0,column=1)


lblGender=Label(RIGHTinsideLF,font=('arial',12,'bold'),text="Gender",fg="Steel Blue", bd=10,anchor='w')
lblGender.grid(row=1,column=0)
txtGender = Entry(RIGHTinsideLF,font=('arial',12,'bold'),bd=20,width=48,bg="powder blue",
                  justify = "right" ,textvariable = Gender)
txtGender.grid(row=1,column=1)


#======================================================= Sol iç Kısım ==============================================

lblPayDate=Label(RIGHTinsideLFLF,font=('arial',12,'bold'),text="PayDate",fg="Steel Blue", bd=10,anchor='w')
lblPayDate.grid(row=0,column=0)
txtPayDate = Entry(RIGHTinsideLFLF,font=('arial',12,'bold'),bd=10,width=18,bg="powder blue",
                   justify = "left" ,textvariable = PayDate)
txtPayDate.grid(row=0,column=1)

lblTaxPeriod=Label(RIGHTinsideLFLF,font=('arial',12,'bold'),text="Tax Period",fg="Steel Blue", bd=10,anchor='w')
lblTaxPeriod.grid(row=1,column=0)
txtTaxPeriod = Entry(RIGHTinsideLFLF,font=('arial',12,'bold'),bd=10,width=18,bg="powder blue",
                     justify = "left" ,textvariable = TaxPeriod)
txtTaxPeriod.grid(row=1,column=1)

lblNINumber=Label(RIGHTinsideLFLF,font=('arial',12,'bold'),text="NI Number",fg="Steel Blue", bd=10,anchor='w')
lblNINumber.grid(row=2,column=0)
txtNINumber = Entry(RIGHTinsideLFLF,font=('arial',12,'bold'),bd=10,width=18,bg="powder blue",
                    justify = "left" ,textvariable = NINumber)
txtNINumber.grid(row=2,column=1)

lblNICode=Label(RIGHTinsideLFLF,font=('arial',12,'bold'),text="NI Code",fg="Steel Blue", bd=10,anchor='w')
lblNICode.grid(row=3,column=0)
txtNICode = Entry(RIGHTinsideLFLF,font=('arial',12,'bold'),bd=10,width=18,bg="powder blue",
                  justify = "left" ,textvariable = NICode)
txtNICode.grid(row=3,column=1)

lblTaxablePay=Label(RIGHTinsideLFLF,font=('arial',12,'bold'),text="Taxable Pay",fg="Steel Blue", bd=10,anchor='w')
lblTaxablePay.grid(row=4,column=0)
txtTaxablePay = Entry(RIGHTinsideLFLF,font=('arial',12,'bold'),bd=10,width=18,bg="powder blue",
                      justify = "left" ,textvariable = TaxablePay)
txtTaxablePay.grid(row=4,column=1)

lblPensionablePay=Label(RIGHTinsideLFLF,font=('arial',12,'bold'),text="Pensionable Pay",fg="Steel Blue", bd=10,anchor='w')
lblPensionablePay.grid(row=5,column=0)
txtPensionablePay= Entry(RIGHTinsideLFLF,font=('arial',12,'bold'),bd=10,width=18,bg="powder blue",
                         justify = "left" ,textvariable = PensionablePay)
txtPensionablePay.grid(row=5,column=1)

lblOtherPaymentDue=Label(RIGHTinsideLFLF,font=('arial',12,'bold'),text="Other Payment Due",fg="Steel Blue", bd=10,anchor='w')
lblOtherPaymentDue.grid(row=6,column=0)
txtOtherPaymentDue= Entry(RIGHTinsideLFLF,font=('arial',12,'bold'),bd=10,width=18,bg="powder blue",
                          justify = "left" ,textvariable = OtheePaymentDue)
txtOtherPaymentDue.grid(row=6,column=1)



btnWagePayment = Button(RIGHTinsideRFRF,padx=8,bd=8,fg = "black", font=('arial',12,'bold'),width=14,
                        text="Wage Payment", bg = "sky blue",command=MonthlySalary).grid(row=0,column=0)

btnReset = Button(RIGHTinsideRFRF,padx=8,bd=8,fg = "black", font=('arial',12,'bold'),width=14,
                        text="Reset", bg = "sky blue", command = Reset).grid(row=1,column=0)

btnPayRef = Button(RIGHTinsideRFRF,padx=8,bd=8,fg = "black", font=('arial',12,'bold'),width=14,
                        text="Pay Reference", bg = "sky blue",command = PayRef).grid(row=2,column=0)

btnPayCode = Button(RIGHTinsideRFRF,padx=8,bd=8,fg = "black", font=('arial',12,'bold'),width=14,
                        text="Pay Code", bg = "sky blue",command =  PayPeriod).grid(row=3,column=0)

btnExit = Button(RIGHTinsideRFRF,padx=8,bd=8,fg = "black", font=('arial',12,'bold'),width=14,
                        text="Exit", bg = "sky blue", command = Exit).grid(row=4,column=0)






payroll.mainloop()
