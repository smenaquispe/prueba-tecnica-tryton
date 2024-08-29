from trytond.model import ModelView, ModelSQL, fields

class TwilioConfiguration(ModelSQL, ModelView):
    'Twilio Configuration'
    __name__ = 'my_module.twilio_configuration'

    # Campos para la configuración de Twilio
    account_sid = fields.Char('Account SID', required=True)
    auth_token = fields.Char('Auth Token', required=True)
    from_number = fields.Char('From Number', required=True)

