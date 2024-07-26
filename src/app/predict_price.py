import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from main import data_values

data = {
    'price': 60753.07585976551,
    'volume_24h': 11719207918.962496,
    'volume_change_24h': -51.7012,
    'percent_change_1h': -0.07064751,
    'percent_change_24h': 0.17099265,
    'percent_change_7d': -5.70157665,
    'percent_change_30d': -11.28454257,
    'percent_change_60d': 1.31048516,
    'percent_change_90d': -13.95309402,
    'market_cap': 1197965966166.8274,
    'market_cap_dominance': 53.4169,
    'fully_diluted_market_cap': 1275814593055.08,
    'tvl': None,
    'last_updated': '2024-06-30T03:31:00.000Z'
}

train_data = {
    "price": 60757.4917999061,
    "volume_24h": 11723623674.845003,
    "volume_change_24h": -51.7034,
    "percent_change_1h": -0.13804143,
    "percent_change_24h": 0.22711246,
    "percent_change_7d": -5.72048497,
    "percent_change_30d": -11.28482617,
    "percent_change_60d": 1.31823973,
    "percent_change_90d": -14.15911635,
    "market_cap": 1198053042350.579,
    "market_cap_dominance": 53.416,
    "fully_diluted_market_cap": 1275907327798.03,
    "tvl": None,
    "last_updated": "2024-06-30T03:18:00.000Z"
}

# Преобразуем данные в массив numpy для обработки
data_values = np.array(list(data.values())[:-13]).reshape(1, -1)  # Исключаем 'last_updated'
train_data_values = np.array(list(train_data.values())[:-13]).reshape(1, -1)

# Нормализация данных
scaler = MinMaxScaler(feature_range=(0, 1))
scaler.fit(train_data_values)
train_scaled_data = scaler.transform(train_data_values)
scaled_data = scaler.transform(data_values)

"""X = [
        60757.4917999061,
        11723623674.84500,
        -51.7034, 
        -0.13804143,
        0.22711246,
        -5.72048497,
        -11.28482617,
        1.31823973,
        -14.15911635,
        1198053042350.579,
        53.416,
        1275907327798.03
    ]

y = [
        'price','volume_24h', 'volume_change_24h', 'percent_change_1h',
        'percent_change_24h', 'percent_change_7d', 'percent_change_30d',
        'percent_change_60d', 'percent_change_90d', 'market_cap',
        'market_cap_dominance', 'fully_diluted_market_cap'
    ]"""
X = [60757.4917999061]
y = ['price']
#Данные не разделяем, сразу берем исходные
X_train = np.array([X]).reshape(1,-1)
y_train = np.array([X[0]])
# Определение архитектуры LSTM нейросети
model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(X_train.shape[1], 1)))
model.add(LSTM(units=50))
model.add(Dense(units=1))

# Компиляция модели
model.compile(optimizer='adam', loss='mean_squared_error')

# Обучение модели
model.fit(X_train, y_train, epochs=25, batch_size=32)

# Прогнозирование
predicted_price = model.predict(data_values)

# Создаем массив с формой (1, 12), где первый элемент - это предсказанная цена,
# а остальные элементы заполняем нулями или другими значениями, которые были использованы при обучении scaler
predicted_price_reshaped = np.zeros((1,2))
predicted_price_reshaped[:, 0] = predicted_price.flatten()  # Предполагаем, что предсказываем 'price'

# Обратное преобразование нормализованных данных в исходный масштаб
predicted_price_original_scale = scaler.inverse_transform(predicted_price_reshaped)



