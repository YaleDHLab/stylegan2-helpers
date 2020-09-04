set -e 

# Load config variables
. ./config.sh

LATEST_SNAPSHOT=$(python latest-snapshot.py)

echo "Using snapshot: $LATEST_SNAPSHOT"
echo "Using data dir: $DATA_DIR"

nohup python stylegan2/run_training.py \
    --num-gpus=1 \
    --data-dir="$DATA_DIR" \
    --config=config-f \
    --dataset=datasets \
    --resume-pkl="$LATEST_SNAPSHOT" \
    --mirror-augment=true &