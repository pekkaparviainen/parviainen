""" Check repo """
from parviainen.session3 import ContextManager, CourseRepo
import sys

if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    print "Error: Too few arguments"
    exit()

temp = path.rpartition('/')
surname = temp[-1]

context = ContextManager(path)
context.__enter__()

repo = CourseRepo(surname)
if repo.check():
    print 'PASS'
else:
    print 'FAIL'
    
context.__exit__(None, None, None)