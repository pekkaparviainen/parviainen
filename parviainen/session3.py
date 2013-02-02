""" Session 3 """
import os, os.path

""" Context manager"""
class ContextManager(object):
    def __init__(self, target):
        self.current_dir = None
        self.new_dir = target
        
    def __enter__(self):
        self.current_dir = os.getcwd()
        os.chdir(self.new_dir)
    
    def __exit__(self, type, value, traceback):
        os.chdir(self.current_dir)
      
""" CourseRepo class """       
class CourseRepo(object):
    required = [ ".git", "setup.py", "README.md", "scripts/getting_data.py", "scripts/check_repo.py", "lastname/__init__.py", "lastname/session3.py"]
    lastname = None

    def __init__(self, surname):
        self.lastname = surname
        self.required[-1] = self.lastname + '/session3.py'
        self.required[-2] =  self.lastname + '/__init__.py'
        
    @property
    def surname(self):
        return self.lastname
    
    @surname.setter
    def surname(self, value):
        self.lastname = value
        self.required[-1] = self.lastname + '/session3.py'
        self.required[-2] =  self.lastname + '/__init__.py'
        
    def check(self):
        for i in range(len(self.required)):
            if not os.path.exists(self.required[i]):
                print 'File ' + self.required[i] + ' does not exist!' 
                return False
        return True