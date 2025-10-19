def validate_pesel(pesel):
    if len(pesel) != 11 or not pesel.isdigit():
        return None
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    checksum = sum(int(pesel[i]) * weights[i] for i in range(10))
    checksum = (10 - (checksum % 10)) % 10
    if checksum != int(pesel[10]):
        return None
    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])
    # Określenie wieku i roku
    if 1 <= month <= 12:
        century = 1900
    elif 21 <= month <= 32:
        century = 2000
        month -= 20
    elif 41 <= month <= 52:
        century = 2100
        month -= 40
    elif 61 <= month <= 72:
        century = 2200
        month -= 60
    elif 81 <= month <= 92:
        century = 1800
        month -= 80
    else:
        return None
    birth_year = century + year
    gender = "Kobieta" if int(pesel[9]) % 2 == 0 else "Mężczyzna"

    return {"birthday": f"{birth_year:04d}-{month:02d}-{day:02d}", "sex": gender}
