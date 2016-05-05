x = 1
# x = <expr> # Assign statement
# x = 1
def foo(var):
	if var > 0:
		print "Var is greater than 0"
	return var + x

print foo(5)


foo(4) + 4 # function_call <expr> + <expr>
