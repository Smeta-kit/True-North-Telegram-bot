
#----- Language list
LANG = {
    "ru": {
        "language_prompt": "Выберите язык / Choose your language:",
        "choose_tour": "Выберите тур из списка:",
        "invalid_choice": "Выберите вариант из кнопок.",
        "days": "На сколько дней поездка? (от {min_days} до {max_days})",
        "invalid_days": "Введите число от {min_days} до {max_days}.",
        "people": "Сколько человек едет?",
        "invalid_number": "Введите число, например 2.",
        "choose_hotel": "Выберите категорию отеля ⭐:",
        "result": "Тур: <b>{tour}</b>\nДней: {days}\nКоличество человек: {people}\nОтель: {hotel}⭐\nИтоговая стоимость: <b>{total:,} BYN</b>",
        "restart": "Если хотите, можете начать заново: /start"
    },
    "en": {
        "language_prompt": "Выберите язык / Choose your language:",
        "choose_tour": "Choose a tour from the list:",
        "invalid_choice": "Choose an option from the buttons.",
        "days": "How many days is the trip? (from {min_days} to {max_days})",
        "invalid_days": "Enter a number from {min_days} to {max_days}.",
        "people": "How many people are traveling?",
        "invalid_number": "Enter a number, e.g. 2.",
        "choose_hotel": "Choose hotel rating ⭐:",
        "result": "Tour: <b>{tour}</b>\nDays: {days}\nTravelers: {people}\nHotel: {hotel}⭐\nTotal price: <b>{total:,} BYN</b>",
        "restart": "If you want, restart: /start"
    }
}

#----- Tours list 

tours = {
    "Norway: Fjords & Peaks": {
        "date": "23/05/2026 – 24/06/2026",
        "duration": (7, 14),
        "difficulty": "Medium",
        "included": "Guides, accommodation, breakfast, transfers",
        "highlights": "Fjord cruise, mountain trails, waterfalls",
        "base_price": 3500
    },
    "Lapland: Northern Lights Hunt": {
        "date": "22/08/2026 – 29/08/2026",
        "duration": (5, 7),
        "difficulty": "Easy",
        "included": "Dog sleds, meals, accommodation",
        "highlights": "Northern Lights, Sámi culture",
        "base_price": 2500
    },
    "Scandinavian Capitals": {
        "date": "25/01/2026 – 28/02/2026",
        "duration": (4, 10),
        "difficulty": "Easy",
        "included": "City transfers, museums, hotels",
        "highlights": "Design, hygge, modern culture",
        "base_price": 2000
    },
    "Iceland: Fire & Ice Adventure": {
        "date": "15/06/2026 – 22/06/2026",
        "duration": (7, 7),
        "difficulty": "Medium",
        "included": "Transport, guide, accommodation, breakfasts",
        "highlights": "Glacier hike, geothermal lagoons, waterfalls",
        "base_price": 3500
    },
    "Patagonia: Torres del Paine National Park Trek": {
        "date": "10/02/2026 – 20/02/2026",
        "duration": (10, 10),
        "difficulty": "Hard",
        "included": "Park permits, mountain huts, professional guide, transfers",
        "highlights": "Torres del Paine peaks, Grey Glacier, Andean condors",
        "base_price": 5000
    },
    "Norway: Fjords & Trolltunga Hike": {
        "date": "15/07/2026 – 22/07/2026",
        "duration": (7, 7),
        "difficulty": "Medium",
        "included": "Professional mountain guide, transport from Bergen, overnight in cabins",
        "highlights": "Trolltunga (Troll's Tongue) rock, Hardangerfjord, traditional Norwegian dinner",
        "base_price": 3500
    },
    "Lofoten Islands: Arctic Summer & Midnight Sun": {
        "date": "20/06/2026 – 27/06/2026",
        "duration": (14, 14),
        "difficulty": "Easy",
        "included": "Rorbu (fisherman's cabin) accommodation, boat tour, bicycle rental",
        "highlights": "Midnight sun photography, fishing villages (Å & Reine), white-sand beaches",
        "base_price": 7000
    },
    "Norway: Northern Lights & Whale Safari in Tromsø": {
        "date": "15/01/2026 – 21/01/2026",
        "duration": (6, 6),
        "difficulty": "Easy",
        "included": "Thermal suits, whale watching boat tour, Aurora Borealis chase with photographer",
        "highlights": "Whale watching (orcas & humpbacks), Sami culture experience, dog sledding",
        "base_price": 3000
    }
}