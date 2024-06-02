from tkinter import *
from PIL import ImageTk, Image, ImageDraw
import requests
from io import BytesIO

# API anahtarınızı burada saklayın
api_key = '6e56a3650937476636427122e2510047'
url = f'https://api.openweathermap.org/data/2.5/weather?&appid={api_key}&lang=tr'
iconurl = 'https://openweathermap.org/img/wn/{}@2x.png'

def getWeather(city):
    # Hava durumu verilerini almak için API çağrısı
    try:
        params = {'q': city, 'appid': api_key, 'lang': 'tr'}
        response = requests.get(url, params=params)
        response.raise_for_status()  # Hatalı cevaplar için HTTPError oluşturur
        data = response.json()

        if data['cod'] != 200:
            raise ValueError(f"Hata: {data['message']}")

        city = data['name'].capitalize()
        country = data['sys']['country']
        temp = int(data['main']['temp'] - 273.15)
        icon = data['weather'][0]['icon']
        condition = data['weather'][0]['description']
        return city, country, temp, icon, condition
    except requests.exceptions.RequestException as e:
        print(f"HTTP İsteği başarısız oldu: {e}")
        return None
    except ValueError as e:
        print(e)
        return None

def create_rounded_icon(icon_img):
    # İkonu yuvarlak hale getir ve siyah arka plan ekle
    size = (100, 100)  # İkon boyutu
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + size, fill=255)

    output = Image.new('RGBA', size, (0, 0, 0, 0))
    output.paste(icon_img, (0, 0), mask)
    
    # Siyah arka plan ekle | background  değişkeni  3. parametresi ile hava durumu arka plan değiştirilebilir Örneğin: ('green') 
    background = Image.new('RGBA', size, ('yellow')) # Black (0, 0, 0, 255)
    background.paste(output, (0, 0), output)
    
    return background

def main():
    # Kullanıcının girdiği şehri al ve hava durumu verilerini getir
    city = cityEntry.get().strip()
    if not city:
        return  # Giriş boşsa hiçbir şey yapma
    
    weather = getWeather(city)
    if weather:
        locationLabel['text'] = f'{weather[0]}, {weather[1]}'
        tempLabel['text'] = f'{weather[2]}°C'
        conditionLabel['text'] = weather[4]
        try:
            icon_response = requests.get(iconurl.format(weather[3]), stream=True)
            icon_response.raise_for_status()  # Hatalı cevaplar için HTTPError oluşturur
            icon_img = Image.open(BytesIO(icon_response.content))
            rounded_icon = create_rounded_icon(icon_img)
            icon_tk = ImageTk.PhotoImage(rounded_icon)
            iconLabel.configure(image=icon_tk)
            iconLabel.image = icon_tk
        except Exception as e:
            print(f"Hava durumu simgesi yüklenemedi: {e}")
            iconLabel.configure(image='')  # Yüklenemezse simgeyi temizle
            iconLabel.image = None
    else:
        locationLabel['text'] = "Hata"
        tempLabel['text'] = ''
        conditionLabel['text'] = ''
        iconLabel.configure(image='')
        iconLabel.image = None

def on_enter(event):
    main()

# Uygulama arayüzü oluşturma
app = Tk()
app.geometry('500x600')
app.title('CE Hava Durumu')
app.resizable(False, False)  # Pencerenin yeniden boyutlandırılmasını devre dışı bırak

# Şehir girişi
cityEntry = Entry(app, justify='center', font=('Arial', 20))
cityEntry.pack(fill=BOTH, ipady=10, padx=18, pady=10)
cityEntry.focus()
cityEntry.bind('<Return>', on_enter)  # Enter tuşuna basıldığında on_enter fonksiyonunu çağır

# Arama butonu
searchButton = Button(app, text="Arama", font=('Arial', 15), command=main)
searchButton.pack(fill=BOTH, ipady=10, padx=20)

# Hava durumu simgesi
iconLabel = Label(app)
iconLabel.pack(pady=10)

# Konum etiketi
locationLabel = Label(app, font=('Arial', 30))
locationLabel.pack()

# Sıcaklık etiketi
tempLabel = Label(app, font=('Arial', 40, 'bold'))
tempLabel.pack()

# Durum etiketi
conditionLabel = Label(app, font=('Arial', 20))
conditionLabel.pack()

# Uygulamayı çalıştırma
app.mainloop()
