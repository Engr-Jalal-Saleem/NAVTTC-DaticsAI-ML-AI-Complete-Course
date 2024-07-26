import random as rn
sml_let = 'qwertyuiopasdfghjklzxcvbnm'
cap_let = sml_let.upper()
digits = "1234567890"
spl_char = "!@#$%^&*|?><."
def password_gen():
    global sml_let, cap_let, digits, spl_char
    ls = []
    for i in range(3):
        rn_sml_let = rn.choice(sml_let)
        ls.append(rn_sml_let)
        rn_cap_let = rn.choice(cap_let)
        ls.append(rn_cap_let)
        rn_digits = rn.choice(digits)
        ls.append(rn_digits)
        rn_spl_char = rn.choice(spl_char)
        ls.append(rn_spl_char)
    password = ''.join(ls)
    return password