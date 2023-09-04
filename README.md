# Mauve - Dictation

My custom scripts for [nerd dictation](https://github.com/ideasman42/nerd-dictation) which adds some features that I'm using for my programming set up.

- NATO phonetic alphabet
- useful shortcuts for tech terms
- special characters like "open bracket"
- different typing modes which you can activate on the fly
  - "mode speak":  the default typing mode where each word is separated by a space and is lower case
  - "mode scream": same as speak but everything is in capital letters
  - "mode snake": same as speak but instead of spaces there are underscores. useful for typing variable names in python
  - "mode screaming snake":  same as snake bite withall caps useful for constant variable names in c-like languages
  - "mode camel": same as speak mode but instead of spaces each word starts with a capital `somethingLikeThis`
  - "mode dictate": same as speak mode butthere are no spaces, useful for typing using the nato phonetic alphabeti

I also have a bunch of word replacements for words that I commonly say that others may notso feel free to remove them if you fork this

I typically use thison my steam deck using the [steam dictation](https://github.com/atcq/steam-dictation) library.

I use the following flags when invoking nerd dictation for best performance and to have the auto shot off in case I forget and leave it running.

```
--continuous --numbers-as-digits --timeout 10 --idle-time 0.5
```
