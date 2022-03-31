# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from itertools import count
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from soupsieve import select
from .models import Colaborador


from apps.home.models import Colaborador, Aso, Epi


# @login_required(login_url="/login/")
# def index(request):
#     context = {'segment': 'index'}
#     colaboradores = Colaborador.objects.all()

#     html_template = loader.get_template('home/index.html', {'colaboradores':colaboradores,})
#     return HttpResponse(html_template.render(context, request),
# )



def index(request):
     colaboradores = Colaborador.objects.all()
     totalcolaboradores = Colaborador.objects.all().count()
     asos = Aso.objects.all()
     numeroasos =Aso.objects.all().count()
     
    
     Epi_item_abafadortem = Epi.objects.filter(abafadores=1).count()
     Epi_item_abafadorcond = Epi.objects.filter(abafadores=3).count()
     Epi_item_abafador =Epi_item_abafadortem + Epi_item_abafadorcond
     abafadoremfalta= numeroasos-Epi_item_abafador
    
      


     Epi_item_camisatem = Epi.objects.filter(camisa=1).count()
     Epi_item_camisacond = Epi.objects.filter(camisa=3).count()
     Epi_item_camisa = Epi_item_camisatem + Epi_item_camisacond
     camisaemfalta= numeroasos-Epi_item_camisa

    
     Epi_item_botastem = Epi.objects.filter(botas=1).count()
     Epi_item_botascond = Epi.objects.filter(botas=3).count()
     Epi_item_botas = Epi_item_botastem + Epi_item_botascond
     Epi_item_botasf = numeroasos-Epi_item_botas

     Epi_item_perneirastem = Epi.objects.filter(perneiras=1).count()
     Epi_item_perneirascond = Epi.objects.filter(perneiras=3).count()
     Epi_item_perneiras = Epi_item_perneirastem+Epi_item_perneirascond
     Epi_item_perneirasf = numeroasos-Epi_item_perneiras

     Epi_item_jugularestem = Epi.objects.filter(jugulares=1).count()
     Epi_item_jugularescond = Epi.objects.filter(jugulares=3).count()
     Epi_item_jugulares = Epi_item_jugularestem+Epi_item_jugularescond
     Epi_item_jugularesf = numeroasos-Epi_item_jugulares

     Epi_item_coletetem = Epi.objects.filter(colete_refletor=1).count()
     Epi_item_coletecond = Epi.objects.filter(colete_refletor=3).count()
     Epi_item_colete = Epi_item_coletetem+ Epi_item_coletecond
     Epi_item_coletef =numeroasos-Epi_item_colete
     
     Epi_item_capatem = Epi.objects.filter(capas_de_chuva_refletores=1).count()
     Epi_item_capacond= Epi.objects.filter(capas_de_chuva_refletores=3).count()
     Epi_item_capa = Epi_item_capatem + Epi_item_capacond
     Epi_item_capaf = numeroasos-Epi_item_capa

     Epi_item_oculostem = Epi.objects.filter(oculos_de_protecao=1).count()
     Epi_item_oculoscond = Epi.objects.filter(oculos_de_protecao=3).count()
     Epi_item_oculos = Epi_item_oculostem+Epi_item_oculoscond
     Epi_item_oculosf = numeroasos- Epi_item_oculos

     Epi_item_galochastem = Epi.objects.filter(galochas=1).count()
     Epi_item_galochascond = Epi.objects.filter(galochas=3).count()
     Epi_item_galochas = Epi_item_galochastem + Epi_item_galochascond
     Epi_item_galochasf = numeroasos-Epi_item_galochas

     Epi_item_luvastem = Epi.objects.filter(Luvas=1).count()
     Epi_item_luvascond = Epi.objects.filter(Luvas=3).count()
     Epi_item_luvas = Epi_item_luvastem +Epi_item_luvascond
     Epi_item_luvasf = numeroasos-Epi_item_luvas

     Epi_item_capacetetem = Epi.objects.filter(capacetes=1).count()
     Epi_item_capacetecond = Epi.objects.filter(capacetes=3).count()
     Epi_item_capacete = Epi_item_capacetetem+Epi_item_capacetecond
     Epi_item_capacetef = numeroasos-Epi_item_capacete

     Epi_item_lanternatem= Epi.objects.filter(lanterna=1).count()
     Epi_item_lanternacond= Epi.objects.filter(lanterna=3).count()
     Epi_item_lanterna = Epi_item_lanternatem + Epi_item_lanternacond
     Epi_item_lanternaf=numeroasos-Epi_item_lanterna

     Aso_item_liberdo = Aso.objects.filter(status="Liberado").count()
     total_pendentes = numeroasos-Aso_item_liberdo






     context= {
         'total_pendentes':total_pendentes,
         'aso_item_laterna':Epi_item_lanterna,
         'aso_item_laternaf':Epi_item_lanternaf,
         'colaboradores':colaboradores,
         'totalcolaboradores':totalcolaboradores,
         'Aso_item_liberdo':Aso_item_liberdo,
         'asos':asos,
         'numeroasos':numeroasos,
         'abafadoremfalta':abafadoremfalta,
         'camisaemfalta':camisaemfalta,
         'aso_item_abafador':Epi_item_abafador,
         'aso_item_abafadorcond':Epi_item_abafadorcond,
         'aso_item_camisa':Epi_item_camisa,
         'aso_item_camisacond':Epi_item_camisacond,

         'aso_item_camisaf':camisaemfalta,
         'aso_item_abafadorf':abafadoremfalta,
         'aso_item_botas':Epi_item_botas,
         'aso_item_botascond':Epi_item_botascond,
         'aso_item_botasf':Epi_item_botasf,
         'aso_item_perneiras':Epi_item_perneiras,
         'aso_item_perneirascond':Epi_item_perneirascond,
         'aso_item_perneirasf':Epi_item_perneirasf,
         'aso_item_jugulares' : Epi_item_jugulares,
         'aso_item_jugularescond' : Epi_item_jugularescond,
         'aso_item_jugularesf' :Epi_item_jugularesf,
         'aso_item_capa' : Epi_item_capa,
         'aso_item_capacond' : Epi_item_capacond,
         'aso_item_capaf':Epi_item_capaf,
         'aso_item_colete' : Epi_item_colete,
         'aso_item_coletecond' : Epi_item_coletecond,
         'aso_item_coletef':Epi_item_coletef,
         'aso_item_capa' : Epi_item_capa,
         'aso_item_capacond' : Epi_item_capacond,
         'aso_item_capaf':Epi_item_capaf,
         'aso_item_oculos' : Epi_item_oculos,
         'aso_item_oculoscond' : Epi_item_oculoscond,
         'aso_item_oculosf':Epi_item_oculosf,
         'aso_item_galochas' : Epi_item_galochas,
         'aso_item_galochascond' : Epi_item_galochascond,
         'aso_item_galochasf':Epi_item_galochasf,
         'aso_item_luvas' : Epi_item_luvas,
         'aso_item_luvascond' : Epi_item_luvascond,
         'aso_item_luvasf':Epi_item_luvasf,
         'aso_item_capacete' : Epi_item_capacete,
         'aso_item_capacetecond' : Epi_item_capacetecond,
         'aso_item_capacetef':Epi_item_capacetef,
         'aso_item_laterna':Epi_item_lanterna,
         'aso_item_laternacond':Epi_item_lanternacond,
         'aso_item_lanternaf':Epi_item_lanternaf,
         
         
         
      }
     return render(request,"home/index.html",context)
     



@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
