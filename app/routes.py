from app import api
from app.view import UploadFileView, DeviceTestView, DeviceTestDeleteView, \
    DeviceTestStatView


api.add_resource(UploadFileView, '/api_v1/upload')
api.add_resource(DeviceTestStatView, '/api_v1/stat')
api.add_resource(DeviceTestView, '/api_v1/test_result')
api.add_resource(DeviceTestDeleteView, '/api_v1/test_result/<int:device_test_id>')

