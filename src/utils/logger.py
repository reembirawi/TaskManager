import logging
from pathlib import Path


def setup_logger():
    base_dir = Path(__file__).resolve().parents[2]
    logs_dir = base_dir / "logs"

    logs_dir.mkdir(exist_ok=True)

    log_file = logs_dir / "app.log"

    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
