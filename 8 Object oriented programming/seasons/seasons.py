from datetime import date  # Importing the 'date' class from the 'datetime' module
import sys  # Importing the 'sys' module for system-related functions
import inflect  # Importing the 'inflect' module for converting numbers to words

def main():
    # Asking the user to input their birth date
    birth_date = input("Date of Birth (YYYY-MM-DD): ")

    # Calling the 'calculate_words' function to calculate the number of minutes lived
    minutes_lived = calculate_words(birth_date)

    # Printing the result in a formatted manner
    print(minutes_lived.capitalize(), "minutes")


def calculate_words(birth_date):
    try:
        # Parsing the birth date string into year, month, and day
        year, month, day = birth_date.split("-")
        year = int(year)
        month = int(month)
        day = int(day)

        # Calculating the time elapsed from the birth date until today
        time_to_birthday = abs(date.today() - date(year, month, day))

        # Converting the time elapsed to minutes
        minutes = time_to_birthday.days * 24 * 60

        # Using inflect to convert the number of minutes to words
        p = inflect.engine()
        words = p.number_to_words(minutes, andword="")
        return words
    except ValueError:
        # Handling the case where the input date format is invalid
        sys.exit("Invalid date")

if __name__ == "__main__":
    # Calling the 'main' function when the script is executed
    main()
