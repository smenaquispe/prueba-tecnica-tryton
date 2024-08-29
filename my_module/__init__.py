from trytond.pool import Pool
from .model import MyModel
from .twilio_configuration import TwilioConfiguration

def register():
    Pool.register(
        MyModel,
        TwilioConfiguration,
        module='my_module', type_='model'
    )

