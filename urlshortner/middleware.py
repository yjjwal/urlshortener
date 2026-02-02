from django.shortcuts import redirect
# authentication
def auth(view_function):
    def wrapped(request,*args,**kwargs):
        if request.user.is_authenticated == False:
            return redirect('login')
        return view_function(request,*args,**kwargs)
    return wrapped
# for Guest
def guest(view_function):
    def wrapped(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return view_function(request,*args,**kwargs)
    return wrapped 