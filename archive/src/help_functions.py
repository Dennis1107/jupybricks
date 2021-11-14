import os


def check_for_ending(filename: str, ending: str):
    if not filename.endswith(ending):
        raise ValueError(f"{filename} not valid. Should be a file with ending {ending}")
    return


def remove_temp_file(filename: str = "temp_file348234283o23478234ip.py"):
    os.remove(filename)
    return
