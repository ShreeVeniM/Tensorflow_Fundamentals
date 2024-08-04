import tensorflow as tf
import logging
from src.basic_operations import create_scalars, create_vectors, create_matrices, create_tensors
from src.tensor_operations import change_tensor, random_tensors, shuffle_tensor, ones_zeros_tensors, tensor_properties
from src.utils import numpy_to_tensor, math_operations, matrix_operations, tensor_casting

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info('Starting main function')
    try:
        print(f"TensorFlow version: {tf.__version__}")
        
        create_scalars()
        create_vectors()
        create_matrices()
        create_tensors()
        
        change_tensor()
        random_tensors()
        shuffle_tensor()
        ones_zeros_tensors()
        tensor_properties()
        
        numpy_to_tensor()
        math_operations()
        matrix_operations()
        tensor_casting()
        
    except Exception as e:
        logging.error(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
