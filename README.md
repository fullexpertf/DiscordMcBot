# Minecraft Discord Botu

Minecraft topluluğunuz için hazırlanmış, premium botların özelliklerini ücretsiz sağlayan bir açık kaynak bot.

## Kurulum

1. `python -m venv venv && source venv/bin/activate`
2. `pip install -r requirements.txt`
3. `python run_setup.py` komutuyla interaktif kurulum ekranından token, prefix vb. girin.
4. `python bot.py` ile botu başlatın.

## Özellikler
- Moderasyon: Ban, kick, mute, temizleme.
- Seviye sistemi: Mesaj aktivitesine göre XP/rol.
- Ekonomi: Sanal para, mağaza, günlük ödül.
- Müzik: YouTube’dan şarkı çalma.
- Minecraft entegrasyonu: Sunucu durumu, oyuncu sayısı vb.

## Komutlar
Komutlar hem slash (`/komut`) hem de metin prefix'i (`!komut`) ile çalışır.

| Komut | Açıklama |
|-------|----------|
| `kick <üye> [sebep]` | Bir üyeyi sunucudan atar. |
| `ban <üye> [sebep]` | Bir üyeyi sunucudan yasaklar. |
| `temizle <miktar>` | Kanalda belirtilen sayıda mesajı siler. |
| `balance` | Mevcut bakiye bilgisini gösterir. |
| `daily` | Günlük 100 coin ödülü alır. |
| `level [üye]` | Belirtilen üyenin (veya komutu yazanın) seviyesini gösterir. |
| `play <url>` | YouTube bağlantısından müzik çalar. |
| `stop` | Ses kanalındaki çalmayı durdurur. |
| `mcstatus <adres>` | Minecraft sunucusunun durumunu kontrol eder. |
