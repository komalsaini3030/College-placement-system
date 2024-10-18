from django.shortcuts import render,redirect
from .models import*
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.db import connection
import datetime
from django.db.models import Q
from datetime import date
import simplejson as json
import json
from django.http import JsonResponse
from django.db.models import Count
import pickle
import numpy as np
from datetime import date
import pandas as pd
from matplotlib import pyplot as mp
'''from CampusPlacement.AppCampusPlacement.models import Student_Details
# Create your views here.
 


	return render(request,'pie_chart.html',{'labels':labels,'data':data})'''

def news(request):
	return render(request,'news.html',{})



def home(request):
	today = date.today()
	print("Today's date:", today)
	'''cursor = connection.cursor()
				test = "SELECT *  FROM CompanyDetails WHERE '"+str(today)+"' between Pre_Placement and Interview_Date";
				cursor = connection.cursor()
				cursor.execute(test)
				details = cursor.fetchall()'''
	
	
	details = CompanyDetails11.objects.filter(Pre_Placement__gt=today, Interview_Date__gt=today).order_by('Pre_Placement')
	print(details)
	'''if CompanyDetails.objects.all().filter(Test_Date__month=month):
					date1 = CompanyDetails.objects.all().filter(Test_Date__month=month)
					print(date1)
					for i in date1:
						a = i.CompanyName
						data2.append(a)
						print(a)
						b = i.Package
						data2.append(b)
						print(b)
				print(data2)
				details = CompanyDetails.objects.filter(Q(Test_Date__month=month) or Q(Pre_Placement__month=month) or Q(Interview_Date__month=month))
				print(details) 
				data = []
				 #CompanyDetails.objects.filter(Test_Date__month=month).filter(Pre_Placement__month=month).filter(Interview_Date__month=month)
				# details = CompanyDetails.objects.all()
				for i in details:
			
					print(i)	
					# print(details)'''
	return render(request,'home.html',{'details':details})

def base(request):
	return render(request,'base.html',{})

def index(request):
	return render(request,'index.html',{})

def index1(request):
	return render(request,'index1.html',{})

def Logins(request):
	return render(request,'Logins.html',{})

def AdminLogin(request):
	if request.method == "POST":
		A_username = request.POST['A_name']
		A_password = request.POST['A_pwds']
		if admindata.objects.filter(Username = A_username,Password = A_password).exists():
			ad = admindata.objects.get(Username=A_username, Password=A_password)
			print('d')
			messages.info(request,'Your login is Sucessfull')
			request.session['type_id'] = 'Admin'
			request.session['UserType'] = 'Admin'
			request.session['login'] = "Yes"
			return redirect("/home")
		else:
			print('y')
			messages.error(request, 'Error wrong username/password')
	else:
		return render(request, "Adminlogin.html", {})
	return render(request,'AdminLogin.html',{})

def College_Login(request):
	if request.method == "POST":
		A_username = request.POST['A_name']
		A_password = request.POST['A_pwds']
		if CollegeLogin.objects.filter(username = A_username,password = A_password).exists():
			ad = CollegeLogin.objects.get(username=A_username, password=A_password)
			print('d')
			messages.info(request,'Your login is Sucessfull')
			request.session['type_id'] = 'College'
			request.session['UserType'] = 'College'
			request.session['login'] = "Yes"
			return redirect("/home")
		else:
			print('y')
			messages.error(request, 'Error wrong username/password')
	else:
		return render(request, "College_Login.html", {})
	return render(request,'College_Login.html',{})


def Logout(request):
	Session.objects.all().delete()
	return redirect('/')

def ManageCompany(request):

	return render(request,'ManageCompany.html',{})

def AddCompany(request):
	if request.method == "POST":
		CompanyName = request.POST['CompanyName']
		Package = request.POST['pack']
		File = request.FILES['File']
		Pre_Placement = request.POST['Pre_Placement']
		Test_Date = request.POST['Test_Date']
		Interview_Date = request.POST['Interview_Date']
		Additional_Information = request.POST['Additional_Information']
		CGPA = request.POST['CGPA']
		check = request.POST.getlist('checks[]')
		print(check)
		'''for i in check:
								    if i == 'CSl':
								    	CSl = 'CSl'
								    else:
								    	CSl = 'Null'
								    if i == 'IS':
								    	IS = 'IS'
								    else:
								    	IS = 'Null'
								    if i == 'ECE':
								    	ECE = 'ECE'
								    else:
								    	ECE = 'Null'
								    if i == 'EEE':
								    	EEE = 'EEE'
								    else:
								    	EEE = 'Null'
								    if i == 'MECH':
								    	MECH = 'MECH'
								    else:
								    	MECH = 'Null'
								    if i == 'IP':
								    	IP = 'IP'
								    else:
								    	IP = 'Null'
								    if i == 'CIVIL':
								    	CIVIL = 'CIVIL'
								    else:
								    	CIVIL = 'Null'
								    if i == 'ALL_BRANCHES':
								    	ALL_BRANCHES = 'ALL_BRANCHES'
								    else:
								    	ALL_BRANCHES = 'Null'
								    print(i)
						'''



		'''IS = request.POST['IS']
		ECE = request.POST['ECE']
		EEE = request.POST['EEE']
		MECH = request.POST['MECH']
		IP = request.POST['IP']
		CIVIL = request.POST['CIVIL']
		ALL_BRANCHES = request.POST['ALL_BRANCHES']CSl=CSl,IS=IS,ECE=ECE,EEE=EEE,MECH=MECH,IP=IP,
CIVIL=CIVIL,ALL_BRANCHES=ALL_BRANCHES,'''
		OTHERS = request.POST['Others']
		CATEGORY = request.POST['CATEGORY']
		#check.append('test')
		checks = ",".join(str(x) for x in check)
		print(type(checks))
		'''jsonDec = json.decoder.JSONDecoder()
								myPythonList = jsonDec.decode(check)
								print(myPythonList)'''

		'''checks = json.dumps(check)
								print(checks)'''
		if CATEGORY == "MASS":
			Category_Number = 1
			data = CompanyDetails11(CompanyName=CompanyName,Package=Package,File=File,Pre_Placement=Pre_Placement,Test_Date=Test_Date,Interview_Date=Interview_Date,Additional_Information=Additional_Information,CGPA=CGPA,Stream = checks +','+'test',OTHERS=OTHERS,CATEGORY=CATEGORY,Category_Number = Category_Number)
			data.save()
		if CATEGORY == "CORE":
			Category_Number = 2
			data = CompanyDetails11(CompanyName=CompanyName,Package=Package,File=File,Pre_Placement=Pre_Placement,Test_Date=Test_Date,Interview_Date=Interview_Date,Additional_Information=Additional_Information,CGPA=CGPA,Stream = checks +','+'test',OTHERS=OTHERS,CATEGORY=CATEGORY,Category_Number = Category_Number)
			data.save()
		if CATEGORY == "DREAM":
			Category_Number = 3
			data = CompanyDetails11(CompanyName=CompanyName,Package=Package,File=File,Pre_Placement=Pre_Placement,Test_Date=Test_Date,Interview_Date=Interview_Date,Additional_Information=Additional_Information,CGPA=CGPA,Stream = checks +','+'test',OTHERS=OTHERS,CATEGORY=CATEGORY,Category_Number = Category_Number)
			data.save()
		if CATEGORY == "OPENDREAM":
			Category_Number = 4
			data = CompanyDetails11(CompanyName=CompanyName,Package=Package,File=File,Pre_Placement=Pre_Placement,Test_Date=Test_Date,Interview_Date=Interview_Date,Additional_Information=Additional_Information,CGPA=CGPA,Stream = checks +','+'test',OTHERS=OTHERS,CATEGORY=CATEGORY,Category_Number = Category_Number)
			data.save()



			
		return render(request,'AddCompany.html',{})
	else:
		return render(request,'AddCompany.html',{})


def DisplayStudent(request):
	cursor = connection.cursor()
	cursor.execute("Select Student_Details.id,Student_Details.Name,Student_Details.USN,Student_Details.Date_of_Birth,Student_Details.Gender,Student_Details.Category,Student_Details.Mode_of_admission,Student_Details.Engineering_branch,Student_Details.Section,Student_Details.Year_of_joining,Student_Details.Year_of_passing,Student_Details.first_sem_SGPA,Student_Details.first_sem_percentage,Student_Details.second_sem_SGPA,Student_Details.second_sem_percentage,Student_Details.Mode_of_admission,Student_Details.Engineering_branch,Student_Details.Section,Student_Details.Year_of_joining,Student_Details.Year_of_passing,Student_Details.first_sem_SGPA,Student_Details.first_sem_percentage,Student_Details.second_sem_SGPA,Student_Details.second_sem_percentage,Student_Details.third_sem_SGPA,Student_Details.third_sem_percentage,Student_Details.fourth_sem_SGPA,Student_Details.fourth_sem_percentage,Student_Details.fifth_sem_SGPA,Student_Details.fifth_sem_percentage,Student_Details.Total_CGPA,Student_Details.Total_CGPA,Student_Details.TOTAL_CREDITS_EARNED_UPTO_5TH_SEMESTER,Student_Details.NUMBER_OF_SUBJECTS_CLEARED_IN_MUTE,Student_Details.CURRENT_ARREARS,Student_Details.NUMBER_OF_SUBJECTS_CLEARED_IN_MUTE,Student_Details.CURRENT_ARREARS,Student_Details.tenth_SSLC_percentage,Student_Details.tenth_sslc_board,Student_Details.Name_of_institution_studied_in_10th_sslc,Student_Details.tenth_sslc_qualified_year,Student_Details.twelveth_PUC_percentage,Student_Details.twelveth_PUC_board,Student_Details.Name_of_the_institution_studied_12th_Puc,Student_Details.twelveth_PUC_qualified_year,Student_Details.Diploma_percentage,Student_Details.Diploma_CET_percentage,Student_Details.Name_of_the_institution_studied_diploma,Student_Details.Diploma_qualified_year,Student_Details.contact_number,Student_Details.LANDLINE_NUMBER,Student_Details.PARENTS_NUMBER,Student_Details.Alternate_contact_number,Student_Details.EMAIL_ID,Student_Details.College_mail,Student_Details.CURRENT_ADDRESS,Student_Details.PERMANENT_ADDRESS,StudentApplication.Company_id,StudentApplication.Company_name,StudentApplication.Select_status from Student_Details join StudentApplication on Student_Details.id = StudentApplication.Student_id")
	results = cursor.fetchall()
	print(results)
	return render(request,'DisplayStudent.html',{'results':results})

	

def Add_Off_Campus_Details(request):
	if request.method == "POST":
		usn = request.POST['usn']
		company = request.POST['c_name']
		package = request.POST['package']
		proof = request.FILES['proof']
        #if .objects.filter(USN=C_name, password=C_password).exists()
		obj = offCampusPlaced(
							USN=usn
							,CompanyName=company
							,package=package
							,proof=proof
								)
		obj.save()
		messages.info(request,'Add Data Sucessfully')
		return redirect('/View_Off_Campus_Details')
	else:
		return render(request,'Add_Off_Campus_Details.html',{})

def View_Off_Campus_Details(request):
	if request.method == "POST":
		searched = request.POST['searched']
		if offCampusPlaced.objects.filter(USN=searched).exists():
			details = offCampusPlaced.objects.filter(USN=searched)
			return render(request,'View_Off_Campus_Details.html',{'details':details})
		else:
			messages.info(request,'Inavlid USN')
			return redirect('/View_Off_Campus_Details')
	else:																
		details = offCampusPlaced.objects.all()
		return render(request,'View_Off_Campus_Details.html',{'details':details})

def OffCampus_Del(request,id):
	del_off = offCampusPlaced.objects.filter(id=id)
	del_off.delete()
	return redirect('/View_Off_Campus_Details')


def view(request,id):
	show = offCampusPlaced.objects.all().filter(id=id)
	return render(request,'view.html',{'show':show})


def Placement_Statistics(request):
	labels = []
	data = []
	queryset = (CompanyDetails11.objects.values('CATEGORY',).annotate(total=Count('id'),).order_by())
	print(queryset)
	for i in queryset:
		print(i)
		i1 = i.values()
		list1 = list(i1)
		labels.append(list1[0])
		data.append(list1[1])
		print(list1[0])
		print(list1[1])
		print(list1)
		print(i1)
		print(labels)
		print(data)
	return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def Visited_Companies(request):
	return render(request,'Visited_Companies.html',{})

def Placement_Policies(request):
	return render(request,'Placement_Policies.html',{})

def Student_Status(request):
	return render(request,'Student_Status.html',{})

def index(request):


	return render(request,'index.html',{})



	'''Student = Student_status.objects.all()
	print(Student)
	for i in Student:
		user = i.Student_id
		print(user)
		data = Student_Details.objects.all().filter(id=user)
		print(data)
		user_data = Student_status.objects.all().filter(Student_id=user)
		print(user_data)
		#details = str(user) +  str(data)
		#print('details',details)
		
		
    
	details = All_Information.objects.all()
	return render(request,'DisplayStudent.html',{'details':details})'''

def Student_Login(request):
	if request.method == "POST":
		C_name = request.POST['uname']
		C_password = request.POST['upass']
		password = request.POST['cpass']
		if Student_Details.objects.filter(USN=C_name, password=C_password).exists():
			if C_password == password:
				users = Student_Details.objects.all().filter(USN=C_name, password=C_password)
				messages.info(request,C_name +' logged in')
				request.session['UserId'] = users[0].id
				request.session['USN_id'] = users[0].USN 
				print(request.session['USN_id'])

				request.session['type_id'] = 'User'
				request.session['UserType'] = C_name
				request.session['login'] = "Yes"
				return redirect("/home")
			else:
				messages.info(request,'Password does not macth')
				return redirect("Student_Login")
		else:
			messages.info(request, 'Please Register')
			return redirect("/User_Registeration")
	else:
		return render(request,'Student_Login.html',{})
	return render(request,'Student_Login.html',{})

	return render(request,'Student_Login.html',{})




def User_Registeration(request):
	if request.method == "POST":
		Name=request.POST['name']
		print(Name)
		USN                                     =request.POST['usn']
		password 								=request.POST['password']
		Date_of_Birth                           =request.POST['dob']
		Gender                                  =request.POST['gender']
		Category                                =request.POST['Category']
		Mode_of_admission                       =request.POST['admission']
		Engineering_branch                      =request.POST['branch']
		Section                                 =request.POST['section']
		Year_of_joining                         =request.POST['yoj']
		Year_of_passing                         =request.POST['yop']
		first_sem_SGPA                          =request.POST['fsem']
		first_sem_percentage                    =request.POST['fper']
		second_sem_SGPA                         =request.POST['ssem']
		second_sem_percentage                   =request.POST['sper']
		third_sem_SGPA                          =request.POST['tsem']
		third_sem_percentage                    =request.POST['tper']
		fourth_sem_SGPA                         =request.POST['foursem']
		fourth_sem_percentage                   =request.POST['fourper']
		fifth_sem_SGPA                          =request.POST['sem5']
		fifth_sem_percentage                    =request.POST['sem5per']
		Total_CGPA                              =request.POST['cgpa']
		Total_CGPA_per							=request.POST['cgpaper']
		TOTAL_CREDITS_EARNED_UPTO_5TH_SEMESTER  =request.POST['credits']
		NUMBER_OF_SUBJECTS_CLEARED_IN_MUTE      =request.POST['cleared']
		CURRENT_ARREARS                         =request.POST['current']
		tenth_SSLC_percentage                   =request.POST['ssc_percentage']
		tenth_sslc_board                        =request.POST['ssc_board']
		Name_of_institution_studied_in_10th_sslc=request.POST['ssc_name']
		tenth_sslc_qualified_year               =request.POST['ssc_year']
		twelveth_PUC_percentage                 =request.POST['hsc_percentage']
		twelveth_PUC_board                      =request.POST['hsc_board']
		Name_of_the_institution_studied_12th_Puc=request.POST['hsc_name']
		twelveth_PUC_qualified_year             =request.POST['hsc_qualifiedYear']
		Diploma_percentage                      =request.POST['diploma_percentage']
		Diploma_CET_percentage                  =request.POST['dipCET_percentage']
		Name_of_the_institution_studied_diploma =request.POST['diploma_name']
		Diploma_qualified_year                  =request.POST['dipQualified_year']
		contact_number                          =request.POST['contact_number']
		LANDLINE_NUMBER                         =request.POST['landline_number']
		PARENTS_NUMBER                          =request.POST['parent_number']
		Alternate_contact_number                =request.POST['alt_number']
		EMAIL_ID                                =request.POST['email']
		College_mail                            =request.POST['clg_id']
		CURRENT_ADDRESS                         =request.POST['current_add']
		PERMANENT_ADDRESS                       =request.POST['permanent_add']
		if  Student_Details.objects.filter(USN = USN).exists():
			myObjects = UserDetails.objects.all().filter(USN = USN)
			messages.error(request,'Already Registered Please Login')
			return render(request,'Student_Login.html',{})
		else:
			obj = Student_Details(
								Name=Name
								,USN=USN
								,password=password
								,Date_of_Birth=Date_of_Birth
								,Gender=Gender
								,Category=Category
								,Mode_of_admission=Mode_of_admission
								,Engineering_branch=Engineering_branch
								,Section=Section
								,Year_of_joining=Year_of_joining
								,Year_of_passing=Year_of_passing
								,first_sem_SGPA=first_sem_SGPA
								,first_sem_percentage=first_sem_percentage
								,second_sem_SGPA=second_sem_SGPA
								,second_sem_percentage=second_sem_percentage
								,third_sem_SGPA=third_sem_SGPA
								,third_sem_percentage=third_sem_percentage
								,fourth_sem_SGPA=fourth_sem_SGPA
								,fourth_sem_percentage=fourth_sem_percentage
								,fifth_sem_SGPA=fifth_sem_SGPA
								,fifth_sem_percentage=fifth_sem_percentage
								,Total_CGPA=Total_CGPA
								,Total_CGPA_per=Total_CGPA_per
								,TOTAL_CREDITS_EARNED_UPTO_5TH_SEMESTER=TOTAL_CREDITS_EARNED_UPTO_5TH_SEMESTER
								,NUMBER_OF_SUBJECTS_CLEARED_IN_MUTE=NUMBER_OF_SUBJECTS_CLEARED_IN_MUTE
								,CURRENT_ARREARS=CURRENT_ARREARS
								,tenth_SSLC_percentage=tenth_SSLC_percentage
								,tenth_sslc_board=tenth_sslc_board
								,Name_of_institution_studied_in_10th_sslc=Name_of_institution_studied_in_10th_sslc
								,tenth_sslc_qualified_year=tenth_sslc_qualified_year
								,twelveth_PUC_percentage=twelveth_PUC_percentage
								,twelveth_PUC_board=twelveth_PUC_board
								,Name_of_the_institution_studied_12th_Puc=Name_of_the_institution_studied_12th_Puc
								,twelveth_PUC_qualified_year=twelveth_PUC_qualified_year
								,Diploma_percentage=Diploma_percentage
								,Diploma_CET_percentage=Diploma_CET_percentage
								,Name_of_the_institution_studied_diploma=Name_of_the_institution_studied_diploma
								,Diploma_qualified_year=Diploma_qualified_year
								,contact_number=contact_number
								,LANDLINE_NUMBER=LANDLINE_NUMBER
								,PARENTS_NUMBER=PARENTS_NUMBER
								,Alternate_contact_number=Alternate_contact_number
								,EMAIL_ID=EMAIL_ID
								,College_mail=College_mail
								,CURRENT_ADDRESS=CURRENT_ADDRESS
								,PERMANENT_ADDRESS=PERMANENT_ADDRESS

			)
			obj.save()
			return redirect('/Student_Login')
	else:
		return render(request,'User_Registeration.html',{})


def Educational_Details(request):
	return render(request,'Educational_Details.html',{})

def Previous_Details(request):
	return render(request,'Previous_Details.html',{})

def Contact_Details(request):
	return render(request,'Contact_Details.html',{})

def practise(request):
	return render(request,'practise.html',{})

def Profile(request):
	User_id =request.session['UserId']
	details = Student_Details.objects.all().filter(id=User_id)
	return render(request,'Profile.html',{'details':details})

def Update(request):
	if request.method == "POST":
		User_id 								= request.POST['UserId']
		Name  									=request.POST['name']
		print(Name)
		USN                                     =request.POST['usn']
		password 								=request.POST['password']
		Date_of_Birth                           =request.POST['dob']
		Gender                                  =request.POST['gender']
		Category                                =request.POST['Category']
		Mode_of_admission                       =request.POST['admission']
		Engineering_branch                      =request.POST['branch']
		Section                                 =request.POST['section']
		Year_of_joining                         =request.POST['yoj']
		Year_of_passing                         =request.POST['yop']
		first_sem_SGPA                          =request.POST['fsem']
		first_sem_percentage                    =request.POST['fper']
		second_sem_SGPA                         =request.POST['ssem']
		second_sem_percentage                   =request.POST['sper']
		third_sem_SGPA                          =request.POST['tsem']
		third_sem_percentage                    =request.POST['tper']
		fourth_sem_SGPA                         =request.POST['fsem']
		fourth_sem_percentage                   =request.POST['fper']
		fifth_sem_SGPA                          =request.POST['sem5']
		fifth_sem_percentage                    =request.POST['sem5per']
		Total_CGPA                              =request.POST['cgpa']
		Total_CGPA_per							=request.POST['cgpaper']
		TOTAL_CREDITS_EARNED_UPTO_5TH_SEMESTER  =request.POST['credits']
		NUMBER_OF_SUBJECTS_CLEARED_IN_MUTE      =request.POST['cleared']
		CURRENT_ARREARS                         =request.POST['current']
		tenth_SSLC_percentage                   =request.POST['ssc_percentage']
		tenth_sslc_board                        =request.POST['ssc_board']
		Name_of_institution_studied_in_10th_sslc=request.POST['ssc_name']
		tenth_sslc_qualified_year               =request.POST['ssc_year']
		twelveth_PUC_percentage                 =request.POST['hsc_percentage']
		twelveth_PUC_board                      =request.POST['hsc_board']
		Name_of_the_institution_studied_12th_Puc=request.POST['hsc_name']
		twelveth_PUC_qualified_year             =request.POST['hsc_qualifiedYear']
		Diploma_percentage                      =request.POST['diploma_percentage']
		Diploma_CET_percentage                  =request.POST['dipCET_percentage']
		Name_of_the_institution_studied_diploma =request.POST['diploma_name']
		Diploma_qualified_year                  =request.POST['dipQualified_year']
		contact_number                          =request.POST['contact_number']
		LANDLINE_NUMBER                         =request.POST['landline_number']
		PARENTS_NUMBER                          =request.POST['parent_number']
		Alternate_contact_number                =request.POST['alt_number']
		EMAIL_ID                                =request.POST['email']
		College_mail                            =request.POST['clg_id']
		CURRENT_ADDRESS                         =request.POST['current_add']
		PERMANENT_ADDRESS                       =request.POST['permanent_add']

		Student_Details.objects.filter(id=User_id).update(
								Name=Name
								,USN=USN
								,password=password
								,Date_of_Birth=Date_of_Birth
								,Gender=Gender
								,Category=Category
								,Mode_of_admission=Mode_of_admission
								,Engineering_branch=Engineering_branch
								,Section=Section
								,Year_of_joining=Year_of_joining
								,Year_of_passing=Year_of_passing
								,first_sem_SGPA=first_sem_SGPA
								,first_sem_percentage=first_sem_percentage
								,second_sem_SGPA=second_sem_SGPA
								,second_sem_percentage=second_sem_percentage
								,third_sem_SGPA=third_sem_SGPA
								,third_sem_percentage=third_sem_percentage
								,fourth_sem_SGPA=fourth_sem_SGPA
								,fourth_sem_percentage=fourth_sem_percentage
								,fifth_sem_SGPA=fifth_sem_SGPA
								,fifth_sem_percentage=fifth_sem_percentage
								,Total_CGPA=Total_CGPA
								,Total_CGPA_per=Total_CGPA_per
								,TOTAL_CREDITS_EARNED_UPTO_5TH_SEMESTER=TOTAL_CREDITS_EARNED_UPTO_5TH_SEMESTER
								,NUMBER_OF_SUBJECTS_CLEARED_IN_MUTE=NUMBER_OF_SUBJECTS_CLEARED_IN_MUTE
								,CURRENT_ARREARS=CURRENT_ARREARS
								,tenth_SSLC_percentage=tenth_SSLC_percentage
								,tenth_sslc_board=tenth_sslc_board
								,Name_of_institution_studied_in_10th_sslc=Name_of_institution_studied_in_10th_sslc
								,tenth_sslc_qualified_year=tenth_sslc_qualified_year
								,twelveth_PUC_percentage=twelveth_PUC_percentage
								,twelveth_PUC_board=twelveth_PUC_board
								,Name_of_the_institution_studied_12th_Puc=Name_of_the_institution_studied_12th_Puc
								,twelveth_PUC_qualified_year=twelveth_PUC_qualified_year
								,Diploma_percentage=Diploma_percentage
								,Diploma_CET_percentage=Diploma_CET_percentage
								,Name_of_the_institution_studied_diploma=Name_of_the_institution_studied_diploma
								,Diploma_qualified_year=Diploma_qualified_year
								,contact_number=contact_number
								,LANDLINE_NUMBER=LANDLINE_NUMBER
								,PARENTS_NUMBER=PARENTS_NUMBER
								,Alternate_contact_number=Alternate_contact_number
								,EMAIL_ID=EMAIL_ID
								,College_mail=College_mail
								,CURRENT_ADDRESS=CURRENT_ADDRESS
								,PERMANENT_ADDRESS=PERMANENT_ADDRESS

			)
		messages.info(request,'Profile Updated Sucessfully')
		return redirect('/Profile')
	else:
		details = Student_Details.objects.all().filter(id=User_id)
		return render(request,'Profile.html',{'details':details})


def COMPUTER_SCIENCE_AND_ENGINEERING(request):
	cs = Student_Details.objects.all()
	return render(request,'COMPUTER_SCIENCE_AND_ENGINEERING.html',{'cs':cs})


def Manage_Company(request):
	if request.method == "POST":
		CID = request.POST['updateid1']
		CompanyName = request.POST['updateCompanyname1']
		Package = request.POST['updatepackage1']
		File = request.FILES['updatefile']
		Pre_Placement = request.POST['updatepre1']
		Test_Date = request.POST['updatetest1']
		Interview_Date = request.POST['updateinter1']
		Additional_Information = request.POST['updateadd1']
		CGPA = request.POST['updatecgpa1']
		check = request.POST.getlist('checks[]')
		print(check)
		OTHERS = request.POST['updateother1']
		CATEGORY = request.POST['updatecat1']
		#check.append('test')
		checks = ",".join(str(x) for x in check)
		print(type(checks))
		CompanyDetails11.objects.all().filter(id = CID).update(CompanyName=CompanyName,Package=Package,File=File,Additional_Information=Additional_Information,CGPA=CGPA,Stream = checks +','+'test',OTHERS=OTHERS,CATEGORY=CATEGORY)
	
		messages.info(request,'Updated Data Sucessfully')
		return redirect('/Manage_Company')
	else:
		details = CompanyDetails11.objects.all()
		return render(request,'Manage_Company.html',{'details':details})


def Change_Password(request):
	Userid = request.session['UserId']
	if request.method == "POST":
		newpass = request.POST['new_pass']
		confirm = request.POST['confirm_pass']
		if newpass == confirm:
			Student_Details.objects.filter(id=Userid).update(password=newpass)
			messages.info(request,'Password changed')
			details = Student_Details.objects.filter(id=Userid)
			return render(request,'Change_Password.html',{'details':details})
		else:
			messages.info(request,'Passwords dont match')
			return redirect('/Change_Password')
	else:
		Userid = request.session['UserId']
		details = Student_Details.objects.filter(id=Userid)
		return render(request,'Change_Password.html',{'details':details})


def Eligible_Company_List(request):

	Userid = request.session['UserId']
	#if StudentApplication.objects.filter(Student_id = USN_id).values(Category)

	details = Student_Details.objects.filter(id=Userid)
	for i in details:
		cgpa = details[0].Total_CGPA
		print(cgpa)
	info = CompanyDetails11.objects.all().filter(CGPA__lt=cgpa)
	info1 = StudentApplication.objects.all()
	for p in StudentApplication.objects.raw('SELECT * FROM StudentApplication'):
		print(p)
		print(p.Company_id)
	'''for a in info:
					cid = a.id
					Company_cgpa = a.CGPA
					if Company_cgpa <= cgpa:
						data = CompanyDetails.objects.all().filter(id=cid)
						print(data)'''

	return render(request,'Eligible_Company_List.html',{'info':info,'Userid':Userid,'info1':info1})

def ELECTRONICS_AND_COMMUNICATION_ENGINEERING(request):
	return render(request,'ELECTRONICS_AND_COMMUNICATION_ENGINEERING.html',{})

def INFORMATION_SCIENCE_AND_ENGINEERING(request):
	return render(request,'INFORMATION_SCIENCE_AND_ENGINEERING.html',{})

def OffCampus_User(request):
	if request.method == "POST":
		searched = request.POST['searched']
		if UsseroffCampusPlaced.objects.filter(USN=searched).exists():
			details = UsseroffCampusPlaced.objects.filter(USN=searched)
			return render(request,'OffCampus_User.html',{'details':details})
		else:
			messages.info(request,'Inavlid USN')
			return redirect('/OffCampus_User')
	else:																
		details = UsseroffCampusPlaced.objects.all()
		return render(request,'OffCampus_User.html',{'details':details})








def Placements_User(request):
	cursor = connection.cursor()
	UserID = request.session['UserId']
	test = "SELECT * FROM `CompanyDetails11` INNER JOIN StudentApplication ON CompanyDetails11.id = StudentApplication.Company_id WHERE StudentApplication.Student_id = '"+str(UserID)+"';"
	cursor.execute(test)
	results = cursor.fetchall()
	print(results)
	for i in results:
		print('i',i)

	#cursor = connection.cursor()
	#cursor.execute(test)
	#results = cursor.fetchall()
	#print(results)
	#results1 = list(results)
	#cursor = connection.cursor()
	#cursor.execute("Select CompanyDetails11.id,CompanyDetails11.CompanyName,CompanyDetails11.Package join StudentApplication.Company_id = CompanyDetails.id ")
	'''UserID = request.session['UserId']
				info = StudentApplication.objects.all().filter(Student_id = UserID)
				for i in info:
					ids = i.Company_id
					print(ids)
					info = CompanyDetails11.objects.all().filter(id = ids)
					print(info)'''
	#info = StudentApplication.objects.all()
	return render(request,'Placements_User.html',{'results':results})

def ApplyJob(request):
	if request.method == "POST":
		c_id = request.POST['C_id']
		print(c_id)
		c_data = CompanyDetails11.objects.all().filter(id = c_id)
		print(c_data)
		C_name = c_data[0].CompanyName
		print(C_name)
		C_Category = c_data[0].Category_Number
		print(C_Category)
		UserID = request.session['UserId']
		U_data = Student_Details.objects.all().filter(id = UserID)
		print(U_data)
		U_name = U_data[0].Name
		U_usn = U_data[0].USN
		print(U_name + U_usn)
		var = 3
		if StudentApplication.objects.filter(Student_id = UserID).exists():
			datas = StudentApplication.objects.all().filter(Student_id = UserID,Select_status = "Placed")
			print('dataa',datas)
			print('datalen',len(datas))
			if len(datas) == 2:
				sentence = 'placed'
				data = {
				'respond': sentence
				}
				return JsonResponse(data)
			elif StudentApplication.objects.all().filter(Student_id = UserID,Select_status = "Placed").filter(Student_Category__gte = var).exists():
				
				#data = StudentApplication.objects.all().filter(Student_id = UserID,Select_status = "Placed").filter(Student_Category__gte = var)
				#print('var',data)
				sentence = 'Category'
				data = {
				'respond': sentence
				}
				return JsonResponse(data)


			elif StudentApplication.objects.filter(Student_id = UserID,Company_id = c_id).exists():
				print('else2')
				sentence = 'exists'
				data = {
				'respond': sentence
				}
				return JsonResponse(data)

			else:
				print('else3')
				data = StudentApplication(Student_id=UserID,Student_name=U_name,Company_id=c_id,Company_name=C_name,Status='Applied',Student_USN=U_usn,Student_Category = C_Category)
				data.save()
				return redirect('/Eligible_Company_List')
		else:
			return redirect('/Eligible_Company_List')
	else:
		return redirect('/Eligible_Company_List')

def EditCompany(request,id):

	return render(request,'EditCompany.html',{})

def DeleteComp(request,id):
	delcomp = CompanyDetails11.objects.get(id=id) 
	delcomp.delete()
	return redirect('/Manage_Company')


def Placement_Admin(request):
	if request.method == "POST":
		admission = request.POST['admission']
		branch = request.POST['branch']
		section = request.POST['section']
		if Student_Details.objects.filter(Q(Engineering_branch=admission) and Q(Mode_of_admission=branch) and Q(Section=section)).exists():
			test1 = Student_Details.objects.filter(Q(Engineering_branch=admission) and Q(Mode_of_admission=branch) and Q(Section=section))
			print(test1)	
			test = "SELECT * FROM `Student_Details` INNER JOIN `StudentApplication` ON Student_Details.id = StudentApplication.Student_id  where Student_Details.Mode_of_admission = '"+str(admission)+"' and Student_Details.Engineering_branch = '"+str(branch)+"' and Student_Details.Section = '"+str(section)+"' ";    
 		#if Student_Details.objects.all().filter(Engineering_branch = branch,Mode_of_admission = admission,Section = section).exists():
			#test = "SELECT * FROM `Student_Details` INNER JOIN StudentApplication ON Student_Details.id = StudentApplication.Student_id WHERE Student_Details.Mode_of_admission = "+str(admission)+" AND Student_Details.Engineering_branch = '"+str(branch)+"' AND WHERE Student_Details.Section = '"+str(section)+"' ;"
			cursor = connection.cursor()
			cursor.execute(test)
			#cursor.execute("Select Student_Details.id,Student_Details.Name,Student_Details.USN,Student_Details.Date_of_Birth,Student_Details.Gender,Student_Details.Category,Student_Details.Mode_of_admission,Student_Details.Engineering_branch,Student_Details.Section,Student_Details.Year_of_joining,Student_Details.Year_of_passing,Student_Details.first_sem_SGPA,Student_Details.first_sem_percentage,Student_Details.second_sem_SGPA,Student_Details.second_sem_percentage,Student_Details.Mode_of_admission,Student_Details.Engineering_branch,Student_Details.Section,Student_Details.Year_of_joining,Student_Details.Year_of_passing,Student_Details.first_sem_SGPA,Student_Details.first_sem_percentage,Student_Details.second_sem_SGPA,Student_Details.second_sem_percentage,Student_Details.third_sem_SGPA,Student_Details.third_sem_percentage,Student_Details.fourth_sem_SGPA,Student_Details.fourth_sem_percentage,Student_Details.fifth_sem_SGPA,Student_Details.fifth_sem_percentage,Student_Details.Total_CGPA,Student_Details.Total_CGPA,Student_Details.TOTAL_CREDITS_EARNED_UPTO_5TH_SEMESTER,Student_Details.NUMBER_OF_SUBJECTS_CLEARED_IN_MUTE,Student_Details.CURRENT_ARREARS,Student_Details.NUMBER_OF_SUBJECTS_CLEARED_IN_MUTE,Student_Details.CURRENT_ARREARS,Student_Details.tenth_SSLC_percentage,Student_Details.tenth_sslc_board,Student_Details.Name_of_institution_studied_in_10th_sslc,Student_Details.tenth_sslc_qualified_year,Student_Details.twelveth_PUC_percentage,Student_Details.twelveth_PUC_board,Student_Details.Name_of_the_institution_studied_12th_Puc,Student_Details.twelveth_PUC_qualified_year,Student_Details.Diploma_percentage,Student_Details.Diploma_CET_percentage,Student_Details.Name_of_the_institution_studied_diploma,Student_Details.Diploma_qualified_year,Student_Details.contact_number,Student_Details.LANDLINE_NUMBER,Student_Details.PARENTS_NUMBER,Student_Details.Alternate_contact_number,Student_Details.EMAIL_ID,Student_Details.College_mail,Student_Details.CURRENT_ADDRESS,Student_Details.PERMANENT_ADDRESS,StudentApplication.Company_id,StudentApplication.Company_name,StudentApplication.Select_status from Student_Details join StudentApplication on Student_Details.id = StudentApplication.Student_id")
			
			results = cursor.fetchall()
			print(results)
			print(admission + branch + section)
			return render(request,'DisplayPlacements.html',{'results':results})
		else:
			messages.info(request,'Invalid Search')
			return redirect('/Placement_Admin')
	else:
		#test = "SELECT * FROM `Student_Details` INNER JOIN StudentApplication ON CompanyDetails11.id = StudentApplication.Company_id WHERE StudentApplication.Student_id = '"+str(UserID)+"' and Student_Details.Mode_of_admission = '"+str(admission)+"';"
		cursor = connection.cursor()
		cursor.execute("Select Student_Details.id,Student_Details.Name,Student_Details.USN,Student_Details.Date_of_Birth,Student_Details.Gender,Student_Details.Category,Student_Details.Mode_of_admission,Student_Details.Engineering_branch,Student_Details.Section,Student_Details.Year_of_joining,Student_Details.Year_of_passing,Student_Details.first_sem_SGPA,Student_Details.first_sem_percentage,Student_Details.second_sem_SGPA,Student_Details.second_sem_percentage,Student_Details.Mode_of_admission,Student_Details.Engineering_branch,Student_Details.Section,Student_Details.Year_of_joining,Student_Details.Year_of_passing,Student_Details.first_sem_SGPA,Student_Details.first_sem_percentage,Student_Details.second_sem_SGPA,Student_Details.second_sem_percentage,Student_Details.third_sem_SGPA,Student_Details.third_sem_percentage,Student_Details.fourth_sem_SGPA,Student_Details.fourth_sem_percentage,Student_Details.fifth_sem_SGPA,Student_Details.fifth_sem_percentage,Student_Details.Total_CGPA,Student_Details.Total_CGPA,Student_Details.TOTAL_CREDITS_EARNED_UPTO_5TH_SEMESTER,Student_Details.NUMBER_OF_SUBJECTS_CLEARED_IN_MUTE,Student_Details.CURRENT_ARREARS,Student_Details.NUMBER_OF_SUBJECTS_CLEARED_IN_MUTE,Student_Details.CURRENT_ARREARS,Student_Details.tenth_SSLC_percentage,Student_Details.tenth_sslc_board,Student_Details.Name_of_institution_studied_in_10th_sslc,Student_Details.tenth_sslc_qualified_year,Student_Details.twelveth_PUC_percentage,Student_Details.twelveth_PUC_board,Student_Details.Name_of_the_institution_studied_12th_Puc,Student_Details.twelveth_PUC_qualified_year,Student_Details.Diploma_percentage,Student_Details.Diploma_CET_percentage,Student_Details.Name_of_the_institution_studied_diploma,Student_Details.Diploma_qualified_year,Student_Details.contact_number,Student_Details.LANDLINE_NUMBER,Student_Details.PARENTS_NUMBER,Student_Details.Alternate_contact_number,Student_Details.EMAIL_ID,Student_Details.College_mail,Student_Details.CURRENT_ADDRESS,Student_Details.PERMANENT_ADDRESS,StudentApplication.Company_id,StudentApplication.id,StudentApplication.Company_name,StudentApplication.Select_status from Student_Details join StudentApplication on Student_Details.id = StudentApplication.Student_id")
		results = cursor.fetchall()
		print(results)
		return render(request,'Placement_Admin.html',{'results':results})



def User_OffCampus(request):
	return render(request,'User_OffCampus.html',{})


def User_AddOffCampus(request):
	if request.method == "POST":
		usn = request.POST['usn']
		company = request.POST['c_name']
		package = request.POST['package']
		proof = request.FILES['proof']
		USN = request.session['USN_id']
		if UsseroffCampusPlaced.objects.filter(USN = USN).exists():
			UsseroffCampusPlaced.objects.filter(USN=usn).update(CompanyName=company,package=package,proof=proof)
			messages.info(request,'Updated Sucessfully')
			return redirect('/OffCampus_User')
		else:
			obj = UsseroffCampusPlaced(USN=usn,CompanyName=company,package=package,proof=proof)
			obj.save()
			messages.info(request,'Added Sucessfully')
			return redirect('/OffCampus_User')
	else:
		Userid = request.session['UserId']
		data = Student_Details.objects.filter(id = Userid).values('USN')
		print(data)
		return render(request,'User_AddOffCampus.html',{'data':data})

def view1(request,id):
	show = UsseroffCampusPlaced.objects.all().filter(id=id)
	return render(request,'view1.html',{'show':show})

def DisplayPlacements(request):
	if request.method == "POST":
		usn_no = request.POST['usn']
		print(usn_no)
		if StudentApplication.objects.filter(Student_USN = usn_no).exists():
			test = "SELECT * FROM `Student_Details` INNER JOIN StudentApplication ON Student_Details.USN = StudentApplication.Student_USN WHERE StudentApplication.Student_usn = '"+str(usn_no)+"' ";
			cursor = connection.cursor()
			cursor.execute(test)
			results = cursor.fetchall()
			print(results)
			return render(request,'DisplayPlacements.html',{'results':results})
		else:
			messages.info(request,'Enter USN doesnt exists')
			return redirect('/DisplayPlacements')
	else:
		return render(request,'DisplayPlacements.html',{})


def pie_chart(request):

	labels = []
	data = []
	queryset = (Student_Details.objects.values('Engineering_branch',).annotate(total=Count('id'),).order_by())
	print(queryset)
	for i in queryset:
		print(i)
		i1 = i.values()
		list1 = list(i1)
		labels.append(list1[0])
		data.append(list1[1])
		print(list1[0])
		print(list1[1])
		print(list1)
		print(i1)
		print(labels)
		print(data)
	return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
	'''labels1 = []
				data1 = []
				queryset = (StudentApplication.objects.values('Select_status',).annotate(total=Count('id'),).order_by())
				print(queryset)
				for i in queryset:
					print(i)
					i1 = i.values()
					list1 = list(i1)
					labels1.append(list1[0])
					data1.append(list1[1])
					print(list1[0])
					print(list1[1])
					print(list1)
					print(i1)
					print(labels1)
					print(data1)'''
	'''queryset = "SELECT COUNT(Name),Engineering_branch  FROM Student_Details GROUP BY Engineering_branch";
				
					cursor = connection.cursor()
					cursor.execute(queryset)
					results = cursor.fetchall()
					print(results)'''
	'''for i in results:
					print(i)
					
					for j in i:
						print(j)
			'''

	'''for Student in queryset:
					labels.append(Student.Engineering_branch)
					data.append(Student.Name)
					print(labels,data)'''
	
#'labels':labels,'data':data,

def AddPlaced_status(request):
	if request.method == "POST":
		USN_id = request.POST['updateid']
		app_id = request.POST['updateids']
		Status = request.POST['status']
		print(USN_id,app_id,Status)
		StudentApplication.objects.filter(Student_USN = USN_id,id = app_id).update(Select_status = Status)
		return render(request,'AddPlaced_status.html',{})


def placed_bar(request):
	labels = []
	data = []
	queryset = (StudentApplication.objects.values('Select_status',).annotate(total=Count('id'),).order_by())
	print(queryset)
	for i in queryset:
		print(i)
		i1 = i.values()
		list1 = list(i1)
		print(list1[0])
		print(list1[1])
		if list1[0]!="Not Updated":
			labels.append(list1[0])
			data.append(list1[1])
		
		
		print(labels)
		print(data)
	return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
	
def Student_ofers(request):
	test = "Select COUNT(finalcount.count),finalcount.count from ( Select COUNT(Student_id) as count from `studentapplication` where Select_status='Placed' group by Student_id ) finalcount group by finalcount.count;"
	cursor = connection.cursor()
	cursor.execute(test)
	results = cursor.fetchall()
	print(results)
	labels = []
	data = []
	for i in results:
		list1 = list(i)
		data.append(list1[0])
		labels.append(list1[1])
		print(list1[0])
		print(list1[1])
		print(labels)
		print(data)
	return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
	
def All_Companies(request):
	details = CompanyDetails11.objects.all()
	print(details)
	return render(request,'All_Companies.html',{'details':details})

#model = pickle.load(open("placed.pkl", "rb"))

def Placed(request):
	
    model = pickle.load(open("placed.pkl", "rb"))
    todays_date = date.today()
    print("Current date: ", todays_date)
    print("Current year:", todays_date.year)
    print("Current month:", todays_date.month)
    print("Current day:", todays_date.day)
    Students = Student_Details.objects.count()
    print(Students)
    #Students = 500
    #print(Students)
    prediction = model.predict([[todays_date.year,Students]])
    print(prediction)
    Notplaced = int(Students) - int(prediction)
    print(Notplaced)
    prediction = round(prediction[0])
    df = pd.read_csv("Placed2.csv")
    df.loc[22, 'Students'] = Students
    df.loc[22, 'Placed'] = prediction
    df.loc[22, 'Notplaced'] = Notplaced
    df.to_csv("Placed2.csv", index=False)
    data = pd.read_csv("Placed2.csv")
    df = pd.DataFrame(data, columns=["Year", "Placed", "Notplaced"])
    df.plot(x="Year", y=["Placed", "Notplaced"], kind="bar", figsize=(9, 8))
    path = "C:/Users/NEVON/Downloads/CampusPlacement (1) (1)/CampusPlacement (1)/CampusPlacement/CampusPlacement/media/"
    mp.savefig(path +'foo.png')
    mp.show()
    return redirect('/Forecasting')

def Display_Placed(request):
	model = pickle.load(open("offers.pkl", "rb"))
	todays_date = date.today()
	print("Current date: ", todays_date)
	print("Current year:", todays_date.year)
	print("Current month:", todays_date.month)
	print("Current day:", todays_date.day)
	Students = Student_Details.objects.count()
	print('Students',Students)
	Placed = StudentApplication.objects.filter(Select_status__icontains='Placed').count()
	print('Placed',Placed)
	Companies = CompanyDetails11.objects.count()
	print('Companies',Companies)
	
	prediction = model.predict([[todays_date.year,Companies,Students,Placed]])
	print(prediction)
	prediction = round(prediction[0])
	print(prediction)
	df = pd.read_csv("offers1.csv")
	df.loc[22, 'Students'] = Students
	df.loc[22, 'Offers'] = prediction
	df.loc[22, 'Placed'] = Placed
	df.loc[22, 'Companies'] = Companies
	df.to_csv("offers1.csv", index=False)
	data = pd.read_csv("offers1.csv")
	df = pd.DataFrame(data, columns=["Year", "Offers"])
	df.plot(x="Year", y="Offers", kind="bar", figsize=(9, 8))
	path = "C:/Users/NEVON/Downloads/CampusPlacement (1) (1)/CampusPlacement (1)/CampusPlacement/CampusPlacement/media/"
	mp.savefig(path +'foo.png')
	mp.show()

	return redirect('/Forecasting')


def CIVIL_Display(request):
	model = pickle.load(open("CIVIL.pkl", "rb"))
	todays_date = date.today()
	print("Current date: ", todays_date)
	print("Current year:", todays_date.year)
	print("Current month:", todays_date.month)
	print("Current day:", todays_date.day)
	Students =Student_Details.objects.count()
	
	Companies = CompanyDetails11.objects.count()

	print(Students)
	prediction = model.predict([[todays_date.year,Companies,Students]])
	print(prediction)
	Notplaced = int(Students) - int(prediction)
	print(Notplaced)
	prediction = round(prediction[0])
	print(prediction)
	df = pd.read_csv("CIVIL1.csv")
	df.loc[22, 'Students'] = Students
	df.loc[22, 'Placed'] = prediction
	df.loc[22, 'Companies'] = Companies
	df.loc[22, 'Notplaced'] = Notplaced
	df.to_csv("CIVIL1.csv", index=False)
	data = pd.read_csv("CIVIL1.csv")
	df = pd.DataFrame(data, columns=["Year", "Placed","Notplaced"])
	df.plot(x="Year", y=["Placed","Notplaced"], kind="bar", figsize=(9, 8))
	path = "C:/Users/NEVON/Downloads/CampusPlacement (1) (1)/CampusPlacement (1)/CampusPlacement/CampusPlacement/media/"
	mp.title('CIVIL')
	mp.savefig(path +'foo2.png')
	mp.show()

	return redirect('/Forecasting')

def CSI_Display(request):
	model = pickle.load(open("CSI.pkl", "rb"))
	todays_date = date.today()
	print("Current date: ", todays_date)
	print("Current year:", todays_date.year)
	print("Current month:", todays_date.month)
	print("Current day:", todays_date.day)
	Students =Student_Details.objects.count()
	
	Companies = CompanyDetails11.objects.count()

	print(Students)
	prediction = model.predict([[todays_date.year,Companies,Students]])
	print(prediction)
	Notplaced = int(Students) - int(prediction)
	print(Notplaced)
	prediction = round(prediction[0])
	print(prediction)
	df = pd.read_csv("CSI.csv")
	df.loc[22, 'Students'] = Students
	df.loc[22, 'Placed'] = prediction
	df.loc[22, 'Companies'] = Companies
	df.loc[22, 'Notplaced'] = Notplaced
	df.to_csv("CSI.csv", index=False)
	data = pd.read_csv("CSI.csv")
	df = pd.DataFrame(data, columns=["Year", "Placed","Notplaced"])
	df.plot(x="Year", y=["Placed","Notplaced"], kind="bar", figsize=(9, 8))
	path = "C:/Users/NEVON/Downloads/CampusPlacement (1) (1)/CampusPlacement (1)/CampusPlacement/CampusPlacement/media/"
	mp.title('CSI')
	mp.savefig(path +'CSI.png')
	mp.show()

	return redirect('/Forecasting')


def ECE_Display(request):
	model = pickle.load(open("ECE.pkl", "rb"))
	todays_date = date.today()
	print("Current date: ", todays_date)
	print("Current year:", todays_date.year)
	print("Current month:", todays_date.month)
	print("Current day:", todays_date.day)
	Students =Student_Details.objects.count()
	
	Companies = CompanyDetails11.objects.count()

	print(Students)
	prediction = model.predict([[todays_date.year,Companies,Students]])
	print(prediction)
	Notplaced = int(Students) - int(prediction)
	print(Notplaced)
	prediction = round(prediction[0])
	print(prediction)
	df = pd.read_csv("ECE.csv")
	df.loc[22, 'Students'] = Students
	df.loc[22, 'Placed'] = prediction
	df.loc[22, 'Companies'] = Companies
	df.loc[22, 'Notplaced'] = Notplaced
	df.to_csv("ECE.csv", index=False)
	data = pd.read_csv("ECE.csv")
	df = pd.DataFrame(data, columns=["Year", "Placed","Notplaced"])
	df.plot(x="Year", y=["Placed","Notplaced"], kind="bar", figsize=(9, 8))
	path = "C:/Users/NEVON/Downloads/CampusPlacement (1) (1)/CampusPlacement (1)/CampusPlacement/CampusPlacement/media/"
	mp.title("ECE")
	mp.savefig(path +'ECE.png')
	mp.show()

	return redirect('/Forecasting')
'''
def ECE_Display(request):
	return render(request,'ECE_Display.html',{})'''


def EEE_Display(request):
	model = pickle.load(open("EEE.pkl", "rb"))
	todays_date = date.today()
	print("Current date: ", todays_date)
	print("Current year:", todays_date.year)
	print("Current month:", todays_date.month)
	print("Current day:", todays_date.day)
	Students =Student_Details.objects.count()
	
	Companies = CompanyDetails11.objects.count()

	print(Students)
	prediction = model.predict([[todays_date.year,Companies,Students]])
	print(prediction)
	Notplaced = int(Students) - int(prediction)
	print(Notplaced)
	prediction = round(prediction[0])
	print(prediction)
	df = pd.read_csv("EEE.csv")
	df.loc[22, 'Students'] = Students
	df.loc[22, 'Placed'] = prediction
	df.loc[22, 'Companies'] = Companies
	df.loc[22, 'Notplaced'] = Notplaced
	df.to_csv("EEE.csv", index=False)
	data = pd.read_csv("EEE.csv")
	df = pd.DataFrame(data, columns=["Year", "Placed","Notplaced"])
	df.plot(x="Year", y=["Placed","Notplaced"], kind="bar", figsize=(9, 8))
	path = "C:/Users/NEVON/Downloads/CampusPlacement (1) (1)/CampusPlacement (1)/CampusPlacement/CampusPlacement/media/"
	mp.title("EEE")
	mp.savefig(path +'EEE.png')
	mp.show()


	return redirect('/Forecasting')

def IP_Display(request):
	model = pickle.load(open("IP.pkl", "rb"))
	todays_date = date.today()
	print("Current date: ", todays_date)
	print("Current year:", todays_date.year)
	print("Current month:", todays_date.month)
	print("Current day:", todays_date.day)
	Students =Student_Details.objects.count()
	
	Companies = CompanyDetails11.objects.count()

	print(Students)
	prediction = model.predict([[todays_date.year,Companies,Students]])
	print(prediction)
	Notplaced = int(Students) - int(prediction)
	print(Notplaced)
	prediction = round(prediction[0])
	print(prediction)
	df = pd.read_csv("IP.csv")
	df.loc[22, 'Students'] = Students
	df.loc[22, 'Placed'] = prediction
	df.loc[22, 'Companies'] = Companies
	df.loc[22, 'Notplaced'] = Notplaced
	df.to_csv("IP.csv", index=False)
	data = pd.read_csv("IP.csv")
	df = pd.DataFrame(data, columns=["Year", "Placed","Notplaced"])
	df.plot(x="Year", y=["Placed","Notplaced"], kind="bar", figsize=(9, 8))
	path = "C:/Users/NEVON/Downloads/CampusPlacement (1) (1)/CampusPlacement (1)/CampusPlacement/CampusPlacement/media/"
	mp.title("IP")
	mp.savefig(path +'IP.png')
	mp.show()

	return redirect('/Forecasting')

def IS_Display(request):
	model = pickle.load(open("IS.pkl", "rb"))
	todays_date = date.today()
	print("Current date: ", todays_date)
	print("Current year:", todays_date.year)
	print("Current month:", todays_date.month)
	print("Current day:", todays_date.day)
	Students =Student_Details.objects.count()
	
	Companies = CompanyDetails11.objects.count()

	print(Students)
	prediction = model.predict([[todays_date.year,Companies,Students]])
	print(prediction)
	Notplaced = int(Students) - int(prediction)
	print(Notplaced)
	prediction = round(prediction[0])
	print(prediction)
	df = pd.read_csv("IS.csv")
	df.loc[22, 'Students'] = Students
	df.loc[22, 'Placed'] = prediction
	df.loc[22, 'Companies'] = Companies
	df.loc[22, 'Notplaced'] = Notplaced
	df.to_csv("IS.csv", index=False)
	data = pd.read_csv("IS.csv")
	df = pd.DataFrame(data, columns=["Year", "Placed","Notplaced"])
	df.plot(x="Year", y=["Placed","Notplaced"], kind="bar", figsize=(9, 8))
	path = "C:/Users/NEVON/Downloads/CampusPlacement (1) (1)/CampusPlacement (1)/CampusPlacement/CampusPlacement/media/"
	mp.title("IS")
	mp.savefig(path +'IS.png')
	mp.show()

	return redirect('/Forecasting')

def MECH_Display(request):
	model = pickle.load(open("MECH.pkl", "rb"))
	todays_date = date.today()
	print("Current date: ", todays_date)
	print("Current year:", todays_date.year)
	print("Current month:", todays_date.month)
	print("Current day:", todays_date.day)
	Students =Student_Details.objects.count()
	
	Companies = CompanyDetails11.objects.count()
	print(Students)
	prediction = model.predict([[todays_date.year,Companies,Students]])
	print(prediction)
	Notplaced = int(Students) - int(prediction)
	print(Notplaced)
	prediction = round(prediction[0])
	print(prediction)
	df = pd.read_csv("MECH.csv")
	df.loc[22, 'Students'] = Students
	df.loc[22, 'Placed'] = prediction
	df.loc[22, 'Companies'] = Companies
	df.loc[22, 'Notplaced'] = Notplaced
	df.to_csv("MECH.csv", index=False)
	data = pd.read_csv("MECH.csv")
	df = pd.DataFrame(data, columns=["Year", "Placed","Notplaced"])
	df.plot(x="Year", y=["Placed","Notplaced"], kind="bar", figsize=(9, 8))
	path = "C:/Users/NEVON/Downloads/CampusPlacement (1) (1)/CampusPlacement (1)/CampusPlacement/CampusPlacement/media/"
	mp.title("MECH")
	mp.savefig(path +'MECH.png')
	mp.show()

	return redirect('/Forecasting')

def Companies(request):
	import csv
	model = pickle.load(open("Companies.pkl", "rb"))
	todays_date = date.today()
	print("Current date: ", todays_date)
	print("Current year:", todays_date.year)
	print("Current month:", todays_date.month)
	print("Current day:", todays_date.day)
	
	import csv

	f = open('Companies.csv')
	csv_f = csv.reader(f)
	data = []
	for row in csv_f:
		data.append(row)
	print(data)
	data = [ele for ele in data if ele != []]
	print(data)
	res = data[-2:]
	print(res)
	sec_last = res[0]
	#MASS
	sec_last_Mass = sec_last[2]  #C22
	print(sec_last_Mass)
	last = res[1]
	print('last',last)
	last_Mass = last[2]   #C23
	print(last_Mass)
	print('sec_last',sec_last)
	next_mass = round(int(last_Mass)+(int(last_Mass)*(int(last_Mass)-int(sec_last_Mass))/100))
	print(next_mass)
	#Core
	sec_last_Core = sec_last[3]  #C22
	print(sec_last_Core)
	last = res[1]
	last_Core = last[3]   #C23
	print(last_Core)
	#print('sec_last',sec_last)
	next_core = round(int(last_Core)+(int(last_Core)*(int(last_Core)-int(sec_last_Core))/100))
	print(next_core)

	print('last',last)
	# print result
	print("The last N elements of list are : " + str(res))
	#Dream
	sec_last_Dream = sec_last[4]  #C22
	print(sec_last_Dream)
	last = res[1]
	last_Dream = last[4]   #C23
	print(last_Dream)
	
	next_dream = round(int(last_Dream)+(int(last_Dream)*(int(last_Dream)-int(sec_last_Dream))/100))
	print(next_dream)

	#OpenDream
	sec_last_OpenDream = sec_last[5]  #C22
	print(sec_last_OpenDream)
	last = res[1]
	last_OpenDream = last[5]   #C23
	print(last_OpenDream)
	
	next_opendream = round(int(last_OpenDream)+(int(last_OpenDream)*(int(last_OpenDream)-int(sec_last_OpenDream))/100))
	print(next_opendream)
	from csv import writer
	Total = 150
	# List 
	List=[todays_date.year,Total,next_mass,next_core,next_dream,next_opendream]
	  
	# Open our existing CSV file in append mode
	# Create a file object for this file
	with open('Companies.csv', 'a') as f_object:
	  
	    # Pass this file object to csv.writer()
	    # and get a writer object
	    writer_object = writer(f_object)
	  
	    # Pass the list as an argument into
	    # the writerow()
	    writer_object.writerow(List)
	  
	    #Close the file object
	    f_object.close()
	data = pd.read_csv("Companies.csv")
	df = pd.DataFrame(data, columns=["Year", "Mass","Core","Dream","Open Dream"])
	df.plot(x="Year", y=["Mass","Core","Dream","Open Dream"], kind="bar", figsize=(9, 8))
	path = "C:/Users/NEVON/Downloads/CampusPlacement (1) (1)/CampusPlacement (1)/CampusPlacement/CampusPlacement/media/"
	mp.title("Companies")
	mp.savefig(path +'company.png')
	mp.show()




	#print(Students)
	'''prediction = model.predict([[todays_date.year,Total]])
				print(prediction)'''
	'''Notplaced = int(Students) - int(prediction)
				print(Notplaced)
				prediction = round(prediction[0])
				print(prediction)
				df = pd.read_csv("Companies.csv")
				df.loc[22, 'Students'] = Students
				df.loc[22, 'Placed'] = prediction
				df.loc[22, 'Companies'] = Companies
				df.loc[22, 'Notplaced'] = Notplaced
				df.to_csv("Companies.csv", index=False)
				data = pd.read_csv("Companies.csv")
				df = pd.DataFrame(data, columns=["Year", "Placed","Notplaced"])
				df.plot(x="Year", y=["Placed","Notplaced"], kind="bar", figsize=(9, 8))
				path = "C:/Users/NEVON/Downloads/CampusPlacement (1) (1)/CampusPlacement (1)/CampusPlacement/CampusPlacement/media/"
				mp.title("MECH")
				mp.savefig(path +'MECH.png')
				mp.show()
			'''
	return redirect('/Forecasting')










'''from csv import wdf.loc[5, 'Name'] = 'SHIV CHANDRA'riter
				List=[Students,prediction,Notplaced]
							#Open our existing CSV file in append mode
							# Create a file object for this file
				with open('Placed2.csv', 'a') as f_object:
					writer_object = writer(f_object)
					f_object.close()'''
'''import matplotlib.pyplot as plt
				import csv
				x = []
				y = []
				with open('Placed2.csv','r') as csvfile:
					plots = csv.reader(csvfile, delimiter = ',')
					for row in plots:
						x.append(row[0])
						y.append(int(row[2]))
			
				plt.bar(x, y, color = 'g', width = 0.72, label = "Placed")
				plt.xlabel('Year')
				plt.xticks(rotation=50)
				plt.ylabel('Placed')
				plt.plot('Year')
				plt.plot('Placed','NotPlaced')
				path = "C:/Users/NEVON/Downloads/CampusPlacement (1) (1)/CampusPlacement (1)/CampusPlacement/CampusPlacement/media/"
				plt.savefig(path +'foo.png')
				plt.title('Number of students placed')
				plt.legend()
				plt.show()'''


def Forecasting(request):
	return render(request,'Forecasting.html',{})


def OffCampus_edit(request,id):
	details = UsseroffCampusPlaced.objects.all().filter(id = id)
	print(details)
	return render(request,'OffCampus_edit.html',{'details':details})