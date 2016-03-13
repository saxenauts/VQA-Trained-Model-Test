##This file is imported in the app flask module and then makes use of a function to pass images to it. 
##SO usage would be:   from predict import predict, and then pass the image folder to predict.  
import kerasvgg as kvgg
from sklearn.externals import joblib
from spacy.en import English
from keras.models import model_from_json 
import cv2, numpy as np

##Need a function to pass the image through the VGG network and obtain the matrix from it. 

    
    
    
##Need a function to convert the  question into the word vector.
#TODO:  Figure out the meaning of timesteps, read the theory behind word2vec



#TODO: Find a way to return a list  of top five elements from the list.
def load_models():
    print ("Loading English")
    nlp = English()
    n_dimensions = nlp.vocab.load_vectors('glove.840B.300d.txt.bz2')
    print (n_dimensions)
    print ("Loading encoder")
    encoder = joblib.load('../models/encoder.pkl')
    print ("Loading model")
    model = model_from_json(open('../models/lstm_1_num_hidden_units_lstm_512_num_hidden_units_mlp_1024_num_hidden_layers_mlp_3.json').read())
    print ("Loading Weights")
    model.load_weights('../models/lstm_1_num_hidden_units_lstm_512_num_hidden_units_mlp_1024_num_hidden_layers_mlp_3_epoch_070.hdf5')
    print ("Compiling Model")
    model.compile(loss = 'categorical_crossentropy', optimizer = 'rmsprop')
    print 'Loaded'

def predict(path, ques):     
    im = cv2.resize(cv2.imread(path), (224, 224))
    im = im.transpose((2,0,1))
    im = np.expand_dims(im, axis=0)

     
    
    img_model = kvgg.VGG_16('../models/vgg16_weights.h5')
    sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
    img_model.compile(optimizer=sgd, loss='categorical_crossentropy')
    img_matrix = img_model.predict(im)
    
    ##Question
    question = unicode(ques)
    timesteps = len(nlp(question))
    word_vec_dim = nlp(question)[0].vector.shape[0]
    question_tensor = np.zeros((1, timesteps, word_vec_dim))
    tokens = nlp(question)
    for i in xrange(len(tokens)):
        if i < timesteps:
            question_tensor[1, i, :] = tokens[i].vector
    
    
    concat_matrix = [ques_tensor, img_matrix]
    
    Y_predicted = model.predict_classes(concat_matrix, verbose = 2 )
    
    return encoder.inverse_transform(Y_predict)



if __name__ == '__main__':
    predict(path, ques)