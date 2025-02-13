# -------------------------------------------------------------------------
# AUTHOR: Arze Lu
# FILENAME: similarity.py
# SPECIFICATION: Find similarities of documents
# FOR: CS 5990 (Advanced Data Mining) - Assignment #1
# TIME SPENT: how long it took you to complete the assignment
# -----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy,
#pandas, or other sklearn modules.
#You have to work here only with standard dictionaries, lists, and arrays

# Importing some Python libraries
import csv
from sklearn.metrics.pairwise import cosine_similarity

documents = []

#reading the documents in a csv file
with open('cleaned_documents.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            documents.append(row)
            #print(row)

#Building the document-term matrix by using binary encoding.
#You must identify each distinct word in the collection without applying any transformations, using
# the spaces as your character delimiter.
#--> add your Python code here

total_docs = len(documents)

for index in range(0, total_docs):
    documents[index] = documents[index][1].split(" ")

docTermMatrix = []

# Compare the pairwise cosine similarities and store the highest one
# Use cosine_similarity([X], [Y]) to calculate the similarities between 2 vectors
# --> Add your Python code here

# initializing the matrix
for i in range(0, total_docs):
    row = [1] * total_docs
    docTermMatrix.append(row)

for i in range(0, total_docs):
    for j in range(i + 1, total_docs):
        words = list(set(documents[i]).union(set(documents[j])))
        vector_1 = []
        vector_2 = []

        for word in words:
            if word in documents[i]:
                vector_1.append(1)
            else:
                vector_1.append(0)

        for word in words:
            if word in documents[j]:
                vector_2.append(1)
            else:
                vector_2.append(0)

        similarity = cosine_similarity([vector_1, vector_2])

        docTermMatrix[i][j] = similarity[0][1]
        docTermMatrix[j][i] = similarity[0][1]

# Print the highest cosine similarity following the information below
# The most similar documents are document 10 and document 100 with cosine similarity = x
# --> Add your Python code here
highest_similarity = 0
doc_pairs = []

for i in range(0, 10):
    for j in range(i + 1, 10):
        if docTermMatrix[i][j] > highest_similarity:
            highest_similarity = docTermMatrix[i][j]
            doc_pairs = [[i, j]]
        elif docTermMatrix[i][j] == highest_similarity:
            doc_pairs.append([i, j])

print("The highest similarity score is: " + str(highest_similarity))
print("The document pair(s) that share this score: ")
for pair in doc_pairs:
    print("doc#" + str(pair[0]) + " & doc#" + str(pair[1]))