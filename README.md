# CE Hava Durumu Uygulaması

## Gereksinimler
- Python 3.x
- `requests` kütüphanesi
- `Pillow` (PIL) kütüphanesi
- `Tkinter` kütüphanesi (Python'un standart kütüphanesi)

## Kurulum
Öncelikle, gerekli Python kütüphanelerini kurmanız gerekiyor. Bunu aşağıdaki komutlarla yapabilirsiniz:

```bash
pip install requests
pip install Pillow
```

## Kullanım

1. Açılan pencerede şehir adını girin.
2. "Arama" butonuna basın veya Enter tuşuna basın.
3. Hava durumu bilgileri ekranda görünecektir.

# Kod Açıklaması

## Giriş

Bu uygulama, OpenWeatherMap API'sini kullanarak hava durumu verilerini alır ve bir GUI (Grafik Kullanıcı Arayüzü) ile kullanıcıya gösterir.

## Fonksiyonlar

- getWeather(city): Belirtilen şehir için hava durumu verilerini almak amacıyla API'ye bir istek gönderir.
- create_rounded_icon(icon_img): Hava durumu ikonu için yuvarlak bir görüntü oluşturur ve siyah bir arka plan ekler.
- main(): Kullanıcının girdiği şehir adını alır, hava durumu verilerini getirir ve GUI'yi günceller.
- on_enter(event): Kullanıcı Enter tuşuna bastığında main() fonksiyonunu çağırır.

## GUI Oluşturma

- `Tk()` ile uygulama penceresi oluşturulur.
- Şehir girişi için bir `Entry` widget'ı kullanılır.
- Arama butonu için bir `Button` widget'ı kullanılır.
- Hava durumu ikonunu göstermek için bir `Label` widget'ı kullanılır.
- Şehir, sıcaklık ve durumu göstermek için `Label` widget'ları kullanılır.
- `mainloop()` ile uygulama döngüsü başlatılır.

# Notlar

- API anahtarınızı güvenli bir şekilde saklamayı unutmayın.
- Hava durumu verilerini almak için kullanılan URL ve parametreler kodda sabit olarak tanımlanmıştır.
- OpenWeatherMap API'si ücretsiz kullanım için belirli bir sınır sunar. Bu sınırları aşmamaya dikkat edin.

# Güvenlik Uyarısı

- API anahtarınızı kod içinde saklamak güvenlik riski oluşturabilir. Daha güvenli yöntemler kullanarak anahtarınızı saklamayı düşünün.
- Kullanıcı girişlerini doğrulamak ve hataları düzgün bir şekilde ele almak önemlidir.

# Lisans

Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasını inceleyin.


