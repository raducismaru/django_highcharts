from django import forms
from .models import DistinctPlatforms, Videogames


class PlatformForm(forms.Form):
    try:
        dropdown = DistinctPlatforms.objects.order_by('platform').all()
        CHOICES = [('all', 'all')]
        CHOICES.extend([(record.platform, record.platform) for record in dropdown])
    except:
        CHOICES = [('all', 'all')]
    platform = forms.ChoiceField(choices=CHOICES)

    def __init__(self, *args, **kwargs):
        super(PlatformForm, self).__init__(*args, **kwargs)
        if 'initial' in kwargs:
            self.initial['platform'] = kwargs.get('initial').get('value')
        else:
            self.initial['platform'] = 'all'


class GameTitleForm(forms.Form):
    game_list = ['Grand Theft Auto V', 'Battlefield 3',
                 'Call of Duty 4: Modern Warfare',
                 'Far Cry 3', 'Far Cry 4', 'Max Payne 3']
    try:
        dropdown = Videogames.objects.values('name').distinct().filter(name__in=game_list).order_by('name').all()
        CHOICES = [('all', 'select a game')]
        CHOICES.extend([(record.get('name'), record.get('name')) for record in dropdown])
    except:
        CHOICES = [('all', 'select a game')]
    name = forms.ChoiceField(choices=CHOICES)

    def __init__(self, *args, **kwargs):
        super(GameTitleForm, self).__init__(*args, **kwargs)
        if 'initial' in kwargs:
            self.initial['name'] = kwargs.get('initial').get('value')
        else:
            self.initial['name'] = 'all'