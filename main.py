#String Analyzer
def clean_text(text):
    return text.lower().replace(" ", "")

def is_palindrome(text):
    text = clean_text(text)
    return text == text[::-1]

def count_vowels(text):
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)

def reverse_string(text):
    return text[::-1]

def char_frequency(text):
    freq = {}
    for char in text:
        if char!= " ":
            freq[char] = freq.get(char,0) + 1
    return freq


def show_menu():
    print("\n" + "="*40)
    print("      STRING ANALYZER TOOL")
    print("="*40)
    print("1. Check Palindrome")
    print("2. Count Vowels")
    print("3. Reverse String")
    print("4. Character Frequency")
    print("5. Enter New String")
    print("6. Exit")
    print("="*40)


def main():
    print("Welcome to String Analyzer 🚀")
    text = input("Enter a string: ").strip()

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            result = is_palindrome(text)
            print(f"\n Palindrome: {'Yes' if result else 'No'}")

        elif choice == "2":
            print(f"\n Vowel count: {count_vowels(text)}")

        elif choice == "3":
            print(f"\n Reversed string: {reverse_string(text)}")

        elif choice == "4":
            freq = char_frequency(text)
            print("\n Character Frequency:")
            for item in freq.items():
                char = item[0]
                count = item[1]
                print(char,"-",count)

        elif choice == "5":
            text = input("\nEnter a new string: ").strip()
            if not text:
                print("⚠️ Empty input! Keeping previous string.")

        elif choice == "6":
            print("\nThank you for using the tool! 👋")
            break

        else:
            print("\n❌ Invalid choice. Please enter 1-5.")

        input("\nPress Enter to return to menu...")

if __name__ == "__main__":
    main()
