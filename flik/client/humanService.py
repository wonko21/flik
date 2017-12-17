from zeep import Client
from ..common import config


def client():
    return Client(config.load()['url'] + 'HumanService?wsdl')
