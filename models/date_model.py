from odoo import models, fields, api

from datetime import datetime

import datetime, math

from dateconversion import *

# import pycurl
# import os

class Date(models.Model):
    _name = 'date'
    english_date = fields.Date(required=True, string='English Date')



    @api.one
    @api.model
    @api.depends('english_date')
    def _converttonepali(self):
        try:
            inputdata=str(self.english_date)
            dt = datenepali()
            converted_date = dt.converttonepali(inputdata)
            self.nep_date = converted_date
        except ValueError:
            return 'Enter Date.'

    nep_date = fields.Char(compute='_converttonepali', store=True, string='Nepali Date')

    # _converttonepali(english_date, nep_date)














































































































































































            #
# def converttoenglish(nepdate):
#     lapseddays=0
#     years=int(nepdate[0:4])
#     months=int(nepdate[5:7])
#     days=int(nepdate[8:])-1
#     for items in nepali_date:
#         if years==items[0]:
#             for monthdays in range(1,13):
#                 if months==monthdays:
#                     break
#                 if months!=monthdays:
#                     lapseddays=lapseddays+items[monthdays]
#             break
#         if years!=items[0]:
#             for monthdays in range(1,13):
#                 lapseddays=lapseddays+items[monthdays]
#     lapseddays=lapseddays+days
#     # englishdate=start_english+lapseddays
#     return start_english+datetime.timedelta(days=lapseddays)
#
# def validatedata(datedata,datetype):
#     #validates data type=1 if nepali and type=2 if english
#     try:
#         years=int(datedata[0:4])
#     except:
#         return False
#     try:
#         months=int(datedata[5:7])
#     except:
#         return False
#     try:
#         days=int(datedata[8:])
#     except:
#         return False
#
#     validated=False
#     if not isinstance(years,int) and isinstance(months,int) and isinstance(days,int):
#         return validated
#     if datetype==1:
#         for items in nepali_date:
#             if years==items[0]:
#                 for monthsarray in range(1,13):
#                     if months==monthsarray:
#                         if days<=items[monthsarray]:
#                             validated=True
#     if datetype==2:
#         try:
#             datev=datetime.date(years,months,days)
#             if datev<start_english or datev>end_english:
#                 validated=False
#             else:
#                 validated=True
#         except:
#             validated=False
#     return validated
#
#
#
#
#
#
#
# if __name__=="__main__":
#     a=input("Insert Type(1=Nepali,2=English)")
#     validation=False
#     inputdate=None
#     if int(a)==2:
#         inputdata=input("Insert Date")
#         try:
#             inputdate=datetime.date(int(inputdata[0:4]),int(inputdata[5:7]),int(inputdata[8:]))
#             validation=validatedata(inputdata,2)
#         except:
#             validation=False
#         if validation==True:
#             print (converttonepali(inputdate))
#     if int(a)==1:
#         abc=input("Insert Date")
#         validation=validatedata(abc,1)
#         print (validation)
#         if validation==True:
#             print (converttoenglish(abc))



# inputdate=input(self)