import fastf1
import fastf1.plotting
import matplotlib.pyplot as plt


print("Hello World just changed this!")

print("Added fastf1")

print("HELLOOO")


fastf1.plotting.setup_mpl()

session = fastf1.get_session(2019, 'Monza', 'Q')

session.load()
fast_leclerc = session.laps.pick_driver('LEC').pick_fastest()
lec_car_data = fast_leclerc.get_car_data()
t = lec_car_data['Time']
vCar = lec_car_data['Speed']

fig, ax = plt.subplots()
ax.plot(t, vCar, label='Fast')
ax.set_xlabel('Time')
ax.set_ylabel('Speed [Km/h]')
ax.set_title('Leclerc Qualifying Monza 2019')
ax.legend()
plt.show()



