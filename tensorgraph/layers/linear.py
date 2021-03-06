import tensorflow as tf
from template import Template


class Linear(Template):

    def __init__(self, prev_dim=None, this_dim=None, W=None, b=None):
        """
        DESCRIPTION:
            This is a fully connected layer
        PARAM:
            prev_dim(int): dimension of previous layer
            this_dim(int): dimension of this layer
            name(string): name of the layer
            W(tensor variable): Weight of 2D tensor matrix
            b(tensor variable): bias of 2D tensor matrix
            params(list): a list of params in layer that can be updated
        """

        self.prev_dim = prev_dim
        self.this_dim = this_dim

        self.W = W
        if self.W is None:
            self.W = tf.Variable(tf.random_normal([self.prev_dim, self.this_dim], stddev=0.1), name='W')

        self.b = b
        if self.b is None:
            self.b = tf.Variable(tf.random_normal([self.this_dim], stddev=0.1), name='b')

    def _train_fprop(self, state_below):
        return tf.matmul(state_below, self.W) + self.b

    def _variables(self):
        return self.W, self.b
