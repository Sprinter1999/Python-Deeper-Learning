s=''
s=input("input a string,then alter to latin-pig mode")
result=''
flag=False
spec=''
for each in s:
    result+=each
    if flag==False:
        if each!="a"or"e"or"i"or"o"or"u":
            flag=True
            spec=each
            result=result[:-1]
spec_str=''+'-'+spec+'ay'
result+=spec_str
print(result)