#once we declare the string we can not modify, if we modify the string new object will be created
s1 = 'kodnest'
s2 = s1.upper()
print(s1, id(s1))
#id method returns the address of the object
print(s2, id(s2))

s3 = 'Hello'
s4 = 'World'
print('s3 ID of H:',id(s3[0]))
print('s4 ID of w:',id(s4[0]))
print('\n')
print('s3 ID of O:',id(s3[-1]))
print('s4 ID of O:',id(s4[1]))

'''
1. Python internally uses String Interning

2.String Interning is the process of checking string intern pool
before creating any new objects.

3.whenever we want to create new object, python first will check
string intern pool, weather that object already exist or not.

4.when object already exist in the  string intern records then address of 
existing object will be reused
'''