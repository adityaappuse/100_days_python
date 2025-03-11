from win10toast import ToastNotifier
import time
toaster = ToastNotifier()
while(True):
    toaster.show_toast("Drink Water Reminder",
                    "Drinking water is necessary for ideal body",
                    duration = 10)
    while(toaster.notification_active):
        time.sleep(10)
    time.sleep(60*60)
    