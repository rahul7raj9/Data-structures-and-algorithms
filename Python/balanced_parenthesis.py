##BALANCED PARENTHESIS

def is_balanced(in_str):
	symbol_dict={'{':'}','(':')','[':']'}
	stack=[]
	bool_is_balanced=True
	for c in in_str:
		if c in symbol_dict.keys():
			stack.append(c)
		elif len(stack)!=0 and c in symbol_dict.values():
			symbol=stack.pop()
			if symbol_dict.get(symbol)!=c:
				bool_is_balanced=False
				break
	return bool_is_balanced
	
print(is_balanced('{{([][])}()}'))
print(is_balanced('[{()]'))
			
