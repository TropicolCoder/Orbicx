from django.shortcuts import render, get_object_or_404
from .models import Project, Category, Image, Member


# Create your views here.
def home(request):
    projects = Project.objects.order_by('-created')[:8]
    categories = Category.objects.all()
    members = Member.objects.all()
    context = {
        'projects': projects,
        'categories': categories,
        'members': members,
    }
    return render(request, 'base.html', context)


def portfolio(request):
    projects = Project.objects.order_by('-created')
    categories = Category.objects.all()
    context = {
        'projects': projects,
        'categories': categories,
    }
    return render(request, 'portfolio/portfolio.html', context)


def project_detail(request, project, category):
    work = get_object_or_404(Project, category__slug=category, slug=project)
    # if the main_image of the project and the other related images are available
    main_image = work.main_image
    images = Image.objects.filter(project=work)

    return render(request, 'portfolio/detail.html', {'project': work, 'images': images, 'main_image': main_image})
