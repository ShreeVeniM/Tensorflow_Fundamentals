import tensorflow as tf
import numpy as np

def numpy_to_tensor():
    try:
        numpy_A = np.arange(1, 25, dtype=np.int32)
        A = tf.constant(numpy_A, shape=[2, 4, 3])
        print(numpy_A, A)
    except Exception as e:
        print(f"Error in numpy_to_tensor: {e}")

def math_operations():
    try:
        tensor = tf.constant([[10, 7], [3, 4]])
        tensor_added = tensor + 10
        tensor_multiplied = tensor * 10
        tensor_subtracted = tensor - 10
        tensor_matmul = tf.matmul(tensor, tensor)
        print(tensor_added)
        print(tensor_multiplied)
        print(tensor_subtracted)
        print(tensor_matmul)
    except Exception as e:
        print(f"Error in math_operations: {e}")

def matrix_operations():
    try:
        X = tf.constant([[1, 2],
                         [3, 4],
                         [5, 6]])
        Y = tf.constant([[7, 8],
                         [9, 10],
                         [11, 12]])
        Y_reshaped = tf.reshape(Y, shape=(2, 3))
        matmul_result = tf.matmul(X, Y_reshaped)
        print(matmul_result)
    except Exception as e:
        print(f"Error in matrix_operations: {e}")

def tensor_casting():
    try:
        B = tf.constant([1.7, 7.4])
        C = tf.constant([1, 7])
        B = tf.cast(B, dtype=tf.float16)
        C = tf.cast(C, dtype=tf.float32)
        print(B)
        print(C)
    except Exception as e:
        print(f"Error in tensor_casting: {e}")
