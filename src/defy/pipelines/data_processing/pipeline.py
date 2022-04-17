"""
This is a boilerplate pipeline 'data_processing'
generated using Kedro 0.18.0
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import maintenance_initial_transformation, maintenance_dataset_preparation

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=maintenance_initial_transformation,
                name="maintenance_initial_transformation",
                inputs=[
                    "data_2020",
                    "data_pre_2020",
                ],
                outputs="maintenance_data",
            ),
            node(
                func=maintenance_dataset_preparation,
                name="maintenance_dataset_preparation",
                inputs=[
                    "maintenance_data",
                    "params:corr_threshold",
                    "params:nan_column_threshold",
                    "params:nan_row_threshold",
                    "params:flag_column",
                    "params:label",
                ],
                outputs=[
                    "maintenance_prepared_data",
                    "corr_matrix",
                    "pre_x_train",
                    "pre_x_test",
                    "pre_y_train",
                    "pre_y_test",
                ]
            ),
        ]
    )


