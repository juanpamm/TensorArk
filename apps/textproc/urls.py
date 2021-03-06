from django.urls import path
from apps.textproc.views import upload_text_nn_template, load_text_set, build_textproc_nn_template, \
    execute_model_training, textproc_download_saved_model, load_textproc_model_template, textproc_load_model, \
    predict_with_loaded_model, download_test_texts

urlpatterns = [
    path('upload_text_nn_page/', upload_text_nn_template, name='upload_text_nn_template'),
    path('upload_txt_set/', load_text_set, name='load_text_set'),
    path('build_nn_page/<str:folder>/', build_textproc_nn_template, name='build_textproc_nn_template'),
    path('train_nn/', execute_model_training, name='execute_model_training'),
    path('download_model/<str:dir_name>/', textproc_download_saved_model, name='download_saved_model'),
    path('load_model_page/', load_textproc_model_template, name='load_textproc_model_template'),
    path('load_model/', textproc_load_model, name='textproc_load_model'),
    path('textproc_test_model/', predict_with_loaded_model, name='predict_with_loaded_model'),
    path('download_text/<str:dir_name>/<str:texts_dir>/<str:text_name>/', download_test_texts,
         name='download_test_texts')
]
