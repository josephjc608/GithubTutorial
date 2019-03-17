#!/usr/bin/env python
# coding: utf-8

# In[3]:
#test

class TestClass:  #Class name in Caps fisrt char
    'This is a test'
    info='Istore name as information'
    
    def __init__(self, name):
        self.name=name
    
    def get_name(self):
        return self.name
   #pass


# In[6]:


test1=TestClass('Joseph1')
test1.get_name()


# In[7]:


test2=TestClass('Joseph2')


# In[8]:


TestClass.get_name(test2)


# In[10]:


test2.get_name()


# In[11]:


test2.info 


# In[12]:


test2.__doc__ #Get doc string of class


# In[13]:


from datetime import datetime


# In[27]:


class PersonInfo:
    'Class to creatr perdons profile'
    
    print_history=0
    def __init__(self, fname,lname,dob):
        'Get first and last name & dob in mmddyyyy format'
        self.fname=fname
        self.lname=lname
        self.dob=dob
        
    def fullname(self):
        'Creates fullname by adding first and last name'
        return self.fname+' ' +self.lname
    
    def age(self):
        curr_year=datetime.today().year
        birth_year=datetime.strptime(self.dob,'%m%d%Y').year
        return curr_year -birth_year

    def generate_email_id(self):
        'Generates emai id in format fname.lname@company.com'
        return self.fname.lower()+'.'+self.lname.lower()+'@company.com'
    
    def employeeID(self):
        return self.fname+self.dob
    
    def print_profile(self):
        print('Complete Profile of '+self.fullname())
        print('='*43+'\n')
        print('{:10s} | {:20s}'.format('Employee ID', self.employeeID()))
        print('{:10s} | {:20s}'.format('-'*10, '-'*20))
        print('{:10s} | {:20s}'.format('Full Name', self.fullname()))
        print('{:10s} | {:20s}'.format('-'*10, '-'*20))
        print('{:10s} | {:20s}'.format('Email ID', self.generate_email_id()))
        print('{:10s} | {:20s}'.format('-'*10, '-'*20))
        print('{:10s} | {:20s}'.format('Age', str(self.age())))
        self.print_history +=1
        
        


# In[29]:


me=PersonInfo('Joseph','C','12071980')


# In[ ]:





# In[21]:


me.print_history


# me.fullname()

# In[23]:


me.print_history


# In[30]:


me.generate_email_id()


# In[31]:


me.age()


# In[32]:


me.employeeID()


# In[35]:


me.print_profile()


# In[36]:


me.print_history


# In[38]:


PersonInfo.print_history ###it will be 0 as we are not chnaging globally


# In[ ]:


### Class Challenge

1. Create a call called BankAccount
2. Class should be initiated with following names:

   2.1. Full Name

   2.2. PAN

   2.3. Balance - 1000 (Default value. Ensure this value is never negative)


3. Create a method to check current balance
4. Create a method to add money (Balance must be updated. Create log for transactions.)
5. Create a method to withdraw money (Balance must be updated. Cant withdraw more than balance. Create log for transactions.)
6. Create a method to get last 5 transactions


# In[ ]:


#Git


# In[1]:


class BankAccount:
    'Class to maintain bank account'
    
    print_history=0
    list1=[]
    def __init__(self, fname,pan,bal):
        'Get first name,pan  & bal amt'
        self.fname=fname
        self.pan=pan
        self.bal=bal
    
    def fullname(self):
        'Returns fullname '
        return self.fname
    
    def panid(self):
        'Returns PAN'
        return self.pan
    
    def balamt(self):
        'Returns Balance'
        return self.bal
    
    def depbalamt(self,dep):
        'Returns Balance'
        self.bal=self.bal+dep
        self.list1.append(dep)
        return self.bal
    
    def wdwbalamt(self,wdw):
        'Returns Balance'
        temp_bal=self.bal
        self.bal=self.bal-wdw
        if self.bal<0 :
            self.bal=temp_bal
            print('Cannot withdraw more than balance amount')
        else:
            self.list1.append(wdw)    
        return self.bal
        
    def lst5tran(self):
        if len(self.list1)<=5:
            print(self.list1)
        else :    
            print(self.list1[-5:])
        
        
    def chk_currbal(self):
        print('Current Balance  of '+self.fullname())
        print('='*43+'\n')
        print('{:10s} | {:20s}'.format('PAN', self.panid()))
        print('{:10s} | {:20s}'.format('-'*10, '-'*20))
        print('{:10s} | {:20s}'.format('Balance', str(self.balamt())))
        self.print_history +=1
        
        


# In[2]:


bank=BankAccount('Joseph','C1',2000)


# In[ ]:





# In[5]:


bank.fullname()


# In[6]:


bank.panid()


# In[3]:


bank.balamt()


# In[131]:


bank.chk_currbal()


# In[4]:


bank.depbalamt(100)


# In[5]:


bank.wdwbalamt(50)


# In[6]:


bank.lst5tran()


# In[135]:


lsi2=[1,2,3,4,5,6,7]


# In[153]:


lsi2[-5:]
len(lsi2)


# In[ ]:


Challenge #1 - Tax Calculator

Calculate the tax payable...based on investment sections and limits
Consider tax slabs for taxation.FY2018-19

* Create a class TaxCalculator which takes annual CTC as input

* Create a method to get the individual components of the annual CTC as follows

    * Basic = 40% of CTC

    * HRA = 30% of CTC

    * Conveyance Allowance = 2% of CTC

    * Medical Allowance = 2% of CTC

    * Statutory Bonus = 1% of CTC

    * Other Allowance = 25% of CTC

* Create a method to accept investments and rent paid (Check for maximum limits in investments)

* Create a method to calulate the net taxable income

* Create a method to calculate the total tax after deductions and investments

* Deductions in salary:

    * Annual Professional Tax - 2400

    * Annual Provident Fund - 21600

* Standard deduction for FY 2018-19 - 40000

    

**References:**



1. https://cleartax.in/s/income-tax-basics-for-beginners

2. https://cleartax.in/paytax/TaxCalculator



**Note:**



* This is a real world project

* Handle Exceptions and have proper validation conditions

* Use proper docstrings (https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html)

* Understand the use of configuration files (Optional) for standard deduction and exemptions limit based on FY--like paramter file for storage of pwd etc
eg name.ini
use import configparser for this 



# In[ ]:





# In[92]:


class TaxCalculator:
    'Class to calculate tax'
    invdtls = {}
    print_history=0
    list1=[]
    
    def __init__(self, empid,fname,ctc):
        'Get empid first name ctc  '
        self.empid=empid
        self.fname=fname
        self.ctc=ctc
        
        
    def nettaxableincome(self):
        'Returns Net Taxable Income'
        conveyance_allowance=(self.ctc*0.02)
        annual_professional_tax=2400
        standard_deduction=40000
        net_tax_income=self.ctc-conveyance_allowance-annual_professional_tax-standard_deduction    
        return net_tax_income
    
    def investmentinput(self):
        'Input the investments'
        #invdtls = { 'empid' : 0, 'name' : 'a', 'ppf' : 0, 'rent' : 0}
        
        self.invdtls['empid'] = self.empid
        self.invdtls['name'] = self.fname
        v_ppf = input("Input PPF amt ")
        self.invdtls['ppf'] = v_ppf
        v_rent = input("Input Rent paid amt ")
        self.invdtls['rent'] = v_rent
        print(self.invdtls)
        for k,v in self.invdtls.items():
            if k=='empid' and v==123:
                print(k, 'corresponds to', v)
    
    def checklimit(self):
        'Check against limits'
        limit_80cc=150000
        print(self.invdtls)
        for k,v in self.invdtls.items():
            print(k, 'corresponds to', v)        
        
        
        
        
        
    


# In[93]:


myTax=TaxCalculator(123,'XYZ',100000)


# In[94]:


myTax.nettaxableincome()


# In[95]:


myTax.investmentinput()


# In[96]:


myTax.checklimit()

