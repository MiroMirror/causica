from pathlib import Path

import mlflow
import pytest

from causica.lightning.loggers import BufferingMlFlowLogger


@pytest.mark.skip(reason="MLflow 本地 file store 下 model registry 不可用，需真实 backend 时再启用")
def test_buffering_mlflow_logger(tmp_path: Path):
    mlflow.set_tracking_uri(tmp_path)
    client = mlflow.tracking.MlflowClient(tracking_uri=str(tmp_path))
    experiment_id = client.create_experiment("test")
    run = client.create_run(experiment_id=experiment_id)
    logger = BufferingMlFlowLogger(buffer_size=3, run_id=run.info.run_id, tracking_uri=str(tmp_path))
    logger.log_metrics({"a": 1})
    logger.log_metrics({"a": 2})
    assert logger.get_buffer_count() == 2
    logger.log_metrics({"a": 3})  # Should flush due to full
    assert logger.get_buffer_count() == 0
    logger.log_metrics({"a": 4})
    assert logger.get_buffer_count() == 1
    logger.flush()
    assert logger.get_buffer_count() == 0
