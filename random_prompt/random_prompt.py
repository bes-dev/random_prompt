"""
Copyright 2022 by Sergei Belousov

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import os
import random
from typing import List
import json


class RandomPromptGenerator:
    def __init__(self):
        cfg_path = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            "configs",
            "random_prompt.json"
        )
        self.cfg = json.load(open(cfg_path))

    def random_prompt(self) -> str:
        prompt = random.choice(self.cfg["templates"])
        for k, v in self.cfg["prompt"].items():
            prompt = prompt.replace(f"{{{k}}}", f"{random.choice(v)}")
        return prompt

    def random_prompts(self, batch_size: int = 1) -> List[str]:
        return [self.random_prompt() for i in range(batch_size)]
