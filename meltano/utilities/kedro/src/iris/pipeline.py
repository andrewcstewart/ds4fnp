"""
This is a boilerplate pipeline
generated using Kedro 0.18.1
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import make_predictions, report_accuracy, report_predictions, split_data, write_table, load_table


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=load_table,
                inputs=["example_iris_data"],
                outputs="meltano_source_table",
                name="load_table",
            ),
            node(
                func=split_data,
                inputs=["meltano_source_table", "parameters"],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split",
            ),
            node(
                func=make_predictions,
                inputs=["X_train", "X_test", "y_train"],
                outputs="y_pred",
                name="make_predictions",
            ),
            node(
                func=report_accuracy,
                inputs=["y_pred", "y_test"],
                outputs=None,
                name="report_accuracy",
            ),
            node(
                func=report_predictions,
                inputs=["y_pred", "X_test", "parameters"],
                outputs="predictions",
                name="report_predictions",
            ),            
            node(
                func=write_table,
                inputs=["predictions"],
                outputs="meltano_target_table",
                name="write_table",
            ),            
        ]
    )
