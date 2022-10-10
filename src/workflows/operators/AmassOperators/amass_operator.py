from airflow.operators import DockerOperator

class AmassOperator(DockerOperator):

    def __init__(
        self, 
        input_task_id, 
        shared_dir_path,
        output_dir_path = '/.config/amass/',
        *args, 
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.input_task_id      = input_task_id
        self.shared_dir_path    = shared_dir_path
        self.output_dir_path    = output_dir_path