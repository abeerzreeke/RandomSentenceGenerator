import random

def get_words_from_file():
    with open('wordStore.txt','r') as f:
        words = [word.replace('\n','') for word in  f.readlines()]
    return words

def get_random_sentence(length):
    words = get_words_from_file()
    sentence = random.choices(words, k=length)
    return ', '.join([word.lower() for word in sentence])

def ask_user():
    valid_flag = False
    while not valid_flag:
        long_sentence = input('how long the sentence you want to be (between 2 and 20)?  ')
        if not long_sentence.isdigit():
            print('input needs to be a digit')
            valid_flag = False 
            continue  
        long_sentence = int(long_sentence)
        if long_sentence < 2 or long_sentence > 20:
            print('long of the input need to be between 2 and 20')
            valid_flag = False
        else:
            valid_flag = True

    return get_random_sentence(long_sentence)


def main():
    print('...HRandom Sentence Generator...')
    return ask_user()

if __name__ == '__main__':
    print(main())