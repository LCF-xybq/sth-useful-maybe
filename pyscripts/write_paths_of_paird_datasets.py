"""writing paired paths, namly data & ground truth."""
# random algorithm is based on np.random.choice().

import os
import argparse
import numpy as np


def _check_difference(a, b, c=None):
    """Make sure all sets are non-overlapping.

    Args:
        a (set): set : 'a'.
        b (set): set : 'b'.
        c (set, optional): set : 'c'.
            Defaults to None.
    """
    seta = set(a)
    setb = set(b)
    print(seta.intersection(setb))
    print(setb.intersection(seta))

    if c is not None:
        setc = set(c)
        print(seta.intersection(setc))
        print(setb.intersection(setc))
        print(setc.intersection(seta))
        print(setc.intersection(setb))
        

def choice_uw_syn(pth, train_nums, val_nums, test_nums):
    """randomly choice paired pictures from synthesized underwater images.

    Args:
        pth (path): root path for dataset.
        train_nums (int): numbers of training samples.
        val_nums (int): numbers of validating samples.
        test_nums (int): numbers of testing samples.
    """
    uw_types = ['type1_data/underwater_type_1', 'type3_data/underwater_type_3', 
                'type5_data/underwater_type_5', 'type7_data/underwater_type_7',
                'type9_data/underwater_type_9', 'typeI_data/underwater_type_I',
                'typeIA_data/underwater_type_IA', 'typeIB_data/underwater_type_IB',
                'typeII_data/underwater_type_II', 'typeIII_data/underwater_type_III']

    gt_types = ['type1_data/gt_type_1', 'type3_data/gt_type_3', 
                'type5_data/gt_type_5', 'type7_data/gt_type_7',
                'type9_data/gt_type_9', 'typeI_data/gt_type_I',
                'typeIA_data/gt_type_IA', 'typeIB_data/gt_type_IB',
                'typeII_data/gt_type_II', 'typeIII_data/gt_type_III']

    for i in range(10):
        pic_pth = os.path.join(pth, uw_types[i])
        img_lsts = os.listdir(pic_pth)   
        selected = np.random.choice(img_lsts, size=train_nums, replace=False)
        
        # ensure same names
        gt_pth = os.path.join(pth, gt_types[i])
        gt_lsts = os.listdir(gt_pth)
        assert img_lsts[i] == gt_lsts[i], f'{img_lsts[i]} != {gt_lsts[i]}'

        with open('uw_syn_train.txt', 'a') as f:
            for imgs in selected:
                src = os.path.join(pic_pth, imgs)
                gt = os.path.join(gt_pth, imgs)
                f.write(f'{src} {gt}\n')

        # val and test
        all_set = set(img_lsts)
        selected_set = set(selected)
        val_test = all_set.difference(selected_set)
        selected_val = np.random.choice(list(val_test), size=val_nums, replace=False)
        
        with open('uw_syn_val.txt', 'a') as f:
            for imgs in selected_val:
                src = os.path.join(pic_pth, imgs)
                gt = os.path.join(gt_pth, imgs)
                f.write(f'{src} {gt}\n')

        remaining_test = val_test.difference(set(selected_val))
        selected_test = np.random.choice(list(remaining_test), size=test_nums, replace=False)

        with open('uw_syn_test.txt', 'a') as f:
            for imgs in selected_test:
                src = os.path.join(pic_pth, imgs)
                gt = os.path.join(gt_pth, imgs)
                f.write(f'{src} {gt}\n')

        _check_difference(selected, selected_val, selected_test)


def choice_uieb(pth, train_nums=800, test_nums=90):
    """randomly choice paired pictures from real-world underwater images.

    Args:
        pth (path): root path for dataset.
        train_nums (int, optional): numbers of training samples.
                                    Defaults to 800.
        test_nums (int, optional): numbers of testing samples.
                                    Defaults to 90.
    """
    uw_types = 'raw-890'
    gt_types = 'reference-890'
    pic_pth = os.path.join(pth, uw_types)
    img_lsts = os.listdir(pic_pth)
    selected = np.random.choice(img_lsts, size=train_nums, replace=False)
    
    # ensure same names
    gt_pth = os.path.join(pth, gt_types)
    gt_lsts = os.listdir(gt_pth)
    
    assert len(img_lsts) == len(gt_lsts), f'numbers of lr_pictures {len(img_lsts)} ' \
                                f'are not equal to gt_pictures {len(gt_lsts)}.'
    for lr, gt in zip(img_lsts, gt_lsts):
        lr_name = os.path.basename(lr)
        gt_name = os.path.basename(gt)
        assert lr_name == gt_name, f'lr_name - {lr_name} != gt_name - {gt_name}.'

    with open('uw_uieb_train.txt', 'a') as f:
        for imgs in selected:
            src = os.path.join(pic_pth, imgs)
            gt = os.path.join(gt_pth, imgs)
            f.write(f'{src} {gt}\n')

    # val and test
    all_set = set(img_lsts)
    selected_set = set(selected)
    val_test = all_set.difference(selected_set)
    selected_test = np.random.choice(list(val_test), size=test_nums, replace=False)
    
    with open('uw_uieb_test.txt', 'a') as f:
        for imgs in selected_test:
            src = os.path.join(pic_pth, imgs)
            gt = os.path.join(gt_pth, imgs)
            f.write(f'{src} {gt}\n')

    _check_difference(selected, selected_test)


def parse_args():
    parser = argparse.ArgumentParser(
        description='write paths of paired datasets.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('syn_folder', help='path to synthesize underwater images.')
    parser.add_argument('uieb_folder', help='path to dataset - UIEB.')
    args = parser.parse_args()
    return args



if __name__ == '__main__':
    # append mode, only run one time
    # usage:
    # python xxx.py path_to_syn_folder path_to_uieb_folder
    
    args = parse_args()
    choice_uw_syn(pth=args.syn_folder, train_nums=125, val_nums=30, test_nums=100)
    choice_uieb(pth=args.uieb_folder, train_nums=800, test_nums=90)
