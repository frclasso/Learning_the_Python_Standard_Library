#!/usr/bin/env python3

## Text Wrap Module
import textwrap


websiteText = """   Learning can happen anywhere with our apps on your computer,
mobile device, and TV, featuring enhanced navigation and faster streaming
for anytime learning. Limitless learning, limitless possibilities."""

print()
print("No dedent: ")
print(textwrap.fill(websiteText))

print()
print("Dedent: ")
dedent_text = textwrap.dedent(websiteText).strip()
print(dedent_text)

print()
print("Fill: ")
print(textwrap.fill(dedent_text, width=50))
print()
print(textwrap.fill(dedent_text, width=70))

print()
print("Controlling Indent")
print(textwrap.fill(dedent_text , initial_indent="   ", subsequent_indent=" "))

print()
print("Shortening text")
short = textwrap.shorten("LinkedIn.com is great!",width=15,placeholder="...")
print(short)
