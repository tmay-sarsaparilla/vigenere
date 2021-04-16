
from vigenere.square import square, get_letter_from_index, get_index_from_letter


def encrypt_letter(letter, keyword_letter):
    """Encrypt a plain-text letter using a given keyword letter"""
    letter_index = get_index_from_letter(letter=letter)
    keyword_letter_index = get_index_from_letter(letter=keyword_letter)

    square_output = square[keyword_letter_index, letter_index]  # Lookup the encrypted letter index

    return get_letter_from_index(square_output)


def decrypt_letter(letter, keyword_letter):
    """Decrypt a given encrypted-text letter using a given keyword letter"""
    letter_index = get_index_from_letter(letter=letter)
    keyword_letter_index = get_index_from_letter(letter=keyword_letter)

    row = square[keyword_letter_index: keyword_letter_index + 1, :].tolist()[0]  # Get row of the keyword letter
    square_output = row.index(letter_index)  # Find column of the given encrypted letter

    return get_letter_from_index(square_output)


def process_text(input_text, keywords, encrypt=True):
    """Process a given input text using a given set of keywords

    If encrypt is True, encrypt the text, otherwise decrypt
    """
    input_text = input_text.upper().replace(" ", "")
    keywords = keywords.strip().upper().split(" ")

    output_text = ""

    for i in range(0, len(input_text)):
        letter = input_text[i]
        for keyword in keywords:
            keyword_letter = keyword[i % len(keyword)]

            if encrypt:
                output_letter = encrypt_letter(letter=letter, keyword_letter=keyword_letter)
            else:
                output_letter = decrypt_letter(letter=letter, keyword_letter=keyword_letter)

            letter = output_letter

        output_text += letter

    return output_text


if __name__ == "__main__":
    print(encrypt_letter('T', 'E'))
    print(decrypt_letter('X', 'E'))

    test_text = process_text("ATTACKATDAWN", "GO CAT")
    print(test_text)

    test_plain_text = process_text("IHSQIRIHCQCU", "GO CAT", False)
    print(test_plain_text)
