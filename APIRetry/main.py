from LogsOptions import LogsOptions
from ApiRetrys import ApiRetry
options = LogsOptions()

options.add_options(save_logs=True, path='data/private')

api = ApiRetry(options=options)
