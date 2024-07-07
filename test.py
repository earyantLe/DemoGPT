import json
from pprint import pprint

from demogpt.chains.chains import Chains

Chains.setLlm("gpt-3.5-turbo", openai_api_base="https://api.chatanywhere.tech/v1")

instruction = "帮我推荐一个快手的广告创意文案，要求简介明了，吸引用户"
res = Chains.appType(instruction=instruction)
pprint(res)
