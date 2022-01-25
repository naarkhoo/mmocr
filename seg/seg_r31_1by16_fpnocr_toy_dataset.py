base_ = [
    '../../_base_/default_runtime.py',
    '../../_base_/recog_datasets/seg_toy_data.py',
    '../../_base_/recog_models/seg.py',
    '../../_base_/recog_pipelines/seg_pipeline.py'
]
train_list = '_train_list_98eb2e'
test_list = '_test_list_eca972'
train_pipeline = '_train_pipeline_1c44f1'
test_pipeline = '_test_pipeline_f058f8'
optimizer = dict(type='Adam', lr=0.0001)
optimizer_config = dict(grad_clip=None)
lr_config = dict(policy='step', step=[3, 4])
total_epochs = 5
data = dict(
    samples_per_gpu=8,
    workers_per_gpu=1,
    train=dict(
        type='UniformConcatDataset',
        datasets='_train_list_98eb2e',
        pipeline='_train_pipeline_1c44f1'),
    val=dict(
        type='UniformConcatDataset',
        datasets='_test_list_eca972',
        pipeline='_test_pipeline_f058f8'),
    test=dict(
        type='UniformConcatDataset',
        datasets='_test_list_eca972',
        pipeline='_test_pipeline_f058f8'))
evaluation = dict(interval=1, metric='acc')
find_unused_parameters = True
work_dir = 'seg'
gpu_ids = range(0, 1)
