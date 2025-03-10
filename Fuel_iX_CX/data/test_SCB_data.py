import os


class SCB_TestData:
    INTENT_NAME = "BA_Schedule_call_back_Scenario"
    FIRST_NODE_NAME = "Schedule_Callback_Get_Available_Slots"
    FIRST_NODE_QUESTION = "Please allocate the earliest possible time slot for a scheduled call"
    FIRST_NODE_ANSWER = "this is test scb"
    FIRST_NODE_UPDATE_ANSWER = ("In order to schedule a callback from TELUS, we'll need to collect the following "
                                "pieces of info from you:")
    FIRST_NODE_ANSWER_CARD = "Thank you {{$local:name}} "
    SECOND_NODE_NAME = "Schedule_New_CallBack_Request"
    SECOND_NODE_ANSWER = "submit call back"
    SECOND_ANSWER_CARD = "Please wait, we are fetching the Agent Info..."
    SECOND_ANSWER_CARD_2 = "Checking the response of the booking success. Webhook response: {{$webhook:sR.responseCode}}"
    THIRD_NODE_NAME = "Booking_Success"
    THIRD_NODE_ANSWER = "this is booking success"
    THIRD_NODE_ANSWER_2 = "Thanks! An agent will contact you at your scheduled time to assist you."
    THIRD_NODE_ANSWER_3 = "If you want to cancel or reschedule your booking, please click below."
    THIRD_NODE_ANSWER_4 = "Your service details are as follows: Service ID:{{$local:serviceId}} ,and Service Name: {{$local:serviceName}}"
    FOURTH_NODE_NAME = "Reschedule_CallBack_Request"
    FOURTH_NODE_ANSWER = "this is reschedule"
    FOURTH_NODE_ANSWER_2 = "Please wait, we are rescheduling your call back..."
    FIFTH_NODE_NAME = "Issue_Occurred"
    FIFTH_NODE_ANSWER = "issue occurred"
    FIFTH_NODE_ANSWER_2 = "I am facing some issues, please try after some time."
    SIXTH_NODE_NAME = "CallBack_Booking_Failed"
    SIXTH_NODE_ANSWER = "booking failed"
    SIXTH_NODE_ANSWER_2 = "Hmm, looks like that time slot is no longer available or you have already booked a time."
    SIXTH_NODE_ANSWER_3 = "Add Card,If you have recently booked a time we will be reaching out within an hour after your scheduled time."
    SEVENTH_NODE_NAME = "Canceling_CallBack_Request"
    SEVENTH_NODE_ANSWER = "this is cancel"
    SEVENTH_NODE_ANSWER_2 = "Please wait we are Canceling your call back ......."
    SEVENTH_NODE_ANSWER_3 = "<b>Please provide your phone number which you have used while booking your slot.</b>"
    SEVENTH_NODE_ANSWER_4 = "Sorry, I can't find any callback request."
    SEVENTH_NODE_ANSWER_5 = "Your callback has been cancelled."
    SEVENTH_NODE_ANSWER_6 = "Sorry, We are unable to cancel your callback. Please try after some time."
    EXPECTED_NODE_CREATE_SUCCESS = "Template Created Successfully."

    # dynamic screenshot path

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Current script's directory
    PROJECT_ROOT = os.path.dirname(BASE_DIR)  # Move up to project_root
    # print(BASE_DIR)
    # Construct the dynamic screenshot path
    SCREENSHOT_PATH = os.path.join(PROJECT_ROOT, "reports", "Screenshots")

    FILE_TYPE = ".png"


    CUSTOMER_SLOT_NAME = "name"
    ASK_SLOT_ANSWER_1 = "<b>So we know who to ask for, what is your name?</b>"
    ASK_SLOT_ANSWER_2 = "<b>Next, please enter the phone number you want us to call.</b>"
    CUSTOMER_SLOT_PHONE_NUMBER = "ph_number"
    WEBHOOK_TIME_ZONE = "{{$sys:TimeZoneName}}"
    WEBHOOK_SELECTED_SLOT = "{{$local:selected_slot}}"
    LOCAL_SERVICE_NAME = "{{$local:serviceName}}"
    LOCAL_SERVICE_ID = "{{$local:serviceId}}"
    WEBHOOK_RESPONSE = "sR.responseCode"
    STATUS_CODE = "200"
    CANCEL_BUTTON = "Cancel"
    NO_THANKS_BUTTON = "No Thanks"
    NO_THANKS_BUTTON_MESSAGE = "NeverMind"
    RESCHEDULE_BUTTON = "Reschedule"
    WEBHOOK_SERVICE_ID = "{{$webhook:sR.serviceID}}"
    WEBHOOK_SERVICE_NAME = "{{$webhook:sR.serviceName}}"
    WEBHOOK_PHONE_NUMBER = "{{$local:ph_number}}"
    SERVICE_NAME_SLOT = "serviceName"
    SERVICE_ID_SLOT = "serviceId"
    WIDGET_FIRST_QUESTION = "Please allocate the earliest possible time slot for a scheduled call"
    WIDGET_CUSTOMER_NAME = "Hulk"
    WIDGET_CUSTOMER_PHONE_NUMBER = "9193736951"
    EXPECTED_SUCCESS_MESSAGE_IMPORT = "Templates imported successfully in bot category."
    EXPECTED_SUCCESS_MESSAGE_TRAIN = "Train job has been scheduled."
    EXPECTED_SUCCESS_MESSAGE_TRAINED = "'Transaction Bot MQA' bot trained successfully"
