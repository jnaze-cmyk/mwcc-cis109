import argparse

def transform_upper(text):
    uppercase = text.upper()
    print(uppercase)

def transform_lower(text):
    lowercase = text.lower()
    print(lowercase)

def get_word_count(text):
    toks = text.split(",")
    return len(toks)

def filter_short(text, min_length):
    min_length = 3
    if len(text) >= min_length:
        print(text)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--action" , help="transformer action [count | lower | upper] " )
    parser.add_argument("-t", "--text" , help="text to transform" )
    args = parser.parse_args()

    if args.action:
        print(f"Action: {args.action}")



    if args.text:
        print(f"text: {args.text}")

    match args.action:
        case "count":
            print(f"Word Count: {get_word_count(args.text)}")

main()