from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from operator import itemgetter
# Create your views here.
def home(request):
    return render(request,'home.html')

def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']
        if password == repassword:
            user = User.objects.create_user(username=username,email=email,password=repassword)
            if user:
                return redirect('civil_work:home')
        else:
            return redirect('civil_work:home')
def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']  
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if request.user.is_authenticated and request.user.is_staff == False:
                return redirect('civil_work:home')
        else:
            return redirect('civil_work:home') 
def log_out(request):
    logout(request)
    return redirect('civil_work:home')
def service_one(request):
    return render(request,'service1.html')

def service_one_result(request):
    if request.method == 'POST':
        rod_length = request.POST['rod_length']
        total_form = request.POST['total_form']

        my_info = []
        for i in range(1,int(total_form) + 1):
            element = dict()
            pic_number = 'number'+str(i)
            size_length = 'lenght'+str(i)
            element['number_pic']= request.POST[pic_number]
            element['rod_length'] = request.POST[size_length]
            my_info.append(element)
        rod_array = [int(rod_length)]*100
        my_info.sort(key=itemgetter('rod_length'),reverse=True)

        for i in my_info:
            pic = i['number_pic']
            size = i['rod_length']
            rod_array.sort()
            for p in range(int(pic)):
                for j in range(len(rod_array)):
                    if int(size) <= rod_array[j]:
                        rod_array[j] = rod_array[j] - int(size)
                        break
        result_list = []
        for i in rod_array:
            if i < int(size):
                result_list.append(i)
        context ={
            'total_rod_use':len(result_list),
            'total_rod':result_list
        }
        # print(result_list)
        # print(len(result_list))
    return render(request,'service-one-result.html',context)

def service_two(request):
    return render(request,'service2.html')

def service_two_result(request):
    if request.method == 'POST':
        rod_length = float(request.POST['rod_length'])
        ring_rod = float(request.POST['ring_rod'])
        piller_height = float(request.POST['piller_height'])
        piller_circle = request.POST['piller_circle']
        circle_space = request.POST['circle_space']
        
        rod_array = [float(rod_length) for i in range(100)]
        total_rod_size = ring_rod * piller_height
        total_full_rod = total_rod_size // rod_length
        over_rod = total_rod_size - (total_full_rod * rod_length)
        for i in range(int(total_full_rod)):
            rod_array[i] = 0
        if over_rod:
            rod_array[total_full_rod] = over_rod
        print(rod_array)

        rod_array.sort()
        total_circle_rod = piller_height / float(circle_space)

        for p in range(int(total_circle_rod)):
            for j in range(len(rod_array)):
                if float(piller_circle) <= rod_array[j]:
                    rod_array[j] = rod_array[j] - float(piller_circle)
                    break

        rod_array.sort() 
        new_rod_list = []
        for i in rod_array:
            if rod_length == i:
                break
            else:
                new_rod_list.append(i)
        print(new_rod_list)
        print(rod_array)
        print(rod_length,ring_rod,piller_height,piller_circle,circle_space)
        context={
            'total_rod':len(new_rod_list),
            'usability':new_rod_list
        }
        return render(request,'service_two_result.html',context)