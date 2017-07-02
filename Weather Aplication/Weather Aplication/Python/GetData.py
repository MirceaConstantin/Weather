import Date
import WeatherType
import TemperatureForToday
import TemperatureMaxAndMin
import HumidityForToday
import WindDirection
import WindSpeed


GetDate = Date.RetData()
GetWeatherType = WeatherType.RetData()
GetTemperatureForToday = TemperatureForToday.RetData()
GetTemperatureMaxAndMin = TemperatureMaxAndMin.RetData()
GetHumidityForToday = HumidityForToday.RetData()
GetWindDirection = WindDirection.RetData()
GetWindSpeed = WindSpeed.RetData()

with open("Get_Data_For_App.txt", 'w') as file_out:
	for i in range(0, 5):
		file_out.write(str(GetDate[i]) + '\n')
		file_out.write(str(GetWeatherType[i]) + '\n')
		file_out.write(GetTemperatureForToday + '\n')
		file_out.write(str(GetTemperatureMaxAndMin[i]) + '\n')
		file_out.write(GetHumidityForToday + '\n')
		file_out.write(str(GetWindDirection[i]) + '\n')
		file_out.write(str(GetWindSpeed[i]) + '\n')
