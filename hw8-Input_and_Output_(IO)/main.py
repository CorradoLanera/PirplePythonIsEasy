# -*- coding: utf-8 -*-

"""
main.py: Homework #8: Input and Output (I/O) (Python Is Easy course by Pirple)

Details:

Create a note-taking program. When a user starts it up, it should prompt
them for a filename.

If they enter a file name that doesn't exist, it should prompt them to
enter the text they want to write to the file. After they enter the
text, it should save the file and exit.

If they enter a file name that already exists, it should ask the user if
they want:

A) Read the file

B) Delete the file and start over

C) Append the file

If the user wants to read the file it should simply show the contents of
the file on the screen. If the user wants to start over then the file
should be deleted and another empty one made in its place. If a user
elects to append the file, then they should be able to enter more text,
and that text should be added to the existing text in the file.



Extra Credit:

Allow the user to select a 4th option:

D) Replace a single line

If the user wants to replace a single line in the file, they will then
need to be prompted for 2 bits of information:

1) The line number they want to update.

2) The text that should replace that line.



Turning it In:

Zip up your code files and attach them here to receive a grade and
continue with the course.

Submit your assignment
You may only submit one file with maximum 100 MB in size
"""

__author__ = "Corrado Lanera"
__credits__ = [
    "https://linuxize.com/post/python-check-if-file-exists/",
    "https://stackoverflow.com/questions/26320175/how-to-convert-integers-in-list-to-string-in-python"
]
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Corrado Lanera"
__email__ = "corrado.lanera@gmail.com"


# ----------------------------------------------------------------------

# https://linuxize.com/post/python-check-if-file-exists/
def file_exist(x):
    try:
        with open(x):
            return True
    except IOError:
        print("File not accessible")

    return False


def check_last_empty_line(x):
    return x[-1][-1] == "\n"


def write_new_note(x, note=None, check_last=True):
    if note is None:
        note = ask_for_content(check_last)
    if check_last is True:
        note = fix_last(note)

    with open(x, "w") as fw:
        fw.writelines(note)
        print("Content written to " + x)

    return x


def continue_note(x, note=None, check_last=True):
    print("Content will be added at the end of the file " + x)

    if note is None:
        note = ask_for_content(check_last)
    if check_last is True:
        note = fix_last(note)

    with open(x, "a") as fc:
        fc.writelines(note)
        print("Content added to " + x)

    return x


def print_note(x):
    with open(x) as fp:
        print(fp.read())
    return x


def fix_last(x):
    if not check_last_empty_line(x):
        x = x + "\n"
    return x


def ask_for_content(check_last=True):
    content = input("Please, enter the content: ")
    if check_last:
        content = fix_last(content)
    return content


def ask_for_filename():
    file_name = input(
        "Please, enter a note's filename (or \"q\" to exit ): "
    )
    if file_name == "q":
        exit()

    return file_name


def ask_for_selection(options):
    options = set(options)

    ok = False
    selection = "q"  # in case of error inside the loop
    while not ok:
        selection = input(
            "Please, enter your selection (\"q\" to exit): "
        )
        print("Selection: " + selection)
        if (selection not in options) and (selection not in {"q"}):
            print("Invalid selection")
            continue
        if selection == "q":
            exit()
        ok = True

    return selection


def possible_lines_to_replace(x):
    with open(x) as fpr:
        # https://stackoverflow.com/questions/26320175/how-to-convert-integers-in-list-to-string-in-python
        options = set(map(str, range(1, len(fpr.readlines()) + 1)))

    return options


def line_replace(x, line_n, replacement, check_last=True):
    if check_last:
        replacement = fix_last(replacement)

    with open(x, "r") as frr:
        current = frr.readlines()
        print("Line to replace was: " + current[int(line_n) - 1])
        current[int(line_n) - 1] = replacement

    with open(x, "w") as frw:
        frw.writelines(current)
        print("Line to replace is now: " + current[int(line_n) - 1])

    return x


def create_new_note(x):
    print("Creating a new '" + x + "' note...")
    write_new_note(x)
    print("Note created.")

    return x


def show_main_menu():
    print("What do you do?")
    main_options = {
        "1": "Read it",
        "2": "Overwrite it",
        "3": "Continue it",
        "4": "Replace a (single) line"
    }
    for i in main_options:
        print(i + " : " + main_options[i])
    selection = ask_for_selection(main_options.keys())

    return selection


def replace_line_in_note(x):
    lines_set = possible_lines_to_replace(x)
    print("Which line you like to replace?")
    print("Options ranges from ", min(lines_set), "to ", max(lines_set))

    n_line = ask_for_selection(lines_set)
    replacement = ask_for_content()
    line_replace(x, n_line, replacement)

    return x


def get_action_selected(selection):
    actions = {
        "1": print_note,
        "2": write_new_note,
        "3": continue_note,
        "4": replace_line_in_note
    }

    return actions[selection]


def note_taking():
    x = ask_for_filename()

    if not file_exist(x):
        create_new_note(x)
    else:
        print("File already exists.")
        selection = show_main_menu()
        act = get_action_selected(selection)
        act(x)

    return x


if __name__ == '__main__':

    # ---- Functions' checks ----
    print("\n\n=== Checks starts ===\n")
    check_res = [
        file_exist("main.py"),
        not file_exist("foo.bar"),
        file_exist(write_new_note("foo.txt", "foo")),
        check_last_empty_line(["foo\n"]),
        not check_last_empty_line(["foo"])
    ]

    with open("foo.txt", "r") as f:
        foo_content = f.readlines()
    check_res.append(foo_content[0] == "foo\n")

    continue_note("foo.txt", "bar")
    continue_note("foo.txt",
                  """baz
    tar"""
                  )

    check_res.append(
        possible_lines_to_replace("foo.txt") == {"1", "2", "3", "4"}
    )

    with open("foo.txt", "r") as f:
        foo_content = f.readlines()

    check_res.extend([
        foo_content[1] == "bar\n",
        foo_content[2] == "baz\n"
    ])

    check_res.extend([
        fix_last("foo") == "foo\n",
        fix_last("foo\n") == "foo\n"
    ])

    line_replace("foo.txt", 1, "biz")
    with open("foo.txt", "r") as f:
        foo_content = f.readlines()

    check_res.append(foo_content[0] == "biz\n")
    check_res.extend([
        get_action_selected("1") == print_note
    ])

    if all(check_res):
        print("\n=== All checks passed ===\n\n")
    else:
        wrong = [i + 1 for i, x in enumerate(check_res) if not x]
        print("\n=== !!! Check(s) not passed:", wrong, "!!! ===\n\n")
        exit()

    # ---- Execution ----
    like_to_start = input(
        "Press Enter to start the interactive simulation" +
        " (anything else will quit it)."
    )
    go = like_to_start == ""
    while go is True:
        note_taking()
        go_on = input(
            "Press Enter to continue the interactive simulation" +
            " (anything else will quit it)."
        )
        go = go_on == ""
