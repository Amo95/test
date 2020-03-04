from textwrap import dedent


def _string():
    """
    code by DummyCod3r_
    """


sounds = {
    "bark": "dog",
    "roar": "lion",
    "moo": "cow",
    "hiss": "snake"
    }


def main():
    try:
        two_words = input("Enter two sounds>> ").split(" ")

        if two_words[0] and two_words[1] in list(sounds.keys()):
            print(f"{two_words[0]} is a {sounds.get(two_words[0])}", end=" ")
            print(f"and {two_words[1]} is a {sounds.get(two_words[1])}")
            _string.__doc__

        else:
            print(dedent("""
                ███╗   ██╗ ██████╗     ███████╗ ██████╗ ██╗   ██╗███╗   ██╗██████╗ ███████╗
                ████╗  ██║██╔═══██╗    ██╔════╝██╔═══██╗██║   ██║████╗  ██║██╔══██╗██╔════╝
                ██╔██╗ ██║██║   ██║    ███████╗██║   ██║██║   ██║██╔██╗ ██║██║  ██║███████╗
                ██║╚██╗██║██║   ██║    ╚════██║██║   ██║██║   ██║██║╚██╗██║██║  ██║╚════██║
                ██║ ╚████║╚██████╔╝    ███████║╚██████╔╝╚██████╔╝██║ ╚████║██████╔╝███████║
                ╚═╝  ╚═══╝ ╚═════╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═════╝ ╚══════╝
                \n""" + _string.__doc__))

    except IndexError:
        print("Enter two sounds!!")
        main()

    except EOFError:
        print(f"\n\nThank you for using the script!! {_string.__doc__}\n\n")

    except KeyboardInterrupt:
        print(f"\n\nThank you for using the script!! {_string.__doc__}\n\n")


if __name__ == '__main__':
    main()

