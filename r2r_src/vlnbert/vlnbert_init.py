# Recurrent VLN-BERT, 2020, by Yicong.Hong@anu.edu.au
import sys
sys.path.append("/VL/space/zhan1624/Recurrent-VLN-BERT/")

from pytorch_transformers import (BertConfig, BertTokenizer)

def get_tokenizer(args):
    tokenizer_class = BertTokenizer
    tokenizer = tokenizer_class.from_pretrained('bert-base-uncased')
    return tokenizer

def get_vlnbert_models(args, config=None):
    config_class = BertConfig
    from vlnbert.vlnbert_PREVALENT import VLNBert
    model_class = VLNBert
    model_name_or_path = "/home/hlr/shared/data/joslin/pretrain_model/checkpoint-21780"
    vis_config = config_class.from_pretrained('bert-base-uncased')
    vis_config.img_feature_dim = 2176
    vis_config.img_visn_dim = 2048 
    vis_config.img_pos_dim = 128
    vis_config.img_feature_type = ""
    vis_config.vl_layers = 4
    vis_config.la_layers = 9

    visual_model = model_class.from_pretrained(model_name_or_path, config=vis_config)

    return visual_model
  