from easydict import EasyDict as edict

# make training faster
# our RAM is 256G
# mount -t tmpfs -o size=140G  tmpfs /train_tmp

config = edict()

# Margin Base Softmax
config.margin_list = (1.0, 0.5, 0.0)
config.network = "r50"
config.resume = False
config.save_all_states = False
config.output = "rfw_arcface_r50"

config.embedding_size = 512

# Partial FC
config.sample_rate = 1
config.interclass_filtering_threshold = 0

config.fp16 = False
config.batch_size = 32

# For SGD 
config.optimizer = "sgd"
config.lr = 0.1
config.momentum = 0.9
config.weight_decay = 5e-4

# For AdamW
# config.optimizer = "adamw"
# config.lr = 0.001
# config.weight_decay = 0.1

config.verbose = 2000
config.frequent = 10

# For Large Sacle Dataset, such as WebFace42M
config.dali = False 
config.dali_aug = False

# Gradient ACC
config.gradient_acc = 1

# setup seed
config.seed = 2048

# dataload numworkers
config.num_workers = 8

# WandB Logger
config.wandb_key = "684aaada212c9a01d6b89c200754c635c40778b5"
config.suffix_run_name = None
config.using_wandb = True
config.wandb_entity = "entity"
config.wandb_project = "project"
config.wandb_log_all = True
config.save_artifacts = False
config.wandb_resume = False # resume wandb run: Only if the you wand t resume the last run that it was interrupted



config.rec = "/home/atzori/Desktop/RFW"
config.num_classes = 11429
config.num_image = 36064
config.warmup_epoch = 0
config.val_targets = ['lfw', 'cfp_fp', "agedb_30"]
config.num_epoch = 50