import tensorflow as tf

def create_scalars():
    try:
        scalar = tf.constant(7)
        print(scalar)
        print(scalar.ndim)
    except Exception as e:
        print(f"Error in create_scalars: {e}")

def create_vectors():
    try:
        vector = tf.constant([10, 10])
        print(vector)
        print(vector.ndim)
    except Exception as e:
        print(f"Error in create_vectors: {e}")

def create_matrices():
    try:
        matrix = tf.constant([[10, 7],
                              [7, 10]])
        print(matrix)
        print(matrix.ndim)
        
        another_matrix = tf.constant([[10., 7.],
                                      [3., 2.],
                                      [8., 9.]], dtype=tf.float16)
        print(another_matrix)
        print(another_matrix.ndim)
    except Exception as e:
        print(f"Error in create_matrices: {e}")

def create_tensors():
    try:
        tensor = tf.constant([[[1, 2, 3],
                               [4, 5, 6]],
                              [[7, 8, 9],
                               [10, 11, 12]],
                              [[13, 14, 15],
                               [16, 17, 18]]])
        print(tensor)
        print(tensor.ndim)
    except Exception as e:
        print(f"Error in create_tensors: {e}")
