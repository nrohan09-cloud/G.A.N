# G.A.N
The code used for training and generating with G.A.N, a Generative Adversarial Network that generates MNIST like instances of the letters G, A and N.

![](download.gif)

# Files

`train_data_G.A.N.npy` is the dataset used for training,

the Generator folder has the trained GAN which can be imported in Keras using `generator = keras.models.load_model('Generator')`

# Credits 
[Tensorflow tutorial on DC-GAN](https://www.tensorflow.org/tutorials/generative/dcgan)
