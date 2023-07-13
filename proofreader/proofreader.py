import sys
from gingerit.gingerit import GingerIt

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py \"text to check\"")
        sys.exit(1)

    text = sys.argv[1]
    parser = GingerIt()

    corrected_text = parser.parse(text)
    print("Original text:", text)
    print("Corrected text:", corrected_text['result'])

if __name__ == "__main__":
    main()
