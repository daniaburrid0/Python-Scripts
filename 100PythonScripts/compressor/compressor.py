import sys
import os
import py7zr

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py file1 file2 ...")
        sys.exit(1)

    output_filename = "compressed.7z"
    with py7zr.SevenZipFile(output_filename, mode='w') as archive:
        for filepath in sys.argv[1:]:
            if os.path.isfile(filepath):
                archive.write(filepath, os.path.basename(filepath))
            else:
                print(f"Skipping {filepath}: not a valid file")

    print(f"Files compressed into {output_filename}")

if __name__ == "__main__":
    main()
