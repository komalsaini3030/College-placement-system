from django.db import models
                           
# Create your models here.
class admindata(models.Model):
    Username = models.CharField(max_length=100 ,default = None)
    Password = models.CharField(max_length=100 ,default = None)

    class Meta:
        db_table = 'admindata'

class CompanyDetails(models.Model):
    CompanyName = models.CharField(max_length=100 ,default = None)
    Package = models.CharField(max_length=100 ,default = None)
    File = models.FileField(upload_to = 'media' ,default = None)
    Pre_Placement = models.DateTimeField()
    Test_Date = models.DateTimeField()
    Interview_Date = models.DateTimeField()
    
    Additional_Information = models.CharField(max_length=100 ,default = None)
    CGPA = models.CharField(max_length=100 ,default = None)
    CSl =models.CharField(max_length=100 ,default = None,blank = True)
    IS = models.CharField(max_length=100 ,default = None,blank = True)
    ECE = models.CharField(max_length=100 ,default = None,blank = True)
    EEE = models.CharField(max_length=100 ,default = None,blank = True)
    MECH = models.CharField(max_length=100 ,default = None,blank = True)
    IP = models.CharField(max_length=100 ,default = None,blank = True)
    CIVIL = models.CharField(max_length=100 ,default = None,blank = True)      
    ALL_BRANCHES = models.CharField(max_length=100 ,default = None,blank = True) 
    OTHERS = models.CharField(max_length=100 ,default = None,blank = True)
    CATEGORY = models.CharField(max_length=100 ,default = None,blank = True)
    
    class Meta:
        db_table = 'CompanyDetails'


class Student_Details(models.Model):
    # Personal Details
    Name = models.CharField(max_length=100,default=None,null=True)
    uname = models.CharField(max_length=100,default=None,null=True)
    password = models.CharField(max_length=100,default=None,null=True) 
    USN = models.CharField(max_length=100,default=None,null=True)
    Date_of_Birth  = models.CharField(max_length=100,default=None,null=True)
    Gender  = models.CharField(max_length=100,default=None,null=True)
    Category = models.CharField(max_length=100,default=None,null=True)

    # Current Educational details
    Mode_of_admission = models.CharField(max_length=100,default=None,null=True)
    Engineering_branch = models.CharField(max_length=100,default=None,null=True)
    Section  = models.CharField(max_length=100,default=None,null=True)
    Year_of_joining = models.IntegerField(default=None,null=True)
    Year_of_passing = models.IntegerField(default=None,null=True)
    first_sem_SGPA = models.IntegerField(default=None,null=True)
    first_sem_percentage = models.IntegerField(default=None,null=True)
    second_sem_SGPA = models.IntegerField(default=None,null=True)
    second_sem_percentage = models.IntegerField(default=None,null=True)
    third_sem_SGPA = models.IntegerField(default=None,null=True)
    third_sem_percentage = models.IntegerField(default=None,null=True)
    fourth_sem_SGPA = models.IntegerField(default=None,null=True)
    fourth_sem_percentage = models.IntegerField(default=None,null=True)
    fifth_sem_SGPA = models.IntegerField(default=None,null=True)
    fifth_sem_percentage = models.IntegerField(default=None,null=True)
    Total_CGPA = models.IntegerField(default=None,null=True)
    Total_CGPA_per = models.IntegerField(default=None,null=True)
    TOTAL_CREDITS_EARNED_UPTO_5TH_SEMESTER  = models.IntegerField(default=None,null=True)
    NUMBER_OF_SUBJECTS_CLEARED_IN_MUTE  = models.IntegerField(default=None,null=True)
    CURRENT_ARREARS  = models.IntegerField(default=None,null=True)

    # Previous educational details 
    tenth_SSLC_percentage = models.IntegerField(default=None,null=True)
    tenth_sslc_board = models.CharField(max_length = 100,default=None,null=True)
    Name_of_institution_studied_in_10th_sslc= models.CharField(max_length = 100,default=None,null=True)
    tenth_sslc_qualified_year = models.IntegerField(default=None,null=True)
    twelveth_PUC_percentage = models.IntegerField(default=None,null=True)
    twelveth_PUC_board = models.CharField(max_length = 100,default=None,null=True)
    Name_of_the_institution_studied_12th_Puc= models.CharField(max_length = 100,default=None,null=True)
    twelveth_PUC_qualified_year = models.IntegerField(default=None,null=True)
    Diploma_percentage  = models.CharField(max_length = 100,default=None,null=True)
    Diploma_CET_percentage  = models.CharField(max_length = 100,default=None,null=True)
    Name_of_the_institution_studied_diploma= models.CharField(max_length = 100,default=None,null=True)
    Diploma_qualified_year = models.CharField(max_length = 100,default=None,null=True)

    #Contact Details
    contact_number  = models.CharField(max_length=100,default=None,null=True)
    LANDLINE_NUMBER  = models.CharField(max_length=100,default=None,null=True)
    PARENTS_NUMBER  = models.CharField(max_length=100,default=None,null=True)
    Alternate_contact_number  = models.CharField(max_length=100,default=None,null=True)
    EMAIL_ID  = models.EmailField(max_length=100,default=None,null=True)
    College_mail = models.EmailField(max_length=100,default=None,null=True)
    CURRENT_ADDRESS  = models.CharField(max_length=100,default=None,null=True)
    PERMANENT_ADDRESS  = models.CharField(max_length=100,default=None,null=True)
    class Meta:
        db_table = 'Student_Details'

class StudentApplication(models.Model):
    Student_id  = models.CharField(max_length=100,default=None,null=True)
    Student_name= models.CharField(max_length=100,default=None,null=True)
    Company_id  = models.CharField(max_length=100,default=None,null=True)
    Company_name= models.CharField(max_length=100,default=None,null=True)
    Status      =  models.CharField(max_length=100,default=None,null=True)
    Student_USN = models.CharField(max_length = 100,default = None,null=True)
    Select_status = models.CharField(max_length=100,default='Not Updated',null=True)
    Student_Category = models.CharField(max_length = 100,default = None,null=True)
    class Meta:
        db_table = 'StudentApplication' 

# class All_Information(models.Model):
#     Name = models.CharField(max_length=100,default=None,null=True) 
#     USN = models.CharField(max_length=100,default=None,null=True)
#     Date_of_Birth  = models.CharField(max_length=100,default=None,null=True)
#     Gender  = models.CharField(max_length=100,default=None,null=True)
#     Category = models.CharField(max_length=100,default=None,null=True)
#     Mode_of_admission = models.CharField(max_length=100,default=None,null=True)
#     Engineering_branch = models.CharField(max_length=100,default=None,null=True)
#     Section  = models.CharField(max_length=100,default=None,null=True)
#     Year_of_joining = models.CharField(max_length=100,default=None,null=True)
#     Year_of_passing = models.CharField(max_length=100,default=None,null=True)
#     first_sem_SGPA = models.CharField(max_length=100,default=None,null=True)
#     first_sem_percentage = models.CharField(max_length=100,default=None,null=True)
#     second_sem_SGPA = models.CharField(max_length=100,default=None,null=True)
#     second_sem_percentage = models.CharField(max_length=100,default=None,null=True)
#     Mode_of_admission = models.CharField(max_length=100,default=None,null=True)
#     Engineering_branch = models.CharField(max_length=100,default=None,null=True)
#     Section  = models.CharField(max_length=100,default=None,null=True)
#     Year_of_joining = models.CharField(max_length=100,default=None,null=True)
#     Year_of_passing = models.CharField(max_length=100,default=None,null=True)
#     first_sem_SGPA = models.CharField(max_length=100,default=None,null=True)
#     first_sem_percentage = models.CharField(max_length=100,default=None,null=True)
#     second_sem_SGPA = models.CharField(max_length=100,default=None,null=True)
#     second_sem_percentage = models.CharField(max_length=100,default=None,null=True)
#     third_sem_SGPA = models.CharField(max_length=100,default=None,null=True)
#     third_sem_percentage = models.CharField(max_length=100,default=None,null=True)
#     fourth_sem_SGPA = models.CharField(max_length=100,default=None,null=True)
#     fourth_sem_percentage = models.CharField(max_length=100,default=None,null=True)
#     fifth_sem_SGPA = models.CharField(max_length=100,default=None,null=True)
#     fifth_sem_percentage = models.CharField(max_length=100,default=None,null=True)
#     Total_CGPA = models.CharField(max_length=100,default=None,null=True)
#     Total_CGPA = models.CharField(max_length=100,default=None,null=True)
#     TOTAL_CREDITS_EARNED_UPTO_5TH_SEMESTER  = models.CharField(max_length=100,default=None,null=True)
#     NUMBER_OF_SUBJECTS_CLEARED_IN_MUTE  = models.CharField(max_length=100,default=None,null=True)
#     CURRENT_ARREARS  = models.CharField(max_length=100,default=None,null=True)
#     NUMBER_OF_SUBJECTS_CLEARED_IN_MUTE  = models.CharField(max_length=100,default=None,null=True)
#     tenth_SSLC_percentage = models.CharField(max_length=100,default=None,null=True)
#     tenth_sslc_board = models.CharField(max_length=100,default=None,null=True)
#     Name_of_institution_studied_in_10th_sslc        = models.CharField(max_length=100,default=None,null=True)
#     tenth_sslc_qualified_year = models.CharField(max_length=100,default=None,null=True)
#     twelveth_PUC_percentage = models.CharField(max_length=100,default=None,null=True)
#     twelveth_PUC_board = models.CharField(max_length=100,default=None,null=True)
#     Name_of_the_institution_studied_12th_Puc        = models.CharField(max_length=100,default=None,null=True)
#     twelveth_PUC_qualified_year = models.CharField(max_length=100,default=None,null=True)
#     Diploma_percentage  = models.CharField(max_length=100,default=None,null=True)
#     Diploma_CET_percentage  = models.CharField(max_length=100,default=None,null=True)
#     Name_of_the_institution_studied_diploma         = models.CharField(max_length=100,default=None,null=True)
#     Diploma_qualified_year = models.CharField(max_length=100,default=None,null=True)
#     contact_number  = models.CharField(max_length=100,default=None,null=True)
#     LANDLINE_NUMBER  = models.CharField(max_length=100,default=None,null=True)
#     PARENTS_NUMBER  = models.CharField(max_length=100,default=None,null=True)
#     Alternate_contact_number  = models.CharField(max_length=100,default=None,null=True)
#     EMAIL_ID  = models.CharField(max_length=100,default=None,null=True)
#     College_mail = models.CharField(max_length=100,default=None,null=True)
#     CURRENT_ADDRESS  = models.CharField(max_length=100,default=None,null=True)
#     PERMANENT_ADDRESS  = models.CharField(max_length=100,default=None,null=True)
#     Student_id  = models.CharField(max_length=100,default=None,null=True)
#     Student_name= models.CharField(max_length=100,default=None,null=True)
#     Company_id  = models.CharField(max_length=100,default=None,null=True)
#     Company_name= models.CharField(max_length=100,default=None,null=True)
#     Status      =  models.CharField(max_length=100,default=None,null=True)
#     class Meta:
#         db_table = 'All_Information'


class CollegeLogin(models.Model):
    username = models.CharField(max_length=100,default=None)
    password = models.CharField(max_length=100,default=None)
    class Meta:
        db_table = 'CollegeLogin'

class offCampusPlaced(models.Model):
    USN = models.CharField(max_length=100,default=None)
    CompanyName = models.CharField(max_length=100,default=None)
    package = models.CharField(max_length=100,default=None)
    proof = models.FileField()

    class Meta:
        db_table = 'offCampusPlaced'


class CompanyDetails11(models.Model):
    CompanyName = models.CharField(max_length=100 ,default = None)
    Package = models.CharField(max_length=100 ,default = None)
    File = models.FileField(upload_to = 'media' ,default = None,null = True)
    Pre_Placement = models.DateTimeField()
    Test_Date = models.DateTimeField()
    Interview_Date = models.DateTimeField()
    
    Additional_Information = models.CharField(max_length=100 ,default = None)
    CGPA = models.CharField(max_length=100 ,default = None)
    Stream = models.TextField(max_length = 100,default = None)
    OTHERS = models.CharField(max_length=100 ,default = None,blank = True)
    CATEGORY = models.CharField(max_length=100 ,default = None,blank = True)
    Category_Number = models.CharField(max_length = 100,default = None,null = True)
    class Meta:
        db_table = 'CompanyDetails11'


class UsseroffCampusPlaced(models.Model):
    USN = models.CharField(max_length=100,default=None)
    CompanyName = models.CharField(max_length=100,default=None)
    package = models.CharField(max_length=100,default=None)
    proof = models.FileField()

    class Meta:
        db_table = 'UsseroffCampusPlaced'














