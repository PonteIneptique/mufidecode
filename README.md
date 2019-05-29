# Mufidecode

Transliterate Unicode text into plain 7-bit ASCII with Medieval flavor.

```python
from mufidecode import mufidecode
from unidecode import unidecode

string = " soffroient Torm̃z⁊"
assert unidecode(string) == " soffroient Tormz7"  # Lostfirst character, et is converted to seven.
assert mufidecode(string) == "et soffroient Tormzet"
assert mufidecode(string, join=False) == ('et', ' ', 's', 'o', 'f', 'f', 'r', 'o', 'i', 'e', 'n', 't', ' ', 'T', 'o', 'r', 'm', 'z', 'et')


assert mufidecode("ꝮꝯꝮꝯ") == "usususus"
```

## Add a new token

**1. Get the code**

```python
string = "ꝯ"
print((ord(string) >> 8, ord(string) % 256))
# (167, 111)
```

**2. Add the code to MUFI**

```python
MUFI[(167, 111)] = "us"  # Accepted transliteration
```

**3. Pull Request**

**4. Enjoy**