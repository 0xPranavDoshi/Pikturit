import sys
import subprocess

def main():
    if len(sys.argv) == 2:
        image_file = sys.argv[1]
        print(f"Image file is {image_file}")    

        # Do stuff    

        
    else:
        print('Usage pikturit.py <image_file_path>')

if __name__ == "__main__":
    main()