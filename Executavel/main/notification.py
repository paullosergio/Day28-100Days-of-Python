from winotify import Notification, audio
from win10toast import ToastNotifier


toast = Notification(app_id="Pomodoro",
                    title= "Break",
                    msg= "Take a 5 minutes break.",
                    duration= "short",)

toast.set_audio(sound=audio.LoopingAlarm, loop = False)

toaster = ToastNotifier()
