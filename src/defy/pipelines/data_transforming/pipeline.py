"""
This is a boilerplate pipeline 'data_transforming'
generated using Kedro 0.18.0
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import pre_training_transformation

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=pre_training_transformation,
                name="pre_training_transformation",
                inputs=[
                    "pre_x_train",
                    "pre_x_test",
                    "pre_y_train",
                    "pre_y_test",
                    "params:list_of_columns",
                ],
                outputs=[
                    "x_train",
                    "y_train",
                    "x_test",
                    "y_test",
                ],
            ),
        ]
    )