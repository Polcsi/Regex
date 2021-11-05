import re
import traceback

class Formats:
    
    __format_types = []
    __types = []
    
    def __new__(cls, *args, **kwargs):
        instance = super(__class__, cls).__new__(cls)
        return instance       
    
    def __init__(self, type: str, check_str: str):
        
        assert type in __class__.__types, f"Invalid Format Type! Format can be: {__class__.__types}."
        
        self.type = type
        self.check_str = check_str
        (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
        self.instance_name = text[:text.find('=')].strip()
        __class__.__search_format(self, searched_format=type, func=lambda idx, key, value: (setattr(self, 'pattern', value)))
    
    def __search_format(self, method = None, searched_format: str = None, func = None):
        if __class__.__format_types:
            for idx, num in enumerate(__class__.__format_types):
                for key, value in num.items():
                    if key == searched_format and func == None:
                        return [idx, value]
                    elif  key == searched_format and func != None:
                        if method == None or method == "remove": func(idx, key, value)
                        return False
            if func != None: 
                if method == None or method == "add": func(idx=0, key=None, value=None)
                return True
            return False
        else:
            if method == "add": func(idx=0, key=None, value=None)
            if method == "remove": print("Format list is empty!")
            return True
        
    def __check(self):
        if re.fullmatch(self.pattern, self.check_str):
            return True
        else:
            return False
    
    def checkPattern(self):
        if self.__check():
            print(f'Match \'{self.type}\' pattern! In this string (\'{self.check_str}\').')
        else:
            print(f'Invalid \'{self.type}\' pattern! In this string (\'{self.check_str}\').')
    
    @classmethod     
    def addNewFormat(cls, format_type: str, format: str):
        def add(): 
            add = {f"{format_type}": format}
            cls.__format_types.append(add)
            cls.__types.append(format_type)
            print(f"Added new format type as '{format_type}'!")
        
        execute = cls.__search_format(cls, method="add", searched_format=format_type, func=lambda idx, key, value: add())
        if execute == False: print(f"'{format_type}' format is already added")
                
    @classmethod
    def removeFormat(cls, format_type: str):
        def remove(index):
            del cls.__format_types[index]
            del cls.__types[index]
            print(f"Removed '{format_type}' format!")
            
        execute = cls.__search_format(cls, method="remove", searched_format=format_type, func=lambda idx, key, value: remove(idx))
        if execute: print(f"There is no '{format_type}' format!")
    
    def __repr__(self):
        return f'{__class__.__name__}("{self.type}", "{self.check_str}")'
    
    def __str__(self):
        return f'{self.instance_name} = {__class__.__name__}("{self.type}", "{self.check_str}")'
    
    @property
    def types(self):
        return self.__types
    
    @property
    def format_types(self):
        return self.__format_types

Formats.removeFormat("email")
Formats.addNewFormat("email", r'\b[A-Za-z0-9._,%+-]+@[A-Za-z._]+\.[A-Z|a-z]{2,}\b') # polcsi.code@gmail.com
Formats.addNewFormat("email", r'\b[A-Za-z0-9._,%+-]+@[A-Za-z._]+\.[A-Z|a-z]{2,}\b') 
email = Formats("email", "polcsi.code@gmail.com")
email.checkPattern()
Formats.addNewFormat("us_phone_number", r'\+1-[0-9]{3,3}\-[0-9]{3,3}\-[0-9]{4,4}') # +1-212-456-7890
Formats.addNewFormat("uk_phone_number", r'\+44\s[0-9]{4,4}\s[0-9]{6,6}') # +44 7911 123456
Formats.addNewFormat("ger_phone_number", r'\+49\s[0-9]{2,4}\s[0-9]{6,7}') # +49 1522 3433333 +49 221 2345678  +49 30 901820
Formats.addNewFormat("sa_phone_number", r'\+27\s\([3|2|5]1+\)\s[0-9]{3,3}\s[0-9]{4,4}') # +27 (21) 123 4567
Formats.addNewFormat("hu_phone_number", r'\+36 [3|2|7]0+/[0-9]{3,3}\-[0-9]{4,4}') # +36 30/742-2936

hu = Formats("hu_phone_number", "+36 30/742-2936")
hu.checkPattern()
uk = Formats("uk_phone_number", "+44 7911 123456")
us = Formats("us_phone_number", "+1-212-456-7890")
ger = Formats("ger_phone_number", "+49 30 901820")
sa = Formats("sa_phone_number", "+27 (21) 123 4567")
    
Formats.addNewFormat("uk_phone_number", r'\+44\s[0-9]{4,4}\s[0-9]{6,6}') # +44 7911 123456
Formats.removeFormat("uk_phone_number")

Formats.removeFormat("us_phone_number")
Formats.removeFormat("us_phone_number")
Formats.removeFormat("ger_phone_number")
Formats.removeFormat("ger_phone_number")
Formats.removeFormat("sa_phone_number")
Formats.removeFormat("sa_phone_number")
Formats.removeFormat("hu_phone_number")
Formats.removeFormat("hu_phone_number")
print(sa.types)
print(sa.format_types)
print(sa)