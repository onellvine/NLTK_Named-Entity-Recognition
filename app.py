from docx import Document
import nltk

# additional requirements
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


document = Document("document.docx")

essay = []

for p in document.paragraphs:
    essay.append(p.text.lstrip("\t"))
    essay.append("\n")

content = ''.join(essay)

print(content)

# NLTK's Named Entity Recognition Tool
# tokenize the content to sentences
sentences = nltk.sent_tokenize(content)
trees = []
for sentence in sentences:
    # 1) Word Tokenize a Sentence
    tokens = nltk.word_tokenize(sentence)

    # 2) POS tag the tokens
    tagged = nltk.pos_tag(tokens)

    # 3) print(nltk.ne_chunk(tagged))
    chunks_tree = nltk.ne_chunk(tagged)
    trees.append(chunks_tree)


# PERSON and LOCATION Entities
chunks = []
for chunks_tree in trees:
    for n in chunks_tree:
        if isinstance(n, nltk.tree.Tree):
            if n.label() == 'PERSON' or n.label() == 'LOCATION':
                chunks.append(n)

print("\n\nPerson and Location Entities\n")
print(chunks)