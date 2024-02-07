import yaml
import os

def init_env():
    """Initialize the project environment"""
    if os.getenv('ENV', 'development') == 'development':
      """Set environment variables to env.yaml when in dev mode"""
      config_path = "./env.yaml"
      config = load_config(config_path)
      set_env_variables(config)

def load_config(config_path):
    """Load configuration from a YAML file."""
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config

def set_env_variables(config):
    """Set environment variables from the loaded configuration."""
    for key, value in config.items():
        os.environ[key] = str(value)
