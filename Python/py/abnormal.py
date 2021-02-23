try:
	a = 1/0
except ZeroDivisionError as e:
	print(e)
except ValueError as ve:
	print(ve)
else:
	print('else')
finally:
	print('finally')
	
#----- raise 抛出异常 -------

def demo():
	a = 1
	b = 2
	
	if a < b:
		raise ValueError('reason')
	
	print(a,b)
	
try:
	demo()
except ValueError as e:
	print('error:', e)
	
#---- assert 调试程序 抛出AssertionError ---------
# assert expression [,reason]

try:
	assert 1 < 2 , ' true'
except AssertionError as ae:
	print(ae)