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


def index(request):
    print(f'INDEX - {request.POST}')

    context = {
        'title_page': 'Brichki.ru',
        'title_center': 'filter',
        'title_right': 'catalog',

        'Ads': Ads.objects.all(),
        'Brand': Brand.objects.all(),
        'Body': Body.objects.all(),
        'EngineType': EngineType.objects.all(),
        'BoostType': BoostType.objects.all(),
        'Drive': Drive.objects.all(),
        'Broken': Broken.objects.all(),
    }

    return render(request, 'ADS/main.html', context)