from iterator import Iterator
import copy_dataset
import copy_dataset_random


copy_dataset.make_copy_dataset()

copy_dataset_random.make_copy_dataset_random()

GoodIter = Iterator("bad")

# print(iter(GoodIter).elem)
for i, val in enumerate(GoodIter):
    print(i, ": ", val)