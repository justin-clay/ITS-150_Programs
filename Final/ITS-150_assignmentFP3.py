import pickle




def getDictionary(fileName):
    infile = open(fileName, 'rb')
    degrees = pickle.load(infile)
    infile.close()
    return degrees



d = getDictionary()