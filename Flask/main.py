import time

def speed_typing_test():
    text = "The quick brown fox jumps over the lazy dog."
    print("Type the following text:")
    print(text)
    print("Press Enter when you're ready.")
    input()

    start_time = time.time()

    typed_text = input("Start typing: ")

    end_time = time.time()

    elapsed_time = end_time - start_time

    words = text.split()
    num_words = len(words)

    typed_words = typed_text.split()
    num_typed_words = len(typed_words)

    accuracy = calculate_accuracy(words, typed_words)
    wpm = calculate_wpm(num_typed_words, elapsed_time)

    print("Time elapsed: {:.2f} seconds".format(elapsed_time))
    print("Accuracy: {:.2f}%".format(accuracy))
    print("Words per minute: {:.2f} WPM".format(wpm))

def calculate_accuracy(words, typed_words):
    correct_words = 0

    for i in range(len(words)):
        if i < len(typed_words) and words[i] == typed_words[i]:
            correct_words += 1

    accuracy = (correct_words / len(words)) * 100
    return accuracy

def calculate_wpm(num_typed_words, elapsed_time):
    minutes = elapsed_time / 60
    wpm = num_typed_words / minutes
    return wpm

speed_typing_test()