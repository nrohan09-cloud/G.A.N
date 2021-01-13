import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

generator= keras.models.load_model('Generator')

noise = tf.random.normal([1, 100])
generated_image = generator(noise, training=False)
plt.imshow(generated_image[0, :, :, 0], cmap='gray')
plt.show()
