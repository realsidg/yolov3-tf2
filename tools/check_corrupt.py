import tensorflow.compat.v1 as tf
import glob
total_images = 0
train_files = sorted(glob.glob('./data/grip_train.tfrecord'))
for f_i, file in enumerate(train_files): 
    print(f_i) 
    total_images += sum([1 for _ in tf.python_io.tf_record_iterator(file)])
