
set +o posix
exec > >(tee logs/train.log) 2>&1
python main.py \
    --method='baseline' \
    --nb_cl=5 \
    --gpu='0' \
    --fusion_mode='mtl' \
    --ckpt_label='03' \
    --lucir