from django.shortcuts import render



from django.shortcuts import render


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
    
    # This tells Django to render the 'index.html' template with the context data
    return render(request, 'web/index.html', context)

