# text-data-augmentation 
### 两个文本数据增强方法
- 回译：用的百度api，支持字符串和list传入
```python
import tda
s1 = '我是需要增强的'
s2 = ['我是需要增强的', '我是需要翻译的']
r1 = tda.translate(s1)
r2 = tda.translate(s2)
 ```

- Easy Data Augmentation   [参考论文](https://arxiv.org/abs/1901.11196v1)  
用到4个方法：近义词替换、近义词插入、随机交换词、随机删除词  
为了方便使用，直接对论文中的参数α固定为0.1，要求句子分词以后词的数量>=10  
支持字符串和list传入  
```python
import tda
s1 = '我是需要翻译的我需要超过10个词，一定要超过10个词'
s2 = ['我是需要翻译的我需要超过10个词，一定要超过10个词', 
      '我是需要翻译的我需要超过10个词，一定要超过10个词']
r1 = tda.eda(s1)
r2 = tda.eda(s2)
 ```