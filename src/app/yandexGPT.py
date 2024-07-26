import requests

prompt = {
    "modelUri": "gpt://b1g9ggm30bfoe5sv1i6s/yandexgpt-lite",
    "completionOptions": {
        "stream": False,
        "temperature": 0.6,
        "maxTokens": "1000"
    },
    "messages": [
        {
            "role": "system",
            "text": "Ты ассистент брокер, способный предсказать стоимость или падение цены на криптовалюту Bitcoin"
        },
        {
            "role": "user",
            "text": "Привет, Брокер! Мне нужна твоя помощь, чтобы узнать больше о криптовалюте. Как я могу научиться ее использовать?"
        },
        {
            "role": "assistant",
            "text": "Изучение основ: Первым делом стоит изучить базовые концепции криптовалют, такие как блокчейн, майнинг, кошельки и транзакции. Это поможет вам понять, как работает криптовалюта."
        },
        {
            "role": "user",
            "text": "Хорошо, а как насчет предсказания стоимости на исходя из данных криптобиржи? У меня есть данные с криптобиржи. Ты сможешь приблизительно предсказать рост или падение стоимости в учебных целях?"
        }
    ]
}


url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Api-Key AQVN1U1YQfFxvnRR42_wjo_aH1esHkQ0aHhWBXrJ"
}

response = requests.post(url, headers=headers, json=prompt)
result = response.text
print(result)