## Shady Text Randomizer

The **Shady Text Randomizer** is a python package that helps to avoid spam-filters by replacing some characters in text with similar characters from other languages. 
As a result, the result text is not equal to the source text. 

The **Shady Text Randomizer** supports latin and cyrillic symbols.

###  Install

```
$ pip install shady_tr
```

### Usage

Class **ShadyTextRandomizer**  has two parameters:
1. [string] Source text
2. [int from 0 to 100] Symbol replace chance. If chance is equals 100, then each possible symbol well be converted to similar one.

```
>> from shady_tr import ShadyTextRandomizer
>>
>> text_rnd = ShadyTextRandomizer("Hello! How are you?", 100)
>> text_rnd.random_latin()
>>
>> text_rnd = ShadyTextRandomizer("Привет! Как дела?", 100)
>> text_rnd.random_cyrillic()
```

### License

This project is licensed under the MIT License
