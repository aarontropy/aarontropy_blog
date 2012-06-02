import os
def abs_path(*x):
	return os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

print(abs_path('static/'))

