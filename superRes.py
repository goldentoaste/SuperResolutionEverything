



import cv2
import os, sys, subprocess, time

'''
first associate .py with python
add waifu2x.py to path
add this to waifu2x.py os.chdir(os.path.dirname(os.path.abspath(__file__)))

'''
remove_original = False


def traverseDirectory(path):
    print(f"now processing directory: {path}")
    
    files = os.listdir(path)
    dirs = filter(lambda dir: os.path.isdir(os.path.join(path, dir)), files)
    files = filter(lambda file: os.path.isfile(os.path.join(path, file)), files)
    
    
    for file in files:
        if file[-4:] != ".jpg" and file[-4:] != ".png":
            continue
        print(f"processing file {file}")
        start = time.time()
        outputcode = subprocess.run(f"waifu2x.py --method noise_scale --noise_level 2 --input {os.path.join(path, file)} --output {path} --arch VGG7 --gpu 0",
                                    shell=True,
                                    capture_output=True
                                    )
       
        ((
            ((print(f"removing {file}"), os.remove(os.path.join(path, file)))) if remove_original else None, print(f"done. Took {time.time() - start} s")
        ),
        ) if outputcode.returncode == 0 else print("an error has occured.")
    
    for dir in dirs:
        traverseDirectory(os.path.join(path, dir))
    


def main():
    global remove_original
    path = input("entering root directory for conversion: ")
    remove_original = True if input("remove original? (y/n)" ) == "y" else False

    
    traverseDirectory(path)
    



if __name__ == "__main__":
    main()