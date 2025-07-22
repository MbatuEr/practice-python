from tries import Trie

if __name__ == "__main__":
    obj = Trie()
    obj.insert("top")
    obj.insert("bye")
    print("Is the prefix 'to' exist? ", obj.has_prefix("to"))
    print("Is 'to' a word? ", obj.search("to"))
    obj.insert("to")
    print("Is 'to' a word? ", obj.search("to"))
    print("-" * 60)

    # Finding words in a matrix
    input_board = [['b', 'y', 's'] , ['r', 't', 'e'] , ['a', 'i', 'n']]
    words = ["byte", "bytes", "rat", "rain", "trait", "train"]
    print("All words in the board: " ,obj.find_all_words_on_a_board(input_board, words))
    print("-" * 60)