import pandas as pd

products = [
    {
        "id": "001",
        "title": "Смартфон Samsung Galaxy S21",
        "description": "Экран AMOLED 6.2 дюйма, 128 ГБ памяти, 8 ГБ ОЗУ, 5G, тройная камера."
    },
    {
        "id": "002",
        "title": "Ноутбук Dell XPS 13",
        "description": "Экран 13.3 дюйма Full HD, Intel Core i7, 16 ГБ ОЗУ, SSD 512 ГБ, Windows 11."
    },
    {
        "id": "003",
        "title": "Робот-пылесос Xiaomi",
        "description": "Интеллектуальная навигация, лазерная карта, автономность 120 мин, управление через приложение."
    },
    {
        "id": "004",
        "title": "Беспроводные наушники Bose QuietComfort",
        "description": "Активное шумоподавление, Bluetooth, 20 часов автономной работы, премиальный комфорт."
    },
    {
        "id": "005",
        "title": "Умные часы Apple Watch Series 7",
        "description": "Дисплей Retina, измерение пульса, отслеживание сна, GPS, водонепроницаемость."
    },
    {
        "id": "006",
        "title": "Планшет Huawei MatePad Pro",
        "description": "10.8-дюймовый экран, 6 ГБ ОЗУ, 128 ГБ памяти, поддержка стилуса, Android."
    },
    {
        "id": "007",
        "title": "Фотоаппарат Canon EOS 250D",
        "description": "Матрица 24.1 МП, видео 4K, поворотный экран, Wi-Fi и Bluetooth."
    },
    {
        "id": "008",
        "title": "Игровая приставка Sony PlayStation 5",
        "description": "SSD 825 ГБ, поддержка 4K, геймпад DualSense, быстрая загрузка."
    },
    {
        "id": "009",
        "title": "Электросамокат Ninebot Max G30",
        "description": "Макс. скорость 25 км/ч, дальность 65 км, колёса 10 дюймов, защита от влаги IPX5."
    },
    {
        "id": "010",
        "title": "Телевизор LG OLED55CX",
        "description": "55 дюймов, OLED-дисплей, 4K, HDR, Dolby Vision, WebOS, управление голосом."
    }
]
#df = pd.read_csv('produits.txt', encoding='utf-8')

# Création du DataFrame
df = pd.DataFrame(products, columns=["description"])

# Enregistrement en CSV
df.to_csv("products.txt", index=False, encoding='utf-8-sig')


