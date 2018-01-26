import tensorflow as tf
import numpy as np 

inputs = [[0,0],[0,1],[1,0],[1,1]]
output = [[0],[0],[0],[1]]

#x_ = tf.placeholder("float", [None,2])
#y_ = tf.placeholder("float", [None,1])

bias  = tf.Variable(tf.zeros([1])
theta = tf.Variable(tf.random_normal([2,1]))

node_out = tf.tanh(tf.add(tf.matmul(inputs,theta),bias)
error = tf.sub(output,node_out)
mse = tf.reduce_mean(tf.square(error))

train = tf.train.GradientDescentOptimizer(0.01).minimize(mse)

sess = tf.Session()
init = tf.initialize_all_variables()
sess.run(init)

err, target = 1, 0.01
epoch, max_epoch = 0, 5000

while err > target and epoch < max_epoch:
    epoch += 1
    err, _ = sess.run([mse, train])

print('epoch:', epoch, 'mse', err)
