from django.db.models import Q
from django.shortcuts import render

from ADS.models import Ads
from FILTER.models import Brand
from FILTER.models import Model
from FILTER.models import Generation
from FILTER.models import Body
from FILTER.models import EngineType
from FILTER.models import BoostType
from FILTER.models import Drive
from FILTER.models import Broken


def main_page(request):
    print(f'INDEX - {request.POST}')

    if request.POST:
        print('POST')
        filter_parameter = {
            'brand_id': request.POST['brand'],
            'model_id': request.POST['model'],
            'generation_id': request.POST['generation'],
            'engine_type_id': request.POST['engine'],
            'boost_type_id': request.POST['boost'],
            'engine_capacity__gte': request.POST['capcty'],
            'engine_capacity__lte': request.POST['capcty-before'],
            'mileage__gte': request.POST['mileage'],
            'mileage__lte': request.POST['mileage-before'],
            'price__gte': request.POST['price'],
            'price__lte': request.POST['price-before'],
            'drive_id': request.POST['drive'],
            'body_id': request.POST['body'],
        }

        filters = Q()
        for key, value in filter_parameter.items():
            if value:
                filters &= Q(**{key: value})

        ads = Ads.objects.filter(filters)
    else:
        ads = Ads.objects.all()

    context = {
        'title_page': 'Brichki.ru',
        'title_center': 'filter',
        'title_right': 'catalog',

        'Ads': ads,

        'Brand': Brand.objects.all(),
        'Model': Model.objects.all(),
        'Generation': Generation.objects.all(),

        'Body': Body.objects.all(),
        'EngineType': EngineType.objects.all(),
        'BoostType': BoostType.objects.all(),
        'Drive': Drive.objects.all(),
        'Broken': Broken.objects.all(),
    }

    return render(request, 'ADS/main_page.html', context)

def ad_page(request):
    pass