from django.urls import path
from apps.improc.views import build_improc_nn_template, upload_image_nn_template, execute_nn_training, \
    upload_image_set, decompress_image_set, convert_image_set, download_saved_model, load_model_template, load_model, \
    predict_with_loaded_model, download_test_images

urlpatterns = [
    path('build_nn_page/<str:folder>/', build_improc_nn_template, name='build_improc_nn_template'),
    path('upload_set_nn_page/', upload_image_nn_template, name='upload_image_nn_template'),
    path('train_nn/', execute_nn_training, name='execute_nn_training'),
    path('upload_img_set/', upload_image_set, name='upload_image_set'),
    path('decomp_img_set/', decompress_image_set, name='decompress_image_set'),
    path('convert_img_set/', convert_image_set, name='convert_image_set'),
    path('download_model/<str:dir_name>/', download_saved_model, name='download_saved_model'),
    path('load_model_page', load_model_template, name='load_model_template'),
    path('load_model/', load_model, name='load_model'),
    path('test_model/', predict_with_loaded_model, name='test_model'),
    path('download_image/<str:dir_name>/<str:image_dir>/<str:image_name>/', download_test_images,
         name='download_test_images')
]
