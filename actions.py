

# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List,Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT
from rasa_sdk.events import SlotSet, EventType
import mysql.connector
import os

class ActionHelloWorld(Action):
     def name(self) -> Text:
         return "action_hello_world"
     def run(self, dispatcher: CollectingDispatcher,
         tracker: Tracker,
         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         acc_no=tracker.get_slot('Port_Num')
         connection = mysql.connector.connect(host='localhost',database='bank_data',user='root',password='Poornima@7')
         cursor = connection.cursor()
         sql_select_query = """select * from bank_demo where acc_no = %s"""
         cursor.execute(sql_select_query,(acc_no,))
         records = cursor.fetchall()
         for row in records:
            x = row[0]
            y = row[1]
            z = row[6]
            if x == acc_no:
                if z == "Pending":
                    dispatcher.utter_message(template="utter_payoption" )
                else:
                    dispatcher.utter_message("Thanks, "+y+" no dues ")
            else:
                dispatcher.utter_message("Enter correct portfolio number to proceed")

         return[]

class ActionHello(Action):
     def name(self) -> Text:
         return "action_sbi"
     def run(self, dispatcher: CollectingDispatcher,
         tracker: Tracker,
         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         os.system("start \"\" https://www.onlinesbi.com")
         dispatcher.utter_message("Payment Successful!, Thanks")
         return

class Action(Action):
     def name(self) -> Text:
         return "action_icici"
     def run(self, dispatcher: CollectingDispatcher,
         tracker: Tracker,
         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         os.system("start \"\" https://www.icicibank.com")
         dispatcher.utter_message("Payment Successful!, Thanks")
         return

class Actio(Action):
     def name(self) -> Text:
         return "action_citi"
     def run(self, dispatcher: CollectingDispatcher,
         tracker: Tracker,
         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         os.system("start \"\" https://www.online.citibank.co.in")
         dispatcher.utter_message("Payment Successful!, Thanks")
         return

class ActionHelloangel(Action):
     def name(self) -> Text:
         return "action_angel_broking"
     def run(self, dispatcher: CollectingDispatcher,
         tracker: Tracker,
         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         os.system("start \"\" https://www.angelbroking.com")
         dispatcher.utter_message("Payment Successful!, Thanks")
         return

class Actionicici(Action):
     def name(self) -> Text:
         return "action_icici_direct"
     def run(self, dispatcher: CollectingDispatcher,
         tracker: Tracker,
         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         os.system("start \"\" https://www.icicidirect.com")
         dispatcher.utter_message("Payment Successful!, Thanks")
         return

class Actiozerodha(Action):
     def name(self) -> Text:
         return "action_zerodha"
     def run(self, dispatcher: CollectingDispatcher,
         tracker: Tracker,
         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         os.system("start \"\" https://zerodha.com/open-account")
         dispatcher.utter_message("Payment Successful!, Thanks")
         return

class Actionkotak_sec(Action):
     def name(self) -> Text:
         return "action_kotak_sec"
     def run(self, dispatcher: CollectingDispatcher,
         tracker: Tracker,
         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         os.system("start \"\" https://www.kotaksecurities.com")
         dispatcher.utter_message("Payment Successful!, Thanks")
         return

class Actiozupstox(Action):
     def name(self) -> Text:
         return "action_upstox"
     def run(self, dispatcher: CollectingDispatcher,
         tracker: Tracker,
         domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         os.system("start \"\" https://upstox.com")
         dispatcher.utter_message("Payment Successful!, Thanks")
         return