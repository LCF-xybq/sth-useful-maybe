# pyscripts
scripts implemented by python.

1. write_paths_of_paird_datasets.py :
    first, randomly select train/val/test samples from UIEB and Synthetic underwater images.
    then, write paired paths of images to txt files.
    like: path_pic_a_lr path_pic_a_gt

2. prepare_data.py :
    soft link images to 'data' folder, which need information of paths provided from 'write_paths_of_paird_datasets.py'.
    