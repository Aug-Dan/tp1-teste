import re

VALID_CPF_LEN = 11


class Barricade:
    @staticmethod
    def is_valid_cpf(cpf: int) -> bool:
        # Um CPF válido deve ter 11 dígitos e não ser uma sequência repetida
        cpf_str = str(cpf).zfill(VALID_CPF_LEN)
        if len(cpf_str) != VALID_CPF_LEN or len(set(cpf_str)) == 1 or (not isinstance(cpf, int)):
            return False

        # Calcula o primeiro dígito verificador
        sum_of_products = sum((10 - i) * int(cpf_str[i]) for i in range(9))
        expected_first_check_digit = (sum_of_products * 10 % 11) % 10

        # Calcula o segundo dígito verificador
        sum_of_products = sum((11 - i) * int(cpf_str[i]) for i in range(10))
        expected_second_check_digit = (sum_of_products * 10 % 11) % 10

        # O CPF é válido se os dígitos verificadores calculados correspondem aos dígitos verificadores reais
        return cpf_str[9] == str(expected_first_check_digit) and cpf_str[10] == str(expected_second_check_digit)

    @staticmethod
    def is_valid_password(password: str) -> bool:
        # A senha é inválida se contém um espaço
        if " " in password:
            return False

        # A senha deve ter pelo menos 8 caracteres, uma letra maiúscula, uma letra minúscula e um caractere especial
        if (
            len(password) >= 8 and
            re.search("[A-Z]", password) and
            re.search("[a-z]", password) and
            re.search("[!@#$%^&*()_+=-]", password)
        ):
            return True

        return False
    
    @staticmethod
    def is_valid_email(email: str) -> bool:
        # Expressão regular para validar o formato do email
        email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(email_regex, email) is not None

    @staticmethod
    def is_string(input) -> bool:
        return isinstance(input, str)

    @staticmethod
    def is_integer(input) -> bool:
        return isinstance(input, int)
