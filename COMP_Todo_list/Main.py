from tkinter import *
from tkinter import ttk
import DataStorage.hashTable as hashTable 
import Pages.Task.TaskPage as taskPage
import Pages.ShoppingList.shopping_list_app as shoppingList
import DataStorage.Data.saveData as saveData
import DataStorage.Data.readData as readData
import requests
import json
import datetime

taskManager = hashTable.Hash_Table()

def display():
    root = Tk()
    root.geometry("800x500")
    root.title("Todo List")
    root.minsize(800,510)
    root.maxsize(800,510)
    appTitle = Label(root,
                    text="Todo List",
                    font=("Arial",30))
    appTitle.pack()

    # labels for switching functions
    functionList = ttk.Notebook(root)

    # creating container for functions
    Task = Frame(functionList)
    Weather = Frame(functionList,bg="#4D4D4D")
    ShoppingList = Frame(functionList)

    # adding all container into the function list
    functionList.add(Task,text="Task")
    functionList.add(Weather,text="Weather")
    functionList.add(ShoppingList,text="Shopping List")

    shoppingListDisplay = shoppingList.ShoppingListApp(ShoppingList)
    
    def page_switch(event):
        root.minsize(800,510)
        root.maxsize(800,510)
        desc_frame.grid(row=0, column=0, padx=10, pady=10)
        info_frame.grid(row=0, column=1, padx=10, pady=10)
        forecast_columns_container.grid_forget()

    functionList.bind("<<NotebookTabChanged>>", page_switch)

    # put the list into the root
    functionList.pack(expand=True,fill=BOTH)

    taskPage.taskPageDisplay(root,Task, taskManager,readData)

    api_url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php"
    locations = {'King\'s Park': 0, 'Hong Kong Observatory': 1, 'Wong Chuk Hang': 2, 'Ta Kwu Ling': 3, 'Lau Fau Shan': 4, 'Tai Po': 5, 'Sha Tin': 6, 'Tuen Mun': 7, 'Tseung Kwan O': 8, 'Sai Kung': 9, 'Cheung Chau': 10, 'Chek Lap Kok': 11, 'Tsing Yi': 12, 'Shek Kong': 13, 'Tsuen Wan Ho Koon': 14, 'Tsuen Wan Shing Mun Valley': 15, 'Hong Kong Park': 16, 'Shau Kei Wan': 17, 'Kowloon City': 18, 'Happy Valley': 19, 'Wong Tai Sin': 20, 'Stanley': 21, 'Kwun Tong': 22, 'Sham Shui Po': 23, 'Kai Tak Runway Park': 24, 'Yuen Long Park': 25, 'Tai Mei Tuk': 26}
    location_num = 1
    readFile = open(".//Pages//Weather//storage.txt", "r")
    chosen_location = readFile.readline()
    if chosen_location != "":
        location_num = locations[chosen_location]
    readFile.close()

    # Create frame for weather description
    desc_frame = Frame(Weather, width=250, height=420)
    desc_frame.grid(row=0, column=0, padx=10, pady=10)
    desc_frame.config(bg="#696868")
    desc_frame.grid_propagate(0)

    # Fetch weather desciption
    desc_url = api_url+"?dataType=flw&lang=en" # Url for weather description
    weather_desc = requests.get(desc_url).text
    weather_desc_data = json.loads(weather_desc)
    today_weather_desc = "No data"
    if weather_desc_data != "":
        today_weather_desc = weather_desc_data["forecastDesc"]

    larger_font = ("Arial", 16, "bold")
    large_font = ("Arial", 13, "bold")
    medium_font = ("Arial", 11)
    small_font = ("Arial", 9)
    Label(desc_frame, text="Weather description", bg="#696868", fg="white", font=large_font).grid(row=1, column=0, padx=5, pady=5)
    desc = Text(desc_frame, height=20, width=30, bg="#696868", fg="white", wrap="word", borderwidth=0)
    desc_text = today_weather_desc
    desc.insert("end", desc_text)
    desc.config(font=medium_font, state=DISABLED)
    desc.grid(row=2, column=0, padx=5, pady=5)

    def info_switch():
        desc_frame.grid_forget()
        info_frame.grid_forget()
        forecast_columns_container.grid(row=0, column=1, padx=10, pady=10)
        root.minsize(1450,510)
        root.maxsize(1450,510)

    def return_to_main():
        desc_frame.grid(row=0, column=0, padx=10, pady=10)
        info_frame.grid(row=0, column=1, padx=10, pady=10)
        forecast_columns_container.grid_forget()
        root.minsize(800,510)
        root.maxsize(800,510)

    forecast_btn = Button(desc_frame, text="9-days forecast", bg="#868686", fg="white", font=small_font, command=info_switch)
    forecast_btn.grid(row=3, column=0, padx=5, pady=5)

    # Create frame for weather info
    info_frame = Frame(Weather, width=100, height=100, bg="#4D4D4D")
    info_frame.grid(row=0, column=1, padx=10, pady=10)

    def temperature(*arguments):
        chosen_location = location_combobox.get()
        file = open(".//Pages//Weather//storage.txt", "w")
        file.write(chosen_location)
        file.close()
        # Create current temperature label for weather info
        chosen_location_hk = locations[chosen_location]
        currentTemp = basic_weather_info_data["temperature"]["data"][chosen_location_hk]["value"]
        Label(info_frame, text=str(currentTemp)+"°C", bg="#4D4D4D", fg="white", font=larger_font).grid(row=5, column=1, padx=5, pady=5)

    # Create dropdown list
    Label(info_frame, text="Your Location", bg="#4D4D4D", fg="white", font=large_font).grid(row=1, column=1, padx=5, pady=5)
    optionVar = StringVar()
    location_combobox = ttk.Combobox(info_frame, width=30, textvariable=optionVar, font=small_font)
    location_combobox["values"]= ('King\'s Park', 'Hong Kong Observatory', 'Wong Chuk Hang', 'Ta Kwu Ling', 'Lau Fau Shan', 'Tai Po', 'Sha Tin', 'Tuen Mun', 'Tseung Kwan O', 'Sai Kung', 'Cheung Chau', 'Chek Lap Kok', 'Tsing Yi', 'Shek Kong', 'Tsuen Wan Ho Koon', 'Tsuen Wan Shing Mun Valley', 'Hong Kong Park', 'Shau Kei Wan', 'Kowloon City', 'Happy Valley', 'Wong Tai Sin', 'Stanley', 'Kwun Tong', 'Sham Shui Po', 'Kai Tak Runway Park', 'Yuen Long Park', 'Tai Mei Tuk')
    location_combobox.grid(row=2, column=1)
    location_combobox.current(location_num)
    optionVar.trace_add("write", temperature)
    chosen_location = location_combobox.get()

    # Create today's date for weather info
    today = datetime.datetime.now()
    today_date = str(today.day)+"/"+str(today.month)+"/"+str(today.year)
    Label(info_frame, text=today_date, bg="#4D4D4D", fg="white", font=medium_font).grid(row=3, column=1, padx=5, pady=5)

    # Fetch today's basic weather info
    url = api_url+"?dataType=rhrread&lang=en" # Url for basic weather data
    basic_weather_info = requests.get(url).text
    basic_weather_info_data = json.loads(basic_weather_info)

    # Create current weather icon for weather info
    icon_number = basic_weather_info_data["icon"][0]
    weather_icon = PhotoImage(file=".//Pages//Weather//images//"+str(icon_number)+".png")
    resize_icon_img = weather_icon.subsample(6,6)
    Label(info_frame, image = resize_icon_img, bg="#4D4D4D", fg="white").grid(row=4, column=1, padx=5, pady=5)

    # Create current temperature label for weather info
    chosen_location_hk = locations[chosen_location]
    currentTemp = basic_weather_info_data["temperature"]["data"][chosen_location_hk]["value"]
    Label(info_frame, text=str(currentTemp)+"°C", bg="#4D4D4D", fg="white", font=larger_font).grid(row=5, column=1, padx=5, pady=5)

    # Create labels for humidity
    Label(info_frame, text="Humidity:", bg="#4D4D4D", fg="white", font=medium_font).grid(row=4, column=2, padx=(5, 0), pady=5)
    humidity_decoration = PhotoImage(file=".//Pages//Weather//images//humidityImg.png")
    resize_humidity_img = humidity_decoration.subsample(60,60)
    Label(info_frame, image = resize_humidity_img, bg="#4D4D4D", fg="white").grid(row=4, column=4, padx=(0, 5), pady=5)
    humidity = basic_weather_info_data["humidity"]["data"][0]["value"]
    Label(info_frame, text=str(humidity)+"%", bg="#4D4D4D", fg="white", font=medium_font).grid(row=4, column=3, padx=5, pady=5)

    # Create labels for uv index
    global uv_img
    Label(info_frame, text="UV Index:", bg="#4D4D4D", fg="white", font=medium_font).grid(row=4, column=5, padx=(5, 0), pady=5)
    uv_img = PhotoImage(file=".//Pages//Weather//images//uvIndexImg.png")
    resize_uv_img = uv_img.subsample(60,60)
    Label(info_frame, image = resize_uv_img, bg="#4D4D4D", fg="white").grid(row=4, column=7, padx=(0, 5), pady=5)
    uvIndexTest = basic_weather_info_data["uvindex"]
    uv_index = 0
    if uvIndexTest != "":
        uv_index = basic_weather_info_data["uvindex"]["data"][0]["value"]
    Label(info_frame, text=uv_index, bg="#4D4D4D", fg="white", font=medium_font).grid(row=4, column=6, padx=5, pady=5)

    # 9-days forecast

    forecast_url = api_url+"?dataType=fnd&lang=en" # Url for weather description
    weather_forecast = requests.get(forecast_url).text
    weather_forecast_data = json.loads(weather_forecast)

    # Create frame for 9-days forecast column

    forecast_columns_container = Frame(Weather, width=1020, height=535, bg="#4D4D4D")
    forecast_columns_container.grid(row=0, column=1, padx=10, pady=10)
    forecast_columns_container.grid_forget()
    
    images = []
    for i in range(9):
        # Fetch forecast data
        forecast_icon = weather_forecast_data["weatherForecast"][i]["ForecastIcon"]
        forecast_psr = weather_forecast_data["weatherForecast"][i]["PSR"]
        forecast_maxrh = weather_forecast_data["weatherForecast"][i]["forecastMaxrh"]["value"]
        forecast_minrh = weather_forecast_data["weatherForecast"][i]["forecastMinrh"]["value"]
        forecast_maxtemp = weather_forecast_data["weatherForecast"][i]["forecastMaxtemp"]["value"]
        forecast_mintemp = weather_forecast_data["weatherForecast"][i]["forecastMintemp"]["value"]
        forecast_date = weather_forecast_data["weatherForecast"][i]["forecastDate"]

        # Forecast dates
        year = int(forecast_date[0:4])
        month = int(forecast_date[4:6])
        day = int(forecast_date[6:8])
        date = datetime.datetime(year, month, day)
        weekday_short = date.strftime("%a")
        day_of_month = date.strftime("%d")
        month_name_short = date.strftime("%b")
        date_string = day_of_month + " " + month_name_short
        day_string = "(" + weekday_short + ")"
        forecast_column = Frame(forecast_columns_container, width=180, height=535, bg="#222222")
        forecast_column.grid(row=0, column=i, padx=10, pady=10)
        Label(forecast_column, text=date_string, bg="#222222", fg="white", font=large_font).grid(row=1, column=i, padx=5, pady=5)
        Label(forecast_column, text=day_string, bg="#222222", fg="white", font=large_font).grid(row=2, column=i, padx=5, pady=5)

        # Forecast weather icon
        forecast_weather_icon = PhotoImage(file=".//Pages//Weather//images//"+str(forecast_icon)+".png")
        resize_forecast_icon_img = forecast_weather_icon.subsample(8,8)
        images.append(resize_forecast_icon_img)
        for resized_weather_icon in images:
            Label(forecast_column, image = resized_weather_icon, bg="#4D4D4D").grid(row=3, column=i, padx=5, pady=5)

        # Forecast temperature
        forcast_temp_string = str(forecast_mintemp) + "-" + str(forecast_maxtemp) + "°C"
        Label(forecast_column, text=forcast_temp_string, bg="#222222", fg="white", font=medium_font).grid(row=4, column=i, padx=5, pady=5)

        # Forecast humidity
        forcast_humid_string = str(forecast_minrh) + "-" + str(forecast_maxrh) + "%"
        Label(forecast_column, text=forcast_humid_string, bg="#222222", fg="white", font=medium_font).grid(row=5, column=i, padx=5, pady=5)

        # Forecast of the probability of significant rain (PSR)
        Label(forecast_column, text="PSR:", bg="#222222", fg="white", font=medium_font).grid(row=6, column=i, padx=5, pady=5)
        Label(forecast_column, text=forecast_psr, bg="#222222", fg="white", font=medium_font).grid(row=7, column=i, padx=5, pady=5)

    return_btn = Button(forecast_columns_container, text="Back to main page", bg="#868686", fg="white", font=small_font, command=return_to_main)
    return_btn.grid(row=9, column=4, padx=5, pady=5)

    root.protocol("WM_DELETE_WINDOW",lambda: saveData.save(root, taskManager))
    root.mainloop()

    shoppingListDisplay.run()

if __name__ == "__main__":
    display()