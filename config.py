from os import environ
from dotenv import load_dotenv

# <- Activate environment ->
load_dotenv()

# <- Secret keys ->
API_KEY = environ["API_KEY"]
DB_PASSWORD = environ["DB_PASSWORD"]

# <- Static messages ->
MSG_UNKNOWN_COMMAND = "Неизвестная команда! Напиши /info для получения списка существующих команд."
MSG_COMMAND_LIST = "/start - Приветственное сообщение\n" \
                   "/info - Список команд\n" \
                   "/money - Получение текущего баланса\n" \
                   "/stat - Статистика по расходам и доходам\n" \
                   "/advice - Узнать у ИИ что он думает насчет трат\n" \
                   "/change - Внести изменения по доходам/расходам"

# <- Formatted messages ->
MSG_START = "Привет, <b>{0}</b>! Этот бот позволит тебе контролировать доходы и расходы," \
            "заполнять информацию по текущему балансу, получать <b>графики</b> трат и ежедневную статистику по счету. " \
            "\nНапиши /info для получения списка существующих команд."
MSG_BUDGET = "Ваш текущий баланс составляет <b>{0}</b> руб."
