import tensorflow as tf
tf.compat.v1.disable_eager_execution()
#creating nodes
node1 = tf.constant(3,dtype=tf.int32)
node2 = tf.constant(3,dtype=tf.int32)
node3 = tf.add(node1,node2)

sess = tf.compat.v1.Session()
results = sess.run(node3)
print("")
print("Sum of node1 and node2 is", results)
print("Hello Tensor Flow!")
print("")
sess.close()