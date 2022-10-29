import cs50
import sys
import csv

def main():
    #コマンドライン引数の確認
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    #csvファイルの読み込み
    with open(sys.argv[1], "r") as f:
        persons = list(csv.DictReader(f))

    #print(f"{persons}")

    subsequences = {}
    for subsequence in persons[0].keys():
        if subsequence != "name":
            subsequences[subsequence] = None

    #txtファイルの読み込み
    sequence = open(sys.argv[2], "r")
    sequence = sequence.read()

    #最大反復回数の導出
    for subsequence in subsequences:
        subsequences[subsequence] = longest_match(subsequence, sequence)
        #print(f"{subsequences[subsequence]}")

    #txtが誰に該当するかの特定
    #print(f"{subsequences.keys()}")
    identify = 0
    for person in persons:
        for subsequence in subsequences.keys():
            identify = 0
            #print(f"{subsequence}")
            #print(f"{person}")
            #print(f"{type(subsequences[subsequence])}, {type(person[subsequence])}")
            if subsequences[subsequence] == int(person[subsequence]):
                #print("!!!!")
                continue
            else:
                identify = 1
                break
        if identify != 1:
            print(f"{person['name']}")
            break

    if identify == 1:
        print("No match")

#DNA配列とSTRを受け取り, 最大反復回数を返す
def longest_match(subsequence, sequence):
    count = 1
    while subsequence*count in sequence:
        count += 1
    return count - 1

main()
