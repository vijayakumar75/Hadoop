import sys

try:
    print 5/0
except Exception as e:
    print "exception is " , type(e) , e

print "life goes on..."
                                                   
