"""Delay optional Japanese tokenizer import on CPUs lacking DyNet wheel ISA.

This does not change Chinese/English ASR or alignment. Japanese still imports
the real tokenizer when requested. Applies only to the pinned qwen-asr 0.0.6.
"""
import hashlib
import importlib.metadata
import json

dist = importlib.metadata.distribution('qwen-asr')
if dist.version != '0.0.6':
    raise RuntimeError('Inspect compatibility patch before applying to another version')
p = dist.locate_file('qwen_asr/inference/qwen3_forced_aligner.py')
text = p.read_text()
before = hashlib.sha256(text.encode()).hexdigest()
needle = '    def tokenize_japanese(self, text: str) -> List[str]:\n        words = nagisa.tagging(text).words'
if '\nimport nagisa\n' in text:
    if needle not in text:
        raise RuntimeError('Unexpected upstream source; refusing patch')
    text = text.replace('\nimport nagisa\n', '\n')
    text = text.replace(needle, needle.replace('        words', '        import nagisa\n        words', 1))
    compile(text, str(p), 'exec')
    p.write_text(text)
elif '        import nagisa\n        words = nagisa.tagging(text).words' not in text:
    raise RuntimeError('Unexpected upstream source')
print(json.dumps({'patch': 'lazy_optional_japanese_import', 'version': dist.version,
                  'before_sha256': before, 'after_sha256': hashlib.sha256(text.encode()).hexdigest()}))
