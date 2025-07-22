"""Creating Dictionary Utility Functions"""

__author__: str = "730766142"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a given dictionary."""
    i: int = 0
    new_values: list[str] = []
    new_keys: list[str] = []
    inverted_dict: dict[str, str] = dict()
    for key in dictionary:
        new_values.append(key)  # creating new lists for the new keys and values
        new_keys.append(dictionary[key])
    while i < len(new_values):
        if (
            new_keys[i] in inverted_dict
        ):  # adding KeyError if a key is already present in the new dictionary
            raise KeyError("Two or more of the same key is not allowed!")
        else:
            inverted_dict[new_keys[i]] = new_values[
                i
            ]  # looping through each elem of lists to create a dict
        i += 1
    return inverted_dict


def favorite_color(dictionary: dict[str, str]) -> str:
    """Returns the color that appears most frequently."""
    popular_color: str = ""
    if len(dictionary) == 0:
        return ""
    count_dict: dict[str, int] = dict()
    for (
        key
    ) in dictionary:  # creating new dictionary with counts of each color w/o repeats
        if dictionary[key] in count_dict:
            count_dict[dictionary[key]] += 1
        else:
            count_dict[dictionary[key]] = 1
    largest_count: int = 0
    for key in count_dict:  # determining the largest count by examining new dictionary
        if count_dict[key] > largest_count:
            largest_count = count_dict[key]
    for key in count_dict:
        if (
            count_dict[key] == largest_count
        ):  # picks the first color whose count matches largest count
            popular_color = key  # assigns this color to the variable popular_color
    return popular_color


def count(values: list[str]) -> dict[str, int]:
    """Counts the number of times a value appears in the input list."""
    dictionary: dict[str, int] = dict()
    i: int = 0
    while i < len(values):
        if values[i] in dictionary:
            dictionary[
                values[i]
            ] += 1  # adding count if the value was already encountered in while loop
        else:
            dictionary[values[i]] = 1
        i += 1
    return dictionary


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Sorts words by their beginning letter."""
    i: int = 0
    alphabetized_dict: dict[str, list[str]] = dict()
    letters: list[str] = []
    while i < len(
        input
    ):  # making a new list with just the first letters of all the words (w/o repeats)
        if (input[i].lower())[0] not in letters:
            letters.append((input[i].lower())[0])
        i += 1
    for (
        letter
    ) in letters:  # now sorting words from input list based on the first letter
        # (which is already stored in new_keys)
        i = 0
        word_list: list[str] = (
            []
        )  # making a list to store the words that begin with the letter (resets!)
        while i < len(
            input
        ):  # looping through input list and seeing if the words' first letter
            # matches the key in new_keys
            if (input[i].lower())[0] == letter:
                word_list.append(input[i])
            i += 1
            alphabetized_dict[letter] = (
                word_list  # adds to dict for each letter in our list b/c of for loop!
            )
    return alphabetized_dict


def update_attendance(log: dict[str, list[str]], day: str, student: str) -> None:
    """Updates attendance log with new students"""
    list_of_days: list[str] = []
    for key in log:
        if (
            key == day and student not in log[key]
        ):  # adding student to preexisitng list if the day is already in dictionary
            log[key].append(student)
        list_of_days.append(key)
    if (
        day not in list_of_days
    ):  # had to do this instead of "else:" in for loop because else would just keep
        # adding new keys even if the day of the week was just found later in the dict.
        new_list: list[str] = (
            []
        )  # have to append student to a new list because values of the dict are lists
        new_list.append(student)
        log[day] = new_list
    return None
