import unittest
from develop.password_generator import generate_password

class UnitTests(unittest.TestCase):

    @staticmethod
    def test_lowercase_letters():
        # Test case 1: Only lowercase letters
        print("\nTest Case 1: Only lowercase letters")

        password = generate_password(10, False, False, False)
        assert password.islower(), "Test Case 1 Failed: Password contains non-lowercase characters"
        print("Test Case 1 Passed")

    @staticmethod
    def test_special_chars_letters():
        print("\nTest Case 2: Include special characters")

        password = generate_password(10, False, False, True)
        # Check if special characters are present
        special_chars = "<>!@#$%^&*\"}{[]|/();:._+-=\\"
        assert any(
            char in special_chars for char in password), "Test Case 2 Failed: Password doesn't contain special characters"
        print("Test Case 2 Passed")

    @staticmethod
    def test_numbers():
        print("\nTest Case 3: Include numbers")

        password = generate_password(10, False, True, False)
        # Check if numbers are present
        assert any(char.isdigit() for char in password), "Test Case 3 Failed: Password doesn't contain numbers"
        print("Test Case 3 Passed")

    @staticmethod
    def test_uppercase_letters():
        print("\nTest Case 4: Include uppercase letters")

        password = generate_password(10, True, False, False)
        # Check if uppercase letters are present
        assert any(char.isupper() for char in password), "Test Case 4 Failed: Password doesn't contain uppercase letters"
        print("Test Case 4 Passed")

    @staticmethod
    def test_all_chars():
        print("\nTest Case 5: All character types")
        special_chars = "<>!@#$%^&*\"}{[]|/();:._+-=\\"

        password = generate_password(10, True, True, True)

        # Check if all character types are present
        has_lower = any(char.islower() for char in password)
        has_upper = any(char.isupper() for char in password)
        has_number = any(char.isdigit() for char in password)
        has_special = any(char in special_chars for char in password)

        assert has_lower and has_upper and has_number and has_special, \
            "Test Case 5 Failed: Password doesn't contain all character types"
        print("Test Case 5 Passed")

    @staticmethod
    def test_minimal_length():
        print("\nTest Case 6: Minimal length")

        password = generate_password(4, True, True, True)
        assert len(password) == 4, f"Test Case 6 Failed: Expected length 4, got {len(password)}"
        print("Test Case 6 Passed")

    @staticmethod
    def test_maximum_length():
        print("\nTest Case 7: Maximum length")

        password = generate_password(20, True, True, True)
        assert len(password) == 20, f"Test Case 7 Failed: Expected length 20, got {len(password)}"
        print("Test Case 7 Passed")





