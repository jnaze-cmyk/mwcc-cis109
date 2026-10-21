import argparse

def transform_upper(data):
    text_uppercase = data.upper()
    return text_uppercase

def transform_lower(data):
    text_lowercase = data.lower()
    return text_lowercase

def get_word_count(data):
    toks = data.split(",")
    return len(toks)

def filter_short(data, min_length):
    min_length = 3
    if len(data) >= min_length:
        print(data)
    else:
        print("None")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--action" , help="transformer action [count | lower | upper] " )
    parser.add_argument("-d", "--data" , help="data to transform" )
    args = parser.parse_args()

    if args.action:
        print(f"Action: {args.action}")

    if args.data:
        print(f"data: {args.data}")

    match args.action:
        case "count":
            print(f"Word Count: {get_word_count(args.data)}")
        case "lower":
            print(f"Text Lowercase: {transform_lower(args.data)}")
        case "upper":
            print(f"Text Uppercase: {transform_upper(args.data)}")
main()
'''

if __name__ == "__main__":
    main()
'''
