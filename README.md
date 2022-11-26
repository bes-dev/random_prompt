# Random Prompt

A simple python library for fast random prompt generation.


## Requirements

* Linux, Windows, MacOS
* Python 3.8.+

## Install package

```bash
pip install random_prompt
```

## Install the latest version

```bash
git clone https://github.com/bes-dev/random_prompt.git
cd random_prompt
pip install .
```

## Example

```python
from random_prompt import RandomPromptGenerator

generator = RandomPromptGenerator()
# generate single prompt
print(generator.random_prompt())
# generate batch of prompts
print(generator.random_prompts(10))
```
