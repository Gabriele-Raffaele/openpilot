import os
import capnp
from importlib.resources import as_file, files

capnp.remove_import_hook()
print("position:", os.getcwd())
with as_file(files("cereal")) as fspath:
  CEREAL_PATH = fspath.as_posix()
  print(f"CEREAL_PATH: {CEREAL_PATH}")
  log = capnp.load(os.path.join(CEREAL_PATH, "log.capnp"))
  car = capnp.load(os.path.join(CEREAL_PATH, "car.capnp"))
  custom = capnp.load(os.path.join(CEREAL_PATH, "custom.capnp"))
