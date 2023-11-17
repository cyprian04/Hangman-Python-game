import nltk

nltk.download('words')

all_words = nltk.corpus.words.words()

file_path = 'all_words.txt'
with open(file_path, 'w') as file:
    for word in all_words:
        file.write(word + '\n')

print(f"All words saved to {file_path}")