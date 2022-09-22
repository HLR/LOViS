name=VLNBERT-test-PREVALENT34

flag="--vlnbert prevalent

      --submit 1
      --test_only 0

      --train validlistener
      --load /home/joslin/Recurrent-VLN-BERT/snap/VLNBERT-train-prevalent_best/state_dict/best_val_unseen

      --features places365
      --maxAction 15
      --batchSize 24
      --feedback sample
      --lr 1e-5
      --iters 300000
      --optim adamW

      --mlWeight 0.20
      --maxInput 80
      --angleFeatSize 128
      --featdropout 0.4
      --dropout 0.5
      "

mkdir -p snap/$name
CUDA_VISIBLE_DEVICES=1 python r2r_src_update/train.py $flag --name $name
