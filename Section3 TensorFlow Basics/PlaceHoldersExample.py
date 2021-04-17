import tensorflow as tf
tf.compat.v1.disable_eager_execution()

#A placeholder is similar to 'Unknown' in TS. It reqquires that we provide the value later in our code
a = tf.compat.v1.placeholder(tf.int32, shape=(3,1))
b = tf.compat.v1.placeholder(tf.int32, shape=(1,3))
c = tf.matmul(a,b)

with tf.compat.v1.Session() as sess: 
    print(sess.run(c, 
    feed_dict= {
        a:[[3],[2],[1]],
        b: [[1,2,3]]
     }))