# G.A.N
The code used for training and generating with G.A.N, a Generative Adversarial Network that generates EMNIST like instances of the letters G, A and N. Tested on Tensorflow 2.4.0

![](dcgan.gif)

# Files

`Generate letter.py` can be run to generate a random letter. Requires matplotlib.

`G_A_N.ipynb` is the jupyter notebook used for training the model.

`train_data.csv` is the dataset used for training,

the `Generator` folder has the trained GAN which can be imported in Keras using 
`generator = keras.models.load_model('Generator')`

# Credits 
[Tensorflow tutorial on DC-GAN](https://www.tensorflow.org/tutorials/generative/dcgan)

Model was trained on Google Colab provided GPU.
