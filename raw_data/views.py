from django.shortcuts import render
from .forms import PlatformForm, GameTitleForm
from .models import Videogames

from django.db.models import Count, Sum
import pandas as pd

def games(request):
    """
    View for games endpoint:
    displays Highcharts bar graph representing number of games releases grouped by
    year and platform.
    In order not to overcrowd the graph, when no platform is selected, history will start from the
    year 2010.
    Once a platform is selected, entire history for that platform will be available
    """
    if request.GET:
        filters = request.GET.get('platform')
        # set initial value for dropdown if any is being sent as request param
        # so on refresh, it will be selected
        context = {'form': PlatformForm(initial={'value': filters})}
    else:
        filters = None
        context = {'form': PlatformForm()}
    if filters == 'all':
        filters = None
    if filters:
        filters = {'platform': request.GET.get('platform')}
        q = Videogames.objects.values('year', 'platform')\
            .annotate(released=Count('rank')).filter(**filters).order_by('year')
    else:
        q = Videogames.objects.values('year', 'platform')\
            .annotate(released=Count('rank')).filter(year__gte=2010).order_by('year')
    # Load query results into a pandas dataframe for further manipulation
    # set_index to year and platform so that platforms not having any release in a year
    # wil have NaN values and fillna to transform them to 0 - this way, each platform is represented in each year
    df = pd.DataFrame(list(q))
    df = df.set_index(['year', 'platform']).unstack().stack(dropna=False).reset_index()
    df = df.fillna(0)
    data = df.groupby(by=['platform'])['released'].apply(list).fillna(0)
    years = list(df.year.unique())
    platforms = list(data.index)
    values = list(data.values)
    data = list(tuple(zip(platforms, values)))
    context.update({'years': years, 'platforms':platforms, 'values': values, 'data':data})
    return render(request, 'interface/games.html', context=context)

def game_sales(request):
    """
    View for favorites sales graphs.
    For graph to be displayed, a game from the dropdown should be selected.
    """
    if request.GET:
        filters = request.GET.get('name')

        context = {'form': GameTitleForm(initial={'value': filters})}
    else:
        filters = None
        context = {'form': GameTitleForm()}
    if filters == 'all':
        filters = None
    if filters:
        filters = {'name': request.GET.get('name')}
    # do the query only if a game is selected
    # filter by name coming as request param
    if filters:
        filters = {'name': request.GET.get('name')}
        q = Videogames.objects.values('name').annotate(north_america=Sum('na_sales'),
                                                       europe=Sum('eu_sales'),
                                                       japan=Sum('jp_sales'),
                                                       other=Sum('other_sales'),
                                                       global_sales=Sum('global_sales'))\
            .filter(**filters)
        df = pd.DataFrame(list(q))
        # Calculate percentages for each region out of global sales
        df['North America'] = round((df['north_america'] / df['global_sales'].sum()) * 100, 1)
        df['Europe'] = round((df['europe'] / df['global_sales'].sum()) * 100, 1)
        df['Japan'] = round((df['japan'] / df['global_sales'].sum()) * 100, 1)
        df['Other'] = round((df['other'] / df['global_sales'].sum()) * 100, 1)
        # drop initial columns since they are no longer needed
        df = df.drop(columns=['north_america', 'europe', 'japan', 'other', 'global_sales'])
        context.update({'data': df.to_dict('records')})
    return render(request, 'interface/favorite_games.html', context=context)