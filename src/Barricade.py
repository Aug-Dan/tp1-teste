from Book import Book 
import re

VALID_CPF_LEN = 11

class Barricade:
    class InputValidator:
        @staticmethod
        def is_valid_cpf(cpf: int) -> bool:
            # Converte o CPF para string
            cpf = str(cpf)

            # Um CPF válido deve ter 11 dígitos
            if len(cpf) != VALID_CPF_LEN:
                return False

            # Calcula o primeiro dígito verificador
            sum_of_products = sum((10 - i) * int(digit) for i, digit in enumerate(cpf[:9]))
            expected_first_check_digit = (sum_of_products * 10 % 11) % 10

            # Calcula o segundo dígito verificador
            sum_of_products = sum((11 - i) * int(digit) for i, digit in enumerate(cpf[:10]))
            expected_second_check_digit = (sum_of_products * 10 % 11) % 10

            # O CPF é válido se os dígitos verificadores calculados correspondem aos dígitos verificadores reais
            return cpf[-2:] == str(expected_first_check_digit) + str(expected_second_check_digit)

        @staticmethod
        def is_valid_password(password: str) -> bool:
            # A senha é inválida se contém um espaço
            if " " in password:
                return False

            # A senha deve ter pelo menos uma letra maiúscula, uma letra minúscula e um caractere especial
            if re.search("[A-Z]", password) and re.search("[a-z]", password) and re.search("[!@#$%^&*()]", password):
                return True

            return False

        @staticmethod
        def is_string(input) -> bool:
            return isinstance(input, str)

        @staticmethod
        def is_integer(input) -> bool:
            return isinstance(input, int)