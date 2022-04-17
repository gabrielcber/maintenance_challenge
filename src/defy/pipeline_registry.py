"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline

from defy.pipelines import data_processing as dp
from defy.pipelines import data_transforming as dt

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """

    data_processing = dp.create_pipeline()
    data_transforming = dt.create_pipeline()

    return {
        "dp": data_processing,
        "dt": data_transforming,
        "__default__": (
            data_processing
            + data_transforming
            #+ model_metrics_pipeline
            #+ indicium_predictor_pipeline
        ),
}
