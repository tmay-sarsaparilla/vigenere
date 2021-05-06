"""Main module of vigenere package"""

import sys
import argparse
from .encrypt import process_text


def main(args):
    """Parse input arguments and execute text processing"""
    parser = argparse.ArgumentParser(description="Vigenère encryptor", usage="Used to encrypt and decrypt messages")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Decryption option")
    parser.add_argument("-text", type=str, required=True, help="Text to be processed by the encryptor")
    parser.add_argument(
        "-keywords", type=str, required=True,
        help="Keywords to be used by the encryptor. To provide multiple keywords separate them by a space")
    parser.add_argument(
        "-step", type=int, default=0, required=False,
        help="How many steps the encryptor should take each keyword cycle")
    args = parser.parse_args(args)

    processed = process_text(input_text=args.text, keywords=args.keywords, step_size=args.step, decrypt=args.decrypt)

    print(f"Input text: {args.text}")
    print(f"Output text: {processed}")


if __name__ == "__main__":
    main(sys.argv[1:])
