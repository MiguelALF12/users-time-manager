# const PLACEHOLDERS
placeholders = {
    'PH_SEARCH_RECORD': "Buscar registro",
    'PH_HOUR': "00:00",
    'PH_BRACELET_NUMBER': "0",
    'PH_TOTAL_USERS': "00",
    'PH_TOTAL_MONEY': "$0",
    'PH_NAME': "Ej: Miguel Lopez",
    'PH_PARENT': "Ej: Juliana Vélez",
    'PH_PARENT_ID': "Ej: La cédula",
    'PH_EXTRA_TIME': "Ej: [15,120]"
}

DEFAULT_USER_TIME_PRICES = {
    '15 minutos': 8000,
    '30 minutos': 14000,
    '1 hora': 18000,
    '2 horas': 32000,
}

VIP_USER_TIME_PRICES = {
    '15 minutos': 8000,
    '30 minutos': 11500,
    '1 hora': 14500,
    '2 horas': 32000,
}

totalTimeConvertion = {
    # TODO: This really need to go like this?
    # (minute-hour, seconds)
    '15 minutos': (0, 15, 900),
    '30 minutos': (0, 30, 1800),
    '1 hora': (1, 60, 3600),
    '2 horas': (2, 120, 7200)
}
