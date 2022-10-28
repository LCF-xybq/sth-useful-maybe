# softlink images through multi-folders
# TODO: add other operator
# 'lr' is the same meaning of 'lq'

import os
import argparse
import os.path as osp


def link_imgs_ann(args):
    """link images from ann.txt

    Operations:
        uw_xxx_train.txt: pic_a_lr_path pic_a_gt_path
        args.save_pth (str): root path to save soft link file.
        args.type_name (str): path of lr images to save soft link file.
        args.label_name (str): path of lr images to save soft link file.
        
        soft link 'pic_a_lr_path' to args.save_pth + args.type_name + image_name.
        soft link 'pic_a_gt_path' to args.save_pth + args.label_name + image_name.
    """
    assert isinstance(args.type_name, str)
    assert isinstance(args.label_name, str)

    data_type = osp.join(args.save_pth, args.type_name)
    label = osp.join(args.save_pth, args.label_name)

    if not osp.exists(data_type):
        os.makedirs(data_type)
        print(f'mkdir {data_type} ...')
    
    if not osp.exists(label):
        os.makedirs(label)
        print(f'mkdir {label} ...')

    img_lsts = scan_ann(args.ann_file)
    for img_pairs in img_lsts:
        lq, gt = img_pairs
        img_name = osp.basename(lq)
        lq_trg_link = osp.join(data_type, img_name)
        gt_trg_link = osp.join(label, img_name)
        os.system(f'ln -s {lq} {lq_trg_link}')
        os.system(f'ln -s {gt} {gt_trg_link}')


def link_imgs_pth(args, create_fake_gt=True):
    """link images from lq_folder.
       used for datasets w/o the corresponding ground truth.

    Operations:
        uw_xxx_train.txt: pic_a_lr_path pic_a_gt_path
        create_fake_gt (bool, Optional): whether create fake gt for this dataset.
                                        for some frameworks need gt info.
    """
    imgs = os.listdir(args.lq_folder)

    if create_fake_gt:
        save_lq = osp.join(args.save_pth, 'lq')
        save_gt = osp.join(args.save_pth, 'gt_fake')
        if not osp.exists(save_lq):
            os.makedirs(save_lq)
            print(f'mkdir {save_lq} ...')
        if not osp.exists(save_gt):
            os.makedirs(save_gt)
            print(f'mkdir {save_gt} ...')
    elif not osp.exists(args.save_pth):
        os.makedirs(args.save_pth)
        print(f'mkdir {args.save_pth} ...')

    for img in imgs:
        src = osp.join(args.lq_folder, img)
        if not create_fake_gt:  
            trg = osp.join(args.save_pth, img)
            os.system(f'ln -s {src} {trg}')
        else:
            trg_lq = osp.join(save_lq, img)
            trg_gt = osp.join(save_gt, img)
            os.system(f'ln -s {src} {trg_lq}')
            os.system(f'ln -s {src} {trg_gt}')

def scan_ann(pth):
    """read paths of lr and gt."""
    img_lsts = []
    with open(pth, 'r') as f: 
        img_pth = f.readlines()
        for line in img_pth:
            lq, gt = line.strip().split(' ')
            img_lsts.append((lq, gt))

    return img_lsts


def parse_args():
    parser = argparse.ArgumentParser(
        description='Prepare dataset',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '--fn', 
        default=1,
        type=int,
        help='1:ann 2:folder')
    parser.add_argument('--ann_file', help='ann file')
    parser.add_argument('--lq_folder', help='data without gt path')
    parser.add_argument(
        '--save_pth', help='path to store data')
    parser.add_argument(
        '--type_name',
        nargs='?',
        default='lq',
        type=str,
        help='folder name for data')
    parser.add_argument(
        '--label_name',
        nargs='?',
        default='gt',
        type=str,
        help='folder name for reference')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    """
        soft link images from ann.txt:
            python xxx.py --fn 1 --ann_file path_to_ann --save_pth path_to_train/test/val_dataset_name 

        soft link images from lq folder:
            python xxx.py --fn 2 --lq_folder path_to_folder --save_pth path_to_train/test/val_dataset_name
    """
    args = parse_args()
    if args.fn == 1:
        link_imgs_ann(args)
    elif args.fn == 2:
        link_imgs_pth(args)
