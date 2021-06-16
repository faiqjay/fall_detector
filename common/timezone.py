import datetime
import time
import pytz



class Date:


    @staticmethod
    def date():
        lagos = pytz.timezone('Africa/Lagos')
        date_1 = datetime.datetime.now(lagos)
        date_2 = date_1.strftime("%I:%M %p, %d/%m/%Y")
        return date_2

    @staticmethod
    def time_stamp():
        date1 = time.time()
        return date1
