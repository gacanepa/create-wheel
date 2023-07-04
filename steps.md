# Steps to generate a wheel file

1. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install the `wheel` Python package:

```bash
pip install wheel build
```

3. Clone this repository:

```bash
git clone https://github.com/gacanepa/create-wheel.git
```

4. Generate the wheel:

```bash
python -m build
```

5. Look for the **.tar.gz** and **.whl** files inside the dist subfolder:

![image](https://github.com/gacanepa/create-wheel/assets/2545170/b4782e4f-07df-48bf-b5f2-411abebdbf3f)

6. Install the wheel after replacing **create_wheel-0.0.1-py3-none-any.whl** for the corresponding filename:

```bash
cd dist
pip install create_wheel-0.0.1-py3-none-any.whl 
```

7. To test, get into a Python REPL:

```bash
python
```

8. Import the functions from the package:

```python
from create_wheel.get_odd_or_even import get_odd, get_even
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
get_odd(numbers_list)
# -> [1, 3, 5, 7, 9, 11]
get_even(numbers_list)
# -> [2, 4, 6, 8, 10, 12]   
```