#information about with statments in Python
#https://www.geeksforgeeks.org/with-statement-in-python/

import tensorflow as tf
tf.compat.v1.disable_eager_execution()

node = tf.Variable(tf.zeros([2,2]))

with tf.compat.v1.Session() as sess: 
    sess.run(tf.compat.v1.global_variables_initializer())
    print("Tensor value before addition: \n", sess.run(node))
    newNode = node + tf.ones([2,2])
    node = tf.compat.v1.assign(node,newNode)
    print("Tensor value after addition: \n", sess.run(node))