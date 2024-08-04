import tensorflow as tf

def change_tensor():
    try:
        changeable_tensor = tf.Variable([10, 7])
        changeable_tensor[0].assign(7)
        print(changeable_tensor)
    except Exception as e:
        print(f"Error in change_tensor: {e}")

def random_tensors():
    try:
        random_1 = tf.random.Generator.from_seed(42)
        random_1 = random_1.normal(shape=(3, 2))
        random_2 = tf.random.Generator.from_seed(42)
        random_2 = random_2.normal(shape=(3, 2))
        print(random_1, random_2, random_1 == random_2)
    except Exception as e:
        print(f"Error in random_tensors: {e}")

def shuffle_tensor():
    try:
        not_shuffled = tf.constant([[10, 7],
                                    [3, 4],
                                    [2, 5]])
        tf.random.set_seed(42)
        shuffled = tf.random.shuffle(not_shuffled, seed=42)
        print(shuffled)
    except Exception as e:
        print(f"Error in shuffle_tensor: {e}")

def ones_zeros_tensors():
    try:
        ones = tf.ones(shape=(3, 2))
        zeros = tf.zeros(shape=(3, 2))
        print(ones)
        print(zeros)
    except Exception as e:
        print(f"Error in ones_zeros_tensors: {e}")

def tensor_properties():
    try:
        rank_4_tensor = tf.zeros([2, 3, 4, 5])
        print("Datatype of every element:", rank_4_tensor.dtype)
        print("Number of dimensions (rank):", rank_4_tensor.ndim)
        print("Shape of tensor:", rank_4_tensor.shape)
        print("Elements along axis 0 of tensor:", rank_4_tensor.shape[0])
        print("Elements along last axis of tensor:", rank_4_tensor.shape[-1])
        print("Total number of elements (2*3*4*5):", tf.size(rank_4_tensor).numpy())
    except Exception as e:
        print(f"Error in tensor_properties: {e}")
