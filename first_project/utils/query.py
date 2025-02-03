from typing import Literal, Union

answer = {"yes": True, "ye": True, "y": True, "no": False, "n": False}


def query_yes_no(
    question: str, default: Literal["yes", "no", None] = "yes"
) -> Union[bool, str]:
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        print(question + prompt)
        user_choice = input().lower()
        if default is not None and user_choice == "":
            return answer[default]
        elif user_choice in answer:
            return answer[user_choice]
        else:
            print("Please respond with 'yes' or 'no' (or 'y' or 'n').\n")


def query_int(question: str) -> int:
    while True:
        print(question)
        user_choice = input()
        if user_choice.isdigit():
            return int(user_choice)
        else:
            print("Value must be a number")
