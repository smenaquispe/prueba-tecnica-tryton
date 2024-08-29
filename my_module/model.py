from trytond.model import ModelSQL, ModelView, fields
import os
import requests
from requests.auth import HTTPBasicAuth
from trytond.exceptions import UserError, UserWarning
from trytond.pool import Pool

class MyModel(ModelSQL, ModelView):
    'My Model'
    __name__ = 'my_module.my_model'

    customer = fields.Many2One('party.party', 'Customer', required=True)
    message = fields.Text('Message', required=True)

    @classmethod 
    def __setup__(cls):
        super(MyModel, cls).__setup__()    
        cls._buttons.update({
            'mybutton': {},
          })

    @classmethod
    @ModelView.button
    def mybutton(cls, records):

        config = Pool().get('my_module.twilio_configuration').search([], limit=1)[0]

        # Sustituye estos valores con tu SID y Auth Token
        ACCOUNT_SID = config.account_sid
        AUTH_TOKEN = config.auth_token
        
        # El número de teléfono desde el cual enviar el mensaje (debe ser un número de Twilio)
        from_number = config.from_number

        for record in records:
            

            ContactMechanism = Pool().get('party.contact_mechanism')
            phone_contact = ContactMechanism.search([
                ('party', '=', record.customer.id),
                ('type', '=', 'phone')
            ], limit=1)

            

            try:
                #to_number = record.number
                to_number = phone_contact[0].value
                message_body = record.message
            
                #URL de la API para enviar mensajes
                url = 'https://api.twilio.com/2010-04-01/Accounts/{}/Messages.json'.format(ACCOUNT_SID)

                # Parámetros de la solicitud
                payload = {
                    'From': from_number,
                    'To': to_number,
                    'Body': message_body
                }

                # Realiza la solicitud POST para enviar el mensaje
                response = requests.post(url, data=payload, auth=HTTPBasicAuth(ACCOUNT_SID, AUTH_TOKEN))

                # Imprime la respuesta
                raise UserWarning(message=f"SMS sent successfully to {to_number}!", name="Success")
            except Exception as e:
            
                error_message = f"Failed to send SMS to {to_number}. Error: {str(e)}\n"

                # Escribir el error en el archivo de log
                #with open(log_file_path, 'a') as log_file:
                 #   log_file.write(error_message)
                raise UserError(error_message)
            
            
