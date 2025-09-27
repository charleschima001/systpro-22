import os
import sys

def make_links(from_dir, to_dir):

    try:
        os.mkdir(to_dir)
    except FileExistsError:
        pass
    except:
        print(f"Directory error: {to_dir}")
        return


    try:
        files = os.listdir(from_dir)
    except:
        print(f"Read error: {from_dir}")
        return


    for fname in files:
        source = os.path.join(from_dir, fname)
        target = os.path.join(to_dir, fname)

        if os.path.isfile(source):
            try:
                os.link(source, target)
                print(f"Created link: {fname}")
            except OSError as err:
                print(f"Failed: {fname} - {err}")



make_links("./папка1", "./папка2")