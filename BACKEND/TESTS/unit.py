from BACKEND.CRUD import CRUD_users
import names
from random import randint

DEFAULT_USER_TIME_PRICES_TEST = [
    ('15 minutos', 8000),
    ('30 minutos', 14000),
    ('1 hora', 18000),
    ('2 horas', 32000)
]

payedAndUserTimeDoneValues = [True, False]

def generateRandomUsers():
    global DEFAULT_USER_TIME_PRICES_TEST

    for _ in range(4):
        timeSelected = randint(0, 3)
        hasUserPayed = randint(0, 1)
        userTimeDone = randint(0, 1)  #  use random only when you don't need false value on the field

        newUser = {
            "Nombre": names.get_full_name(gender='male'),
            "Manilla": str(randint(1, 101)),
            "Tiempo": DEFAULT_USER_TIME_PRICES_TEST[timeSelected][0],
            "Acudiente": names.get_full_name(),
            "ID-Acudiente": str(randint(0, 1000)),
            "Dinero": DEFAULT_USER_TIME_PRICES_TEST[timeSelected][1],
            "Pagado": payedAndUserTimeDoneValues[hasUserPayed],
            "Usuario VIP": False,
            "Hora entrada": 0,
            "Hora salida": 0,
            "Sale": payedAndUserTimeDoneValues[1]
        }
        CRUD_users.createUser(newUser)
