import random
import string


def log_gen():
    lst_1 = ["Ae", "Di", "Mo", "Fam", "Ri", "Tr", "Sa"]
    lst_2 = ["dar", "kil", "glar", "dom", "tlar", "pyt", "ben", "sed", "grim"]
    rand_number = random.randint(0, 1)
    if rand_number == 1:
        random_log = f"{random.choice(lst_1)}{random.choice(lst_2)}{random.randint(1, 100)}"
        return random_log
    else:
        random_log = f"{random.choice(lst_1)}{random.choice(lst_2)}"
        return random_log


def pass_gen():
    result = ""
    choices = string.ascii_letters + string.digits + "!@#$%^&*"
    for i in range(8):
        result += random.choice(choices)
    return result


def mails_gen(login):
    lst_mails = ["gmail.com", "mail.ru", "uk.net"]
    result_mail = f"{login}@{random.choice(lst_mails)}"
    return result_mail

