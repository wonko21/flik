from zeep import Client
from yaml import safe_dump
from ..common import config, storage
from ..common.util import quote, sessionID
from .baseService import autologin


def client():
    return Client(config.load()['url'] + 'MasterDataService?wsdl')


@autologin
def syncActivities():
    raw_activities = client().service.getActivities(sessionID())

    activities = {}
    for activity in filter(lambda x: x.active, raw_activities):
        activities[quote(activity.name)] = str(activity.activityID)
    storage.writeShare(
        'activities.yaml', safe_dump(
            activities, default_flow_style=False))
