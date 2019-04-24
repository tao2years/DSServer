from rasa_core_sdk import Action

class ActionAskTime(Action):
    def name(self):
        return 'tell_result'

    def run(self, dispatcher, tracker, domain):
        flight_no = tracker.get_slot("flight_no")
        check_time = tracker.get_slot("check_time")
        check_person = tracker.get_slot("check_person")
        text = "信息如下" + flight_no + "   " + check_time + "   " + check_person
        dispatcher.utter_message(text)
        return []
