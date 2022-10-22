from django.shortcuts import render

from my_app.models import Familia

# Create your views here.
def familias(request):
    familias = Familia.objects.all()

    context_dict = {"familias": familias}

    return render(
        request=request,
        context=context_dict,
        template_name="my_app/familia_list.html",


    )
