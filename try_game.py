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
        two_words = input("Enter two sounds>> ")
        split_words = two_words.split(' ')

        if split_words[0] and split_words[1] in list(sounds.keys()):
            print(f"{split_words[0]} is a {sounds.get(split_words[0])}", end=" ")
            print(f"and {split_words[1]} is a {sounds.get(split_words[1])}")
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
