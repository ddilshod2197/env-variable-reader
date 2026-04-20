import os

def oling_environment_variable(ismi):
    """Environment variable olish uchun funksiya"""
    qiymat = os.environ.get(ismi)
    if qiymat is None:
        raise ValueError(f"Environment variable '{ismi}' topilmadi")
    return qiymat

# Misol uchun ishlatish
print(oling_environment_variable('VARIABLE_NAME'))
```

```python
import dotenv

def oling_environment_variable(ismi):
    """Environment variable olish uchun funksiya"""
    dotenv.load_dotenv()
    qiymat = os.environ.get(ismi)
    if qiymat is None:
        raise ValueError(f"Environment variable '{ismi}' topilmadi")
    return qiymat

# Misol uchun ishlatish
print(oling_environment_variable('VARIABLE_NAME'))
```

```python
import yaml

def oling_environment_variable(ismi, fayl='config.yaml'):
    """Environment variable olish uchun funksiya"""
    with open(fayl, 'r') as file:
        config = yaml.safe_load(file)
    qiymat = config.get(ismi)
    if qiymat is None:
        raise ValueError(f"Environment variable '{ismi}' topilmadi")
    return qiymat

# Misol uchun ishlatish
print(oling_environment_variable('VARIABLE_NAME'))
