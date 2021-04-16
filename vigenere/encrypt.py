"""Module for encryption functions"""

from numpy import floor
from square import square, get_letter_from_index, get_index_from_letter


def encrypt_letter(letter_index, keyword_letter_index):
    """Encrypt a plain-text letter using a given keyword letter index"""

    square_output = square[keyword_letter_index, letter_index]  # Lookup the encrypted letter index

    return get_letter_from_index(square_output)


def decrypt_letter(letter_index, keyword_letter_index):
    """Decrypt a given encrypted-text letter using a given keyword letter"""

    row = square[keyword_letter_index: keyword_letter_index + 1, :].tolist()[0]  # Get row of the keyword letter
    square_output = row.index(letter_index)  # Find column of the given encrypted letter

    return get_letter_from_index(square_output)


def process_text(input_text, keywords, step_size=0, decrypt=False):
    """Process a given input text using a given set of keywords

    If encrypt is True, encrypt the text, otherwise decrypt
    """
    input_text = input_text.upper().replace(" ", "")
    keywords = keywords.strip().upper().split(" ")

    output_text = ""

    for i in range(0, len(input_text)):
        letter = input_text[i]
        letter_index = get_index_from_letter(letter=letter)
        for keyword in keywords:
            keyword_length = len(keyword)
            cycles = int(floor(i / keyword_length))  # Count the number of times we've cycled through the keyword
            keyword_letter = keyword[i % keyword_length]
            # Increase the keyword letter index by the number of cycles multiplied by the step size
            # This causes the encryption to jump every keyword cycle
            keyword_letter_index = get_index_from_letter(letter=keyword_letter) + (cycles * step_size)

            if decrypt:
                output_letter = decrypt_letter(letter_index=letter_index, keyword_letter_index=keyword_letter_index)
            else:
                output_letter = encrypt_letter(letter_index=letter_index, keyword_letter_index=keyword_letter_index)

            letter = output_letter
            letter_index = get_index_from_letter(letter=letter)

        output_text += letter

    return output_text
