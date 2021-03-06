import G6_iris_recognition

def trainModel():
    G6_iris_recognition.iris_model_train('Input_database/', 'encodingModel/irisEncodings.pickle')

def testIris(path):
    iris_name = G6_iris_recognition.iris_model_test('encodingModel/irisEncodings.pickle', path)
    return iris_name
