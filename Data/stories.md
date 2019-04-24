## Story 1
* greet
    - utter_greet
* goodbye
    - utter_goodbye
    
## Generated Story -8296529886011708313
* check_in{"check_person": "\u6211"}
    - slot{"check_person": "\u6211"}
    - utter_ask_time
* tell_check_time{"check_time": "\u73b0\u5728"}
    - slot{"check_time": "\u73b0\u5728"}
    - utter_ask_flightNo
* tell_check_no{"flight_no": "NH12456"}
    - slot{"flight_no": "NH12456"}
    - tell_result
* goodbye
    - utter_goodbye

## Generated Story -8296529886011708314
* check_in{"check_person": "\u6211"}
    - slot{"check_person": "\u6211"}
    - utter_ask_flightNo
* tell_check_no{"flight_no": "NH12456"}
    - slot{"flight_no": "NH12456"}
    - utter_ask_time
* tell_check_time{"check_time": "\u73b0\u5728"}
    - slot{"check_time": "\u73b0\u5728"}
    - tell_result
    
## Generated Story -8296529886011708315
* check_in{"check_person": "\u6211","check_time": "\u73b0\u5728"}
    - slot{"check_person": "\u6211"}
    - slot{"check_time": "\u73b0\u5728"}
    - utter_ask_flightNo
* tell_check_no{"flight_no": "NH12456"}
    - slot{"flight_no": "NH12456"}
    - tell_result