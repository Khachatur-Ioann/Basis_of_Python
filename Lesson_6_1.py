from time import sleep

class TrafficLight:
    __color = "Белый"

    def running(self):
        while True:
            print("Светофор сейчас красный")
            sleep(7)
            print("Светофор сейчас желтый")
            sleep(2)
            print("Светофор сейчас зеленый")
            sleep(7)
            print("Светофор сейчас желтый")
            sleep(2)


trafficlight = TrafficLight()
trafficlight.running()