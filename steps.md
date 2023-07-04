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



6. Install the wheel after replacing **create_wheel-0.0.1-py3-none-any.whl** for the corresponding filename:

```bash
pip install create_wheel-0.0.1-py3-none-any.whl 
```