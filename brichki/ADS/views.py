from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from ADS.models import Ads
from FILTER.models import Brand, Model, Generation, Body
from FILTER.models import EngineType, BoostType, Drive, Broken


def main_page(request):
    print(f'main_page - {request.POST, request.GET}')

    if request.POST:
        filter_parameter = {
            'brand_id': request.POST['brand'],
            'model_id': request.POST['model'],
            'generation_id': request.POST['generation'],
            'engine_type_id': request.POST['engine'],
            'boost_type_id': request.POST['boost'],
            'engine_capacity__gte': request.POST['capcty'],
            'engine_capacity__lte': request.POST['capcty-to'],
            'mileage__gte': request.POST['mileage'],
            'mileage__lte': request.POST['mileage-to'],
            'price__gte': request.POST['price'],
            'price__lte': request.POST['price-to'],
            'drive_id': request.POST['drive'],
            'body_id': request.POST['body'],
        }

        filters = Q()
        for key, value in filter_parameter.items():
            if value:
                filters &= Q(**{key: value})

        ads = Ads.objects.filter(filters).order_by(request.POST['sort'])
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
        'electro': EngineType.objects.get(pk=4),

        'BoostType': BoostType.objects.all(),
        'Drive': Drive.objects.all(),
        'Broken': Broken.objects.all(),

        'sort_list': {
            'По возрастанию цены': 'price',
            'По убыванию цены': '-price',
            'По пробегу': 'mileage',
        },
    }

    return render(request, 'ADS/main_page.html', context)


def ad_page(request, ad_pk):
    print(f'ad_page - {request.POST, request.GET}')
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