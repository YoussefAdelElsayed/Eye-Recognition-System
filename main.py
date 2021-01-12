import G6_iris_recognition

# trainig model
G6_iris_recognition.iris_model_train('Input_database/', 'encodingModel/irisEncodings.pickle')

# test same training data
iris_name = G6_iris_recognition.iris_model_test('encodingModel/irisEncodings.pickle', 'data_temp/1r.jpg')
print(iris_name)
print("---------")

# test existing person with different image
iris_name = G6_iris_recognition.iris_model_test('encodingModel/irisEncodings.pickle', 'data_temp/3r.jpg')
print(iris_name)
print("---------")

# test strange person
iris_name = G6_iris_recognition.iris_model_test('encodingModel/irisEncodings.pickle', 'data_temp/Databa18.gif')
print(iris_name)
print("---------")
