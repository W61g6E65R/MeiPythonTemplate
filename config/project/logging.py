from pydantic import BaseModel, Field
from typing import Optional, Dict, List, Any
import yaml

class FormatterConfig(BaseModel):
    format: str

class HandlerConfig(BaseModel):
    class_: str = Field(alias="class")  # wegen "class" als reserviertes Wort
    level: str
    formatter: str
    stream: Optional[str] = None
    filename: Optional[str] = None
    mode: Optional[str] = None
    maxBytes: Optional[int] = None
    backupCount: Optional[int] = None

class RootConfig(BaseModel):
    level: str
    handlers: List[str]

class LogConfig(BaseModel):
    version: int
    disable_existing_loggers: bool
    formatters: Dict[str, FormatterConfig]
    handlers: Dict[str, HandlerConfig]
    root: RootConfig
    
def load_config(path: str) -> LogConfig:
    with open(path, "r") as f:
        raw_data = yaml.safe_load(f)
    return LogConfig.model_validate(raw_data)

def get_config(path: str)-> dict[str, Any]:
    config = load_config(path)
    logging_config_dict = config.model_dump()
    return logging_config_dict
