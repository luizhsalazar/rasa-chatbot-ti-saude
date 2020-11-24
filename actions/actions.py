# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher


# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

def message_imc(imc):
    if (imc >= 30): return 'muito acima do peso.'
    elif (imc >= 25):  return 'acima do peso.'
    elif (imc >= 18.5): return 'na faixa normal de peso.'
    return 'abaixo do peso.'

class ActionCalcImc(Action):

    def name(self) -> Text:
        return "action_calc_imc"

    def run(self, dispatcher, tracker, domain):

        peso  = tracker.get_slot('peso')
        altura  = tracker.get_slot('altura')

        print('peso')
        print(peso)

        print('altura')
        print(altura)

        message = 'Não foi possível calcular o seu IMC :('

        if (peso is not None and altura is not None):
            peso_float = float(peso)
            altura_float = float(altura)
            imc = peso_float / (altura_float * altura_float)
            print('imc')
            print(imc)
            message = 'Legal! Com essas informações podemos ver que o seu IMC é {:.2f}.'.format(imc)

            message_calc = message_imc(imc)
            message = message + '\n' + 'Este valor indica que você está ' + message_calc

        dispatcher.utter_message(text=message)
        return []