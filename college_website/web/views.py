# web/views.py

from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Corrected Signup View
def signup_view(request): # Renamed to standard Python convention (snake_case)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('resource_hub')
        # If form is NOT valid, we no longer have an 'else' block.
        # The function will continue to the render statement below,
        # passing the form with its errors back to the template.
    else:
        # This runs for a GET request (when a user first visits the page)
        form = UserCreationForm()
        
    return render(request, 'web/signup.html', {'form': form})

# Login View (This was already correct)
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('resource_hub')
    else:
        form = AuthenticationForm()
    return render(request, 'web/login.html', {'form': form})

# Logout View (This was already correct)
def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('resource_hub')

# About View (No longer duplicated)
def about(request):
    return render(request, 'web/about.html')



def resource_hub(request):
    
    resources = [
      {'id': 1, 'name': 'Advanced Algorithms Notes', 'type': 'pdf', 'branch': 'Computer Science', 'year': 4, 'category': 'Study Material'},
      {'id': 2, 'name': 'Thermodynamics PYQ 2022', 'type': 'pdf', 'branch': 'Mechanical', 'year': 2, 'category': 'Previous Year Papers'},
      {'id': 3, 'name': 'Data Structures in C++', 'type': 'epub', 'branch': 'Computer Science', 'year': 2, 'category': 'E-books'},
      {'id': 4, 'name': 'Fluid Mechanics Lab Report', 'type': 'docx', 'branch': 'Civil', 'year': 3, 'category': 'Study Material'},
      {'id': 5, 'name': 'Digital Electronics Mid-Sem', 'type': 'pdf', 'branch': 'Electronics', 'year': 2, 'category': 'Previous Year Papers'},
      {'id': 6, 'name': 'Operating Systems by Galvin', 'type': 'pdf', 'branch': 'Computer Science', 'year': 3, 'category': 'E-books'},
      {'id': 7, 'name': 'Engineering Drawing Practice', 'type': 'pdf', 'branch': 'Mechanical', 'year': 1, 'category': 'Study Material'},
      {'id': 8, 'name': 'Strength of Materials - 2023', 'type': 'pdf', 'branch': 'Civil', 'year': 2, 'category': 'Previous Year Papers'},
    ]

    context = {
        'resources': resources,
        'branches': ['Computer Science', 'Mechanical', 'Civil', 'Electronics'],
        'years': [1, 2, 3, 4],
        'categories': ['Previous Year Papers', 'Study Material', 'E-books']
    }
    

    return render(request, 'web/home.html', context)

