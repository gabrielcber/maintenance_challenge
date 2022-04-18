"""Project pipelines."""
from typing import Dict

from kedro.pipeline import Pipeline, pipeline

from defy.pipelines import data_processing as dp
from defy.pipelines import data_transforming as dt
from defy.pipelines import fitting_model as fm

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from a pipeline name to a ``Pipeline`` object.
    """

    data_processing = dp.create_pipeline()
    data_transforming = dt.create_pipeline()
    fitting_model = fm.create_pipeline()

    return {
        "dp": data_processing,
        "dt": data_transforming,
        "fm": fitting_model,
        "__default__": (
            data_processing
            + data_transforming
            + fitting_model
            #+ model_metrics_pipeline
            #+ indicium_predictor_pipeline
        ),
}
