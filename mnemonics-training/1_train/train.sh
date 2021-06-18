
set +o posix
exec > >(tee logs/train2.log) 2>&1
python main.py \
    --method='baseline' \
    --nb_cl_fg=5 \
    --nb_cl=5 \
    --gpu='0' \
    --fusion_mode='mtl' \
    --ckpt_label='07' \
    --lucir \
    --backbone=0 \
    --epochs=80 \
    --dynamic_budget \
    --base_lr1=0.01 \
    --base_lr2=0.01