# Scrabble Word Finder
A python script which shows you the possible words that fit in the board depending on the missing letters and the word length using a whole dictionary as the dataset.

## Sample Game Board
Below screenshot has been taken from a game named [Word Universe](https://play.google.com/store/apps/details?id=com.librasoftworks.worduniverse&hl=en_US)

![game_screen_2](https://user-images.githubusercontent.com/36932448/62010088-cd46d100-b16e-11e9-9151-5bbb0eb61a86.png)

## Usage
The idea is to find all of the valid combinations that have an equivalent at the dictionary when you revealed at least one letter of the word. To find out the words **[1], [2]** and **[3]**, following codes can be used:

```python
bul("_____k", "faktri")
bul("__r_f", "faktri")
bul("a_i_", "faktri")
```

bul() ("find" in Turkish) function takes two parameters:

- Revealed letter(s)
- Usable letters

and returns all the words which contain any letter from Turkish alphabet at indexes with "**_**", and the given revealed letter at its index.

The output of the above code will be:

![Capture](https://user-images.githubusercontent.com/36932448/62009727-2a408800-b16b-11e9-86c3-c8fd36cc0be7.PNG)

## References

The whole dictionary has been taken from [TDKDictionaryCrawler](https://github.com/ncarkaci/TDKDictionaryCrawler) repository which collects all the words from the Turkish Language Institue.
Any other language and its dictionary can be used with this algorithm.
