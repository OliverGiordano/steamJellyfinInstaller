import vdf
import os

def main():
    print(getUID("/home/oliver/.local/share/Steam/userdata"))


def getUID(steamPath) -> list:
    uids = os.listdir(steamPath)
    return uids


main()
