def count_words():
    fname = input("Enter file name or full path (with .txt extension): ")

    fname = fname.strip().strip('"').strip("'")

    try:
        f = open(fname, "r")
    except FileNotFoundError:
        print("\nError: File not found.")
        print("Please check:")
        print("  1. The file name/extension is correct (e.g. sample.txt)")
        print("  2. The file is in the same folder as this script, OR")
        print("  3. You have typed the correct full path")
        return
    except Exception as e:
        print("\nSomething went wrong while opening the file:", e)
        return

    total_lines = 0
    total_words = 0
    total_chars = 0

    for line in f:
        total_lines += 1
        total_words += len(line.split())
        total_chars += len(line)

    f.close()

    print("\n----- File Statistics -----")
    print("File           :", fname)
    print("Total Lines    :", total_lines)
    print("Total Words    :", total_words)
    print("Total Characters:", total_chars)

count_words()