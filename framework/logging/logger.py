from __future__ import annotations

import logging
from pathlib import Path


class EvalForgeLogger:

    _configured = False

    @classmethod
    def configure(
        cls,
        log_directory: str = "logs",
        level: int = logging.INFO,
    ) -> logging.Logger:

        logger = logging.getLogger(
            "evalforge"
        )

        if cls._configured:
            return logger

        Path(log_directory).mkdir(
            parents=True,
            exist_ok=True,
        )

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler = logging.FileHandler(
            Path(log_directory) / "evalforge.log",
            encoding="utf-8",
        )

        file_handler.setFormatter(
            formatter
        )

        console_handler = logging.StreamHandler()

        console_handler.setFormatter(
            formatter
        )

        logger.setLevel(level)

        logger.addHandler(file_handler)

        logger.addHandler(console_handler)

        cls._configured = True

        return logger