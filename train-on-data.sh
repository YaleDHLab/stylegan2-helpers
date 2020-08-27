. ./config.sh

# --data-dir="/home/dhlab/EveryPixel/2020 Data/sg2/" \


nohup python stylegan2/run_training.py \
    --num-gpus=1 \
    --data-dir="/home/dhlab/sg2/" \
    --config=config-f \
    --dataset=datasets \
    --resume-pkl="results/00016-stylegan2-datasets-1gpu-config-f/network-snapshot-001065.pkl" \
    --mirror-augment=true &