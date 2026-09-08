import schedule
import time

def task(message):
    print(message)
    
#Schedule from Monday to Friday

for day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    getattr(schedule.every(), day).at("08:00").do(task, "Wake Up! Go brush your teeth and take a shower")
    getattr(schedule.every(), day).at("08:30").do(task, "Change into your school uniform!")
    getattr(schedule.every(), day).at("09:00").do(task, "Go and eat breakfast, mom is waiting!")
    getattr(schedule.every(), day).at("09:45").do(task, "Time for school, follow dad to the car!")
    getattr(schedule.every(), day).at("16:30").do(task, "Welcome home! Change out of your uniform and into your home attire!")
    getattr(schedule.every(), day).at("18:00").do(task, "Time for a puzzle! Pick any one of your choice!")
    getattr(schedule.every(), day).at("19:00").do(task, "Time to play on your iPad, let's do Sorting!")
    getattr(schedule.every(), day).at("21:30").do(task, "Time to eat dinner, mom is waiting!")
    getattr(schedule.every(), day).at("22:30").do(task, "Time for bed, change into your night clothes and go wash your face!")
    getattr(schedule.every(), day).at("22:45").do(task, "Good night, sleep well!")

#Schedule on Saturday and Sunday

for day in ["saturday", "sunday"]:
    getattr(schedule.every(), day).at("09:00").do(task, "Good morning! Wake up! Go brush your teeth and take a shower")
    getattr(schedule.every(), day).at("09:45").do(task, "Go and eat breakfast, mom is waiting!")
    getattr(schedule.every(), day).at("10:30").do(task, "Let's go cycling, get changed and follow dad out the house!")
    getattr(schedule.every(), day).at("12:00").do(task, "Lunch time. Go to the dining table, mom is waiting!")
    getattr(schedule.every(), day).at("15:00").do(task, "Time for a puzzle, pick any one of your choice!")
    getattr(schedule.every(), day).at("17:00").do(task, "Time to play on your iPad, choose any game you want!")
    getattr(schedule.every(), day).at("18:30").do(task, "Time to go to the gym, get changed and meet dad in the living room!")
    getattr(schedule.every(), day).at("21:00").do(task, "Dinner time, go and sit on the dining table!")
    getattr(schedule.every(), day).at("23:30").do(task, "Time for bed, go and change into your night clothes!")
    getattr(schedule.every(), day).at("23:45").do(task, "Good night, sleep well!")
    
print("Schedule loaded. Waiting...")

while True:
    schedule.run_pending()
    time.sleep(1)
