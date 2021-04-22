import numpy as np
import tensorflow as tf
tf.compat.v1.disable_eager_execution()

#define variables
X_1 = tf.compat.v1.placeholder(tf.float32, name="X_1")
X_2 = tf.compat.v1.placeholder(tf.float32, name="X_2")

#define computation
multiply = tf.multiply(X_1, X_2, name="multiply")

with tf.compat.v1.Session() as sess: 
    result = sess.run(multiply, feed_dict = {X_1: [1,2,3], X_2: [4,5,6]})
    print(result)




