from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.template import Engine

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


def ad_page(request, ad_pk):
    ad = get_object_or_404(Ads, pk=ad_pk)

    context = {
        'title_left': 'filter',
        'title_center': 'ad',
        'title_right': 'catalog',

        'brand': Brand.objects.get(pk=ad.brand_id),
        'model': Model.objects.get(pk=ad.model_id),
        'generation': Generation.objects.get(pk=ad.generation_id),
        'price': ad.price,
        'comment': ad.comment,

        'ad_parameters': {
            'Двигатель': EngineType.objects.get(pk=ad.engine_type_id),
            'Нагнетатель': BoostType.objects.get(pk=ad.boost_type_id),
            'Кузов': Body.objects.get(pk=ad.brand_id),
            'Привод': Drive.objects.get(pk=ad.drive_id),
            'Пробег': ad.mileage,
        },
    }

    return render(request, 'ADS/ad_page.html', context)