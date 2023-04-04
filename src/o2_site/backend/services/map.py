import folium
from folium.plugins import MarkerCluster

from backend import models
from backend.utils.price import prices_to_str
from o2_site import settings


def get_gs_map():
    map = folium.Map(location=settings.NCH_COORDINATES)
    cluster = MarkerCluster().add_to(map)
    for gas_station in models.GasStation.objects.all():
        folium.Marker(
            location=(gas_station.latitude, gas_station.longitude),
            popup=f'№ {gas_station.gs_number}',
            tooltip=prices_to_str(gas_station),
            icon=folium.Icon(icon='gas-pump', prefix='fa')
        ).add_to(cluster)
    return map._repr_html_()
