from django.shortcuts import render,redirect,get_object_or_404
from .forms import ShortURLForm
from .utils import generate_short_code
from .models import ShortURL
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def create_short_url(request):
    if request.method =="POST":
        form = ShortURLForm(request.POST)
        if form.is_valid():
            short_url = form.save(commit=False)
            short_url.user = request.user
            short_url.short_code = generate_short_code()
            short_url.save()
            return redirect('dashboard') 
    else:
        form = ShortURLForm()
    return render(request,'shortner/create.html',{'form':form})
def redirect_short(request,short_code):
    short_url = get_object_or_404(ShortURL,short_code=short_code)
    short_url.clicks+=1
    short_url.save(update_fields=['clicks'])
    return redirect(short_url.original_url)
def delete(request,pk):
    remove = get_object_or_404(ShortURL,pk=pk)
    remove.delete()
    return redirect('dashboard')