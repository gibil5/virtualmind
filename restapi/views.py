"""
virtualmind - View

"""
from django.shortcuts import render

# Create your views here.
def helloworld(request, args):
    print('helloworld')
    print(request)
    print(args)
    arr = args.split(',')
    print(arr)
    res = 1 
    for arg in arr: 
        arg_int = int(arg)
        res = res * arg_int
    print(res)    
    return render(request, "restapi/hello.html", {
        "result":  res,        
    })

