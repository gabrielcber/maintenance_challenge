"""
This is a boilerplate pipeline 'fitting_model'
generated using Kedro 0.18.0
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import fitting_model

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [ 
            node(
                func=fitting_model,
                name="fitting_model",
                inputs=[
                    "x_train",
                    "y_train",
                ],
                outputs="model"
            ),
        ]
    )