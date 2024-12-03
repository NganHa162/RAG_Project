import pickle
with open('/mnt/disk1/HaNTN/Hydrogen_RAG/code/source_code/chunkers_final.pkl', 'rb') as file:
    documents = pickle.load(file)

print(len(documents))
